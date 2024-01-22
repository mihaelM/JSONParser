import json

f = open ('jsonfile/SabotageSAS.mup')
data = json.load(f)
print (data["ideas"])