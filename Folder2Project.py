import sublime_plugin
import sublime
import os
import re
import json


class OpenCurrentFolderAsProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        file_name = self.window.active_view().file_name()
        folder = os.path.abspath(os.path.dirname(file_name))
        self.window.run_command("open_folder_as_project", {"folder": folder})


class OpenFolderAsProjectCommand(sublime_plugin.WindowCommand):
    def run(self, folder):
        win = sublime.active_window()
        project_sign = re.compile("(\s|\S)*\.sublime-project")
        data = None
        for file in os.listdir(folder):
            if project_sign.match(file):
                with open(os.path.join(folder, file)) as project_data:
                    data = json.load(project_data)
                    break
        if not data:
            data = {}
            data["folders"] = []
            data["folders"].append({'follow_symlinks': True,
                                    'path': folder})
        else:
            for idx, x_folder in enumerate(data["folders"]):
                folder_sequence = x_folder["path"].split(os.sep)
                if folder_sequence[0] == ".":
                    folder_sequence[0] = folder
                elif folder_sequence[0] == "..":
                    folder_sequence[0] = os.path.dirname(folder)
                else:
                    pass
                data["folders"][idx]["path"] = os.sep.join(folder_sequence)
        win.set_project_data(data)


class RemoveFolderFromProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        file_name = self.window.active_view().file_name()
        print(file_name)
        win = sublime.active_window()
        folder = os.path.dirname(file_name)
        data = win.project_data()
        temp = None
        for path in data["folders"]:
            if path["path"] == folder:
                temp = path
        if temp:
            data["folders"].remove(temp)
        win.set_project_data(data)
