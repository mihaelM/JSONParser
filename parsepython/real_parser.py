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

# "Directly send manipulated measurement values to IED with process bus rogue device"
# "Directly send manipulated measurement values to IED from process bus switch"
# "MITM attack which manipulates measurement values sent to IED"
def deleteNodesAffectedBySMVProtectionOurTree(resDict):
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to IED"]["children"].pop("Directly send manipulated measurement values to IED with process bus rogue device")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to IED"]["children"].pop("Directly send manipulated measurement values to IED from process bus switch")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"].pop("MITM attack which manipulates measurement values sent to IED")

    #data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("1")
    #data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("3")
    #data["ideas"]["1"]["ideas"]["0.5625"]["ideas"].pop("3")
    #replace measuerment with measurement

f = open('jsonfile/SabotageSAS.mup', 'r')
data = json.load(f)

#dobro, čini se da mi od ovih vršnih podataka ne treba ništa
resDict = parseJson(data)
print (resDict)

deleteNodesAffectedBySMVProtectionOurTree(resDict)
print (resDict)
