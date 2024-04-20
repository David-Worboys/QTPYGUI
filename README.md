# QTPYGUI
### Author: David Worboys 
##### 2024-04-11 - Initial Draft
##### Update
## Index
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
   - [Containers](#containers)
   - [GUI Controls](#gui-controls)
   - [Event Handling](#event-handling)
4. [Hello World Application](#building-your-first-application)
5. [Application Distribution](#distributing-your-application)
6. [Boot Camp](#boot-camp)
7. [QTPYGUI Control Reference](#qtpygui-control-api-reference)
   - [Button](#button) 
8. [QTPYGUI Enumerated Types/Classes](#qtpygui-enumerated-typesclass-reference)

## Introduction
QTPYGUI is a declarative user interface wrapper around Pyside6 and, as there are 
a number of GUI (Graphical User Interface) wrappers around various widget sets,
including Pyside6, the natural question is why another one? The answer lies in 
at least two parts, my dissatisfaction with how the other GUI wrappers were 
implemented/managed and because I could and there is much to be learned with 
that approach.

The next question the reader might find themselves asking is why not a web UI
based on the old favourites of HTML, CSS and Javascript, something like React 
perhaps? I am a firm believer in "horses for courses", so why bring a browser to
the desktop fight and all the resources, memory/compute, that entails when a 
well-designed widget set with better performance and memory usage is 
available. Worse, building web apps is a complicated business even with the
web UI frameworks, of course some may same the same of desktop widget sets, and 
this is where GUI wrappers like QTPYGUI come in.

In closing, it is worth noting that a major advantage in utilising a GUI wrapper,
aside from ease of programming, is that if the underlying widget set is 
deprecated, or licensing changes, then the GUI wrapper can change widget sets.
Although this would be a large task, the major benefit is that applications using 
the GUI wrapper will be minimally impacted.

### What Is A Declarative User Interface?
A declarative UI (user interface) is an application user interface coded in
the application source code using a formal specification. There is no need for
GUI designers, and the application programmer writes the UI as just another 
part of the code. This is an old idea, going back at least to the early 1980's
and applications like dBase II and Clipper but just because it is old does not 
mean it is bad ot not relevant.

### Notes
1. Development of QTPYGUI started privately in 2020, moving to a public release in 2024.
   - This version is an early public release and doco and code streamlining is onging.
   
   - Although QTPYGUI is used in production applications, there are bound to be bugs, 
   certainly Dateedit and Treeview need much more work as they are infrequently 
   used.
    
   - The feature set of other GUI components needs to be widened. Missing also is
   theming and this will be required for a larger audience.

2. **HELP IS WANTED AND I WELCOME ALL CONTRIBUTIONS!**

    - Please reach out to me via Discussions (https://github.com/David-Worboys/QTPYGUI/discussions)
    if you want to help or have ideas on improvements
   
    - Bugs can be logged at https://github.com/David-Worboys/QTPYGUI/issues  

3. QTPYGUI will always remain opensource, unlike some other similar frameworks
   that used "bait and switch" tactics

4. QTPYGUI uses Python 3.11 for development and ruff (https://github.com/astral-sh/ruff)
for formatting. Type hinting is mandatory as are asserts to check all arguments to 
functions/methods

5. My time is limited (both figuratively and literally), but I will put in as 
much effort as I can to help move things along

6. I strongly suggest using Nutika (https://nuitka.net/) to distribute your 
Python desktop applications. I use this method exclusively with great success.

7. Finally, to the reader's relief, I only use Linx Mint for development and 
do not have access to a Windows installation, and therefore

   - ***HELP IS Neeeded 
   To Verify QTPYGUI's Operations Under Windows***


### Where To Find An Application That Uses QTPYGUI?
https://github.com/David-Worboys/Black-DVD-Archiver



## QTPYGUI 101
First up, QTPYGUI is pronounced "Cutey Pie GUI" which follows the "QT Groups"
own pronunciation and appeals to my, admitably lame, sense of humour.
### Prerequities
1. Pyside6
2. Python version >= 3.8 
   - If Nuitka is used for application distribution, then Python versions 3.12 
   and above are not currently supported.
### Installation
1. Create your Python project folder and set up your Python project using 
the virtual environment manager of your choice

2. Follow the installation instructions at https://pypi.org/project/PySide6/ or 
just enter:

    `pip install PySide6`

3. Until I get a PyPy installation configured, go to https://github.com/David-Worboys/QTPYGUI 
and download all the python source code (.py) files and the requirements.txt 
file into your Python project folder.

4. Now install all QTPYGUI dependencies in your Python project folder

   `pip install -r requirements.txt`

### Boot Camp
First up, check out the examples in https://github.com/David-Worboys/QTPYGUI/tree/master/Examples .
There is one example per python source file, and I will be adding more as time 
progresses.

#### Basic Concepts
1. QTPYGUI is event driven and there are no "busy" loops waiting for something
to happen

2. By default, width and height settings are in characters
   - Pixels can be used as an argument is provided to allow for this
   - This works best with monospaced fonts
   
   - The default font is "IBM Plex Mono" and the default font size is 10
     - This is included in the installation of QTPYGUI 
     - If this font is missing, then QTPYGUI will try and find a system font that 
     will work

3. The basic structure of a QTPY GUI Program is as follows:

```
import qtpygui as qtg

Class Example_App
    def __init__(self):
        """ Setup application instance variable """
        self.example_app = qtg.QtPyApp(
            display_name="Example App",
            callback=self.event_handler,
            height=100,
            width=100,
        ) 
    
    def event_handler(self, event: qtg.Action):
        """Handles  events"""
    
    def layout()-> qtg.VBoxContainer:
        """ Defines The User Interface Layout """
    
    def run(self):
        """Run Example App"""
        self.example_app.run(layout=self.layout())
        
if __name__ == "__main__":
    example_app = Example_App()
    example_app.run()            
        
```
1. This defines the structure of the application main.py file

2. https://github.com/David-Worboys/QTPYGUI/blob/master/Examples/example_01.py
shows this in action.

3. The python classes that utilise a GUI are defined as below:
```
import qtpygui as qtg

Class Example_Class:
    def event_handler(self, event: qtg.Action):
        """Handles  events"""
        
    def layout()-> qtg.VBoxContainer:
        """ Defines The User Interface Layout """    

```
1. When the Example_Class is instantiated, the layout method is called to 
generate the GUI elements of the display and this is assigned to the calling 
window/GUI object

##### Containers
Containers are at the heart of the QTPYGUI system and define the layout of the 
GUI items. The following are four types of containers:

- FormContainer
  - Lays out GUI controls vertically as per the associated platform (Linux, 
  Windows, Mac) GUI specifications
- HBoxContainer
  - Lays out the GUI controls horizontally 
  
- VBoxContainer
  - Lays out the GUI controls vertically, similar to the FormContainer but does
  not adhere as tightly to the associated platform specifications
  
- GridContainer
  - Lays out the GUI controls as a grid.  This container is seldom used.

To add a GUI control to a container, the ```add_row``` method is used as below:

```
qtg.HBoxContainer(tag="button_example").add_row(
                qtg.Button(
                    tag="example_1", text="Example 1", callback=self.event_handler, width=10
                ),
                qtg.Button(
                    tag="example_2", text="Example 2", callback=self.event_handler, width=10
                ),
)                
```
- This will layout two Buttons Horizontally. If a FormContainer or a VBoxContainer
was used, the buttons would be laid out vertically.

- **Note the use of the tag, text and callback arguments as these are fundamental
to the operation of QTPYGUI [GUI Controls](#gui-controls)**
  - If a Container has a text argument, it becomes a Group box.

##### GUI Controls
These are the GUI components that comprise the UI of an application. Declaring them
utilises a standard pattern of arguments with additional arguments for specific
GUI controls.

**Note: If an argument is not supported by a GUI control, it is ignored.**

Let us consider the Button GUI control

````commandline
qtg.Button(tag="example_1", text="Example 1",label="Click Me!", callback=self.event_handler)
````
**Note: The following arguments are common to all QTPYGUI controls**

"tag" — The "tag" is the name of the control, as it is housed in a container 
then the container "tag" and the button "tag" make a unique pair.
- This makes it easier to code larger applications as each GUI element 
  does not have to have a unique name.
  
- If a "tag" is not provided, then the application generates one automatically.
  - This is fine for "Container" and "Label" objects where the programmer does 
  not intend to reference an object. 
  
"text" — The "text" is the text displayed on the control, it is optional

"label" — The "label" argument places a label to the left of the control, it is
optional

"callback" — Is the name of the method that will process the envents generated
by the GUI control. By convention, I declare this as the "event_handler" method. 

- If a callback method is not provided, then the control cannot send events to it

- The "event_handler" method takes only one argument ````atg.Action```` 
    
    


##### Event Handling
The burning question in the reader's mind is what happens when an operation occurs
on a GUI control, say if a Button (as defined below) is clicked on:
```
qtg.Button(tag="example_2", text="Example 2", callback=self.event_handler, width=10),
```
The answer is that the ```callback``` method ```self.event_handler``` is triggered 
with a CLICKED event, and it can be processed as below:

```
    def event_handler(self, event: qtg.Action):
        """Handles  form events
        Args:
            event (qtg.Action): The triggering event
        """
        assert isinstance(self,event:qtg.Action), f"{event=}. Must be Action"

        match event.event:
            case qtg.Sys_Events.CLICKED:
                match event.tag:                    
                    case "example_2":
                        popups.PopMessage(title="Hi", message="Example 2 Was Clicked").show()
```
This results in a Pop-up window opening with a title of "Hi" displaying
"Example 2 Was Clicked" 

**Note: This is the essence of event driven programming, nothing happens until an
event is triggered, mostly by the application GUI controls - like Buttons.**

The observant reader may notice the event instance passed to the ```event handler``` 
is a class of ```qtg.Action``` which probably should have been named 
```qtg.Event``` but for historical reasons that nomenclature is staying. 

The ```qtg.Action``` class has a number of very useful methods and properties, and 
a programmer using QTPYGUI will become very familiar with them.

#### Building Your First Application:

As is traditional, a "hello world" program needs to be written first, so let's 
get to it!

```
import qtpygui as qtg

class Hello_World:
    def __init__(self):
        self.hello_world = qtg.QtPyApp(
            display_name="Hello World",
            callback=self.event_handler,
            height=100,
            width=100,
        )

    def event_handler(self, event: qtg.Action):
        """Handles  form events
        Args:
            event (qtg.Action): The triggering event
        """
        assert isinstance(event, qtg.Action), f"{event=}. Must be Action"

        match event.event:
            case qtg.Sys_Events.CLICKED:
                match event.tag:
                    case "ok":
                        self.hello_world.app_exit()

    def layout(self) -> qtg.VBoxContainer:
        """The layout of the window
        Returns:
            qtg.VBoxContainer: The layout
        """
        return qtg.VBoxContainer(align=qtg.Align.BOTTOMRIGHT).add_row(
            qtg.FormContainer().add_row(
                qtg.Label(
                    text="Hello World!",
                    txt_fontsize=48,
                    txt_align=qtg.Align.CENTER,
                    txt_font=qtg.Font(backcolor="blue", forecolor="yellow"),
                ),
            ),
            qtg.HBoxContainer().add_row(
                qtg.Button(
                    tag="ok",
                    text="OK",
                    callback=self.event_handler,
                    width=10,
                    tooltip="Exit Example 01",
                ),
            ),
        )

    def run(self):
        """Run example_01"""
        self.hello_world.run(layout=self.layout())

if __name__ == "__main__":
    hello_world = Hello_World()
    hello_world.run()
```

This is a slightly simplified version of example_01.

Copy the above source code into a hello_world.py file and run it like so:

```python3 -OO hello_world.py```

And the follwing screen will be displayed:
![](./userguide_images/hello_world.png)

#### Distributing Your Application
I strongly recommend using Nuitka (https://nuitka.net/) to distribute your 
program as it can produce a single compiled file, housing all dependencies 
that can be copied to a host machine. 

Nuitka's Kay Hayen is simply the Python GOAT when it comes to this type of thing.

To compile ```hello_world.py``` the reader will need to install Nuika

```pip install Nuitka```

and run this command, after amending the ```--include-data-dir=``` path to the 
readers own installed path :
```
python -m nuitka                                                                            \
--show-anti-bloat-changes                                                                   \
--assume-yes-for-downloads                                                                  \
--lto=yes                                                                                   \
--python-flag=-OO                                                                           \
--python-flag=no_warnings                                                                   \
--python-flag=isolated                                                                      \
--standalone                                                                                \
--onefile                                                                                   \
--prefer-source-code                                                                        \
--enable-plugin=pyside6                                                                     \
--include-qt-plugins=sensible                                                               \
--include-data-dir=/home/david/PycharmProjects/QTPYGUI/IBM-Plex-Mono=./IBM-Plex-Mono        \
hello_world.py
```
This will produce a ```hello_world.bin``` file on Linux, double-click on it and 
the ```hello_world``` application will start.

Note:
1. On occasion the ```hello_world.bin``` file will need to be made executable, and this
is done as follows:

- Right-click on the ```hello_world.bin``` file and select "Properties." This 
will open the file properties window. select  "Permissions" and tick "Allow 
executing file as program" and then "Close"

2. At the time of writing, this will produce a 58MB ```hello_world.bin``` 
executable file - This is simply how it is when distributing Python applications
 as so much is included during the build process. It is worth noting that 
PyInstaller produces even larger executables! 

### QTPYGUI Control API Reference

| Control                   | Description                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [Button](#button)         | Creates a button, text and icon are optional                                                                                 |
| [Checkbox](#checkbox)     | Creates a check box that a user can click on or off                                                                          | 
| [ComboBox](#combobox)     | Creates a drop down selection box, icon in list is <br/>optional                                                             |
| [Dateedit](#dateedit)     | Creates a date edit control with a dropdown calendar and <br/>an erase button                                                |
| [FolderView](#folderview) | Creates a control that displays the contents of a folder in a Grid                                                           |
| Grid                      | Creates a control that displays data in a table (grid) format                                                                |
| Image                     | Creates a control that displays an image                                                                                     |
| Label                     | Creates a text string                                                                                                        |
| LineEdit                  | Creates a control that allows text to be edited and displayed<br/> in a single line                                          |
| Menu                      | Creates a menu just below the title bar                                                                                      |
| ProgressBar               | Creates a control that displays the progress of an operation                                                                 |
| RadioButton               | Creates a radio button control. In a group only one can be <br/>selected at a time                                           |
| [Slider](#slider)         | Creates a slider control than can be used to set a value <br/>by dragging the handle                                         |
| Spinbox                   | Creates a spinbox control that allows numbers to be set <br/>via clicking up and down arrows or entering the number directly |
| Switch                    | Creates a switch control that can be used to turn on and <br/>off a feature                                                  |
| Tab                       | Creates a tab control that has multiple pages, each <br/>housing their own set of GUI controls                               |
| TextEdit                  | Creates a text entry control that can span multiple lines                                                                    |
| Timeedit                  | Creates a time edit control with an erase button                                                                             |
| Treeview                  | Creates a control that displays data as a tree view                                                                          |

### _qtpyBase_Control
 
This is the ancestor of all QTPYGUI GUI controls, and the properties here are 
used to set the behavior of the GUI control when instantiated.
  
**Properties** 
- Not all properties will be supported or used by descendant GUI controls and will be ignored
- Some properties will be overridden by descendant GUI controls

| **Property**      | **Type**                                       | **Description**                                                                                                                                   |
|-------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| align             | [Align](#align) (Align.LEFT)                   | Used to align GUI controls in containers                                                                                                          |
| allow_clear       | bool (True)                                    | True, allow GUI controls that can be cleared to be cleared, Otherwise not                                                                         |
| bold              | bool (False)                                   | True, sets GUI controls that have text bold, Otherwise not                                                                                        |
| buddy_control     | _qtpyBase_Control \| None (None)               | Set the buddy GUI control or Container                                                                                                            | 
| buddy_callback    | Callable \| None (None)                        | Sets the callback method for the buddy GUI control (Functon, Method or Lambda)                                                                    |
| callback          | Callable \| None (None)                        | Sets the callback method for the GUI control (Functon, Method or Lambda)                                                                          |
| container_tag     | str ("")                                       | Sets the container_tag for the GUI control. If "" then system generated                                                                           |
| editable          | bool (True)                                    | True, sets GUI controls that support editing into edit mode, Otherwise not                                                                        |
| enabled           | bool (True)                                    | True, enables the GUI control, Otherwise disable the GUI control                                                                                  |
| frame             | [Widget_Frame](#widget_frame) \| None (None)   | Sets the frame of a GUI control tht supports frames                                                                                               |
| icon              | None \| qtG.QIcon \| qtG.QPixmap \| str (None) | Sets the icon on a GUI control were supported. If a str then this is the filename  of the icon                                                    |
| italic            | bool (False)                                   | True, sets GUI controls that have text italic, Otherwise not                                                                                      |
| height            | int (-1)                                       | The height of the GUI control in characters if pixel_unit is False, Otherwise the height is in pixels.<br> -1 automatically calculates the height |
| label             | str ("")                                       | The label string, if not provided no label is shown                                                                                               |
| label_align       | [Align_Text](#align_text) (Align_Text.RIGHT)   | The alignment of the label text                                                                                                                   |
| label_width       | int (-1)                                       | The width of the label in  characters if pixel_unit is False, Otherwise the width is in pixels.<br> -1 automatically calculates the width         |
| label_font        | [Font](#font) \| None (None)                   | The Font of the label                                                                                                                             |
| pixel_unit        | bool (False)                                   | True, width and height settings are in pixels, Otherwise in characters                                                                             |
| size_fixed        | bool (True)                                    | True, Sets the size of the GUI controls as fixed, Otherwise not fixed. TODO: fix this setting as it has no effect                                 |
| tag               | str ("")                                       | The tag of the GUI control, system generated. If "" then system generated                                                                         |
| text              | str ("")                                       | The text displayed on the GUI control if this is supported by the GUI control                                                                     |
| tooltip           | str ("")                                       | The tooltip displayed when the mouse hovers over the GUI control                                                                                  |
| txt_align         | [Align_Text](#align_text) (Align_Text.LEFT)    | Aligns the GUI controls text, if supported.                                                                                                       |
| txt_font          | [Font](#None)\| None (None)                    | The font of the GUI controls text, if supported                                                                                                   |
| txt_fontsize      | int (DEFAULT_FONT_SIZE)                        | The fontsize in points of the GUI control text, if supported                                                                                      |
| tune_vsize        | int (0)                                        | Used to adjust the vertical size of the GUI control. In pixels                                                                                    |
| tune_hsize        | int (0)                                        | Used to adjust the horizontal size of the GUI control. In pixels                                                                                  |
| translate         | bool (True)                                    | True, translate the text on the GUI control, if supported, Otherwiise not                                                                         |
| width             | int (-1)                                       | The width of the GUI control in characters if pixel_unit is False, Otherwise the width is in pixels.<br> -1 automatically calculates the width    |
| underline         | bool (False)                                   | True, sets GUI controls that have text underline, Otherwise not                                                                                   |
| user_data         | any (None)                                     | User sepecified data attached to the GUI control                                                                                                  |
| validate_callback | Callable \| None (None)                        | A callback to validate the contents of the GUI control. Applicable only to GUI controls that allow the entry of text                              |
| visible           | bool (True)                                    | True, make the GUI control visible,Otherwise hide the GUI control                                                                                 |

**Methods** 
- Not all methods will be used by descendant GUI controls
- Some methods will be overridden

| **Method**          | **Arguments**   | **Type**                                | **Description**                                                                                                                      | **Optional** |
|---------------------|-----------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------|
| block_signals       |                 | None                                    | Blocks or unblocks signals for the widget (Used rarely where signals might be generated very frequently e.g. [Slider](#slider))      |              |
|                     | block_signals   | bool (True)                             | True, stop this widget from generating signals (events), Otherwise do  not do not stop signals (events)  being generated .           | ✓            |
| clear               |                 | None                                    | Clears the contents of the GUI control, if supported                                                                                 |              | 
| buddy_text_set      |                 | None                                    | Sets the text on the buddy control, where supported                                                                                  |              |
|                     | value           | str                                     | The label text set to the left of the buddy widget.                                                                                  | ❌            |
| ediitable_set       |                 | None                                    | Controls the edit setting of a GUI control, where supported.                                                                         |              |
|                     | editable        | bool (False)                            | True, set the GUI control editable, where supported, Otherwise not.                                                                  | ✓            |
| enable_get          |                 | bool                                    | <br><b>Returns:</b><br> The enable value of the widget.<br>                                                                          |              |
| enable_set          |                 | int                                     | Enables/Disables the GUI control where supported <br><b>Returns:</b><br> 1 - set ok, -1 - set failed<br>                             |              |
|                     | enable          | bool                                    | True enable control, Otherwise disable the control.                                                                                  | ❌            |
| fonts_available_get |                 | tuple[str]                              | <br><b>Returns:</b><br> A tuple of font name strings.<br>                                                                            |              |
| font_set            |                 | None                                    | Sets the font on the GUI control (Usually used internally as the [Font](#font) property is set when the GUI control is instantiated) |              |
|                     | app_font        | Font                                    | Application font                                                                                                                     | ❌            |
|                     | widget_font     | Font                                    | Control font                                                                                                                         | ❌            |
|                     | widget          | qtW.QWidget (None)                      | The QT widget having the font set (defaults to current GUI control)                                                                  | ✓            |
| font_system_get     |                 | None                                    | Gets the sstem font <br><b>Returns:</b><br> A QFont object.<br>                                                                      |              |
|                     | fixed           | bool (True)                             | True, return the fixed size system font, Otherwise not                                                                               |              |
| frame_style_set     |                 | None                                    | Sets the frame style of the GUI control, where supported                                                                             |              |
|                     | frame           | [Widget_Frame](#widget_frame)           | Frame definition object.                                                                                                             | ✓            |
| icon_set            |                 | None                                    |                                                                                                                                      |              |
|                     | icon            | None \| qtG.QIcon \| qtG.QPixmap \| str | Sets the icon on a GUI control were supported. If a str then this is the filename  of the icon                                       | ❌            |
| guiwidget_get       |                 | qtW.QWidget                             | Returns the underlying QT widget so that specialised operations can be performed<br><b>Returns:</b><br> The QT GUI widget.<br>       |              |
| guiwidget_set       |                 | None                                    | Sets the GUI Control (Almost never used by QTPYGUI programmers)                                                                      |              |
|                     | widget          | qtW.QWidget \| qtG.QAction              | The widget being set                                                                                                                 | ❌            |
| pixel_str_size      |                 | [Char_Pixel_Size](#char_pixel_size)     | <br><b>Returns:</b><br> The pixel size of the string in a [Char_Pixel_Size](#char_pixel_size) instance   .<br>                       |              |
|                     | text            | str                                     | The text to be measured                                                                                                              | ❌            |
| pixel_char_size     |                 | [Char_Pixel_Size](#char_pixel_size)     | The size of a char in pixels<br><b>Returns:</b><br> [Char_Pixel_Size](#char_pixel_size) <br>                                         |              |
|                     | char_height     | int                                     | Character height in chars                                                                                                            | ❌            |
|                     | char_width      | int                                     | Character width in chars                                                                                                             | ❌            |
|                     | height_fudge    | float (1.1)                             | Fudge factor multiplier to provide height adjustment                                                                                 | ✓            |
|                     | width_fudge     | float (1.1)                             | Fudge factor multiplier to provide width adjustment                                                                                  | ✓            |
| text_pixel_size     |                 | tuple[int,int]                          | Returns the height and width of a string of text in pixels <br><b>Returns:</b><br> The [height,width] of the text in pixels.<br>     |              |
|                     | text            | str                                     | The text to be measured.                                                                                                             | ❌            |
| tooltip_get         |                 | str                                     | <br><b>Returns:</b><br> The tooltip text.<br>                                                                                        |              |
| tooltip_set         |                 | None                                    |                                                                                                                                      |              |
|                     | tooltip         | str                                     | The text to display in the tooltip.                                                                                                  | ❌            |
|                     | width           | int (200) _Currently 400 for testing_   | The width of the tooltip in pixels. ( Width setting is still being ignored TODO Find Fix)                                            | ✓            |
|                     | txt_color       | str                                     | The color of the tooltip text. Defaults to black.                                                                                    | ✓            |
|                     | bg_color        | str                                     | The background color of the tooltip. Defaults to white.                                                                              | ✓            |
|                     | border          | str                                     | The border style of the tooltip. Defaults to "1px solid #000000".                                                                    | ✓            |
| tooltipsvisible_get |                 | bool                                    | <br><b>Returns:</b><br> True - visible, False - not visible.<br>                                                                     |              |
| tooltipsvisible_set |                 | None                                    |                                                                                                                                      |              |
|                     | visible         | bool                                    | True, tooltip visible, Otherwise not.                                                                                                | ❌            |
| trans_get           |                 | bool                                    | <br><b>Returns:</b><br> True - text translated, False - text not translate<br>                                                       |              |
| trans_set           |                 | None                                    |                                                                                                                                      |              |
|                     | no_trans        | bool                                    | True, text not translated, Otherwise text is translated                                                                              | ❌            |
| trans_str           |                 | str                                     | <br><b>Returns:</b><br> The translated text.<br>                                                                                     |              |
|                     | text            | str                                     | The text to be translated.                                                                                                           | ❌            |
|                     | force_translate | bool (False)                            | Translate text if True,Otherwise do not translate text. Defaults to False                                                            | ✓            |
| validate            |                 | bool                                    | <br><b>Returns:</b><br> True if validation ok, otherwise False<br>                                                                   |              |
| value_get           |                 | any                                     | <br><b>Returns:</b><br> The value of the widget.<br>                                                                                 |              |
| userdata_get        |                 | any                                     | <br><b>Returns:</b><br> The user data stored on the widget                                                                           |              |
| userdata_set        |                 | None                                    | Sets the user data on the widget.                                                                                                    |              |
|                     | user_data       | any                                     | The user data can be of any type                                                                                                     | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | bool                                    | Sets the bool value set of the widget.                                                                                               | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | int                                     | Sets the int value set of the widget.                                                                                                | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | float                                   | Sets the float value set of the widget.                                                                                              | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | Combo_Data                              | Sets the [Combo_Data](#combo_data) value set of the widget.                                                                          | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | str                                     | Sets the str value set of the widget.                                                                                                | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | datetime.date                           | Sets the date value set of the widget                                                                                                | ❌            |
| value_set           |                 | None                                    | Sets the widget value - These are overloaded types                                                                                   |              |
|                     | value           | datetime.datetime                       | Sets the datetime value set of the widget                                                                                            | ❌            |
| visible_get         |                 | bool                                    | <br><b>Returns:</b><br> True - widget visible, False - widget hidden.<br>                                                            |              |
| visible_set         |                 | None                                    |                                                                                                                                      |              |
|                     | visible         | bool                                    | True, sets widget visible, Otherwise widget hidden.                                                                                  | ❌            |


#### Button

Calling Button in a layout will generate a button control on a form. The "tag"
,"text" and "callback" arguments are generally the only arguments used. It is 
suggested to set width and height as the font selected might not 
automatically size correctly.  

<br>**Properties**
<br>The following properties apply when a button is instantiated with the Button call as below 

| **Property**         | **Description**                                                                                      | **Type**                                    | **Optional** |
|----------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------|--------------|
| auto_repeat_interval | If > 0 the button keeps firing Clicked events when <br>held down (milliseconds)                      | int >= 0 (0)                                | ✓            |
| bold                 | Sets the button text bold if True otherwise not                                                      | bool (False)                                | ✓            |
| buddy_control        | Control or container with controls that sit to the right of the button                               | Container or GUI Control                    | ✓            | 
| callback             | The method called when the button is pressed                                                         | Callable (None)                             | ✓            |
| enabled              | Enables/Disables the button                                                                          | bool (True)                                 | ✓            |
| height               | The height of the button (in characters if pixel_unit is<br> False,Otherwise pixels)                 | int > 0 (10)                                | ✓            |
| icon                 | The icon image displayed on the button                                                               | str [File Name]<br/>,QIcon,QPixmap          | ✓            |
| italic               | Sets the button text italic if True otherwise not                                                    | bool (False)                                | ✓            |
| label                | Displays text to the left of the button                                                              | str ("")                                    | ✓            |
| label_align          | Alignment of the text displayed in the label                                                         | [Align_Text](#align_text) (Align_Text.LEFT) | ✓            |
| label_font           | The font definition for the label                                                                    | [Font](#font)                               | ✓            |
| label_width          | Sets the label width (in characters if pixel_unit is<br> False,Otherwise pixels)                     | int > 0 (0)                                 | ✓            |
| pixel_unit           | Use pixels for width/height, pixels if True, Otherwise characters                                    | bool (False)                                | ✓            |
| tag                  | The application name of the button                                                                   | str (System Generated)                      | ✓            |
| text                 | The text displayed on the button                                                                     | str  ("")                                   | ✓            |
| txt_align            | Alignment of the text displayed on the button                                                        | [Align_Text](#align_text) (Align_Text.LEFT) | ✓            |
| txt_font             | The font definition for the button (style will override<br> italic,size will override txt_fontsize ) | [Font](#font)                               | ✓            |
| txt_fontsize         | The point size of the text                                                                           | int (10)                                    | ✓            |
| tune_hsize           | Add or subtracts pixels units to the width. Used in aligning controls                                | int (0)                                     | ✓            |
| tune_vsize           | Add or subtracts pixels units to the height. Used in aligning controls                               | int (0)                                     | ✓            |
| tooltip              | Sets the tooltip displayed when the button is hovered over                                           | str                                         | ✓            |
| translate            | Translates text if True Otherwise does not translate                                                 | bool (True)                                 | ✓            |
| user_data            | Any data item the user wants to attach to the button                                                 | any (None )                                 | ✓            |
| underline            | Underlines the button text if True otherwise not                                                     | bool (False)                                | ✓            |
| visible              | Makes the button visible if True otherwise invisible                                                 | bool (True)                                 | ✓            |
| width                | The width of the button (in characters if pixel_unit is<br> False,Otherwise pixels)                  | int > 0 (10)                                | ✓            |

A fully loaded button declaration:
- **Note: Only "tag", "text" and "callback" are usually needed**

```
Button(
        tag="button_1",
        text="Button",
        label="Button 1",
        label_align=qtg.Align_Text.CENTER,
        label_width=10,
        label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE,size=14),
        callback=self.event_handler,
        width=10,
        height=1,
        txt_align=qtg.Align_Text.CENTER,
        txt_font =qtg.Font(style=qtg.Font_Style.NORMAL,size=15),
        txt_fontsize=12,
        bold=True,
        italic=True,
        underline=True,
        enabled=True,                        
        visible=True,
        tooltip="Button 1 Press Me",
        tune_hsize=15,
        tune_vsize=15,
        user_data = {"key":"value"},
        buddy_control=qtg.HBoxContainer().add_row(
            qtg.Spacer(width=1),
                    qtg.Checkbox(tag="button_check", text="Tick Me!", callback=self.event_handler, width=12)
        ),
    )
```
<br>**Methods**
<br>A subset of the [_qtpyBase_Control](#_qtpybase_control) methods apply to Button instances 

| **Method** | **Arguments** | **Type**    | **Description**                     | **Optional** |
|------------|---------------|-------------|-------------------------------------|--------------|
| text_set   |               | None        | Sets the text on the button         |              |
|            | button_text   | str         | The text to be placed on the button | ❌            |
|            | translate     | bool (True) | Translate the text                  | ✓            |

#### Checkbox

Calling Checkbox in a layout will generate a checkbox control on a form. The "tag"
,"text" and "callback" arguments are generally the only arguments used. It is 
suggested to set width and height as the font selected might not 
automatically size correctly.

<br>**Properties**
<br>The following properties apply when a Checkbox is instantiated with the Checkbox call as below

| **Property**  | **Description**                                                                                        | **Type**                                    | **Optional** |
|---------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------|--------------|
| bold          | Sets the checkbox text bold if True otherwise not                                                      | bool (False)                                | ✓            |
| buddy_control | Control or container with controls that sit to the right of the checkbox                               | Container or GUI Control                    | ✓            | 
| callback      | The method called when the checkbox is checked                                                         | Callable (None)                             | ✓            |
| enabled       | Enables/Disables the checkbox                                                                          | bool (True)                                 | ✓            |
| height        | The height of the checkbox (in characters if pixel_unit is False,Otherwise pixels)                     | int > 0 (10)                                | ✓            |
| italic        | Sets the checkbox text italic if True otherwise not                                                    | bool (False)                                | ✓            |
| label         | Displays text to the left of the checkbox                                                              | str ("")                                    | ✓            |
| label_align   | Alignment of the text displayed in the label                                                           | [Align_Text](#align_text) (Align_Text.LEFT) | ✓            |
| label_font    | The font definition for the label                                                                      | [Font](#font)                               | ✓            |
| label_width   | Sets the label width (in characters if pixel_unit is<br> False,Otherwise pixels)                       | int > 0 (0)                                 | ✓            |
| pixel_unit    | Use pixels for width/height, pixels if True, Otherwise characters                                      | bool (False)                                | ✓            |
| tag           | The application name of the checkbox                                                                   | str (System Generated)                      | ✓            |
| text          | The text displayed next to the checkbox                                                                | str  ("")                                   | ✓            |
| txt_align     | Alignment of the text displayed next to the checkbox                                                   | [Align_Text](#align_text) (Align_Text.LEFT) | ✓            |
| txt_font      | The font definition for the checkbox (style will override<br> italic,size will override txt_fontsize ) | [Font](#font)                               | ✓            |
| txt_fontsize  | The point size of the text                                                                             | int (10)                                    | ✓            |
| tune_hsize    | Add or subtracts pixels units to the width. Used in aligning controls                                  | int (0)                                     | ✓            |
| tune_vsize    | Add or subtracts pixels units to the height. Used in aligning controls                                 | int (0)                                     | ✓            |
| tooltip       | Sets the tooltip displayed when the checkbox is hovered over                                           | str                                         | ✓            |
| translate     | Translates text if True Otherwise does not translate                                                   | bool (True)                                 | ✓            |
| user_data     | Any data item the user wants to attach to the checkbox                                                 | any (None )                                 | ✓            |
| underline     | Underlines the checkbox text if True otherwise not                                                     | bool (False)                                | ✓            |
| visible       | Makes the checkbox visible if True otherwise invisible                                                 | bool (True)                                 | ✓            |
| width         | The width of the checkbox (in characters if pixel_unit is False,Otherwise pixels)                      | int > 0 (10)                                | ✓            |

A fully loaded checkbox declaration:
- **Note: Only "tag", "text" and "callback" are usually needed**

```
Checkbox(
            tag="checkbox",
            text="Tick Me!",
            label="Check Box",
            callback=self.event_handler,
            label_align=qtg.Align_Text.CENTER,
            label_width=10,
            label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
            width=6,
            height=1,
            txt_align=qtg.Align_Text.CENTER,
            txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=20),
            txt_fontsize=12,
            bold=True,
            italic=True,
            underline=True,
            enabled=True,
            visible=True,
            tooltip="Check Box Press Me",
            tune_hsize=15,
            tune_vsize=15,
            user_data={"key": "value"},
            buddy_control=qtg.HBoxContainer().add_row(
                qtg.Spacer(width=1),
                qtg.Button(tag="button_push", text="Push Me!", callback=self.event_handler, width=12)
            ),
    
        )
```

<br>**Methods**
<br>A subset of the [_qtpyBase_Control](#_qtpybase_control) methods apply to Checkbox instances

| **Method**     | **Arguments** | **Type** | **Description**                                                | **Optional** |
|----------------|---------------|----------|----------------------------------------------------------------|--------------|
| button_checked |               | bool     | <br><b>Returns:</b><br> The checked state of the checkbox.<br> |              |
| button_toggle  |               | None     |                                                                |              |
|                | value (True)  | bool     | True checkbox is checked, False checkbox is unchecked.         | ✓            |
| label_get      |               | str      | <br><b>Returns:</b><br> The text of the label.<br>             |              |
| value_get      |               | bool     | <br><b>Returns:</b><br> True checked, False not checked<br>    |              |
| value_set      |               | None     |                                                                |              |
|                | value         | bool     | True checkbox is checked, False checkbox is unchecked.         | ❌            |

#### ComboBox

Calling ComboBox in a layout will generate a dropdown combobox control on a form. The "tag"
,"text", "callback" and "items" arguments are generally the only arguments used. It is 
suggested to set width and height as the font selected might not 
automatically size correctly.

<br>**Properties**
<br>The following properties apply when a ComboBox is instantiated with the ComboBox call as below

| **Property**      | **Description**                                                                                                      | **Type**                                    | **Optional** |
|-------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|--------------|
| bold              | Sets the combobox text bold if True otherwise not                                                                    | bool (False)                                | ✓            |
| buddy_control     | Control or container with controls that sit to the right of the combobox                                             | Container or GUI Control                    | ✓            | 
| callback          | The method called when the combobox is modified                                                                      | Callable (None)                             | ✓            |
| display_na        | Displays N/A (Not Applicable/Available) in the drop down list if True Otherwise not                                  | bool (True)                                 | ✓            |
| dropdown_width    | The width of the combobox (in characters if pixel_unit is False,Otherwise pixels)                                    | int > 0 (10)                                | ✓            |
| enabled           | Enables/Disables the combobox                                                                                        | bool (True)                                 | ✓            |
| height            | The height of the combobox (in characters if pixel_unit is False,Otherwise pixels)                                   | int > 0 (10)                                | ✓            |
| italic            | Sets the combobox text italic if True otherwise not                                                                  | bool (False)                                | ✓            |
| items             | Items to add to the dropdown list                                                                                    | list or tuple [Combo_Item](#combo_item)     | ✓            |
| label             | Displays text to the left of the combobox                                                                            | str ("")                                    | ✓            |
| label_align       | Alignment of the text displayed in the label                                                                         | [Align_Text](#align_text) (Align_Text.LEFT) | ✓            |
| label_font        | The font definition for the label                                                                                    | [Font](#font)                               | ✓            |
| label_width       | Sets the label width (in characters if pixel_unit is<br> False,Otherwise pixels)                                     | int > 0 (0)                                 | ✓            |
| num_visible_items | Number of items displayed in the dropdown list                                                                       | int >= 1 (15)                               | ✓            |
| pixel_unit        | Use pixels for width/height, pixels if True, Otherwise characters                                                    | bool (False)                                | ✓            |
| tag               | The application name of the combobox                                                                                 | str (System Generated)                      | ✓            |
| txt_font          | The font definition for the combobox dropdown list (style will override<br> italic,size will override txt_fontsize ) | [Font](#font)                               | ✓            |
| txt_fontsize      | The point size of the text   in the combobox dropdown list                                                           | int (10)                                    | ✓            |
| tune_hsize        | Add or subtracts pixels units to the width. Used in aligning controls                                                | int (0)                                     | ✓            |
| tune_vsize        | Add or subtracts pixels units to the height. Used in aligning controls                                               | int (0)                                     | ✓            |
| tooltip           | Sets the tooltip displayed when the combobox is hovered over                                                         | str                                         | ✓            |
| translate         | Translates dropdown text if True Otherwise does not translate                                                        | bool (True)                                 | ✓            |
| user_data         | Any data item the user wants to attach to the combobox                                                               | any (None )                                 | ✓            |
| underline         | Underlines the combobox dropdown text if True otherwise not                                                          | bool (False)                                | ✓            |
| visible           | Makes the combobox visible if True otherwise invisible                                                               | bool (True)                                 | ✓            |
| width             | The width of the combobox (in characters if pixel_unit is False,Otherwise pixels)                                    | int > 0 (10)                                | ✓            |

A fully loaded combobox declaration:
- **Note: Only "tag", "text" ,"callback" and "items" are usually needed**
```
ComboBox(
            tag="combo_box",
            label="Combo Box",
            display_na=True,
            dropdown_width=35,
            items=[
                qtg.Combo_Item(
                    display="Item 1",
                    data=None,
                    icon=qtg.Sys_Icon.computericon.get(),
                    user_data=None,
                ),
                qtg.Combo_Item(
                    display="Item 2", data=None, icon=None, user_data=None
                ),
                qtg.Combo_Item(
                    display="Item 3", data=None, icon=None, user_data=None
                ),
            ],
            callback=self.event_handler,
            label_align=qtg.Align_Text.CENTER,
            label_width=10,
            label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
            width=8,
            height=1,
            txt_font=qtg.Font(style=qtg.Font_Style.ITALIC, size=12),
            txt_fontsize=12,
            bold=True,
            italic=True,
            underline=True,
            enabled=True,
            visible=True,
            tooltip="Check Box Press Me",
            tune_hsize=15,
            tune_vsize=1,
            user_data={"key": "value"},
            buddy_control=qtg.HBoxContainer().add_row(
                qtg.Spacer(width=1),
                qtg.Button(tag="button_push2", text="Push Me 2!", callback=self.event_handler, width=12)
            ),
        ),
```

<br>**Methods**
<br>A subset of the [_qtpyBase_Control](#_qtpybase_control) methods apply to ComboBox instances

| **Method**           | **Arguments**  | **Type**                             | **Description**                                                                                                                                                                                         | **Optional** |
|----------------------|----------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| count_items          |                | int \>= 0 <= number of items in list | <br><b>Returns:</b><br> The number of items in the Combobox<br>                                                                                                                                         |              |
| display_width_set    |                | None                                 |                                                                                                                                                                                                         |              |
|                      | display_width  | int                                  | The number of characters to display in the Combobox                                                                                                                                                     | ❌            |
| get_items            |                | list [Combo_Data](#combo_data)       | <br><b>Returns:</b><br> returns the List of items in the combo box<br>                                                                                                                                  |              |
| icon_set             |                | int                                  | <br><b>Returns:</b><br> 1 if successful, -1 if not<br>                                                                                                                                                  |              |
|                      | combo_index    | int                                  | Row index in the combobox where the icon is to be placed                                                                                                                                                | ❌            |
|                      | icon           | str [File Name], QIcon,QPixmap       | A QPixmap, QIcon or the icon file name                                                                                                                                                                  | ❌            |
| is_combo_child       |                | bool                                 | <br><b>Returns:</b><br> True if the Combobox is child of another combo box. False if not.<br>                                                                                                           |              |
| load_csv_file        |                | int                                  | <br><b>Returns:</b><br> Length of maximum item if load OK, Otherwise -1<br>                                                                                                                             |              |
|                      | data_index     | int (1)                              | The column in the file to load into user data                                                                                                                                                           | ✓            |
|                      | delimiter      | str (",")                            | CSV file field separator                                                                                                                                                                                | ✓            |
|                      | file_name      | str                                  | The path to the CSV file                                                                                                                                                                                | ❌            |
|                      | ignore_header  | bool (true)                          | Set True if the CSV file has a header row                                                                                                                                                               | ✓            |
|                      | line_start     | int (1)                              | The line in the file to start loading data from                                                                                                                                                         | ✓            |
|                      | select_text    | str (")                              | The text to select after load                                                                                                                                                                           | ✓            |
|                      | text_index     | int (1)                              | The column in the CSV file to load into display                                                                                                                                                         | ✓            |
| load_items           |                | int                                  | <br><b>Returns:</b><br> int<br>                                                                                                                                                                         |              |
|                      | auto_na        | bool (True)                          | True puts na_string (Not Available) in combobox, Otherwise not                                                                                                                                          | ✓            |
|                      | clear_items    | bool (True)                          | Clears existing items from the combobox                                                                                                                                                                 | ✓            |
|                      | na_string      | str ("N/A")                          | The "Not Available" string                                                                                                                                                                              | ✓            |
| print_all_to_console |                | None                                 | Debug method - prints items to console                                                                                                                                                                  |              |
| select_index         |                | None                                 | Scrolls to an index in the combobox and  sets the current index of the widget to the select_index argument                                                                                              |              |
|                      | select_index   | int                                  | The index of the item to select                                                                                                                                                                         | ❌            |
| select_text          |                | int                                  | Selects the text in the combobox <br><b>Returns:</b><br> The index of the selected text in the dropdown.                                                                                                |              |
|                      | select_text    | int                                  | <br><b>Returns:</b><br> The index of the selected text in the dropdown.<br>                                                                                                                             | ❌            |
|                      | case_sensitive | bool (False)                         | Whether to perform a case-sensitive match.                                                                                                                                                              | ✓            |
|                      | partial_match  | bool (False)                         | Whether to perform a partial text match.                                                                                                                                                                | ✓            |
|                      | select_text    | str                                  | The text to select.                                                                                                                                                                                     |              |
| value_get            |                | [Combo_Data](#combo_data)            | <br><b>Returns:</b><br> Current row [Combo_Data](combo_data) if index = -1, Selected row [Combo_Data](combo_data) if row > 0<br>                                                                        |              |
|                      | index          | int (-1)                             | The index of the item to get. Defaults to current row.                                                                                                                                                  | ✓            |
| value_remove         |                | None                                 | Remove an item from the combobox a the given index.                                                                                                                                                     |              |
|                      | index          | int                                  | The index of the item to remove.                                                                                                                                                                        | ❌            |
| value_set            |                | None                                 | Sets a value in the dropdown and scrolls to that value. if COMBO_DATA index is -1 then data and display. <br> Values must match for scroll to happen                                                    |              |
|                      | value          | str \| [Combo_Data](#combo_data)     | Inserts a value in the dropdown. <br>If [Combo_Data](#combo_data) index = -1 insert alphabetically when insert_alpha is True, Otherwise insert at bottom of list. if index > 1 insert at index position | ❌            |                                                                                                                                                  |
|                      | insert_alpha   | bool (True)                          | Insert alphabetically                                                                                                                                                                                   | ✓            |

#### Dateedit

Calling Dateedit in a layout will generate a Dateedit control, with an erase button
and a dropdown calendar, on a form. The "tag" ,"text" and "callback" arguments 
are generally the only arguments used. It is suggested to set width and height 
as the font selected might not automatically size correctly.

**Constants**

| **Constant** | **Description**                                            | **Type**         |
|--------------|------------------------------------------------------------|------------------|
| MINDATE      | The minimum date supported by Dateedit (1 Jan 100 AD)      | QDate(100, 1, 1) |
| NODATE       | Used internally by Dateedit to signify a no date condition | QDate(1, 1, 1)   |

<br>**Properties**
<br>The following properties apply when a Datedit is instantiated with the Datedit call as below

| **Property** | **Description**                                                                                                                    | **Type** | **Optional** |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|----------|--------------|
| date         | Set to the current date if not set ("")                                                                                            | str ("") | ✓            |
| format       | Date format. The `format` property is set to the current locale's date format if this is not set ("")<br>Follows QT date formating | str ("") | ✓            |
| min_date     | Set to **MINDATE** if not set ("")                                                                                                 | str ("") | ✓            |
| max_date     | Set to the to the current date if not set ("")                                                                                     | str ("") | ✓            |

A fully loaded Dateedit declaration:
- **Note: Only "tag", "text" ,and "callback" are usually needed **
  - text behaves a little differently here as it serves to set the tooltip on the erase button
  - max_date, min_date and format can be used to configure the date range and 
  format of the Dateedit GUI Control if desired

```
Dateedit(
            tag="dateedit2",
            text="Tick Me!",
            date="2022-01-01",
            format="yyyy-MM-dd",
            max_date="2032-01-01",
            min_date="2000-01-01",
            label="Date edit 2",
            callback=self.event_handler,
            label_align=qtg.Align_Text.CENTER,
            label_width=10,
            label_font=qtg.Font(style=qtg.Font_Style.OBLIQUE, size=14),
            width=6,
            height=1,
            txt_align=qtg.Align_Text.CENTER,
            txt_font=qtg.Font(style=qtg.Font_Style.NORMAL, size=20),
            txt_fontsize=12,
            bold=True,
            italic=True,
            underline=True,
            enabled=True,
            visible=True,
            tooltip="Date Edit 2 ",
            tune_hsize=15,
            tune_vsize=15,
            user_data={"key": "value"},
            buddy_control=qtg.HBoxContainer().add_row(
                qtg.Spacer(width=1),
                qtg.Button(
                    tag="dateedit_button_push",
                    text="Date Edit 2 Push Me!",
                    callback=self.event_handler,
                    width=12,
                ),
        )
```

<br>**Methods**
<br>A subset of the [_qtpyBase_Control](#_qtpybase_control) methods apply to Dateedit instances

| **Method** | **Arguments**       | **Type**                  | **Description**                                                                                                                    | **Optional** |
|------------|---------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------|
| clear      |                     | None                      | Clears the date displayed                                                                                                          |              |
|            | default_text        | str ("-")                 | Date text to place in the edit control (must be a valid date string or - to clear the date)                                        | ✓            |
| date_get   |                     | str                       | Gets the date. If date_tuple as a [Date_Tuple](#date_tuple), Otherwise a string formatted as per date_format<br>This is Overloaded |              |
|            | date_format ("")    | str                       | Set the date format for a string return if date_tuple is False<br>Follows QT date formating                                        | ✓            |
|            | date_tuple  (False) | bool                      | True, return date format as a [Date_Tuple](#date_tuple), Otherwise a string, formated as per date_format                           | ✓            |
| date_get   |                     | [Date_Tuple](#date_tuple) | Gets the date. If date_tuple as a [Date_Tuple](#date_tuple), Otherwise a string formatted as per date_format<br>This is Overloaded |              |
|            | date_format ("")    | str                       | Set the date format for a string return if date_tuple is False<br>Follows QT date formating                                        | ✓            |
|            | date_tuple  (False) | bool                      | True, return date format as a [Date_Tuple](#date_tuple), Otherwise a string, formated as per date_format                           | ✓            |
| date_set   |                     | None                      | Sets the date in the control                                                                                                       |              |
|            | date                | str ("")                  | A string representing the date to set, formatted as 'y-m-d'.                                                                       | ✓            |
|            | date_format         | str ("")                  | The format of the date string, defaults to an empty string.                                                                        | ✓            |
|            | default_text        | str  ("-")                | if the date string is '-' then the date control is cleared                                                                         | ✓            |
| date_valid |                     | bool                      | Checks if a date is valid<br><b>Returns:</b><br> True if date is valid, False otherwise<br>                                        |              |
|            | date                | str                       | date in string format                                                                                                              | ❌            |
|            | date_format         | str                       | The format of the date string.                                                                                                     | ❌            |
| value_get  |                     | str                       | Gets the date. If date_tuple as a [Date_Tuple](#date_tuple), Otherwise a string formatted as per date_format<br>This is Overloaded |              |
|            | date_format ("")    | str                       | Set the date format for a string return if date_tuple is False<br>Follows QT date formating                                        | ✓            |
|            | date_tuple  (False) | bool                      | True, return date format as a [Date_Tuple](#date_tuple), Otherwise a string, formated as per date_format                           | ✓            |
| value_get  |                     | [Date_Tuple](#date_tuple) | Gets the date. If date_tuple as a [Date_Tuple](#date_tuple), Otherwise a string formatted as per date_format<br>This is Overloaded |              |
|            | date_format ("")    | str                       | Set the date format for a string return if date_tuple is False<br>Follows QT date formating                                        | ✓            |
|            | date_tuple  (False) | bool                      | True, return date format as a [Date_Tuple](#date_tuple), Otherwise a string, formated as per date_format                           | ✓            |
| value_set  |                     | None                      | Sets the date in the control                                                                                                       |              |
|            | date                | str ("")                  | A string representing the date to set, formatted as 'y-m-d'.                                                                       | ✓            |
|            | date_format         | str ("")                  | The format of the date string, defaults to an empty string.                                                                        | ✓            |

### FolderView

FolderView is a widget that displays a folder path in a tree format

<br>**Properties**
<br>The following properties apply when a Datedit is instantiated with the Datedit call as below

| **Property**  | **Description**                                                                                                                                                                    | **Type**                                 | **Optional** |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|--------------|
| width         | The width of the FolderView GUI control <br>Generally not set as header_widths determines the widths<br> Characters if [pixel_unit](#_qtpybase_control) is False, Otherwise pixels | int (40)                                 | ✓            |
| height        | The height of the FolderView GUI control<br> Characters if [pixel_unit](#_qtpybase_control) is False, Otherwise pixels                                                             | int (15)  # In  lines                    | ✓            |
| root_dir      | Sets root path of the FolderView                                                                                                                                                   | str ("\\") #Current directory            | ✓            |
| dir_only      | True, displays directories only, Otherwise display all directories and files                                                                                                       | bool (False)                             | ✓            |
| multiselect   | True, allows multiple files and/or folders to be selected, Otherwise only allow one file and/or folder to be selected at a time                                                    | bool (False)                             | ✓            |
| header_widths | Sets the header widths - maximum of 4 allowed <br> Characters if [pixel_unit](#_qtpybase_control) is False, Otherwise pixels                                                       | list [int,...] \| tuple(int,...) = (40,) | ✓            | 
| header_font   | Sets the font properties of the header row                                                                                                                                         | [Font](#font) \| None (None)             | ✓            |
| click_expand  | True, expand folders when clicked on, Otherwise only expand folders if the handle is clicked                                                                                       | bool (False)                             | ✓            |


<br>**Methods**
<br>A subset of the [_qtpyBase_Control](#_qtpybase_control) methods apply to FolderView instances

| **Method**      | **Arguments** | **Type** | **Description**                                                                                    | **Optional** |
|-----------------|---------------|----------|----------------------------------------------------------------------------------------------------|--------------|
| change_folder   |               | None     |                                                                                                    |              |
| expand_on_click |               | bool     | <br><b>Returns:</b><br> The expand on click setting (true == dir node expands when clicked on)<br> |              |
| headerData      |               | None     |                                                                                                    |              |
|                 | section       | int      | The column number.                                                                                 |              |
| value_get       |               | None     | <br><b>Returns:</b><br> The tuple containing the file values from the selected node<br>            |              |
| value_set       |               | None     |                                                                                                    |              |
|                 | value         | str      | The text to set the text to                                                                        |              |

### Slider
 
Instantiates a Slider widget and associated properties

| **Property**         | **Description**                                                     | **Type**           | **Optional** |
|----------------------|---------------------------------------------------------------------|--------------------|--------------|
| orientation          | "vertical" or "horizonral" presentation of the slider               | str ("horizontal") | ✓            |
| page_step            | The step size when the page up/down is pressed                      | int (10)           | ✓            |
| range_max            | The maximum value of the slider                                     | int (100)          | ✓            |
| range_min            | The minimum value of the slider                                     | int (0)            | ✓            |
| scale_factor_percent | Scales the value internally by a certain perentage (_Experimental_) | float (0.0)        | ✓            |
| single_step          | The step size when a single step is taken                           | int (1)            | ✓            |



 
| **Method**    | **Arguments** | **Type**     | **Description**                                                     | **Optional** |
|---------------|---------------|--------------|---------------------------------------------------------------------|--------------|
| scale_factor  |               | float        | The scale factor calculated from the percentage                     |              |
| scale_factor  |               | None         | Sets the scale factor as a percentage.                              |              |
|               | value         | float        | The scale factor as a percentage                                    | ❌            |
| range_min_set |               | None         | Sets the minimum value of the slider.<br><br>                       |              |
|               | range_min     | int          | The minimum value of the slider.                                    | ❌            |
| range_max_set |               | None         | Sets the maximum value of the slider.<br><br>                       |              |
|               | range_max     | int          | The maximum value of the slider.                                    | ❌            |
| value_get     |               | int          | <br><b>Returns:</b><br> - int: The value of the slider.<br>         |              |
| value_set     |               | None         | Sets the value of the slider.<br><br>                               |              |
|               | value         | int          | The value to set the slider to.                                     | ❌            |
|               | block_signals | bool (False) | True, stop the slider from emitting signals, Otherwise emit signals | ✓            |


### QTPYGUI Enumerated Types/Class Reference

The following enumerated types and classes are used to define the features and 
behaviour of QTPYGUI 

#### Align

Align is an enumerated type used in defining the alignment of containers and GUI controls

| Property     | Description | Type                             |
|--------------|-------------|----------------------------------|
 | LEFT         |             | Qt.AlignLeft                     |
| CENTER       |             | Qt.AlignCenter                   |
| CENTERLEFT   |             | Qt.AlignCenter \| Qt.AlignLeft   |
| CENTERRIGHT  |             | Qt.AlignCenter \| Qt.AlignRight  |
| RIGHT        |             | Qt.AlignRight                    |
| TOP          |             | Qt.AlignTop                      |
| TOPCENTER    |             | Qt.AlignTop                      |
| TOPLEFT      |             | Qt.AlignTop \| Qt.AlignLeft      |
 | TOPRIGHT     |             | Qt.AlignTop \| Qt.AlignRight     |
| BOTTOM       |             | Qt.AlignBottom                   |
| VCENTER      |             | Qt.AlignVCenter                  |
| HCENTER      |             | Qt.AlignHCenter                  |
| BOTTOMCENTER |             | Qt.AlignBottom \| Qt.AlignCenter |
| BOTTOMLEFT   |             | Qt.AlignBottom \| Qt.AlignLeft   |
| BOTTOMRIGHT  |             | Qt.AlignBottom \| Qt.AlignRight  |

#### Align_Text

Align_Text is an enumerated type that aligns text using style sheet type 
declaration (Some controls will remap to [Align](#align) types)

| Property | Description | Type              |
|----------|-------------|-------------------|
 | LEFT     |             | text-align:left   |
| CENTER   |             | text-align:center |
| RIGHT    |             | text-align:right  |
| TOP      |             | text-align:top    |
| BOTTOM   |             | text-align:bottom |

### Char_Pixel_Size

Char_Pixel_Size is a helper class that stores the width and height values in 
pixels 

| Property | Description      | Type |
|----------|------------------|------|
| height   | Height in pixels | int  |
| } width  | Width in pixels  | int  |

#### Combo_Data

Combo_Data is a helper class used to store data sourced from combo box items

| Property  | Description                          | Type                                                               |
|-----------|--------------------------------------|--------------------------------------------------------------------|
| display   | Text displayed in dropdown row       | str                                                                |
| data      | user data held in dropdown row       | str, int, float, bytes, bool, None                                 |
| index     | Row index of data item               | int >= 0                                                           |
| user_data | Data stored by user  in dropdown row | None , str, int , float , bytes , bool , tuple , list , dict, None |

#### Combo_Item

Combo_Item is a helper class used to set combo box items.  All attributes are mandatory.

| Property  | Description                            | Type                                                               |
|-----------|----------------------------------------|--------------------------------------------------------------------|
| display   | Text displayed in dropdown row         | str                                                                |
| data      | user data held in dropdown row         | str, int, float, bytes, bool, None                                 |
| icon      | The icon image displayed on the button | str [File Name]<br/>,QIcon,QPixmap, None                           |
| user_data | Data stored by user  in dropdown row   | None , str, int , float , bytes , bool , tuple , list , dict, None |

#### Col_Def

Col_Def is a helper class used to set the column attributes of grid controls. All attributes are mandatory.

| Property  | Description                                                                                   | Type    |
|-----------|-----------------------------------------------------------------------------------------------|---------|
| checkable | The column rows have a check-box if True, Otherwise no checkbox is displayed                  | bool    |
| editable  | The column rows can be edited if True, Otherwise the column rows can not be edited            | bool    |
| label     | the label displayed in the columns first  row denoting the column name                        | str     |
| tag       | The application name for the column                                                           | str     |
| width     | The width of the column in chars if GUI control argument pixel_unit is True, Otherwise pixels | int > 0 |

### Date_Tuple
Date_Tuple is a helper class used by [Dateedit](#dateedit) to store the date. 
Basic date validation checks are done.

| Property | Description | Type |
|----------|-------------|------|
| year     | The year    | int  |
| month    | The month   | int  |
| day      | The day     | int  |

#### Font

Font is a helper class that defines the [font](#font) properties, utilised in 
font related arguments in GUI control definitions.

Colours are checked to ensure they are valid and will raise an assertion error 
if they are not. 

| Property   | Description                 | Type                                 |
|------------|-----------------------------|--------------------------------------|
| backcolor  | Background colour           | str ("")                             |
| forecolor  | Foreground colour           | str ("")                             |
| font_name  | The font name               | str ("")                             |
| selectback | Selection background colour | str ("")                             |
| selectfore | Selection foreground colour | str ("")                             |
| size       | The font point size         | int (10)                             |
| style      | The font style              | [Font_Style](#font_style) (NORMAL)   |
| weight     | The font weight             | [Font_Weight](#font_weight) (NORMAL) |

#### Font_Style
Font_Style is an enumerated type that defines the style of the [font](#font)

| Property | Description                   | Type               |
|----------|-------------------------------|--------------------|
| NORMAL   | Font has no special features  | QFont.StyleNormal  |
| ITALIC   | Defines font as italic style  | QFont.StyleItalic  |
| OBLIQUE  | Defines font as oblique style | QFont.StyleOblique |

#### Font_Weight
Font_Weight is an enumerated that defines the weight of the [font](#font)

| Property   | Description                                         | Type       |
|------------|-----------------------------------------------------|------------|
| BLACK      | Defines the font as black                           | Enumerated |
| BOLD       | Defines the font as bold                            | Enumerated |
| DEMIBOLD   | Defines the font as demibold                        | Enumerated |
| EXTRABOLD  | Defines the font as extra bold                      | Enumerated |
| EXTRALIGHT | Defines the font as extra light                     | Enumerated |
| LIGHT      | Defines the font as light                           | Enumerated |
| MEDIUM     | Defines the font as medium                          | Enumerated |
| NORMAL     | Defines the font as normal with no special features | Enumerated |
| THIN       | Defines the font as thin                            | Enumerated |

#### Frame
Frane is an enumerated type that defines the frame of a GUI control where supported

| Property | Description    | Type              |
|----------|----------------|-------------------|
| PLAIN    | A flat frame   | qtW.QFrame.Plain  |
| RAISED   | A raised frame | qtW.QFrame.Raised |
| SUNKEN   | A sunken frame | qtW.QFrame.Sunken |

#### Frame_Style
Frame_Style is an enumerated type that defines the frame of a GUI control where supported

| Property | Description             | Type                   |
|----------|-------------------------|------------------------|
| BOX      | A box frame             | qtW.QFrame.Box         |
| PANEL    | A panel frame           | qtW.QFrame.Panel       |
| HLINE    | A horizontal line frame | qtW.QFrame.HLine       |
| NONE     | No frame                | qtW.QFrame.NoFrame     |
| VLINE    | A vertical line frame   | qtW.QFrame.VLine       |
| WPANEL   | A window panel frame    | qtW.QFrame.WinPanel    |
| STYLED   | A Styled panel frame    | qtW.QFrame.StyledPanel |


#### Widget_Frame
 Widget_Frame` is a helper class that defines the style of the frame around a widget

| Property      | Description | Type                        |
|---------------|-------------|-----------------------------|
| frame         |             | [Frame](#frame)             |
| frame_style   |             | [Frame_Style](#frame_style) |
| line_width    |             | int =3                      |
| midline_width |             | int = 0                     |





# TO BE CONTINUED....







 














