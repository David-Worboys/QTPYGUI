"""
This module is used to translate text from one language to another.

Copyright (C) 2018  David Worboys (-:alumnus Moyhu Primary School et al.:-)

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

import re
import platformdirs
from typing import Optional, Final

try:
    from sqldb import SQLDB, App_Settings, ColDef, SQL
    from file_utils import File
    from utils import Is_Complied, Singleton
except ImportError:
    from .sqldb import SQLDB, App_Settings, ColDef, SQL
    from .file_utils import File
    from .utils import Is_Complied, Singleton


class Lang_Tran(metaclass=Singleton):
    """
    This class is used to translate text from one language to another.
        - 2022-05 Rewritten by David Worboys to use sqllite storage.
    """

    APP_LANG_DB_KEY: Final[str] = "app_lang_db_key"
    SDELIM: Final[str] = (
        "||"  # Delimiter used to cut out sections of the string that do not need translating
    )

    def __init__(self, program_name: str):
        assert isinstance(program_name, str) and program_name.strip() != "", (
            f"{program_name=}. Must be a non-empty str"
        )

        self._program_name = program_name

        self._error_code: int = 0
        self._error_msg: str = ""
        self._db_file: str = "lang_tran"
        self._path = platformdirs.user_data_dir(appname=self._program_name)
        self._language_code: str = ""
        self._DB: Optional[SQLDB] = None
        self._db_settings = App_Settings(self._program_name)

    def _config_db(self):
        file_manager = File()

        if not file_manager.path_exists(self._path):
            print(f"*** Need To Create {self._path}")
            file_manager.make_dir(self._path)

            if not file_manager.path_exists(self._path):
                raise RuntimeError(
                    f"Failed To Start {self._program_name} - Could Not Create <{self._path}>"
                )

        self.DB = SQLDB(
            appname=self._program_name,
            dbpath=self._path,
            dbfile=self._db_file,
            suffix=".db",
            dbpassword="",
        )

        error_status = self.DB.get_error_status()

        self._error_code = error_status.code
        self._error_msg = error_status.message

        if self._error_code == 1 and not self.DB.table_exists(self._db_file):
            lang_tran_def = (
                ColDef(
                    name="id",
                    description="pk_id",
                    data_type=SQL.INTEGER,
                    primary_key=True,
                ),
                ColDef(
                    name="language",
                    description="language",
                    data_type=SQL.VARCHAR,
                    size=255,
                ),
                ColDef(
                    name="language_code",
                    description="language_code",
                    data_type=SQL.VARCHAR,
                    size=3,
                ),
                ColDef(
                    name="word",
                    description="word or phrase",
                    data_type=SQL.VARCHAR,
                    size=255,
                ),
                ColDef(
                    name="base_lang_id",
                    description="base language id",
                    data_type=SQL.INTEGER,
                ),
            )

            if self.DB.table_create("lang_tran", lang_tran_def, drop_table=True) == -1:
                raise RuntimeError(
                    f"Failed To Configure {self._program_name} - Could Not Create Table"
                    f" <{self._db_file}>"
                )

    def get_existing_language_codes(self) -> list[str]:
        """Get all existing language codes from the lang tran database

        Returns:
            list[str]: List of language codes

        """
        language_codes = []
        trans_sql = f"{SQL.SELECT} language_code {SQL.FROM} lang_tran"

        result = self.DB.sql_execute(trans_sql, debug=False)
        error = self.DB.get_error_status()

        if error.code == 1 and result:
            for row_index, result_row in enumerate(result):
                if result_row[0] is not None and result_row[0] not in language_codes:
                    language_codes.append(result_row[0])

        return language_codes

    def translate(self, trans_word: str, delim: str = "") -> str:
        """This method translates the word to the selected foreign language word or returns the original word if
        there is no translation.
        The delimiter <delim>  is used to cut out sections of the string that do not need translating.
        E.g "This is ||Do Not Translate|| an example" will only translate "This is an example"

        Args:
            trans_word (str): The word that is to be translated
            delim (str): The delimiter used to cut out sections that do not need translating

        Returns (str): The translated word or the original word if there is no translation
        """

        if self._DB is None:
            self._config_db()

        debug = False

        assert isinstance(trans_word, str), f"{trans_word=}. Must be str"
        assert isinstance(delim, str) and delim.strip() != "", (
            f"{delim=}. Must be a non-empty str"
        )

        if delim.strip() == "":
            delim = self.SDELIM

        # Do not want to translate some single chars,char sequences. Bit brutal.
        if (
            len(trans_word) > 255
            or trans_word.strip() in ("", "&", ",", ";", "---")
            or re.search("[\x00/\\\\]", trans_word)
            or (
                delim not in trans_word
                and re.search("<(\"[^\"]*\"|'[^']*'|[^'\">])*>", trans_word)
            )
        ):
            return trans_word.strip(delim)

        if self._db_settings.setting_exist(self.APP_LANG_DB_KEY):
            self._language_code = self._db_settings.setting_get(self.APP_LANG_DB_KEY)

        ignore_chars = "+="
        split_list = trans_word.split(delim)

        deleted_wordlist = []
        trans_list = []

        for word_token in split_list:
            delim_token = delim + word_token.strip() + delim

            if delim_token in trans_word:
                deleted_wordlist.append(word_token.strip())  #
                trans_list.append(delim)
            elif word_token != "":
                trans_list.append(word_token.strip())

        deleted_wordlist.reverse()

        trans_string = ""

        for word_token in trans_list:
            if word_token == delim:
                notrans_word = deleted_wordlist.pop()

                if notrans_word != "":
                    trans_string = f"{'' if trans_string == '' else trans_string + ' '}{notrans_word}"
            else:
                if word_token != "":
                    word_token = word_token.replace("'", "''")
                    trans_sql = (
                        f"{SQL.SELECT} id, word {SQL.FROM} lang_tran"
                        f" {SQL.WHERE} word = '{word_token}'"
                        f" {SQL.AND} language_code {SQL.IS_NULL}"
                    )

                    result = self.DB.sql_execute(trans_sql, debug=False)
                    error = self.DB.get_error_status()

                    if error.code == 1 and result:  # Have a base word
                        base_lang_id = result[0][0]
                    else:
                        base_lang_id = -666  # Should never be in base lang

                    if base_lang_id == -666:
                        # If not in base dict and not HTML and does not end in ignore chars add to base dict
                        if (
                            word_token[-1:] not in ignore_chars
                            and word_token not in (" ", "", "&", ",", ";")
                            and not word_token.isnumeric()
                            and not word_token.isdecimal()
                            and not re.search(
                                "<(\"[^\"]*\"|'[^']*'|[^'\">])*>", word_token
                            )
                        ):
                            sql = (
                                f"{SQL.INSERTINTO} lang_tran (language_code,"
                                " word)"
                                f" {SQL.VALUES} (NULL,'{word_token.strip()}')"
                            )
                            result = self.DB.sql_execute(sql, debug=False)
                            error = self.DB.get_error_status()

                            if error.code == 1:
                                if self.DB.sql_commit == -1:
                                    print(f"SQL Error {error.code=} {error.message=}")
                            trans_string = f"{'' if trans_string == '' else trans_string + ' '}{word_token}"
                        else:
                            trans_string = f"{'' if trans_string == '' else trans_string + ' '}{word_token}"
                    else:
                        trans_sql = (
                            f"{SQL.SELECT} id, word {SQL.FROM} lang_tran"
                            f" {SQL.WHERE} base_lang_id = '{base_lang_id}'"
                            f" {SQL.AND} language_code = '{self._language_code}'"
                        )

                        result = self.DB.sql_execute(trans_sql, debug=False)
                        error = self.DB.get_error_status()

                        if error.code == 1 and result:  # Have a foreign word
                            foreign_word = result[0][1]

                            trans_string = f"{'' if trans_string == '' else trans_string + ' '}{foreign_word}"
                        else:
                            trans_string = f"{'' if trans_string == '' else trans_string + ' '}{word_token}"

        if debug and not Is_Complied():
            print(f"DBG Trans {trans_word=} {trans_string=}")

        return trans_string
