import glob
import numpy as np
import sys
import os

class ReadFiles:
    path_to_files = ""
    users_data = None
    def __init__(self):
        self.path_to_files = os.getcwd()
        self.users_data = []

    def loadFiles(self):
        level1 = glob.glob(os.path.join(self.path_to_files, 'txtdata', '*'))
        for f in level1:
            level2 = glob.glob(os.path.join(f, "*"))
            for f2 in level2:
                level3 = glob.glob(os.path.join(f2, '*.txt'))
                print(os.path.basename(f2))
                username = os.path.basename(f2)
                self.users_data.append({"username": username, "contents": []})
                for f3 in level3:
                    with open(f3) as contens:
                        self.users_data[-1]["contents"].append(contens.read())

        return self.users_data

    def outputFiles(self):
        pass
