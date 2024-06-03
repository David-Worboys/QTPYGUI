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
import QTPYGUI.sqldb as sqldb
import platformdirs
from QTPYGUI.utils import Singleton
from QTPYGUI.file_utils import File


@dataclasses.dataclass(slots=True)
class App_Database(metaclass=Singleton):
    """This class implements the database handling logic of the application."""

    program_name: str

    # instantiated:bool = False
    data_path: str = ""
    error_code: int = 1
    error_message: str = ""

    _app_db: sqldb.SQLDB = None

    def __post_init__(self):
        """Creates a directory and database for the application's data files, creates a directory and database for
        application's settings
        """

        assert (
            isinstance(self.program_name, str) and self.program_name.strip() != ""
        ), f"{self.program_name=}. Must be a non-empty str"
        assert isinstance(self.data_path, str), f"{self.data_path=}. Must be a str"
        assert (
            isinstance(self.error_code, int)
            and self.error_code == 1
            or self.error_code == 1
        ), f"{self.error_code=}. Must be an int -1  | 1"
        assert isinstance(
            self.error_message, str
        ), f"{self.error_message=}. Must be a str"

        if self.data_path.strip() == "":
            self.data_path = platformdirs.user_data_dir(self.program_name)
        print(f"DBG A {self.data_path=}")
        if self._app_db is None:
            print(f"DBG B {self._app_db=}")
            if not File.path_exists(self.data_path):
                print(f"*** Need To Create {self.data_path}")
                result = File.make_dir(self.data_path)

                if result == -1 or not File.path_exists(self.data_path):
                    self.error_code = -1
                    self.error_message = f"Could not create {self.data_path}"
                    print(f"DBG {self.error_code=} {self.error_message=}")
                    raise RuntimeError(
                        f"Failed To Start {self.program_name} - {self.error_message}"
                    )
            print(f"DBG Make DB {self.data_path} {self.program_name=}")
            self._app_db = sqldb.SQLDB(
                appname=self.program_name,
                dbpath=self.data_path,
                dbfile=self.program_name,
                suffix=".db",
                dbpassword="666evil",
            )

            error_status = self._app_db.get_error_status()

            print(f"DBG {error_status=}")

            self.error_code = error_status.code
            self.error_message = error_status.message

            if self.error_code == 1:
                user_admin(program_name=self.program_name).create_database(self._app_db)

    @property
    def app_db(self):
        return self._app_db


@dataclasses.dataclass(slots=True)
class database_setup:
    """Performs database configuration operations"""

    def configure_database(self) -> int:
        """Configures the database for use

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1


@dataclasses.dataclass(slots=True)
class patient:
    """Performs patient database operations"""

    def add_patient(self) -> int:
        """Adds a new patient to the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def create_database(self) -> int:
        """Creates the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def delete_patient(self) -> int:
        """Deletes a patient from the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def moify_patient(self) -> int:
        """Modifies a patient in the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1


@dataclasses.dataclass(slots=True)
class optometrist:
    """Performs patient database operations"""

    def add_optometrist(self) -> int:
        """Adds a new patient to the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def create_database(self) -> int:
        """Creates the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def delete_optometrist(self) -> int:
        """Deletes a patient from the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def moify_optometrist(self) -> int:
        """Modifies a patient in the database

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1


@dataclasses.dataclass(slots=True)
class user_admin:
    """Performs user admin operations"""

    program_name: str
    _table_name = "users"

    def __post_init__(self):
        """Creates a directory and database for the application's data files, creates a directory and database for
        application's settings
        """

        assert (
            isinstance(self.program_name, str) and self.program_name.strip() != ""
        ), f"{self.program_name=}. Must be a non-empty str"

    def create_database(self, app_database: sqldb.SQLDB) -> tuple[int, str]:
        """Creates the database

        Returns:
            tuple[int,str]: 1,"" if successful, -1, error message if not
        """
        schema_col_def = [
            sqldb.ColDef(
                name="unid",
                description="User unique id",
                size=40,
                data_type=sqldb.SQL.VARCHAR,
            ),
            sqldb.ColDef(
                name="user_name",
                description="User Name",
                size=10,
                data_type=sqldb.SQL.VARCHAR,
            ),
            sqldb.ColDef(
                name="user_password",
                description="User Password",
                size=20,
                data_type=sqldb.SQL.VARCHAR,
            ),
            sqldb.ColDef(
                name="user_surname",
                description="User Surname",
                size=80,
                data_type=sqldb.SQL.VARCHAR,
            ),
            sqldb.ColDef(
                name="user_firstname",
                description="User First Name",
                size=80,
                data_type=sqldb.SQL.VARCHAR,
            ),
            sqldb.ColDef(
                name="user_othernames",
                description="User Other Names",
                size=80,
                data_type=sqldb.SQL.VARCHAR,
            ),
        ]

        if app_database.table_exists(self._table_name):
            for col_def in schema_col_def:
                if app_database.col_exists(
                    table_name=self._table_name, column_name=col_def.name
                ):
                    pass  # TODO Check if col_def is the same
                else:
                    pass  # TODO add new column to table

        else:
            app_database.table_create(
                table_name=self._table_name,
                col_defs=schema_col_def,
                drop_table=True,
            )

        return (
            app_database.get_error_status().code,
            app_database.get_error_status().message,
        )

    def create_user(self) -> int:
        """Creates a new user

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def delete_user(self) -> int:
        """Deletes a user

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def modify_user(self) -> int:
        """Modifies a user

        Returns:
            int: 1 if successful, -1 if not
        """

        return 1

    def user_list(self) -> tuple[list, str]:
        """Lists all users

        Returns:
            int: 1 if successful, -1 if not
        """
        app_database = App_Database(self.program_name).app_db
        error_status = app_database.get_error_status()

        if error_status.code == -1:
            return [], error_status.message

        result = app_database.sql_select(
            col_str="unid,user_surname,user_firstname,user_othernames",
            table_str=self._table_name,
        )

        error_status = app_database.get_error_status()

        if error_status.code == -1:
            return [], error_status.message

        user_list = []

        for result in result:
            user_list.append(result)

        return user_list, ""
