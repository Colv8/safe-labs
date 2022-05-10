

def music():
  print("Qual a temperatura no seu local ? ")
  temp = input()
  temp = int(temp)
  if temp > 30:
    return print("party track!")
  elif 14 < temp < 31:
    return print("pop music!")
  elif 9 < temp < 15:
    return print("rock music")
  elif temp < 10:
    return print("Classical Music")