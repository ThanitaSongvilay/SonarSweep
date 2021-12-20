str_list = []
aim = 0
depth = 0
horizontal = 0

def inputList():
  while True:
    line = input()
    if line:
      str_list.append(line)
    else:
      break

def splitComp(str_list):
  compList = [str.split() for str in str_list]
  return compList

def splitList(list):
  for i in list:
    i[1] = int(i[1])
  print(list)
  return list

def doCounting(list):
  aim = 0
  depth = 0
  horizontal = 0
  answer = 0
  for direction in list:
    if direction[0] == 'down':
      aim = aim + direction[1]
    if direction[0] == 'up':
      aim = aim - direction[1]
    if direction[0] == 'forward':
      horizontal += direction[1]
      depth = depth + aim * direction[1]

  answer = depth * horizontal
  print(answer)

inputList()
doCounting(splitList(splitComp(str_list)))
