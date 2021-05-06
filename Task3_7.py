# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:26:39 2021
@author: Asaf
"""
import re
import json  
DictionaryOfDictionaries ={}
text_list = [] # using this lint to make sure no dubbule names are in 
Id_counter = 0
id_list = [] # main lint for storing all the dicsinoryes
metadata = {} # storing all metadata about the WhatsApp group  
Date_format = re.compile(r"\d+\.\d+\.\d{4}, \d+:\d\d")
Id_format = re.compile(r" - [^:]*:")
Flag01 = 0 
lineNumbr = 0 
LineForOpenGroup = "נוצרה על ידי"
file = open('TXTT.txt',encoding="utf8")
fileR = file.readlines()
for line in fileR:
    lineNumbr += 1
    dic = {}
    if "נוצרה על ידי" in line and Flag01 == 0:
        Flag01 = 1
        name = line.split(chr(34))[1]
        metadata["creation_date"] = line.split("-")[0]
        metadata["creator"] = line.split(LineForOpenGroup)[1] ##ss
        metadata["chat_name"] = name
    if Date_format.search(line) :
        dic['Date'] = line.split("-")[0]
        if Id_format.search(line) in id_list:
            x = id_list["id":Id_format.search(line)]
            dic['id'] = x
        else:
            dic['id'] = Id_counter
            id_list.append(Id_counter)
            Id_counter += 1
        text0 = line.replace(line.split("-")[0], "")
        if ":" in text0 and lineNumbr > 3 :
            dic['text'] = text0.split(":")[1]
        else:
            dic['text'] = ""
    text_list.append(dic)          
metadata["num_of_participants"] = Id_counter +1 
#nameoffinalfile = metadata['chat_name']+".json"
print(metadata["chat_name"])
name = name + ".json"
DictionaryOfDictionaries ={"messages": text_list , "metadata": metadata}
#Create a file with the data
with open(name, "w") as fp:
    json.dump(DictionaryOfDictionaries, fp)
print(metadata)