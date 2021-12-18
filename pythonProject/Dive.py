str_list = []

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
  return list


def doCounting(list):
  horizontal = 0
  depth = 0
  position = 0
  for direction in list:
    if direction[0] == 'forward':
      horizontal += direction[1]
    if direction[0] == 'up':
      depth += direction[1]
    if direction[0] == 'down':
      depth -= direction[1]

  position = horizontal * abs(depth)
  print("Position is:", position)


inputList()
doCounting(splitList(splitComp(str_list)))





