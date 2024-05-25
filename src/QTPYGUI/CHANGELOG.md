# QTPYGUI Change Log
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
