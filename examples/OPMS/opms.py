"""
This module implements an example Optometrist Patient Management System  that
shows how to use QTPYGUI for a line og busines application.

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

import QTPYGUI.qtpygui as qtg
import QTPYGUI.popups as popups
import sys_consts
import database


class OPMS:
    def __init__(self):
        self.opms = qtg.QtPyApp(
            display_name="OPMS",
            callback=self.event_handler,
            height=100,
            width=100,
        )

    def event_handler(self, event: qtg.Action):
        """Handles  form events
        Args:
            event (qtg.Action): The triggering event
        """
        print(
            f"DBG {event.event=} {event.action=} {event.container_tag=} {event.tag} {event.value}"
        )
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        match event.event:
            case qtg.Sys_Events.APPPOSTINIT:
                self.startup_handler()
            case qtg.Sys_Events.CLICKED:
                pass
            case qtg.Sys_Events.MENUCLICKED:
                match event.tag:
                    case "about":
                        informative_text = (
                            '<h2 style="text-align: center;"><strong><span style="color:'
                            f' #3366ff;">{sys_consts.PROGRAM_NAME} - {sys_consts.PROGRAM_VERSION}'
                            f'</span></strong></h2><p style="text-align: center;">&#169;'
                            f' {sys_consts.COPYRIGHT_YEAR()} </p><p style="text-align: center;">'
                            f' <br/><img src={qtg.App_Path("logo.jpg")} width="300"  /></p>'
                            f'<p style="text-align: center;">Created & Coded By: '
                            f'{sys_consts.AUTHOR}</p><p style="text-align:'
                            f' center;">License: {sys_consts.LICENCE}</p>'
                        )

                        popups.PopAbout(
                            title="About",
                            informative_text=informative_text,
                            informative_font=qtg.Font(size=13, backcolor="wheat"),
                            height=20,
                            border=qtg.Widget_Frame(
                                frame=qtg.Frame.RAISED,
                                frame_style=qtg.Frame_Style.PANEL,
                                line_width=1,
                            ),
                        ).show()
                    case "app_exit":
                        self.opms.app_exit()

    def startup_handler(self):
        """Handles OPMS startup activities"""

        result = database.database_setup().configure_database()

        if result == -1:
            popups.PopError(
                title="Startup Error",
                message="Could not configure database.\n Shutting Down",
            ).show()
            self.opms.app_exit()

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the OPMS main window
        Returns:
            qtg.VBoxContainer: The OPMS main window layout
        """

        def main_menu() -> qtg.Menu:
            """Creates the OPMS main menu

            Returns:
                qtg.Menu: The main menu
            """
            menu = qtg.Menu(container_tag="main_menu", tag="main_menu")

            # Top level menu elements
            menu.element_add(
                parent_tag="",
                menu_element=qtg.Menu_Element(
                    text="&File", tag="file", callback=self.event_handler
                ),
            )

            menu.element_add(
                parent_tag="",
                menu_element=qtg.Menu_Element(
                    text="&Help", tag="help", callback=self.event_handler
                ),
            )

            # File menu elements - note tag file
            menu.element_add(
                parent_tag="file",
                menu_element=qtg.Menu_Element(
                    separator=True,
                ),
            )

            menu.element_add(
                parent_tag="file",
                menu_element=qtg.Menu_Element(
                    text="&Exit", tag="app_exit", callback=self.event_handler
                ),
            )

            # Help menu elements - note tag help
            menu.element_add(
                parent_tag="help",
                menu_element=qtg.Menu_Element(
                    text="&About",
                    tag="about",
                    callback=self.event_handler,
                ),
            )

            return menu

        return qtg.VBoxContainer(
            align=qtg.Align.BOTTOMRIGHT,
            pixel_unit=True,
            width=self.opms.available_width - 50,
            height=self.opms.available_height - 50,
        ).add_row(
            main_menu(),
        )

    def run(self):
        """Run OPMS (Optometrist Patient Management System)"""
        self.opms.run(layout=self.layout())


if __name__ == "__main__":
    opms = OPMS()
    opms.run()
