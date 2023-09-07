# Michael Hobden 07/09/23
# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("James", 5)
cat2 = Cat("Jim", 12)
cat3 = Cat("Jacob", 3)

'''
this is fine but the loop should be replaced with max(args)
 def find_oldest_cat(*args):
     return max(args)
'''


def find_oldest_cat(*args):
    oldest_age = 0
    for cat in args:
        if (captured_age := cat.age) > oldest_age:
            oldest_age = captured_age

    return oldest_age


age = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {age} years old.")
