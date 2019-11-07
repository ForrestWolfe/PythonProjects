import os.path
from os import path

# just simply counts the folders and files in your directory
# if your folder has a period it will be considered a directory
# I will try to  replace that with os.isdir(filename) for some reason I can't get it to work.
# todo replace the __contains__(filename) with os.isdir(filename) maybe incorrect syntax?


class FileCounter:
    def __init__(self, Path):
        self.path = Path
        self.files = []
        self.folders = []

    def count_files(self):
        for filename in os.listdir(self.path):
            if filename.__contains__('.'):
                self.files.append(filename)
            else:
                self.folders.append(filename)
        print(len(self.files), " Total files ", len(self.folders), " Total Folders")


count = FileCounter("Enter your path")
count.count_files()

