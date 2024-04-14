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
| Control           | Description                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| [Button](#button) | Creates a button, text and icon are optional                                                                                 |
| Checkbox          | Creates a check box that a user can click on or off                                                                          | 
| ComboBox          | Creates a drop down selection box, icon in list is <br/>optional                                                             |
| Label             | Creates a text string                                                                                                        |
| Dateedit          | Creates a date edit control with a dropdown calendar and <br/>an erase button                                                |
| FolderView        | Creates a control that displays the contents of a folder in a Grid                                                           |
| Grid              | Creates a control that displays data in a table (grid) format                                                                |
| Image             | Creates a control that displays an image                                                                                     |
| LineEdit          | Creates a control that allows text to be edited and displayed<br/> in a single line                                          |
| Menu              | Creates a menu just below the title bar                                                                                      |
| ProgressBar       | Creates a control that displays the progress of an operation                                                                 |
| RadioButton       | Creates a radio button control. In a group only one can be <br/>selected at a time                                           |
| Switch            | Creates a switch control that can be used to turn on and <br/>off a feature                                                  |
| Slider            | Creates a slider control than can be used to set a value <br/>by dragging the handle                                         |
| Spinbox           | Creates a spinbox control that allows numbers to be set <br/>via clicking up and down arrows or entering the number directly |
| Tab               | Creates a tab control that has multiple pages, each <br/>housing their own set of GUI controls                               |
| TextEdit          | Creates a text entry control that can span multiple lines                                                                    |
| Timeedit          | Creates a time edit control with an erase button                                                                             |
| Treeview          | Creates a control that displays data as a tree view                                                                          |

#### Button

Calling Button() in a layout will generate a button control on a form. The "tag"
,"text" and "callback" arguments are generally the only arguments used. It is 
suggested to set width and height as the font selected might not 
automatically size correctly.  

| Argument             | Description                                                                          | Type                                        | Optional |
|----------------------|--------------------------------------------------------------------------------------|---------------------------------------------|----------|
| auto_repeat_interval | If > 0 the button keeps firing Clicked events when <br>held down (milliseconds)      | int >= 0 (0)                                | ✓        |
| bold                 | Sets the button text bold if True otherwise not                                      | bool (False)                                | ✓        |
| callback             | The method called when the button is pressed                                         | Callable                                    | ✓        |
| enabled              | Enables/Disables the button                                                          | bool (True)                                 | ✓        |
| height               | The height of the button (in characters if pixel_unit is<br> False,Otherwise pixels) | int > 0 (10)                                | ✓        |
| icon                 | The icon image displayed on the button                                               | str [File Name]<br/>,QIcon,QPixmap          | ✓        |
| italic               | Sets the button text italic if True otherwise not                                    | bool (False)                                | ✓        |
| label                | Displays text to the right of the button                                             | str                                         | ✓        |
| label_align          | Alignment of the text displayed in the label                                         | Align_Text](#align_text) (Align_Text.LEFT)  | ✓        |
| pixel_unit           | unit of width/height is pixels if True, Otherwise False                              | bool (False)                                | ✓        |
| tag                  | The application name of the button                                                   | str                                         | ✓        |
| text                 | The text displayed on the button                                                     | str                                         | ✓        |
| txt_align            | Alignment of the text displayed on the button                                        | [Align_Text](#align_text) (Align_Text.LEFT) | ✓        |
| txt_font             | The font definition for the button                                                   | [Font](#font)                               | ✓        |
| underline            | Underlines the button text if True otherwise not                                     | bool (False)                                | ✓        |
| visible              | Makes the controls visible if True otherwise invisible                               | bool (True)                                 | ✓        |
| width                | The width of the button (in characters if pixel_unit is<br> False,Otherwise pixels)  | int > 0 (10)                                | ✓        |



### QTPYGUI Enumerated Types/Class Reference

The following enumerated types and classes are used to define the features and 
behaviour of QTPYGUI 

#### Align

Used in defining the alignment of containers and GUI controls

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
Aligns text using style sheet type declaration (Some controls will remap to 
[Align](#align) types)

| Property | Description | Type              |
|----------|-------------|-------------------|
 | LEFT     |             | text-align:left   |
| CENTER   |             | text-align:center |
| RIGHT    |             | text-align:right  |
| TOP      |             | text-align:top    |
| BOTTOM   |             | text-align:bottom |

#### Font
Defines the [font](#font) properties, utilised in font related arguments in GUI control 
definitions.

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
Defines the style of the [font](#font)

| Property | Description                   | Type               |
|----------|-------------------------------|--------------------|
| NORMAL   | Font has no special features  | QFont.StyleNormal  |
| ITALIC   | Defines font as italic style  | QFont.StyleItalic  |
| OBLIQUE  | Defines font as oblique style | QFont.StyleOblique |

#### Font_Weight
Defines the weight of the [font](#font)

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




# TO BE CONTINUED....







 














