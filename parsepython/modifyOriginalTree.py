import json
# "Directly send manipulated measurement values to IED with process bus rogue device"
# <-> data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"]["1"]["title"]
# "Directly send manipulated measurement values to IED from process bus switch"
# <-> data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"]["3"]["title"]
# "MITM attack which manipulates measurement values sent to IED" (3_3)
# <-> data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["3"]["title"]
def deleteNodesAffectedBySMVProtection(data):
    data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("1")
    data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("3")
    data["ideas"]["1"]["ideas"]["0.5625"]["ideas"].pop("3")


# "Directly send manipulated measurement values to SCADA with station bus rogue device"
# <-> data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"]["1"]["title"]
# "Directly send manipulated measurement values to the SCADA from corporate WAN"
# <-> data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"]["3"]["title"]
# "Directly send manipulated measurement values to the SCADA from station bus switch"
# <-> data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"]["5"]["title"]
# "MITM attack which manipulates measurement values sent to the SCADA" (3_4)
# <-> data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["4"]["title"]
def deleteNodesAffectedByOnlyMMSProtection(data):
    data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"].pop("1")
    data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"].pop("3")
    data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"].pop("5")
    data["ideas"]["1"]["ideas"]["0.5625"]["ideas"].pop("4")


#Directly send a command to IED with station bus rogue device
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["1"]["ideas"]["1"]["title"]
#Directly send a command to IED from corporate WAN (5_1_1)
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["1"]["ideas"]["2"]["title"]
#Directly send a command to IED from station bus switch
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["1"]["ideas"]["7"]["title"]
#MITM attack which sends a command to IED
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["3"]["title"]
def deleteNodesAffectedByGOOSEandMMSProtection(data):
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["1"]["ideas"].pop("1")
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["1"]["ideas"].pop("2")
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["1"]["ideas"].pop("7")
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"].pop("3")


#Directly send a command to circuit breaker IED with process bus rogue device
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["2"]["ideas"]["1"]["title"]
#Directly send a command to circuit breaker IED from process bus switch
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["2"]["ideas"]["5"]["title"]
#MTIM attack which sends a command to circuit breaker IED
# <-> data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["4"]["title"]
def deleteNodesAffectedByOnlyGOOSEProtection(data):
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["2"]["ideas"].pop("1")
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"]["2"]["ideas"].pop("5")
    data["ideas"]["1"]["ideas"]["0.75"]["ideas"].pop("4")


def deleteNodesAffectedByPhysicalProtections(data):
    if not("ideas" in data):
        return
    keys = list(data["ideas"])
    for key in keys:
        if "rogue device" in data["ideas"][key]["title"]:
            data["ideas"].pop(key)
        else:
            deleteNodesAffectedByPhysicalProtections(data["ideas"][key])

def outputData(data, whichProtection):
    f = open('output_original_tree/SabotageSAS_withProtection{}.mup'.format(whichProtection), 'w')
    json.dump(data, f)
    f.close()


f = open('jsonfile/SabotageSAS.mup', 'r')
data = json.load(f)
deleteNodesAffectedBySMVProtection(data)
#outputData(data, "SMV")
deleteNodesAffectedByOnlyMMSProtection(data)
#outputData(data, "OnlyMMS")
deleteNodesAffectedByGOOSEandMMSProtection(data)
#outputData(data, "GOOSEandMMS")
deleteNodesAffectedByOnlyGOOSEProtection(data)
#outputData(data, "OnlyGOOSE")
deleteNodesAffectedByPhysicalProtections(data)
#outputData(data, "PhysicalProtections")
outputData(data, "AllProtections")
f.close()