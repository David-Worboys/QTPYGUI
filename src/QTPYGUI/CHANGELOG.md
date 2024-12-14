# QTPYGUI Change Log
## 1.0.3
- Removed sys_const.py, possible breaking change.  Each application should have its own sys_const.py 
- Modifed ComboBox and supporting class CSV_File_Def used only with class ComboBox
  - CSV_File_Def properties now are
    
    | **Property**      | **Type**             | **Description**                                          | **Optional** |
    |-------------------|----------------------|----------------------------------------------------------|--------------|
    | data_index        | int (1)              | The column in the file to load into user data            | ✓            |
    | delimiter         | str (",")            | CSV file field separator                                 | ✓            |
    | file_name         | str                  | The path to the CSV file                                 | ❌            |
    | **filter**        | list[tuple[int,str]] | Filters the returned results                             | ✓            |
    | **ignore_errors** | bool (False)         | Set True to ignore CSV errors, Otherwise return an error | ✓            |
    | ignore_header     | bool (True)          | Set True if the CSV file has a header row                | ✓            |
    | line_start        | int (1)              | The line in the file to start loading data from          | ✓            |
    | select_text       | str (")              | The text to select after load                            | ✓            |
    | text_index        | int (1)              | The column in the CSV file to load into display          | ✓            |
    
    ComboBox now supports limited filtering - exact match only 
  
    Note: filter is a list of tuples of (column_index, filter_string) where the
          column index is the index of the column in the CSV file which must equal
          the filter_string. **Currently only handles an exact match**
    ```
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
    ``` 
 
- ComboBox now respects the editable property. True allow user edits, Otherwise 
user cannot edit. Defaults to False. Recommendation, generally user edits should
not be allowed in ComboBox. 
<br><br>**Note:** <br>When value_get is called and the editable property is True 
then only the display property should be used as the data property is undefined on 
user entries
- Fixed a bug with LineEdit width when a password mask is set. It was 1 char too
long.
## 1.0.2
- Added program_name property to class QtPyApp
  - Defaults to display_name property and if display_name is not set, program_name
  is set to "QTPYGUI"
  - Fixes a bug where the langtran database was put in the wrong folder
- Added a csv_file_def property to class ComboBox 
  - Allows csv files to be loaded when a ComboBox is defined as in the example below
  
  ```
  country_combo = qtg.ComboBox(label="Country",
            tag="country",
            callback=self.event_handler,
            width=40,
            csv_file_def=qtg.CSV_File_Def(file_name=qtg.App_Path("countries.csv"),text_index=2,data_index=3))

  ```
  
  - Introduced supporting class CSV_File_Def used only with class ComboBox
    - properties are: 
        
    | **Property**  | **Type**                             | **Description**                                                                                                                                                                                         | **Optional** |
    |---------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
    | data_index    | int (1)                              | The column in the file to load into user data                                                                                                                                                           | ✓            |
    | delimiter     | str (",")                            | CSV file field separator                                                                                                                                                                                | ✓            |
    | file_name     | str                                  | The path to the CSV file                                                                                                                                                                                | ❌            |
    | ignore_header | bool (true)                          | Set True if the CSV file has a header row                                                                                                                                                               | ✓            |
    | line_start    | int (1)                              | The line in the file to start loading data from                                                                                                                                                         | ✓            |
    | select_text   | str (")                              | The text to select after load                                                                                                                                                                           | ✓            |
    | text_index    | int (1)                              | The column in the CSV file to load into display                                                                                                                                                         | ✓            |

- Ensured that a scrollbar appears in the dropdown list of a ComboBox when needed
- Ensured that quotes (") do not appear around multiple words in the dropdown 
list of a ComboBox e.g "United States" now displays as United States
- Fixed a bug where Containers were not sized correctly when the 'pixel_unit' property was set True
- Fixed a bug in Treeview where the value sent to the event_handler was not always set
