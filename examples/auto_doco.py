import ast
from pathlib import Path


from src.file_utils import File


py_file = Path("../src/qtpygui.py")
raw_tree = py_file.read_text()
tree = ast.parse(raw_tree)
class_dict = {}


def docostring_parser(docstring: str) -> dict:
    doclines = docstring.splitlines()
    parsed_docstring_dict = {"definition": "", "args": [], "returns": []}

    arg_on = False
    return_on = False

    definition_line = ""
    arg_definition = ""
    arg_name_base = ""
    args = []
    for docline in doclines:
        if docline.replace(":", "").startswith("Args") or docline.replace(
            ":", ""
        ).startswith("Parameters"):
            arg_on = True
            return_on = False

        if docline.replace(":", "").startswith("Returns"):
            arg_on = False
            return_on = True

        if not arg_on and not return_on:
            definition_line += docline + "<br>"

        if arg_on:
            if ":" in docline:
                args = []
                # args.append(arg_name_base + ":" + arg_definition)
                arg_name_base = docline.split(":")[0].strip()
                arg_definition = docline.split(":")[1].strip()

                arg_name = arg_name_base
                arg_type = ""
                if "(" and ")" in arg_name_base:
                    arg_name = arg_name_base.split("(")[0]
                    arg_type = arg_name_base.split("(")[1].replace(")", "")

                args.append([arg_name, arg_type, arg_definition])
                parsed_docstring_dict["args"].append(args)
            else:
                args[-1][2] += docline
                arg_definition += docline
        if return_on:
            return_type = docline
            return_desc = ""
            if ":" in docline:
                return_type = docline.split(":")[0].strip()
                return_desc = docline.split(":")[1].strip()

            parsed_docstring_dict["returns"].append((return_type, return_desc))

    return parsed_docstring_dict


def get_public_instance_variables(node):
    """
    Extracts public instance variables (attributes) from a class definition node.

    Args:
        node (ast.AST): The class definition node from the parsed AST.

    Returns:
        list: A list of strings representing the public instance variable names.
    """
    public_vars = []

    # Look for assignments and directly defined attributes
    for body_node in node.body:
        if isinstance(body_node, (ast.Assign)):
            # Handle assignments within the class body
            # target = body_node.target  # Use singular target for AnnAssign
            for x in body_node.targets:
                if isinstance(x, ast.Name):
                    print(x.id)
                if x is not None and x.attr is not None and x.attr.startswith("_"):
                    print(x.attr)
                    public_vars.append(x.attr)

            # Handle multiple assignments with various value structures
            if isinstance(body_node, ast.Assign) and len(body_node.targets) > 1:
                for i, target in enumerate(body_node.targets):
                    if isinstance(target, ast.Attribute) and not target.attr.startswith(
                        "_"
                    ):
                        public_vars.append(target.attr)
                    elif isinstance(body_node.value, (ast.Tuple, ast.List)):
                        if i < len(body_node.value.elts):
                            value_part = body_node.value.elts[i]
                            if isinstance(
                                value_part, ast.Name
                            ):  # Simple variable assignment
                                public_vars.append(value_part.id)

        # Check for directly defined attributes
        elif isinstance(body_node, ast.Expr):
            if isinstance(
                body_node.value, ast.Attribute
            ):  # Check for attribute definition
                if not body_node.value.attr.startswith(
                    "_"
                ):  # Public attribute (doesn't start with underscore)
                    public_vars.append(body_node.value.attr)
    print(public_vars)
    return public_vars


