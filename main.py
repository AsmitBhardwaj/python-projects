#for loop in python
range_list = [num*2 for num in range(0,5)]
print(range_list)

names = ["Alex", "Beana", "Pedri", "Aitanna", "Vinicius", "Ronaldo", "Hansi", "Dybala"]
short_names = [name for name in names if len(name)<6]
caps_names = [name.upper() for name in names if len(name)>6]
print(short_names)
print(caps_names)

with open("names1.txt") as n1:
    names1 = [name for name in n1]

with open("names2.txt") as n2:
    names2 = [name for name in n2]

sames_names = [name for name in names1 if name in names2]
print(sames_names)



