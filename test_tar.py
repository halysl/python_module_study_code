# -*- coding=utf-8 -*-

import os
import tarfile
import re

curr_path = os.path.dirname(os.path.abspath(__file__))

tar = tarfile.open("study.tar.gz", "w:gz")

for root, dir, files in os.walk(os.getcwd()):
    for file in files:
        fullpath = os.path.join(root, file)
        if re.search(".git|.ipynb|.idea|.tar.gz", fullpath):
            continue
        else:
            print(fullpath)
            tar.add(fullpath)
tar.close()