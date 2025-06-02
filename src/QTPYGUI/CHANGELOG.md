# QTPYGUI Change Log
## 1.0.4.1
 - Included a missing file to the QTPYGUI distribution - text.svg
 - Added a wait indicator to  Langtran_Popup as it can take some seconds to load
## 1.0.4
- Works With Python 3.13
- Updated to PySide6 6.9.0
- LineEdit respects placeholder text when it is set
- Code refactoring
- Improved Pixel Char Size calculation
- Fixed occasional bug in method _media_status_change class Video_Player
- Added APP_DATA to Special_Path to get the user application data folder
- Added a missing file to the QTPYGUI distribution - folder-plus.svg
- Added a new widget PlainTextEdit for users who need a plain text edit widget for logs etc.

### PlainTextEdit

Calling PlainTextEdit in a layout will generate a PlainTextEdit control on a form. 
A PlainTextEdit control is used to enter or display a large amount of plain text. The standard use case is for logs.
 

<br>**Properties**
<br> A PlainTextEdit control has the following properties, but can also use a subset of 
[_qtpyBase_Control](#_qtpybase_control) properties, which are not shown in the "fully loaded" example below

| **Property** | **Description**                                                                                   | **Type**      | **Optional** |
|--------------|---------------------------------------------------------------------------------------------------|---------------|--------------|
| height       | Characters if [pixel_unit](#_qtpybase_control) is False, Otherwise pixels. This will need setting | int (1)       | ✓            | |
| max_chars    | The maximum number of characters that can be entered into the PlainTextEdit control               | int (-1)      | ✓            |
| max_block_count| The number of blocks that can be displayed in the PlainTextEdit control before earlier blocks are deleted | int (-1)      | ✓            |
| width        | Characters if [pixel_unit](#_qtpybase_control) is False, Otherwise pixels. This will need setting | int (10)      | ✓            | |
| word_wrap    | True, text line wraps, Otherwise it does not                                                      | bool (True)   | ✓            |
| tag          | The system name of the PlainTextEdit control (required for application processing)                | str           | ❌            |
 

<br>A fully loaded PlainTextEdit declaration:
<br><br>**Note: Only "tag", "text" (To preload the PlainTextEdit control) and "callback" are usually needed**
- It is possible to paste text into the PlainTextEdit control

```
PlainTextEdit(
            tag="plaintextedit",
            text="Plain Text Edit",
            label="Plain Text Edit",
            callback=self.event_handler,
            height=5,
            max_chars=10,
            word_wrap=True,
    
            label_font=qtg.Font(
                style=qtg.Font_Style.OBLIQUE, backcolor="blue",forecolor="yellow", size=12
            ),
            txt_font=qtg.Font(
                style=qtg.Font_Style.NORMAL, backcolor="yellow", size=15,font_name="DejaVu Sans Mono"
            ),
            enabled=True,
            visible=True,
            tooltip="Plain Text Edit",
            tune_hsize=15,
            tune_vsize=15,
            user_data={"key": "value"},
            buddy_control=qtg.HBoxContainer().add_row(
                qtg.Button(
                    tag="plaintextedit_push",
                    text="PlainText Edit!",
                    callback=self.event_handler,
                    width=10,
                    height=1,
                )
            ),
        )
```

<br>**Methods**
<br>A subset of the [_qtpyBase_Control](#_qtpybase_control) methods apply to a PlainTextEdit instance
 
| **Method** | **Arguments**     | **Type** | **Description**                                                                                        | **Optional** |
|------------|-------------------|----------|--------------------------------------------------------------------------------------------------------|--------------|
| value_get  |                   | str      | Returns the text from the PlainTextEdit` widget <br><b>Returns:</b><br> The text in the text box .<br> |              |
| value_set  |                   | None     | Sets the text of the widget to the string value                                                        |              |
|            | value             | str      | The string value to set the PlainTextEdit widget to.                                                   | ❌            |
|            | append            | bool     | True - Append the text, Otherwise overwrite the text                                                   | ✓            |


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
