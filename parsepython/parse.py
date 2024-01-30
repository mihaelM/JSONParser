import json
# "Directly send manipulated measurement values to IED with process bus rogue device"
# <-> data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"]["1"]["title"]
# "Directly send manipulated measurement values to IED from process bus switch"
# <-> data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"]["3"]["title"]
# "MITM attack which manipulates measurement values sent to IED" (3_3)
# <->

#tested and seems to be working
def deleteNodesAffectedBySMVProtection(data):
    data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("1")
    data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("3")

# "Directly send manipulated measurement values to SCADA with station bus rogue device"
# <-> data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"]["1"]["title"]
# "Directly send manipulated measurement values to the SCADA from corporate WAN"
# <->
# "Directly send manipulated measurement values to the SCADA from station bus switch"
# <->
# "MITM attack which manipulates measurement values sent to the SCADA" (3_4)
# <->



def deleteNodesAffecteByMMSProtection(data):
    pass

def outputData(data):
    f = open('output/SabotageSAS_withProtection.mup', 'w')
    json.dump(data, f)
    f.close()

f = open('jsonfile/SabotageSAS.mup', 'r')
data = json.load(f)

#deleteNodesAffectedBySMVProtection(data)
#outputData(data)
print (data["ideas"]["1"]["ideas"]["0.5625"]["ideas"]["2"]["ideas"]["1"]["title"])

f.close()
