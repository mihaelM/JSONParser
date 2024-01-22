import json

str1 = "Directly send maniuplated meassurement values to IED with process bus rogue device"
str2 = "Directly send maniuplated meassurement values to IED from process bus switch"

lst = []
lst.append(str1)
lst.append(str2)
print (lst)

f = open ('jsonfile/SabotageSAS.mup')
data = json.load(f)
print (data["ideas"]['1']['ideas']['21']['ideas']['3']["title"])

#samo backtrackam za ove druge koje su analogna shema kao "Directly send a command to circuit breaker"
#i onda ako mogu izbrisati gg