import json

#for a shape I need a more representative looking file

#we can solve this without shapes for start
def parseJson(data):
    resultingDict = {}
    for key in data["ideas"]:
        currDict = data["ideas"][key]
        title = currDict["title"]
        position = []
        try:
            position = currDict["attr"]["position"]
        except:
            pass
        resultingDict[title] = {}
        resultingDict[title]["position"] = position
        resultingDict[title]["shape"] = "TODO"
        if "ideas" in currDict:
            resultingDict[title]["children"] = parseJson(currDict)
    return resultingDict

f = open('mockfile/Kifla.mup', 'r')
data = json.load(f)

#dobro, čini se da mi od ovih vršnih podataka ne treba ništa
resDict = parseJson(data)
print(resDict)