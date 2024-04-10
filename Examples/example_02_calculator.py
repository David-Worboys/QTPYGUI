"""
This module implements example_02 that shows how to implement a basic calculator.

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

from typing import Final

import popups
import qtpygui as qtg

MAX_DIGITS: Final[int] = 8


class Example_02:
    def __init__(self):
        self.example_02 = qtg.QtPyApp(
            display_name="Example 02 - Calculator",
            callback=self.event_handler,
            height=100,
            width=100,
        )

        self.display_buffer = []
        self.hold_buffer = []
        self.operation = ""
        self.exit = False

    def event_handler(self, event: qtg.Action):
        """Handles  form events
        Args:
            event (qtg.Action): The triggering event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        match event.event:
            case qtg.Sys_Events.APPCLOSED:
                if not self.exit:
                    self.exit = True
                    self.exit_calculator()

            case qtg.Sys_Events.CLICKED:
                if event.tag.startswith("btn_"):
                    if len(self.display_buffer) >= MAX_DIGITS:
                        popups.PopError(
                            title="Error..", message="Too Many Digits Entered"
                        ).show()
                    else:
                        self.display_buffer.append(event.tag[4:])
                        display_value = "".join(self.display_buffer)
                        event.value_set(
                            container_tag="calculator",
                            tag="lcd_display",
                            value=display_value,
                        )
                elif event.tag.startswith("oper_"):
                    if self.display_buffer and self.hold_buffer:
                        self.execute_command(event)

                    self.hold_buffer = self.display_buffer
                    self.display_buffer = []
                    self.operation = event.tag[5:]

                elif event.tag.startswith("cmd_"):
                    match event.tag:
                        case "cmd_clear":
                            self.display_buffer = []
                            event.value_set(
                                container_tag="calculator", tag="lcd_display", value=0
                            )
                        case "cmd_backspace":
                            if len(self.display_buffer) > 0:
                                self.display_buffer.pop()
                                display_value = "".join(self.display_buffer)
                                event.value_set(
                                    container_tag="calculator",
                                    tag="lcd_display",
                                    value=display_value,
                                )
                        case "cmd_=":
                            self.execute_command(event)
                else:
                    match event.tag:
                        case "exit":
                            if not self.exit:
                                self.exit = True
                                self.exit_calculator()

                        case "btn_1":
                            event.value_set(
                                container_tag="calculator", tag="lcd_display", value=1
                            )

    def exit_calculator(self):
        """Exits the calculator"""
        if (
            popups.PopYesNo(
                title="Exit",
                message="Are you sure you want to exit?",
                callback=self.event_handler,
            ).show()
            == "yes"
        ):
            self.example_02.app_exit()

    def execute_command(self, event: qtg.Action):
        """Executes the operation selected by the user

        Args:
            event (qtg.Action): The triggering event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        if self.operation == "":
            popups.PopError(title="Error..", message="No Operation Selected").show()

        else:
            display_value = "".join(self.display_buffer)
            hold_value = "".join(self.hold_buffer)

            if self.operation == "+":
                result = float(display_value) + float(hold_value)
            elif self.operation == "-":
                result = float(hold_value) - float(display_value)
            elif self.operation == "*":
                result = float(hold_value) * float(display_value)
            elif self.operation == "/":
                result = float(hold_value) / float(display_value)
            else:
                result = ""

            event.value_set(
                container_tag="calculator", tag="lcd_display", value=f"{result}"
            )

            self.operation = ""
            self.hold_buffer = []
            self.display_buffer = [digit for digit in str(result)]

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the window
        Returns:
            qtg.VBoxContainer: The layout
        """
        operation_buttons = qtg.VBoxContainer(tag="operation_buttons").add_row(
            qtg.Button(tag="oper_/", text="/", callback=self.event_handler, width=3),
            qtg.Button(tag="oper_*", text="*", callback=self.event_handler, width=3),
            qtg.Button(tag="oper_-", text="-", callback=self.event_handler, width=3),
            qtg.Button(tag="oper_+", text="+", callback=self.event_handler, width=3),
            qtg.Spacer(height=2),
        )

        calc_buttons = qtg.VBoxContainer(tag="calc_buttons").add_row(
            qtg.HBoxContainer(tag="row_1").add_row(
                qtg.Button(tag="btn_7", text="7", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_8", text="8", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_9", text="9", callback=self.event_handler, width=3),
            ),
            qtg.HBoxContainer(tag="row_2").add_row(
                qtg.Button(tag="btn_4", text="4", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_5", text="5", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_6", text="6", callback=self.event_handler, width=3),
            ),
            qtg.HBoxContainer(tag="row_3").add_row(
                qtg.Button(tag="btn_1", text="1", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_2", text="2", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_3", text="3", callback=self.event_handler, width=3),
            ),
            qtg.HBoxContainer(tag="row_4").add_row(
                qtg.Button(tag="btn_0", text="0", callback=self.event_handler, width=3),
                qtg.Button(tag="btn_.", text=".", callback=self.event_handler, width=3),
                qtg.Button(tag="cmd_=", text="=", callback=self.event_handler, width=3),
            ),
            qtg.HBoxContainer(tag="row_5").add_row(
                qtg.Button(
                    tag="cmd_clear", text="C", callback=self.event_handler, width=3
                ),
                qtg.Button(
                    tag="exit",
                    text="&Exit",
                    width=7,
                    callback=self.event_handler,
                    tooltip="Exit Example 02",
                ),
            ),
        )

        return qtg.VBoxContainer(
            tag="calculator", margin_right=20, align=qtg.Align.BOTTOMCENTER
        ).add_row(
            qtg.LCD(
                tag="lcd_display",
                width=23,
                height=3,
            ),
            qtg.HBoxContainer(align=qtg.Align.HCENTER).add_row(
                calc_buttons,
                operation_buttons,
            ),
        )

    def run(self):
        """Run example_02"""
        self.example_02.run(layout=self.layout())


if __name__ == "__main__":
    example_02 = Example_02()
    example_02.run()
