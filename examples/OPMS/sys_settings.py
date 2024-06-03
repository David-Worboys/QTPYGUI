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
from typing import cast

import QTPYGUI.qtpygui as qtg
import QTPYGUI.popups as popups

from password import password_popup


@dataclasses.dataclass
class sys_settings(qtg.PopContainer):
    """Performs system settings"""

    title: str = ""

    def __post_init__(self):
        """Sets-up the form"""
        assert (
            isinstance(self.title, str) and self.title.strip() != ""
        ), f"{self.title=}. Must be a non-empty str"

        self.container = self.layout()

        super().__post_init__()  # This statement must be last

    def event_handler(self, event: qtg.Action):
        """Master control event processing of the popup window

        Args:
            event (Action): event raising this control event
        """
        print(
            f"DBG {event.event=} {event.action=} {event.container_tag=} {event.tag=} {event.value=}"
        )

        match event.event:
            case qtg.Sys_Events.CLICKED:
                match event.tag:
                    case "cancel":
                        super().close()
                    case "ok":
                        super().close()
                    case "user_admin":
                        password_popup(
                            title="User Admin", user_name="admin", new_cfg=True
                        ).show()
            case qtg.Sys_Events.TEXTCHANGED:
                # Note the use of CSV files is for illustration, ideally a database would be used
                match event.tag:
                    case "default_country":
                        self.default_country_handler(event)
                    case "default_state":
                        self.default_state_handler(event)

    def default_state_handler(self, event):
        """Event handler for the default state selection

        Args:
            event (Action): event raising this control event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        if (
            event.widget_exist(container_tag="default_details", tag="default_country")
            and event.widget_exist(container_tag="default_details", tag="default_state")
            and event.widget_exist(container_tag="default_details", tag="default_city")
        ):
            country_combobox: qtg.ComboBox = cast(
                qtg.ComboBox,
                event.widget_get(
                    container_tag="default_details",
                    tag="default_country",
                ),
            )

            state_combobox: qtg.ComboBox = cast(
                qtg.ComboBox,
                event.widget_get(container_tag="default_details", tag="default_state"),
            )

            city_combobox: qtg.ComboBox = cast(
                qtg.ComboBox,
                event.widget_get(container_tag="default_details", tag="default_city"),
            )

            country_iso_code = country_combobox.value_get().data
            state_code = state_combobox.value_get().data

            # Note the use of CSV files is for illustration, ideally a database would be used
            result, message = city_combobox.load_csv_file(
                csv_file_def=qtg.CSV_File_Def(
                    file_name=qtg.App_Path("cities.csv"),
                    text_index=2,
                    data_index=3,
                    ignore_header=False,
                    filter=[
                        (6, f"{country_iso_code}"),
                        (4, f"{state_code}"),
                    ],
                    ignore_errors=True,
                )
            )

            if result == -1:
                popups.PopError(title="CSV Load Error..", message=message).show()

    def default_country_handler(self, event: qtg.Action):
        """Event handler for the default country selection

        Args:
            event (Action): event raising this control event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        if (
            event.widget_exist(container_tag="default_details", tag="default_country")
            and event.widget_exist(container_tag="default_details", tag="default_state")
            and event.widget_exist(container_tag="default_details", tag="default_city")
        ):
            country_iso_code = event.value.data

            state_combobox: qtg.ComboBox = cast(
                qtg.ComboBox,
                event.widget_get(container_tag="default_details", tag="default_state"),
            )
            state_combobox.clear()

            city_combobox: qtg.ComboBox = cast(
                qtg.ComboBox,
                event.widget_get(container_tag="default_details", tag="default_city"),
            )
            city_combobox.clear()

            # Note the use of CSV files is for illustration, ideally a database would be used
            result, message = state_combobox.load_csv_file(
                csv_file_def=qtg.CSV_File_Def(
                    file_name=qtg.App_Path("subdivisions.csv"),
                    text_index=3,
                    data_index=2,
                    ignore_header=False,
                    filter=[(1, f"{country_iso_code}")],
                    ignore_errors=True,
                )
            )

            if result == -1:
                popups.PopError(title="CSV Load Error..", message=message).show()

    def layout(self) -> qtg.VBoxContainer:
        """Defines the layout of the system settings popup window
        Returns
            VBoxContainer: The system settings popup window layout container
        """
        layout = qtg.VBoxContainer(align=qtg.Align.BOTTOMRIGHT)

        # Define company details user interface
        company_container = qtg.FormContainer(text="Company Details").add_row(
            qtg.LineEdit(
                label="Name", tag="name", callback=self.event_handler, width=40
            ),
            qtg.LineEdit(
                label="Address", tag="address", callback=self.event_handler, width=40
            ),
            qtg.LineEdit(
                label="Phone",
                tag="phone",
                callback=self.event_handler,
                width=13,
                input_mask="(9999) 999-9999",
            ),
            qtg.LineEdit(
                label="Email", tag="email", callback=self.event_handler, width=40
            ),
            qtg.LineEdit(
                label="Website", tag="website", callback=self.event_handler, width=40
            ),
        )

        # Note the use of CSV files is for illustration, ideally a database would be used
        country_combo = qtg.ComboBox(
            label="Country",
            tag="default_country",
            callback=self.event_handler,
            width=40,
            csv_file_def=qtg.CSV_File_Def(
                file_name=qtg.App_Path("countries.csv"), text_index=2, data_index=4
            ),
        )

        default_company_details_container = qtg.FormContainer(
            tag="default_details", text="Default Company Details"
        ).add_row(
            country_combo,
            qtg.ComboBox(
                label="State",
                tag="default_state",
                callback=self.event_handler,
                width=40,
            ),
            qtg.ComboBox(
                label="City",
                tag="default_city",
                callback=self.event_handler,
                width=20,
                editable=True,
                buddy_control=qtg.LineEdit(
                    label="Postcode",
                    tag="postcode",
                    callback=self.event_handler,
                    width=10,
                    char_length=10,
                ),
            ),
        )

        # Want the user interface controls aligned left
        data_input_container = qtg.VBoxContainer(align=qtg.Align.LEFT).add_row(
            company_container,
            default_company_details_container,
        )

        (
            layout.add_row(
                data_input_container,
                qtg.HBoxContainer().add_row(
                    qtg.Button(
                        text="User Admin",
                        tag="user_admin",
                        callback=self.event_handler,
                        width=11,
                    ),
                    qtg.Spacer(width=18),
                    qtg.Command_Button_Container(
                        ok_callback=self.event_handler,
                        cancel_callback=self.event_handler,
                        margin_right=9,
                    ),
                ),
            ),
        )

        return layout
