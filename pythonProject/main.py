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


def compare(dict):
    counter = 0
    #Iterate through list while comparing on index i and j
    for i in range(len(dict)):
        for j in range(i + 1, len(dict)):
            if dict[i] < dict[j]:
                counter += 1
            break
    print(counter)

def sweepOcean2():
    depths = []
    window = []
    dict = {}

    for i in range(0, 2000):
        ele = int(input())
        depths.append(ele)

    for i in range(len(depths)):
        if len(window) == 0:
            window.append(i)
            dict[i] = depths[i]
        elif len(window) == 1:
            window.append(i)
            getKeys(window, dict, depths[i])
        elif len(window) == 2:
            window.append(i)
            getKeys(window, dict, depths[i])
        else:
            window.remove(window[0])
            window.append(i)
            getKeys(window, dict, depths[i])

    compare(dict)

def getKeys(window, dict, depths):

    lngth = len(window)
    if lngth == 2:
        dict[window[0]] = dict.get(window[0]) + depths
        dict[window[1]] = depths
    if lngth == 3:
        dict[window[0]] = dict.get(window[0]) + depths
        dict[window[1]] = dict.get(window[1]) + depths
        dict[window[2]] = depths

sweepOcean2()