import random
#for loop in python
#range_list = [num*2 for num in range(0,5)]
#print(range_list)

#names1 = ["Alex", "Beana", "Pedri", "Aitanna", "Vinicius", "Ronaldo", "Hansi", "Dybala"]
#short_names = [name for name in names1 if len(name)<6]
#caps_names = [name.upper() for name in names1 if len(name)>6]
#print(short_names)
#print(caps_names)

#with open("names1.txt") as n1:
#    names1 = [name for name in n1]

#with open("names2.txt") as n2:
#    names2 = [name for name in n2]

#sames_names = [name for name in names1 if name in names2]
#print(sames_names)

names = ["Lewandoski", "Raphinha", "Lamine", "Pedri", "Frenkie", "Bernal", "Gavi", "Casado", "Cubarsi", "Araujo", "Eric", "kounde", "Balde", "Christensen"]
player_scores = {name:random.randint(1,100) for name in names}
print(player_scores)
good_players = {player for (player, score) in player_scores.items() if score > 60}
print(good_players)

