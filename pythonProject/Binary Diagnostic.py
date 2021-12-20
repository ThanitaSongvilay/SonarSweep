#bit = 12
#fins the most common rate in tje correspondent position
#Then multiply gamma and epsilon

gammaRate = 0
epsilonRate = 0

#first take in user input in a list...

binarylist = []

def inputList():
  while True:
    line = int(input())
    if line:
      binarylist.append(line)
    else:
      break
  print(binarylist)


inputList()