def get_type(annotation):
    if isinstance(annotation, ast.Name):
        return annotation.id
    elif isinstance(annotation, ast.Attribute):
        return f"{annotation.value.id}.{annotation.attr}"
    elif isinstance(annotation, ast.Call):
        if annotation.func.id == "Union":
            return f"Union[{', '.join(get_type(arg) for arg in annotation.args)}]"
    elif isinstance(annotation, ast.Subscript):
        if isinstance(annotation.slice, ast.Slice):
            slice_info = f"{annotation.value.id}[{get_type(annotation.slice.lower) if annotation.slice.lower else ''}:{get_type(annotation.slice.upper) if annotation.slice.upper else ''}:{get_type(annotation.slice.step) if annotation.slice.step else ''}]"
            return slice_info
        elif isinstance(annotation.slice, ast.Index):
            return f"{annotation.value.id}[{get_type(annotation.slice.value)}]"
        elif isinstance(annotation.slice, ast.ExtSlice):
            dims = [get_type(dim) for dim in annotation.slice.dims]
            return f"{annotation.value.id}[{', '.join(dims)}]"
        else:
            return f"{annotation.value.id}[{get_type(annotation.slice)}]"
    elif isinstance(annotation, ast.Tuple):
        elements = [get_type(elt) for elt in annotation.elts]
        return f"({', '.join(elements)})"
    elif isinstance(annotation, ast.List):
        return f"[{', '.join(get_type(elt) for elt in annotation.elts)}]"
    elif isinstance(annotation, ast.Dict):
        keys = [get_type(key) for key in annotation.keys]
        values = [get_type(value) for value in annotation.values]
        return f"{{{', '.join(f'{k}: {v}' for k, v in zip(keys, values))}}}"
    elif isinstance(annotation, ast.BinOp):
        left_type = get_type(annotation.left)
        right_type = get_type(annotation.right)
        return f"({left_type} {type(annotation.op).__name__} {right_type})"
    elif isinstance(annotation, ast.FunctionType):
        return f"Callable[[{', '.join(get_type(arg) for arg in annotation.args)}], {get_type(annotation.returns)}]"
    elif isinstance(annotation, ast.Constant):
        return str(annotation.value)
    else:
        return str(annotation)


def get_class_methods(node, current_path=[], level=1):
    """
    Recursive function to analyze methods within a class definition node.

    Args:
        node (ast.AST): The current node in the AST.

    Returns:
        list: A list of dictionaries containing method information:
            - name (str): Name of the method
            - docstring (str): Docstring of the method (if present)
            - args (list): List of dictionaries for arguments:
                - name (str): Name of the argument
                - type_annotation (str, None): Type annotation (if present)
            - return_type (str, None): Return type annotation (if present)
    """

    methods = []
    method_info = {}

    for child in node.body:
        if isinstance(child, ast.FunctionDef):
            method_info = {
                "name": child.name,
                "docstring": ast.get_docstring(child),  # Get docstring (if present)
                "args": [],
                "vars": [],
                "return_type": None,
                "path": current_path.copy(),
            }
            method_info["path"].append(node.name)  # Add current class to path

            for arg in child.args.args:
                arg_info = {"name": arg.arg, "type_annotation": None}

                if (
                    hasattr(arg, "annotation") and arg.annotation is not None
                ):  # Check for type annotation
                    if hasattr(arg.annotation, "id"):
                        arg_info["type_annotation"] = (
                            arg.annotation.id
                        )  # Extract type name
                        method_info["args"].append(arg_info)

            if child.returns:  # Check for return type annotation
                method_info["return_type"] = (
                    child.returns.id if hasattr(child.returns, "id") else None
                )
            methods.append(method_info)
        elif isinstance(child, ast.AnnAssign):
            # Extract instance variables from dataclass fields
            # if child.target.id != '_USER_DATA':
            # print(f"DBG {child.target.id}  On {node.name} ")
            # print(f"DBG {get_type(child.annotation)}")
            print(f"DBG {node.name}, {child.target.id, get_type(child.annotation)}")

        elif isinstance(child, ast.ClassDef):
            # Recursively search for methods within nested classes
            methods.extend(
                get_class_methods(child, current_path + [node.name], level + 1)
            )

    return methods


def split_line_by_words(line, max_width=80):
    """
    Splits a line of text into multiple lines, breaking around words
    and ensuring each line is no wider than the specified width.

    Args:
        line (str): The line of text to split.
        max_width (int, optional): The maximum width of each line. Defaults to 80.

    Returns:
        list: A list of strings representing the split lines.
    """

    words = line.split()
    current_line = ""
    split_lines = []

    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:  # Add 1 for space
            current_line += f" {word}"  # Prepend space for all except first word
        else:
            split_lines.append(
                current_line.strip()
            )  # Add previous line without trailing space
            current_line = word

    # Add the last line (if any)
    if current_line:
        split_lines.append(current_line)

    return split_lines


