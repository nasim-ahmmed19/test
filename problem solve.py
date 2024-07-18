# forits=["apple","bannana","cherry"]
# # print(forits[-1])
# # forits[1]="kiwi"
# # print(forits)
# # forits.append('orange')
# # print(forits)
# # forits.insert(1,"lemon")
# # print(forits)
# forits.remove("bannana")
# print(forits)

# txt="Hello World"
# # print(txt[2:5])
# print(txt.strip())
# print(txt.upper())
# x=txt.lower()
# print(x)
# y=txt.replace("H","J")
# print(y)


# age=21
# age_str=str(age)
# # d="My name is Nasim, and I am {}"
# # print(d.format(age))
# e=f"My name is Nasim and i am" " "
# print(e+ age_str)


# y=99
# y_str=str(99)
# c=88
# # d=favorits
# nasim=f"My favorits number is a"" "
# print(nasim+y_str)
#
# x = {"name" : "John", "age" : 36}
# print((x))


# thistuple=("apple","banana","cherry")
# print(thistuple)
# thistuple=('apple','banana','cherry','apple','cherry')
# print(thistuple)
# thistuple=("apple","banana","cherry")
# print(len(thistuple))
# tuple=("nasim",)
# print(type(tuple))

# N=("nasim","nayeem","ridoy","rumon")
# A=(1,5,4,6,3,)
# s=(True,False,False,True)
# print(N+A+s)

# tuple=("nasim",22,True,"ridoy",31.5)
# print(tuple)
# h="hello word"
# print(h[3:7])
# print(len(h))
# thistuple=("apple","banana","cherry")
# print(thistuple[0])
# print(len(thistuple))
# na=("apple","banana","cherry")
# print(na[-1])
# bb=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(bb[2:7])
# print(len(bb))
# print(bb[4])

# x=("apple","banana","cherry")
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
# print(x)


# x=("apple","banana","cherry")
# y=list(x)
# y.append("orange")
# x=tuple(y)
# print(x)


# x=("apple","banana","cherry")
# y=list(x)
# y.insert(1,"orange")
# x=tuple(y)
# print(x)

# x=("apple","banana","cherry")
# y=list(x)
# # y.remove("cherry")
# # x=tuple(y)
# # print(x)
# y.pop(2)
#
# x=tuple(y)
# print(x)

# furits=("apple","banana","cherry")
# a,b,c=furits
# print(c)
# for x in furits:
#     print(x)

# furits=("apple","banana","cherry","orange")
# k,l,*c=furits
# print(k)
# print(l)
# print(c)

# furits=("apple","banana","cherry","orange")
# for x in furits:
#     print(x)
# for x in range(len(furits)):
#     print(x)
# for x in range(len(furits)):
#     print(x)

# furits=("apple","banana","cherry","orange")
# i=0
# while i<len(furits):
#     print(furits[i])
#     i+=3
# i=2
# while i <len(furits):
#     print(furits[i])
#     i+=1

##################  set problem #########################
#True=1
#False=0
# myset={"apple","banana","cherry","apple",True,False,54}
# print(len(myset))
# print(myset)
# for x in myset:
#     print(x)
# print("banana" in myset)
# myset.add("orange")
# print(myset)
# set={11,22,21,31,4}
# myset.update(set)
# print(myset)
# myset.remove("cherry")
# myset.discard("apple")
# myset.pop()
# myset.clear()
# del myset
# N={"nasim","nayeem","ridoy","rumon"}
# x=myset | N
# myset.update(N)

################################################################
#                      dictionaries                            #
################################################################
thisdict= {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
# # print(len(thisdict))
# print(thisdict.get("model"))
# x=thisdict.keys()
# print(x)
# print(thisdict.values())
# thisdict["year"]=2024
# print(thisdict)
# x=thisdict.items()
# print(x)
# thisdict.update({"model":2020})
# print(thisdict)
# thisdict["color"]="red"
# print(thisdict)
# thisdict.update({"nasim":"biva"})
# print(thisdict)
# thisdict.pop("model")
# print(thisdict)
# thisdict.popitem()
# print(thisdict)
# del thisdict
# print(thisdict)
# thisdict.clear()
# print(thisdict)
# for x in thisdict :
#     print(x)
# for y in thisdict:
#     print(thisdict[y])
# for x in thisdict:
#     print(thisdict[x])
# for x in thisdict.values():
#     print(x)
# nn=thisdict.copy()
# print(nn)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child3"]["name"])
