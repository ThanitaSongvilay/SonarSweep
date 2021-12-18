str_list = []
depth = 0
horizontalPosition = 0


def inputList():
  while True:
    line = input()
    if line:
      str_list.append(line)
    else:
      break


def splitComp(list):
  compList = [str.split() for str in str_list]
  print(compList)


inputList()
splitComp(list)











