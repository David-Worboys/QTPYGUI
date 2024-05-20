"""
This module houses OPMS system wide constants.

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

import datetime
from typing import Final

PROGRAM_NAME: Final[str] = "OPMS"
PROGRAM_VERSION: Final[str] = "0.0.1"
AUTHOR: Final[str] = "David Worboys"
LICENCE: Final[str] = "GNU V3 GPL"


def COPYRIGHT_YEAR() -> str:
    """
    The COPYRIGHT_YEAR function returns the current year if it is 2024, otherwise it returns a string of the
    form '2024-&lt;current_year&gt;'.

    Returns:
        str: The current year, or the current year and the next if it's 2024

    """
    return f"{'2024' if str(datetime.date.today().year) == '2024' else '2024-' + str(datetime.date.today().year)}"


VERSION_TAG = (
    f"{PROGRAM_NAME} {PROGRAM_VERSION} {LICENCE} (c){COPYRIGHT_YEAR()} {AUTHOR} "
)
