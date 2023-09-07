some_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

count = 0 
for term in some_list:
  for term2 in some_list[count+1:len(some_list)]:
    if(term == term2):
      print(term)
  count += 1


duplicates = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)
