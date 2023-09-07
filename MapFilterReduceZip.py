from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def CapitalizeFirst(name):
    return name.capitalize()


print(list(map(CapitalizeFirst, my_pets)))

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
new_list = list(zip(my_strings, my_numbers))[::-1]
print(new_list)


def scorePassed(score):
    return score > 50


scores = [73, 20, 65, 19, 76, 100, 88]
passed_scores = list(filter(scorePassed, scores))
print(passed_scores)


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers, reduce(accumulator, scores, 0)))

print(accumulator, (my_numbers + scores))
