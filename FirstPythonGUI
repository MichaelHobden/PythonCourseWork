picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  temp_row = ""
  for pixel in row:
    temp_row = temp_row + " " if pixel == 0 else temp_row + "*"
  print(temp_row)

for row in picture:
  for pixel in row:
    if(pixel == 1):
      print("*", end='')
    else:
      print(" ", end='')
  print()
