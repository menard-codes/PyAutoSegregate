import os
import shutil
from pathlib import PurePath
import json


class AutoSegregateFiles:
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(self.path)

    def files_and_extensions(self):
        path_and_files = [self.path + file for file in self.files]
        pure_window_path = [
            PurePath(file_directory) for file_directory in path_and_files
        ]
        files_and_ext = {
            file: file_path.suffix for file, file_path in zip(self.files, pure_window_path)
        }
        return files_and_ext

    def new_folder(self):
        with open("categories.json") as categories:
            types = json.load(categories)
        for category in types:
            if category not in self.files:
                os.makedirs(self.path + category)

    def segregate(self):
        self.new_folder()
        extensions = self.files_and_extensions()
        with open("categories.json") as categories:
            types = json.load(categories)
        for filename, extension in extensions.items():
            for category in types:
                if extension in types[category]:
                    shutil.move(self.path + filename, self.path + f"{category}/" + filename)
