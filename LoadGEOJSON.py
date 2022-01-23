import json

class File:
    def __init__(self, fileName):
        self.fileName=fileName
        self.dataJSON = {}
        self.newPolylines = []