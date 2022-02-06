import json

class Labeler:
    def __init__(self, jsonFile):
        self.labels = []

        with open(jsonFile) as json_file:
            labelsJson = json.load(json_file)
            for label in labelsJson:
                matches = []
                for match in label["matches"]:
                    matches.append(match)
                self.labels.append(Label(label["label"], matches))


    def addLabel(self, label):
        self.labels.append(label)

    def isValidLabel(self, input:str):
        for label in self.labels:
            if(input==label.label):
                return True
        
        return False

    def matchesLabel(self, input:str):
        for label in self.labels:
            if(label.matchLabel(input)):
                return label.label

        return ''


class Label:
    def __init__(self, label:str, matches):
        self.label = label
        self.matches = matches
    
    def matchLabel(self, input) -> bool:
        for match in self.matches:
            if(match in input.lower()):
                return True

        return False