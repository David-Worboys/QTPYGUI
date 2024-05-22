"""
This module houses OPMS system settings pop-up.

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
import QTPYGUI.qtpygui as qtg


@dataclasses.dataclass
class sys_settings(qtg.PopContainer):
    """Performs system settings"""

    def __post_init__(self):
        self.container = self.layout()

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
        layout = qtg.VBoxContainer()
        layout.add_row(
            qtg.Command_Button_Container(
                ok_callback=self.event_handler, cancel_callback=self.event_handler
            )
        )

        return layout
