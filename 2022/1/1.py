elvesFood=[]

with open('input','r') as f:
    values = f.readlines()
    calories = 0
    for value in values:
        if value != "\n":
            calories=calories + int(value)
        else:
            elvesFood.append(calories)
            calories = 0

elvesFood.sort()
print ("Elf with the most calories has: ", elvesFood[-1])

# Part 2
totalCaloriesOfTop3Elves = sum(elvesFood[-3:])
print ("Total calories of top 3 elves: ", totalCaloriesOfTop3Elves)