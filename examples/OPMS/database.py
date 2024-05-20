"""
This module houses OPMS database configuration and query classes.

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


@dataclasses.dataclass(slots=True)
class database_setup():
    """Performs database configuration operations"""

    def configure_database(self) -> int:
        """Configures the database for use

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1
