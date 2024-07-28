
list1 = []
string1 = ""
string2 = " "
string3 = ""


while True:
    string1 = input()
    if string1 == "":
        break
    list1.append(string1)
    string2 = string2 + string1+ " "

print(string2)
print(list1)








