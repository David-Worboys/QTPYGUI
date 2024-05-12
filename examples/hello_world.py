"""
This module implements a hello world that shows how to use the QTPYGUI.

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

sys.path.insert(0, "../src/QTPYGUI")

import qtpygui as qtg


class Hello_World:
    def __init__(self):
        self.hello_world = qtg.QtPyApp(
            display_name="Hello World",
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
                match event.tag:
                    case "ok":
                        self.hello_world.app_exit()

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the window
        Returns:
            qtg.VBoxContainer: The layout
        """
        return qtg.VBoxContainer(align=qtg.Align.BOTTOMRIGHT).add_row(
            qtg.FormContainer().add_row(
                qtg.Label(
                    text="Hello World!",
                    txt_fontsize=48,
                    txt_align=qtg.Align.CENTER,
                    txt_font=qtg.Font(backcolor="blue", forecolor="yellow"),
                ),
            ),
            qtg.HBoxContainer().add_row(
                qtg.Button(
                    tag="ok",
                    text="OK",
                    callback=self.event_handler,
                    width=10,
                    tooltip="Exit Example 01",
                ),
            ),
        )

    def run(self):
        """Run example_01"""
        self.hello_world.run(layout=self.layout())


if __name__ == "__main__":
    hello_world = Hello_World()
    hello_world.run()
