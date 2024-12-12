# ModuleSearchApp - README

## Overview

This project is a KivyMD-based Python application designed to allow users to search for modules in two categories: Community and Enterprise. It features a search bar where users can input a module name and get information about whether the module is available in the Community or Enterprise version. The app also includes a theme toggle button to switch between Light and Dark modes.

## Requirements

Before running this project, you need to install the following dependencies:

- Python 3.7 or higher
- Kivy
- KivyMD

### Install Dependencies

To install the required dependencies, follow these steps:

1. **Install Python 3.7 or higher**  
   If you don't have Python installed on your machine, download and install the latest version from [Python's official website](https://www.python.org/downloads/).

2. **Install Virtual Environment (optional but recommended)**  
   It's a good practice to use a virtual environment to manage dependencies for your project. To install `virtualenv`, run the following command:

   ```ini
   pip install virtualenv
  

**3. Setting Up and Running the Project**

**Create a Virtual Environment**

Navigate to your project folder (where `main.py` is located) and create a virtual environment by running the following command:

```ini
python -m venv .venv
.\venv\Scripts\activate
```
**4. Install the Required Packages**
Once the virtual environment is activated, install Kivy and KivyMD by running:

```ini
pip install kivy kivymd
```

**5. Running the Project**
To run the ModuleSearchApp:

Make sure you are in the project directory (where main.py is located).
Activate your virtual environment (if it's not already activated).
Run the script using Python:
```ini
python main.py
```
The app will start, and you can begin using the module search functionality. Enter a module name into the input field, click "Search", and the result will be displayed with a check or cross icon depending on the module's availability. You can also toggle between Light and Dark themes using the "Dark Mode" button.



