"""
This module houses OPMS password setting pop-up.

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

import dataclasses
from typing import cast

import QTPYGUI.qtpygui as qtg
import QTPYGUI.popups as popups


@dataclasses.dataclass
class password_popup(qtg.PopContainer):
    """Performs system settings"""

    title: str = ""
    user_name: str = ""
    new_cfg: bool = False

    def __post_init__(self):
        """Sets-up the form"""
        assert (
            isinstance(self.title, str) and self.title.strip() != ""
        ), f"{self.title=}. Must be a non-empty str"

        self.container = self.layout()

        assert (
            isinstance(self.user_name, str) and self.user_name.strip() != ""
        ), f"{self.user_name=}. Must be a non-empty string"
        assert isinstance(self.new_cfg, bool), f"{self.new_cfg=}. Must be a bool"

        super().__post_init__()  # This statement must be last

    def event_handler(self, event: qtg.Action):
        """Master control event processing of the popup window

        Args:
            event (Action): event raising this control event
        """
        match event.event:
            case qtg.Sys_Events.CLICKED:
                match event.tag:
                    case "cancel":
                        super().close()
                    case "ok":
                        super().close()

    def layout(self) -> qtg.VBoxContainer:
        """Defines the layout of the system settings popup window
        Returns
            VBoxContainer: The system settings popup window layout container
        """
        layout = qtg.VBoxContainer(align=qtg.Align.BOTTOMRIGHT)

        # Define OPMS administrator user interface
        admin_container = qtg.FormContainer(text="User Details").add_row(
            qtg.LineEdit(
                label="User Name",
                tag="user_name",
                text=self.user_name,
                callback=self.event_handler,
                width=10,
                char_length=20,
            ),
            qtg.LineEdit(
                label="Password",
                tag="password",
                callback=self.event_handler,
                width=10,
                input_mask="@XXXXXXXXXX",
                char_length=10,
                buddy_control=qtg.LineEdit(
                    label="Confirm Password",
                    tag="confirm_password",
                    callback=self.event_handler,
                    width=10,
                    input_mask="@XXXXXXXXXX",
                    char_length=10,
                ),
            ),
        )

        # Want the user interface controls aligned left
        data_input_container = qtg.VBoxContainer(align=qtg.Align.LEFT).add_row(
            admin_container,
        )

        layout.add_row(
            data_input_container,
            qtg.Command_Button_Container(
                ok_callback=self.event_handler,
                cancel_callback=self.event_handler,
                margin_right=9,
            ),
        )

        return layout
