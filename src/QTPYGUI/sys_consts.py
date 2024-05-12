"""
System wide constants for dvd archiver.

Copyright (C) 2022  David Worboys (-:alumnus Moyhu Primary School et al.:-)

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

# Tell Black to leave this block alone (realm of isort)
# fmt: off
import datetime
from typing import Final

import platformdirs
try:
    from file_utils import App_Path, File
    from utils import strEnum
except ImportError:
    from .file_utils import App_Path, File
    from .utils import strEnum

# fmt: on

executable_folder = App_Path()

file_sep = File().ossep

PROGRAM_NAME: Final[str] = "Not Set"
PROGRAM_VERSION: Final[str] = "Not Set"
AUTHOR: Final[str] = "Not Set"
LICENCE: Final[str] = "GNU V3 GPL"


def COPYRIGHT_YEAR() -> str:
    """
    The COPYRIGHT_YEAR function returns the current year if it is 2024, otherwise it returns a string of the
    form '2024-&lt;current_year&gt;'.

    Returns:
        str: The current year, or the current year and the next if it's 2024

    """
    return f"{'2022' if str(datetime.date.today().year) == '2024' else '2024-' + str(datetime.date.today().year)}"


VERSION_TAG = (
    f"{PROGRAM_VERSION} {LICENCE} (c){COPYRIGHT_YEAR()} {AUTHOR} {PROGRAM_NAME}"
)

SDELIM = (  # Used to delimit strings - particularly non-translatable sections of strings
    "||"
)

# Database Setting Keys
APP_LANG_DBK: Final[str] = "app_lang"  # All qtgui apps
APP_COUNTRY_DBK: Final[str] = "app_country"  # All qtgui apps


class SPECIAL_PATH(strEnum):
    """Contains enums for strings that represent special paths on the user's computer"""

    DESKTOP: Final[str] = platformdirs.user_desktop_dir()
    DOCUMENTS: Final[str] = platformdirs.user_documents_dir()
    DOWNLOADS: Final[str] = platformdirs.user_downloads_dir()
    MUSIC: Final[str] = platformdirs.user_music_dir()
    PICTURES: Final[str] = platformdirs.user_pictures_dir()
    VIDEOS: Final[str] = platformdirs.user_videos_dir()