def write_table_to_file(table_rows: list[str]):
    file_utils = File()

    doco_path = "./doco"
    if not file_utils.path_exists(doco_path):
        file_utils.make_dir(doco_path)

    classy_list = []
    classy_name = ""
    for table_row in table_rows:
        if table_row.startswith("###"):
            classy_name = table_row.split("###")[1]

        classy_list.append(table_row)

    if classy_list:
        result, message = file_utils.write_list_to_txt_file(
            str_list=classy_list, text_file=f"{doco_path}/{classy_name}.md"
        )


if __name__ == "__main__":
    class_methods = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_methods.append({
                "class_name": node.name,
                "docstring": ast.get_docstring(node, clean=True),
                "methods": get_class_methods(node),
            })

    for class_info in class_methods:
        if (
            class_info["class_name"].startswith("_")
            and class_info["class_name"].strip() != "_qtpyBase_Control"
        ):
            continue

        docstring = ""

        if class_info["docstring"] is not None:
            docstring_list = split_line_by_words(
                class_info["docstring"].replace("\n", "<br>")
            )

            for string_index, string in enumerate(docstring_list):
                docstring = (
                    docstring + string + "<br>"
                    if string_index != len(docstring_list) - 1
                    and not string.endswith("<br>")
                    else docstring + string
                )

        table_rows = [f"### {class_info['class_name']}", " ", f"{docstring}", " "]

        for class_key, class_values in class_info.items():
            if class_key == "class_name":
                table_rows.append(
                    "| **Method** | **Arguments** | **Type** | **Description** | **Optional** |"
                )
                table_rows.append(
                    "|------------|---------------|----------|-----------------|--------------|"
                )  # Separator line

            if class_key == "methods":
                class_info["methods"].sort(key=lambda x: x["name"])
                for method in class_info["methods"]:
                    if (
                        method["name"].startswith("_")
                        and method["name"].strip() != "init"
                    ):
                        continue

                    parsed_doc_string = {}
                    method_docstring = ""

                    if method["docstring"] is not None:
                        parsed_doc_string = docostring_parser(method["docstring"])
                        # method_docstring = parsed_doc_string["definition"]
                        docstring_list = split_line_by_words(
                            parsed_doc_string["definition"].replace("\n", "<br>", 60)
                        )

                        for string_index, string in enumerate(docstring_list):
                            method_docstring = (
                                method_docstring + string + "<br>"
                                if string_index != len(docstring_list) - 1
                                and not string.endswith("<br>")
                                else method_docstring + string
                            )

                        return_doc_string = ""

                        for doc_string in parsed_doc_string["returns"]:
                            doc_string_type = (
                                f"{doc_string[0]}:" if doc_string[0] else ""
                            )
                            if doc_string[1].strip().strip() and doc_string[1].strip():
                                # return_doc_string += f"{doc_string_type} {doc_string[1]}<br>"
                                return_doc_string += f"{doc_string[1]}<br>"

                        if return_doc_string:
                            if (
                                return_doc_string.strip()
                                and return_doc_string.strip() != ":"
                            ):
                                method_docstring += (
                                    f"<br><b>Returns:</b><br> {return_doc_string}"
                                )

                    table_rows.append(
                        f"|{method['name']}||{method['return_type']}|{method_docstring}||"
                    )

                    if parsed_doc_string:
                        # print(parsed_doc_string["args"])
                        pass

                    method["args"].sort(key=lambda x: x["name"])
                    for arg in method["args"]:
                        arg_definition = ""
                        if parsed_doc_string:
                            for doc_args in parsed_doc_string["args"]:
                                for doc_arg in doc_args:
                                    if (
                                        arg["name"].strip().lower()
                                        == doc_arg[0].strip().lower()
                                    ):
                                        arg_definition = doc_arg[2]
                        table_rows.append(
                            f"||{arg['name']}|{arg['type_annotation']}|{arg_definition}||"
                        )

        write_table_to_file(table_rows=table_rows)
