import glob
import numpy as np
import sys
import os
from janome.tokenizer import Tokenizer
import pandas as pd

class ReadFiles:
    path_to_files = ""
    users_data = None
    pnja_dic = None
    t = None 

    def __init__(self):
        self.path_to_files = os.getcwd()
        self.users_data = []
        self.pnja_dic = self.__make_dict()
        self.t = Tokenizer()

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

    def analytics(self, text):
        point = 0.0
        texts_num = 0
        for token in self.t.tokenize(text):
            if token.base_form in self.pnja_dic:
                point = point + self.pnja_dic[str(token.base_form)]
                texts_num = texts_num + 1
        if texts_num == 0:
            return 0
        return point/texts_num

    def outputFiles(self):
        pass

    def __make_dict(self):
        pn_ja = pd.read_csv('./dict/pn_ja.dic', sep=':',encoding='cp932', names=('Tango','Yomi','Hinshi', 'Score'))
        word = pn_ja['Tango']
        score = pn_ja['Score']

        return dict(zip(word, score))
