import re
import os.path

#reading file
file_path = "sample-test.minic"
if os.path.exists('test.minic'):
    file_path = "test.minic"
with open(file_path,"r") as f:
    data = f.read()


#regex for finding...
forr = re.findall(r'\bfor\b',data)
whilee = re.findall(r'\bwhile\b',data)
mosbat = re.findall(r'\+',data)
mosaavi = re.findall(r'\=',data)
openn = re.findall(r'\(',data)
closee = re.findall(r'\)',data)
opennn = re.findall(r'\{',data)
closeee = re.findall(r'\}',data)
iden = re.findall(r"\b(?!while\b|if\b|for\b)[_a-zA-Z][_a-zA-Z0-9]*\b",data)
integ = re.findall(r'\b[-]?[1-9]\d*\b|0',data)
iff = re.findall(r'\bif\b',data)

#showing the result
print("your program:\n","=====================================\n",data,"\n================================\n\n", "-----------------------\ndetected tokens:\n-----------------------\n")
print(f"for : {forr}")
print(f"while : {whilee}")
print(f"mosavi : {mosaavi}")
print(f"mosbat : {mosbat}")
print(f"open () : {openn}")
print(f"close (): {closee}")
print(f"open curly bruket: {opennn}")
print(f"close curly bruket: {closeee}")
print(f"identifier : {iden}")
print(f"int : {integ}")
print(f"if : {iff}")
