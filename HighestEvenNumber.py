def highest_even(li):
  curHighest = 0
  for i in li:
    if i % 2 == 0 and curHighest < i:
      curHighest = i
  return curHighest

print(highest_even([2,0,3,1,7]))

def highest_even2(li):
  evens = []
  for i in li:
    if i % 2 == 0:
      evens.append(i)
  return max(evens)

print(highest_even2([2,0,3,1,7]))
