"""
This module implements example_04 that shows how to use the Tab Control.

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

import sys

try:
    import QTPYGUI.qtpygui as qtg
    import QTPYGUI.popups as popups
except ImportError:
    sys.path.insert(0, "../src/QTPYGUI")

    import qtpygui as qtg
    import popups


class Example_04:
    def __init__(self):
        self.example_04 = qtg.QtPyApp(
            display_name="Example 04 - Tab Control",
            callback=self.event_handler,
            height=100,
            width=100,
        )

    def event_handler(self, event: qtg.Action):
        """Handles  form events
        Args:
            event (qtg.Action): The triggering event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        match event.event:
            case qtg.Sys_Events.CLICKED:
                if event.tag == "add_page":
                    # Get tab widget
                    tab_widget = cast(
                        qtg.Tab,
                        event.widget_get(container_tag="tab_container", tag="tab"),
                    )

                    # Add page
                    page_count = tab_widget.page_count()

                    new_page_tag = f"tab_page{page_count + 1}"

                    if tab_widget.page_exists(new_page_tag):
                        tab_widget.page_remove(new_page_tag)

                    tab_widget.page_add(
                        tag=new_page_tag,
                        title=f"Page {page_count + 1}",
                        control=qtg.VBoxContainer().add_row(
                            qtg.Label(
                                text=f"Page {page_count + 1}",
                                align=qtg.Align.CENTER,
                            ),
                            qtg.Button(
                                text="Delete Page",
                                tag=f"delete_page{page_count + 1}",
                                callback=self.event_handler,
                            ),
                        ),
                    )
                elif event.tag.startswith("delete_page"):
                    # Get tab widget
                    tab_widget = cast(
                        qtg.Tab,
                        event.widget_get(container_tag="tab_container", tag="tab"),
                    )

                    page_count = tab_widget.page_count()
                    page_tag = tab_widget.current_page_tag()

                    # Never delete the first page. page_index returns 0 if first page
                    if page_count == 1 or tab_widget.page_index(page_tag) == 0:
                        popups.PopError(
                            title="Error...",
                            message="A Tab Must Have One Page And First Page Can Not Be Deleted",
                        ).show()
                    else:
                        # Delete page
                        tab_widget.page_remove(page_tag)
                        # tab_widget.page_remove(event.tag)
                elif event.tag == "ok":
                    self.example_04.app_exit()

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the window
        Returns:
            qtg.VBoxContainer: The layout
        """

        def tab_definition() -> qtg.Tab:
            """Creates the tab control definition"""

            # 1st Create a tab page layout (this could be in another function, file or method)
            # Here we have an Image with two buttons layed out horizontally under it
            tab_page_layout = qtg.VBoxContainer(align=qtg.Align.CENTER).add_row(
                qtg.Spacer(height=1),
                qtg.Image(
                    tag="image",
                    # label="Image",
                    width=20,
                    height=20,
                    callback=self.event_handler,
                    image="example.jpg",
                ),
                qtg.Spacer(height=1),
                qtg.HBoxContainer().add_row(
                    qtg.Button(
                        tag="add_page", text="Add Page", callback=self.event_handler
                    ),
                    qtg.Button(
                        tag="delete_page",
                        text="Delete Page",
                        callback=self.event_handler,
                    ),
                ),
            )

            # 2nd, Create the tab
            tab = qtg.Tab(
                tag="tab",
                label="Example Tab",
                label_font=qtg.Font(backcolor="yellow", forecolor="blue", size=20),
                callback=self.event_handler,
                width=35,
                height=13,
            )

            # 3rd, Add Pages
            tab.page_add(
                tag="tab_pg1",
                title="Page 1",
                control=tab_page_layout,
            )

            return tab

        return qtg.VBoxContainer(align=qtg.Align.BOTTOMRIGHT).add_row(
            qtg.VBoxContainer(tag="tab_container").add_row(
                tab_definition(),
            ),
            qtg.HBoxContainer().add_row(
                qtg.Button(
                    tag="ok",
                    text="OK",
                    callback=self.event_handler,
                    width=10,
                    tooltip="Exit Example 04",
                ),
            ),
        )

    def run(self):
        """Run example_01"""
        self.example_04.run(layout=self.layout())


if __name__ == "__main__":
    example_04 = Example_04()
    example_04.run()
