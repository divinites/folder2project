# Open Folder From File As a Project

## Introduction

Sublime Text has a bunch of useful API, However, given an opened file, there is no explicit way to open the folder that contains this file as a project, especially when a *.sublime-project inside that folder. That's why I develop this small plug-in. Basically, this plug-in does two things:

- Open the folder that contains the openned file as a project. If there is a sublime-project file in this folder, load it (This may change the interpreter, syntax theme, etc.)
- provide an API for futher developement:

  *window.run_command("open_folder_as_project", {"folder": folder})*


It is a bit tricky to implement this API. First, Sublime only has three project-related API:

    - sublime.window.project_file_name()

    - sublime.window.project_data()

    - sublime.window.set_project_data()

Admittedly, if you have already opened a project file, the methods API are enough to retrive the project settings, but no method can directly open a sublime-project file, nor open a folder as a project.

Therefore, I designed a workaround: 
1. Search the folder for *.sublime-project file
2. If exist, load this file. Otherwise create a temporary project configuration.
3. put folder's path in project settings, temporarily change all relative paths to absolute paths to correctly show relevant folders in side bar.
4. update project data.


## Usage
- "open_current_folder_as_project": Add the folder that contains current file to the sidebar.
- "remove_folder_from_project": Remove the folder that contains current file from sidebar.

