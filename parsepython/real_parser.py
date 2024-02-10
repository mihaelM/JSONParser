import json

#for a shape I need a more representative looking file

#we can solve this without shapes for start
#good, we add shapes and that is it

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

        shape = None

        try:
            backgroundColor = currDict["attr"]["style"]["backgroundColor"]
            textColor = currDict["attr"]["style"]["text"]["color"]

            if backgroundColor == "#000000" and textColor == "#FFFFFF":
                shape = "rhombus"

            if backgroundColor == "#E0E0E0" and textColor == "#4F4F4F":
                shape = "circle"

            if backgroundColor == "#FFFFFF" and textColor == "#000000":
                shape = "hexagon"

        except:
            pass

        resultingDict[title]["shape"] = shape
        if "ideas" in currDict:
            resultingDict[title]["children"] = parseJson(currDict)
    return resultingDict

f = open('jsonfile/SabotageSAS.mup', 'r')
data = json.load(f)

#dobro, čini se da mi od ovih vršnih podataka ne treba ništa
resDict = parseJson(data)
print(resDict)