#lst = [2,4,8]

#x = [n * 2 for n in lst]
#print(x)

#while True:
   # x = int(input())
   # if x == 6740:
       # depths.append(x)
       # counter += 1
       # break
   # depths.append(x)
   # counter += 1

depths = []


def sweepOcean():

    counter = 0
#Getting user input in a list
    for i in range(0, 2000):
        ele = int(input())
        depths.append(ele)

#Iterate through list while comparing on index i and j
    for i in range(len(depths)):
        for j in range(i + 1, len(depths)):
            if depths[i] < depths[j]:
                counter += 1
            break

    print(counter)

sweepOcean()
