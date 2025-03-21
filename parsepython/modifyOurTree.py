import json

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

        if shape == None:
            shape = "circle" #seems to be that default is gray combination (since not black-white)

        resultingDict[title]["shape"] = shape
        if "ideas" in currDict:
            resultingDict[title]["children"] = parseJson(currDict)
        else:
            resultingDict[title]["children"] = []
    return resultingDict


def generateAttrDictionary(shape, position):
    genAttrDict = {}
    genAttrDict["style"] = {}
    genAttrDict["style"]["text"] = {}
    if not (position == []):
        genAttrDict["position"] = position

    if shape == "rhombus":
        genAttrDict["style"]["backgroundColor"] = "#000000"
        genAttrDict["style"]["text"]["color"] = "#FFFFFF"
    elif shape == "circle":
        genAttrDict["style"]["backgroundColor"] = "#E0E0E0"
        genAttrDict["style"]["text"]["color"] = "#4F4F4F"
    elif shape == "hexagon":
        genAttrDict["style"]["backgroundColor"] = "#FFFFFF"
        genAttrDict["style"]["text"]["color"] = "#000000"
    return genAttrDict

some_number = 0
def parseJsonBackToMup(title, dataDict):
    global some_number
    resultingMupDict = {}
    resultingMupDict["title"] = title
    resultingMupDict["id"] = some_number + 1
    resultingMupDict["attr"] = generateAttrDictionary(dataDict["shape"], dataDict["position"])
    resultingMupDict["ideas"] = {}

    for child in dataDict["children"]:
        some_number = some_number + 1
        resultingMupDict["ideas"][some_number] = parseJsonBackToMup(child, dataDict["children"][child])

    return resultingMupDict


# "Directly send manipulated measurement values to IED with process bus rogue device"
# "Directly send manipulated measurement values to IED from process bus switch"
# "MITM attack which manipulates measurement values sent to IED"
def deleteNodesAffectedBySVProtectionOurTree(resDict):
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to IED"]["children"].pop("Directly send manipulated measurement values to IED with process bus rogue device")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to IED"]["children"].pop("Directly send manipulated measurement values to IED from process bus switch")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"].pop("MITM attack which manipulates measurement values sent to IED")
    #replace measuerment with measurement


# "Directly send manipulated measurement values to the SCADA with station bus rogue device"
# "Directly send manipulated measurement values to the SCADA from corporate WAN"
# "Directly send manipulated measurement values to the SCADA from station bus switch"
# "MITM attack which manipulates measurement values sent to the SCADA" (3_4)
def deleteNodesAffectedByOnlyMMSProtectionOurTree(resDict):
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to the SCADA"]["children"].pop("Directly send manipulated measurement values to the SCADA with station bus rogue device")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to the SCADA"]["children"].pop( "Directly send manipulated measurement values to the SCADA from corporate WAN")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to the SCADA"]["children"].pop( "Directly send manipulated measurement values to the SCADA from station bus switch")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"].pop("MITM attack which manipulates measurement values sent to the SCADA")


#Directly send a command to IED with station bus rogue device
#Directly send a command to IED from corporate WAN
#Directly send a command to IED from station bus switch
#MITM attack which sends a command to IED
def deleteNodesAffectedByGOOSEandMMSProtectionOurTree(resDict):
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["Directly send a command to IED"]["children"].pop("Directly send a command to IED with station bus rogue device")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["Directly send a command to IED"]["children"].pop("Directly send a command to IED from corporate WAN")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["Directly send a command to IED"]["children"].pop("Directly send a command to IED from station bus switch")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"].pop("MITM attack which sends a command to IED")


#Directly send a command to circuit breaker IED with process bus rogue device
#Directly send a command to circuit breaker IED from process bus switch
#MITM attack which sends a command to circuit breaker IED
def deleteNodesAffectedByOnlyGOOSEProtectionOurTree(resDict):
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"][ "Directly send a command to circuit breaker IED"]["children"].pop( "Directly send a command to circuit breaker IED with process bus rogue device")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"][ "Directly send a command to circuit breaker IED"]["children"].pop( "Directly send a command to circuit breaker IED from process bus switch")
    resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"].pop("MITM attack which sends a command to circuit breaker IED")


def deleteNodesAffectedByDisablyingRougeDeviceOurTree(currentNode, dataDict):
    if "rogue device" in currentNode:
        dataDict.pop(currentNode)
        return
    childs = (dataDict[currentNode]["children"]).copy() #only keys should be here, so we do not iterate on dictionary
    for child in childs:
        deleteNodesAffectedByDisablyingRougeDeviceOurTree(child, dataDict[currentNode]["children"])

def includeProtectionRecursively(relevantDict, protectionName):
    if "protection" in relevantDict:
        relevantDict["protection"].append(protectionName)
    else:
        relevantDict["protection"] = []
        relevantDict["protection"].append(protectionName)

    for child in relevantDict["children"]:
        includeProtectionRecursively(relevantDict["children"][child], protectionName)

