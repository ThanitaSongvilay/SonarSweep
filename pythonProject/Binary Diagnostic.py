gammaRate = []
epsilonRate = []
binarylist = []


def inputList():
  while True:
    line = input()
    if line:
      binarylist.append(list(line))

    else:
      break
  # for obj in binarylist:
  # print(obj)
  return binarylist


def checkRows(binarylist):
  for c in range(12):
    zero = 0
    one = 0
    for i in binarylist:
      if i[c] == "0":
        zero += 1
      else:
        one += 1
    if zero > one:
      gammaRate.append("0")
      epsilonRate.append("1")
    if one > zero:
      gammaRate.append("1")
      epsilonRate.append("0")

  epsilon = "".join(epsilonRate)
  gamma = "".join(epsilonRate)

  e = int(epsilon, 2)
  g = int(gamma, 2)

  result = e * g

  print(result)


checkRows(inputList())
