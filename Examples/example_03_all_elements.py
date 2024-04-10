"""
This module implements example_03 that shows all the GUI elements qtpygui.

Copyright (C) 2024  David Worboys (-:alumnus Moyhu Primary School et al.:-)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import popups
import qtpygui as qtg
from sys_consts import PROGRAM_NAME


class Example_03:
    def __init__(self):
        self._grid = None
        self._lcd = None
        self._treeview = None
        self.example_03 = qtg.QtPyApp(
            display_name="Example 03 - All GUI Elements",
            callback=self.event_handler,
            height=200,
            width=300,
        )

    def event_handler(self, event: qtg.Action):
        """Handles  form events
        Args:
            event (qtg.Action): The triggering event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        match event.event:
            case qtg.Sys_Events.APPPOSTINIT:
                self._grid.value_set(value="value 1", row=0, col=0, user_data=None)
                self._grid.value_set(value="value 1", row=0, col=1, user_data=None)

                self._lcd.value_set(value=88888)

                self._treeview.child_add(treeview_path="Test 1", items="Test 3")
                self._treeview.child_add(
                    treeview_path=["Test 1", "Test 3"], items="Test 4"
                )
            case qtg.Sys_Events.CLICKED:
                match event.tag:
                    case "ok":
                        self.example_03.app_exit()
                    case "popup_hi":
                        popups.PopMessage(title="Hi", message="Hello World").show()

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the window
        Returns:
            qtg.VBoxContainer: The layout
        """
        # Check out event handler to see how to load
        self._grid = qtg.Grid(
            tag="grid",
            label="Grid",
            callback=self.event_handler,
            col_def=[
                qtg.Col_Def(
                    label="Col 1", checkable=True, editable=False, tag="col_1", width=10
                ),
                qtg.Col_Def(
                    label="Col 2", checkable=False, editable=True, tag="col_2", width=10
                ),
            ],
            height=2,
        )

        self._lcd = qtg.LCD(
            tag="lcd", label="LCD", callback=self.event_handler, width=8, height=1
        )

        tab = qtg.Tab(
            tag="tab",
            label="Tab",
            callback=self.event_handler,
            width=48,
            height=14,
        )
        tab.page_add(
            tag="tab_pg1",
            title="Page 1",
            control=qtg.VBoxContainer(height=4, align=qtg.Align.HCENTER).add_row(
                qtg.Image(
                    tag="image",
                    label="Image",
                    width=20,
                    height=20,
                    callback=self.event_handler,
                    image="example.jpg",
                ),
                qtg.Spacer(),
                qtg.Button(
                    tag="button",
                    label="Button",
                    text="Tab Button",
                    callback=self.event_handler,
                ),
            ),
        )
        tab.page_add(
            tag="tab_pg2",
            title="Page 2",
            control=qtg.FormContainer().add_row(
                qtg.Slider(tag="slider", label="Slider", callback=self.event_handler),
            ),
        )

        self._treeview = qtg.Treeview(
            tag="treeview",
            label="Treeview",
            callback=self.event_handler,
            width=15,
            height=5,
            toplevel_items=["Test 1", "Test 2"],
        )

        return qtg.VBoxContainer(align=qtg.Align.BOTTOMRIGHT).add_row(
            qtg.VBoxContainer().add_row(
                qtg.HBoxContainer(tag="row_1").add_row(
                    qtg.Button(
                        tag="button",
                        text="Button",
                        label="Button",
                        callback=self.event_handler,
                    ),
                    qtg.Button(
                        tag="icon_button",
                        text=" Icon",
                        label="Icon",
                        callback=self.event_handler,
                        icon=qtg.Sys_Icon.computericon.get(),
                    ),
                    qtg.Checkbox(
                        tag="checkbox",
                        text="Tick Me!",
                        label="Check Box",
                        callback=self.event_handler,
                        width=12,
                    ),
                    qtg.ComboBox(
                        tag="combo_box",
                        label="Combo Box",
                        display_na=False,
                        items=[
                            qtg.Combo_Item(
                                display="Item 1",
                                data=None,
                                icon=qtg.Sys_Icon.computericon.get(),
                                user_data=None,
                            ),
                            qtg.Combo_Item(
                                display="Item 2", data=None, icon=None, user_data=None
                            ),
                            qtg.Combo_Item(
                                display="Item 3", data=None, icon=None, user_data=None
                            ),
                        ],
                        callback=self.event_handler,
                        width=8,
                    ),
                    qtg.Spacer(),
                ),
                qtg.HBoxContainer(tag="row_2").add_row(
                    qtg.Label(
                        label="Label",
                        text="Example 03",
                        txt_fontsize=42,
                        txt_align=qtg.Align.CENTER,
                        txt_font=qtg.Font(backcolor="blue", forecolor="yellow"),
                        width=22,
                    )
                ),
                qtg.HBoxContainer(tag="row_3").add_row(
                    qtg.Dateedit(
                        tag="dateedit", label="Date Edit", callback=self.event_handler
                    ),
                    qtg.FolderView(
                        tag="folderview",
                        label="Folder View",
                        callback=self.event_handler,
                        height=5,
                        header_widths=[10, 10, 10],
                    ),
                ),
                qtg.HBoxContainer(tag="row_3").add_row(
                    self._grid,
                    qtg.Image(
                        tag="image",
                        label="Image",
                        width=20,
                        height=20,
                        callback=self.event_handler,
                        image="example.jpg",
                    ),
                    self._lcd,
                    qtg.LineEdit(
                        tag="lineedit",
                        label="Line Edit",
                        text="Place Holder",
                        callback=self.event_handler,
                        width=12,
                        height=1,
                        char_length=12,
                    ),
                ),
                qtg.HBoxContainer(tag="row_4").add_row(
                    qtg.ProgressBar(
                        tag="progressbar",
                        label="Progress Bar",
                        callback=self.event_handler,
                    ),
                    qtg.HBoxContainer(text="Radio Buttons", tag="radios").add_row(
                        qtg.RadioButton(
                            tag="radio1",
                            text="Radio 1",
                            checked=True,
                            callback=self.event_handler,
                        ),
                        qtg.RadioButton(
                            tag="radio2", text="Radio 2", callback=self.event_handler
                        ),
                    ),
                    qtg.HBoxContainer(text="Switches", tag="switches").add_row(
                        qtg.Switch(
                            tag="switch", label="Switch", callback=self.event_handler
                        )
                    ),
                    qtg.Slider(
                        tag="slider", label="Slider", callback=self.event_handler
                    ),
                    qtg.Spinbox(
                        tag="spinbox", label="Spin Box", callback=self.event_handler
                    ),
                ),
                qtg.HBoxContainer(tag="row_5").add_row(
                    tab,
                    qtg.TextEdit(
                        tag="textedit",
                        label="Text Edit",
                        callback=self.event_handler,
                        height=5,
                    ),
                    qtg.Timeedit(
                        tag="timeedit", label="Time Edit", callback=self.event_handler
                    ),
                    self._treeview,
                ),
            ),
            self.menu_layout(),
            qtg.HBoxContainer().add_row(
                qtg.Button(
                    tag="popup_hi", text="Popup", callback=self.event_handler, width=10
                ),
                qtg.Button(
                    tag="ok",
                    text="OK",
                    callback=self.event_handler,
                    width=10,
                    tooltip="Exit Example 03",
                ),
            ),
        )

    def menu_layout(self) -> qtg.Menu:
        """Creates the application menu layout.

        Returns:
            Menu : The application menu:
        """
        menu = qtg.Menu(text=f"{PROGRAM_NAME} Menu", tag=f"{PROGRAM_NAME}_menu")

        # File Menu
        menu.element_add(
            parent_tag="",
            menu_element=qtg.Menu_Element(
                text="&Test", tag="test", callback=self.event_handler, tooltip=""
            ),
        )
        menu.element_add(
            parent_tag="test",
            menu_element=qtg.Menu_Element(
                text="&Level 2 Test 1",
                tag="level2_test1",
                callback=self.event_handler,
                tooltip="",
            ),
        )
        menu.element_add(
            parent_tag="test",
            menu_element=qtg.Menu_Element(
                text="&Level 2 Test 2",
                tag="level2_test",
                callback=self.event_handler,
                tooltip="",
            ),
        )
        menu.element_add(
            parent_tag="level2_test",
            menu_element=qtg.Menu_Element(
                text="&Level 3 Test",
                tag="level3_test",
                callback=self.event_handler,
                tooltip="",
            ),
        )
        menu.element_add(
            parent_tag="level3_test",
            menu_element=qtg.Menu_Element(
                text="&Level 4 Test",
                tag="level4_test",
                callback=self.event_handler,
                tooltip="",
            ),
        )
        (
            menu.element_add(
                parent_tag="level3_test", menu_element=qtg.Menu_Element(text="---")
            ),
        )
        menu.element_add(
            parent_tag="level3_test",
            menu_element=qtg.Menu_Element(
                text="&Level 4 Test 1",
                tag="level4_test1",
                callback=self.event_handler,
                tooltip="",
            ),
        )

        return menu

    def run(self):
        """Run example_01"""
        self.example_03.run(layout=self.layout())


if __name__ == "__main__":
    example_03 = Example_03()
    example_03.run()
