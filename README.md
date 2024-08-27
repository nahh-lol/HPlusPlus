# H++ Readme
## Introduction

What is up *[r/TheLetterH](https://www.reddit.com/r/TheLetterH/)* people? I was bored so I made this basic programming language

# Installation

## Windows
The install instructions for windows
### Step 1
Download the repo

### Step 2
Move the H++ folder to the place where you want to keep it, I put mine in program files, so the path for me is: `C:\Program Files\H++`. This folder should have the `h.py`, `h.ico`, and `h.bat` files.

### Step 3
**In this step we make h++ globally accesible so you can run it from any directory in your terminal**

Add the path to the H++ folder into your path environment variable.
* If you dont know how to *edit your environment variables*, heres how.
    1.  In the start menu, search **environment variables** and click **Edit the system environment variables**. Once in the menu, click the **Environment Variables** button and a new menu will pop up.
    
    2. Make a new variable called `HPP_PATH` under **System variables** and set the value to be the path to your H++. Click ok to exit all the menus and your done.
    
### Step 4
**SKIP THIS STEP IF YOU ARE UNCOMFORTABLE MESSING WITH YOUR REGISTRY**
Okay, this one is optional but if you dont do this my icon file will go to waste 😭. Anyways, to give the `.hhh` files a **Custom Icon**, remember that `h.ico` file from earlier? Well we're finally gonna use it! 
Purpose: This step **registers the .hhh extension** in the **Windows Registry** so the system knows how to handle files with this extension.

1. Open Registry Editor:
    * Press Win + R to open the Run dialog. Type regedit and press Enter. This opens the Registry Editor.

**WAIT UP!!!!!**
Before making changes, it's a good idea to back up your registry. Click on `File > Export` and save a backup.

2. Navigate to File Types:
   * Go to the following path: `HKEY_CLASSES_ROOT`

3. Create the **.hhh** Key:
     * Right-click on `HKEY_CLASSES_ROOT` in the left-hand pane.
    Select `New > Key`
    Name this key `.hhh`.

4. Set the Default Value:
    * After creating the .hhh key, click on it.
      In the ***right-hand pane***, you'll see a field labeled `(Default)`.
      Double-click on `(Default)` and set its value to a name that will represent the file type, such as **H++ File**.

Explanation: The **.hhh key** tells Windows that when it encounters a file with the **.hhh extension**, it should treat it according to the **rules defined in another key** (which you'll create in the next step).

Step 4 (Part 2)
Purpose: This step defines how Windows should display and handle **files with the .hhh extension**. You'll give it a **human-readable description** (like "H++ File") and **associate an icon** with it.

1. Create a Key for the File Type Description
   * In `HKEY_CLASSES_ROOT`, right-click again and select `New > Key`.
     Name this new key the same as the value you set in the `(Default)` field for the `.hhh key`. For example, if you set the value to `H++ File`, name this new key `H++ File`.

2. Create the DefaultIcon Key:
   * Right-click on the `H++ File` key you just created.
     Select `New > Key` and name this key `DefaultIcon`.

3. Set the Icon Path:
    * Click on the `DefaultIcon` key.
      In the **right-hand pane**, double-click `(Default)`.
      Enter the path to your **h.ico file**, e.g., `C:\Program Files\H++\h.ico`.

Explanation: The **H++ File** key defines what type of file *.hhh* is (*e.g., "H++ File"*) and specifies a **custom icon** to display. The **DefaultIcon** key within it points to the actual icon file that will be used for **.hhh files**.

# Linux
### I'm not gonna explain in too much detail, because, if your on linux, you probably know what your doing already anyways. 
If your on linux, just put the H++ folder in your `usr/local/bin` folder, make it executable, and thats about it I think.

# Example Code

### Hello World
```H++
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh H
```
*writing this gave me a brain aneurysm*

# How it works

## Writing code

To print a character (eg: H), since uppercase H is the 72nd letter in ascii, you would use lowercase h to increment the value 72 times and uppercase H to print it out.

## Reading code

No, thank you.

## Running code

Assuming you did everything right, you just need to cd into the directory of the file your tryna run. The command to run it is `h filename.hhh`.

# Will I be adding more?

Maybe, if i can manage to stop procrastinating lol.