def embedSMVProtectionOurTree(resDict):
    protectionName = "protect_SMV_with_MAC"
    relevantSubTree1 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to IED"]["children"]["Directly send manipulated measurement values to IED with process bus rogue device"]
    includeProtectionRecursively(relevantSubTree1, protectionName)
    relevantSubTree2 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to IED"]["children"]["Directly send manipulated measurement values to IED from process bus switch"]
    includeProtectionRecursively(relevantSubTree2, protectionName)
    relevantSubTree3 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["MITM attack which manipulates measurement values sent to IED"]
    includeProtectionRecursively(relevantSubTree3, protectionName)

def embedMMSProtectionOurTree(resDict):
    protectionName = "protect_MMS_with_TLS"
    relevantSubTree1 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to the SCADA"]["children"]["Directly send manipulated measurement values to the SCADA with station bus rogue device"]
    includeProtectionRecursively(relevantSubTree1, protectionName)
    relevantSubTree2 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to the SCADA"]["children"]["Directly send manipulated measurement values to the SCADA from corporate WAN"]
    includeProtectionRecursively(relevantSubTree2, protectionName)
    relevantSubTree3 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["Directly send manipulated measurement values to the SCADA"]["children"]["Directly send manipulated measurement values to the SCADA from station bus switch"]
    includeProtectionRecursively(relevantSubTree3, protectionName)
    relevantSubTree4 = resDict["Sabotage IEC 61850 SAS"]["children"]["Manipulate measurement values"]["children"]["MITM attack which manipulates measurement values sent to the SCADA"]
    includeProtectionRecursively(relevantSubTree4, protectionName)

def embedGOOSEandMMSProtectionOurTree(resDict):
    protectionName = "protect_GOOSE_with_MAC + protect_MMS_with_TLS"
    relevantSubTree1 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["Directly send a command to IED"]["children"]["Directly send a command to IED with station bus rogue device"]
    includeProtectionRecursively(relevantSubTree1, protectionName)
    relevantSubTree2 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["Directly send a command to IED"]["children"]["Directly send a command to IED from corporate WAN"]
    includeProtectionRecursively(relevantSubTree2, protectionName)
    relevantSubTree3 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["Directly send a command to IED"]["children"]["Directly send a command to IED from station bus switch"]
    includeProtectionRecursively(relevantSubTree3, protectionName)
    relevantSubTree4 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["MITM attack which sends a command to IED"]
    includeProtectionRecursively(relevantSubTree4, protectionName)

def embedGOOSEProtectionOurTree(resDict):
    protectionName = "protect_GOOSE_with_MAC"
    relevantSubTree1 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"][ "Directly send a command to circuit breaker IED"]["children"]["Directly send a command to circuit breaker IED with process bus rogue device"]
    includeProtectionRecursively(relevantSubTree1, protectionName)
    relevantSubTree2 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"][ "Directly send a command to circuit breaker IED"]["children"]["Directly send a command to circuit breaker IED from process bus switch"]
    includeProtectionRecursively(relevantSubTree2, protectionName)
    relevantSubTree3 = resDict["Sabotage IEC 61850 SAS"]["children"]["Send a command to control element"]["children"]["MITM attack which sends a command to circuit breaker IED"]
    includeProtectionRecursively(relevantSubTree3, protectionName)

def embedPhysicalProtections(currentNode, dataDict):
    protectionName = "include_physical_protections"
    if "rogue device" in currentNode:
        includeProtectionRecursively(dataDict[currentNode], protectionName)
        return
    childs = (dataDict[currentNode]["children"]).copy() #only keys should be here, so we do not iterate on dictionary
    for child in childs:
        embedPhysicalProtections(child, dataDict[currentNode]["children"])

f = open('jsonfile/SabotageSAS.mup', 'r')
data = json.load(f)

resDict = parseJson(data)
#print(resDict)

#deleteNodesAffectedBySVProtectionOurTree(resDict)
#deleteNodesAffectedByOnlyMMSProtectionOurTree(resDict)
#deleteNodesAffectedByGOOSEandMMSProtectionOurTree(resDict)
#deleteNodesAffectedByOnlyGOOSEProtectionOurTree(resDict)

embedSMVProtectionOurTree(resDict)
embedMMSProtectionOurTree(resDict)
embedGOOSEandMMSProtectionOurTree(resDict)
embedGOOSEProtectionOurTree(resDict)


title = "Sabotage IEC 61850 SAS"
embedPhysicalProtections(title, resDict)
print(resDict)

"""
resultingMupDict = parseJsonBackToMup(title, resDict[title])
finalResultingMupDict = {}
finalResultingMupDict["attr"] = {}
finalResultingMupDict["attr"]["theme"] = "straightlines"
finalResultingMupDict["formatVersion"] = 3
finalResultingMupDict["id"] = "root"
finalResultingMupDict["ideas"] = {}
finalResultingMupDict["ideas"]["1"] = resultingMupDict
finalResultingMupDict["title"] = "Compromise (P)RNG Somehow"
finalResultingMupDict["links"] = []

finalJson = json.dumps(finalResultingMupDict)
print (finalJson)
"""