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

# Note, these are fully loaded examples and most of the arguments will not be needed in a real program.
# Refer to README.md for the user manual

import sys

try:
    import QTPYGUI.qtpygui as qtg
    import QTPYGUI.popups as popups
except ImportError:
    sys.path.insert(0, "../src/QTPYGUI")

    import qtpygui as qtg
    import popups


class Example_03:
    def __init__(self):
        self._grid = None
        self._lcd = None
        self._menu = None
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

        #print(f"DBG {event.event=} {event.container_tag=} {event.tag=} {event.value=}")
        match event.event:
            case qtg.Sys_Events.APPPOSTINIT:
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
            case qtg.Sys_Events.MENUCLICKED:
                pass

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the window
        Returns:
            qtg.VBoxContainer: The layout
        """

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
            grid_items=[
                qtg.Grid_Item(
                    row_index=0,
                    col_index=0,
                    current_value="value 1",
                    user_data=None,
                    tag="",
                ),
                qtg.Grid_Item(
                    row_index=0,
                    col_index=1,
                    current_value="value 2",
                    user_data=None,
                    tag="",
                ),
                qtg.Grid_Item(
                    row_index=1,
                    col_index=0,
                    current_value="value 3",
                    user_data=None,
                    tag="",
                ),
                qtg.Grid_Item(
                    row_index=1,
                    col_index=1,
                    current_value="value 4",
                    user_data=None,
                    tag="",
                ),
            ],
            height=3,
            label_align=qtg.Align_Text.CENTER,
            label_width=10,
            label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, backcolor="red", size=14),
            txt_align=qtg.Align_Text.CENTER,
            txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=15),
            txt_fontsize=12,
            bold=True,
            italic=True,
            underline=True,
            enabled=True,
            visible=True,
            tooltip="Grid",
            tune_hsize=15,
            tune_vsize=15,
            user_data={"key": "value"},
            buddy_control=qtg.HBoxContainer().add_row(
                qtg.Spacer(width=1),
                qtg.Button(
                    tag="grid_push",
                    text="Grid Push Me!",
                    callback=self.event_handler,
                    width=12,
                ),
            ),
        )

        self._lcd = qtg.LCD(
            tag="lcd",
            label="LCD",
            callback=self.event_handler,
            label_align=qtg.Align_Text.CENTER,
            label_width=10,
            label_font=qtg.Font(
                style=qtg.Font_Style.OBLIQUE, backcolor="yellow", size=14
            ),
            txt_font=qtg.Font(size=1),
            txt_align=qtg.Align_Text.LEFT,
            text="88888",
            width=8,
            height=1,
            txt_fontsize=12,
            enabled=True,
            visible=True,
            tooltip="LCD Control",
            tune_hsize=15,
            tune_vsize=15,
            user_data={"key": "value"},
            buddy_control=qtg.HBoxContainer().add_row(
                qtg.Spacer(width=1),
                qtg.Button(
                    tag="lcd_button",
                    text="Press Me!",
                    callback=self.event_handler,
                    width=12,
                ),
            ),
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
            control=qtg.VBoxContainer(align=qtg.Align.HCENTER).add_row(
                qtg.Image(
                    tag="image",
                    label="Image",
                    width=20,
                    height=20,
                    callback=self.event_handler,
                    image="example.jpg",
                ),
                qtg.Spacer(height=1),
                qtg.Button(
                    tag="button",
                    label="Button",
                    text="Tab Button",
                    callback=self.event_handler,
                ),
                qtg.Spacer(height=1),
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
                qtg.HBoxContainer(
                    tag="row_1",
                ).add_row(
                    qtg.Button(
                        tag="button_1",
                        text="Button",
                        label="Button 1",
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
                        callback=self.event_handler,
                        width=10,
                        height=1,
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=20),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="Button 1 Press Me",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Checkbox(
                                tag="checkbox_check",
                                text="Tick Me!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
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
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
                        width=6,
                        height=1,
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=20),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="Check Box Press Me",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Button(
                                tag="button_push",
                                text="Push Me!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
                    ),
                    qtg.ComboBox(
                        tag="combo_box",
                        label="Combo Box",
                        display_na=True,
                        dropdown_width=35,
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
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
                        width=8,
                        height=1,
                        txt_font=qtg.Font(style=qtg.Font_Style.ITALIC, size=12),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="Check Box Press Me",
                        tune_hsize=15,
                        tune_vsize=1,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Button(
                                tag="button_push2",
                                text="Push Me 2!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
                    ),
                    qtg.Spacer(),
                ),
                qtg.HBoxContainer(tag="row_2").add_row(
                    qtg.Label(
                        tag="example03",
                        label="Label",
                        text="Example 03",
                        label_font=qtg.Font(
                            font_name="Courier",
                            style=qtg.Font_Style.OBLIQUE,
                            size=42,
                            backcolor="yellow",
                            forecolor="blue",
                        ),
                        txt_fontsize=42,
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(
                            font_name="DejaVu Sans Mono",
                            backcolor="blue",
                            forecolor="yellow",
                            size=50,
                        ),
                        width=8,
                        frame=qtg.Widget_Frame(
                            frame_style=qtg.Frame_Style.BOX,
                            frame=qtg.Frame.RAISED,
                            line_width=5,
                            midline_width=2,
                        ),
                        # height=2,
                        tune_hsize=30,
                        tune_vsize=15,
                    )
                ),
                qtg.HBoxContainer(tag="row_3").add_row(
                    qtg.Dateedit(
                        tag="dateedit", label="Date Edit", callback=self.event_handler
                    ),
                    qtg.Dateedit(
                        tag="dateedit2",
                        text="Date Edit 2",
                        date="2022-01-01",
                        format="yyyy-MM-dd",
                        max_date="2132-01-01",
                        min_date="2000-01-01",
                        label="Date edit 2",
                        callback=self.event_handler,
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
                        width=6,
                        height=1,
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=20),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="Date Edit 2 ",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Button(
                                tag="dateedit_button_push",
                                text="Date Edit 2 Push Me!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
                    ),
                    qtg.FolderView(
                        tag="folderview",
                        label="Folder View",
                        callback=self.event_handler,
                        height=5,
                        header_widths=[10, 10, 10, 10],
                        multiselect=False,
                        click_expand=False,
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=20),
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=14),
                        header_font=qtg.Font(
                            style=qtg.Font_Style.OBLIQUE,
                            backcolor="cyan",
                            forecolor="orange",
                            size=20,
                        ),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="FolderView Press Me",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Button(
                                tag="folderview_button_push",
                                text="Push Me!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
                    ),
                ),
                qtg.HBoxContainer(tag="row_3").add_row(
                    self._grid,
                    qtg.Image(
                        tag="image",
                        label="Image",
                        width=13,
                        height=10,
                        callback=self.event_handler,
                        image="example.jpg",
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=12),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="Image Press Me",
                        tune_hsize=1,
                        tune_vsize=1,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Button(
                                tag="image_button_push",
                                text="Push Me!",
                                callback=self.event_handler,
                                width=12,
                                height=2,
                            ),
                        ),
                    ),
                    qtg.LCD(
                        tag="lcd",
                        label="LCD",
                        callback=self.event_handler,
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(
                            style=qtg.Font_Style.OBLIQUE, backcolor="yellow", size=14
                        ),
                        txt_font=qtg.Font(size=12),
                        digit_count=9,
                        text="-123456.7",
                        width=9,
                        height=1,
                        txt_fontsize=12,
                        enabled=True,
                        visible=True,
                        tooltip="LCD Control",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Spacer(width=1),
                            qtg.Button(
                                tag="lcd_button",
                                text="Press Me!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
                    ),
                    qtg.LineEdit(
                        tag="lineedit",
                        label="Line Edit",
                        text="Place Holder",
                        callback=self.event_handler,
                        input_mask="(9999) 999-9999",
                        width=15,
                        height=1,
                        char_length=15,
                        label_align=qtg.Align_Text.CENTER,
                        label_width=10,
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=10),
                        txt_align=qtg.Align_Text.CENTER,
                        txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=10),
                        txt_fontsize=12,
                        bold=True,
                        italic=True,
                        underline=True,
                        enabled=True,
                        visible=True,
                        tooltip="LineEDit ",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Checkbox(
                                tag="telephone_checkbox_check",
                                text="Phone Number!",
                                callback=self.event_handler,
                                width=13,
                            ),
                        ),
                    ),
                ),
                qtg.HBoxContainer(tag="row_4").add_row(
                    qtg.ProgressBar(
                        tag="progressbar",
                        label="Progress Bar",
                        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=10),
                        callback=self.event_handler,
                        horizontal=True,
                        width=15,
                        height=1,
                        range_min=0,
                        range_max=200,
                        enabled=True,
                        visible=True,
                        tooltip="Progress Bar",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Button(
                                tag="progressbar_button",
                                text="Press Me!",
                                callback=self.event_handler,
                                width=12,
                            ),
                        ),
                    ),
                    qtg.HBoxContainer(text="Radio Buttons", tag="radios").add_row(
                        qtg.RadioButton(
                            tag="radio1",
                            text="Radio 1",
                            checked=True,
                            callback=self.event_handler,
                            label="Radio Button 1",
                            label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=10),
                            enabled=True,
                            visible=True,
                            tooltip="Radio Button",
                            tune_hsize=15,
                            tune_vsize=15,
                            user_data={"key": "value"},
                            buddy_control=qtg.HBoxContainer().add_row(
                                qtg.Button(
                                    tag="radio_button_push",
                                    text="R1 Push Me!",
                                    callback=self.event_handler,
                                    width=15,
                                    height=1,
                                )
                            ),
                        ),
                        qtg.RadioButton(
                            tag="radio2", text="Radio 2", callback=self.event_handler
                        ),
                    ),
                    qtg.HBoxContainer(text="Switches", tag="switches").add_row(
                        qtg.Switch(
                            tag="switch1",
                            label="SW1 Off",
                            text="SW1 On!",
                            callback=self.event_handler,
                            label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=10),
                            txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=15),
                            enabled=True,
                            visible=True,
                            height=1,
                            tooltip="Sw 1",
                            tune_hsize=-15,
                            tune_vsize=-10,
                            user_data={"key": "value"},
                            buddy_control=qtg.HBoxContainer().add_row(
                                qtg.Button(
                                    tag="switch_button_push",
                                    text="SW1 Push Me!",
                                    callback=self.event_handler,
                                    width=15,
                                    height=1,
                                )
                            ),
                        ),
                        qtg.Switch(
                            tag="switch2",
                            label="SW2 Off",
                            text="SW2On!",
                            callback=self.event_handler,
                        ),
                    ),
                    qtg.Slider(
                        tag="slider",
                        label="Slider",
                        callback=self.event_handler,
                        range_max=500,
                        range_min=0,
                        label_font=qtg.Font(
                            style=qtg.Font_Style.OBLIQUE, backcolor="yellow", size=15
                        ),
                        enabled=True,
                        visible=True,
                        tooltip="Sliders",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Button(
                                tag="slider_push",
                                text="Sliders!",
                                callback=self.event_handler,
                                width=10,
                                height=1,
                            )
                        ),
                    ),
                ),
                qtg.HBoxContainer(tag="row_5").add_row(
                    qtg.Spinbox(
                        tag="spinbox",
                        label="Spin Box",
                        prefix="Far ",
                        suffix=" km",
                        callback=self.event_handler,
                        range_max=500,
                        range_min=0,
                        width=8,
                        height=1,
                        label_font=qtg.Font(
                            style=qtg.Font_Style.OBLIQUE,
                            backcolor="blue",
                            font_name="DejaVu Sans Mono",
                            forecolor="yellow",
                            size=10,
                        ),
                        enabled=True,
                        visible=True,
                        tooltip="Spin Box",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Button(
                                tag="spinbox_push",
                                text="Spin Box!",
                                callback=self.event_handler,
                                width=10,
                                height=1,
                            )
                        ),
                    ),
                    tab,
                    qtg.TextEdit(
                        tag="textedit",
                        text="Text Edit",
                        label="Text Edit",
                        callback=self.event_handler,
                        height=5,
                        max_chars=10,
                        word_wrap=True,
                        label_font=qtg.Font(
                            style=qtg.Font_Style.OBLIQUE,
                            backcolor="blue",
                            forecolor="yellow",
                            size=12,
                        ),
                        txt_font=qtg.Font(
                            style=qtg.Font_Style.NORMAL,
                            backcolor="yellow",
                            size=15,
                            font_name="DejaVu Sans Mono",
                        ),
                        enabled=True,
                        visible=True,
                        tooltip="Text Edit",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Button(
                                tag="textedit_push",
                                text="Text Edit!",
                                callback=self.event_handler,
                                width=10,
                                height=1,
                            )
                        ),
                    ),
                    qtg.Timeedit(
                        tag="timeedit",
                        label="Time Edit",
                        hour=12,
                        min=23,
                        sec=1,
                        msec=0,
                        callback=self.event_handler,
                        txt_font=qtg.Font(
                            style=qtg.Font_Style.NORMAL,
                            backcolor="wheat",
                            forecolor="darkgray",
                            size=15,
                            font_name="DejaVu Sans Mono",
                        ),
                        label_font=qtg.Font(
                            style=qtg.Font_Style.OBLIQUE,
                            backcolor="blue",
                            forecolor="yellow",
                            size=20,
                        ),
                        enabled=True,
                        visible=True,
                        tooltip="Time Edit",
                        tune_hsize=15,
                        tune_vsize=15,
                        user_data={"key": "value"},
                        buddy_control=qtg.HBoxContainer().add_row(
                            qtg.Button(
                                tag="timeedit_push",
                                text="Time Edit!",
                                callback=self.event_handler,
                                width=10,
                                height=1,
                            )
                        ),
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
        menu = qtg.Menu(container_tag="main_menu", tag="top_level")

        # File Menu
        menu.element_add(
            parent_tag="",
            menu_element=qtg.Menu_Element(
                text="&Test", tag="test", callback=self.event_handler, tooltip="Test"
            ),
        )
        menu.element_add(
            parent_tag="test",
            menu_element=qtg.Menu_Element(
                text="&Level 2 Test 1",
                tag="level2_test1",
                callback=self.event_handler,
                tooltip="Test 2",
            ),
        )
        menu.element_add(
            parent_tag="test",
            menu_element=qtg.Menu_Element(
                separator=True,
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
                checkable=True,
                font=qtg.Font(style=qtg.Font_Style.ITALIC, forecolor="red", size=14),
                tooltip="level4_test",
                icon=qtg.Sys_Icon.filenew.get(),
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
                visible=False,
            ),
        )

        return menu

    def run(self):
        """Run example_01"""
        self.example_03.run(layout=self.layout())


if __name__ == "__main__":
    example_03 = Example_03()
    example_03.run()
