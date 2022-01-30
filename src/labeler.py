import json

class Labeler:
    def __init__(self):
        # f = open('label.json')
        # data = json.load(f)
        # for i in data['emp_details']:
        #     print(i)
        # f.close()
        self.labels = [
            Label("Transport", ["uber","train", "bus", "transport for wales", "tfl"]),
            Label("Entertainment", ["netflix","disney","spotify", "steam"]),
            Label("Shopping", ["sainsburys", "morrisons", "co-op", "deliveroo", "aldi", "tesco", "domino"]),
            Label("Miscellaneous", ["amznmktplace"])
        ]

    def checkLabels(self, input:str):
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