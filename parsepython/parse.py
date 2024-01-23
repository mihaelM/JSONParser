import json

str1 = "Directly send manipulated measurement values to IED with process bus rogue device"
str2 = "Directly send manipulated measurement values to IED from process bus switch"

lst = []
lst.append(str1)
lst.append(str2)
#print (lst)

f = open ('jsonfile/SabotageSAS.mup')
data = json.load(f)

print (data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"]["1"]["title"])
print (data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"]["3"]["title"])

"""
data[")ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("1")
data["ideas"]['1']['ideas']["0.5625"]["ideas"]["1"]["ideas"].pop("3")
print(data)
"""
#samo backtrackam za ove druge koje su analogna shema kao "Directly send a command to circuit breaker"
#i onda ako mogu izbrisati gg
#we found them
#now we have to find out, not only how to delte them, but also their children