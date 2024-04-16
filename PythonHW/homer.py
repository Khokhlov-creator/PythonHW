"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""
def maxExpirationDay(fridge):
    if not fridge:
        return -1
    maxDate = 0
    for food in fridge:
        if food.expiration > maxDate:
            maxDate = food.expiration
    return maxDate



# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""
def histogramOfExpirations(fridge):
    lst = [0] * (maxExpirationDay(fridge)+1)
    for tmp in range(1, maxExpirationDay(fridge)+1):
        for food in fridge:
            if food.expiration == tmp:
                lst[tmp] += 1
    return lst

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    lstTmp = histogram.copy()
    for i in range(len(histogram)-1):
        lstTmp[i+1] = lstTmp[i]+lstTmp[i+1]
    return lstTmp


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    if not fridge:
        return []

    histogram = histogramOfExpirations(fridge)
    cumSum = cumulativeSum(histogram)

    sortedFridge = [Food] * len(fridge)

    for food in fridge:
        cumSum[food.expiration] -= 1
        posInd = cumSum[food.expiration]
        sortedFridge[posInd] = food

    return sortedFridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""
def reverseFridge(fridge):
    return fridge[::-1]
# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    lstTmp = []
    for food in fridge:
        if food.name == name:
            lstTmp.append(food)
    if not len(lstTmp):
        lstTmp = fridge.copy()
        return lstTmp

    foodToDelete = reverseFridge(sortFoodInFridge(lstTmp)).pop()
    lstTmp = []

    for food in fridge:
        if food == foodToDelete:
            continue
        else:
            lstTmp.append(food)
    newFridge = lstTmp.copy()
    return newFridge


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)


fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]

print(histogramOfExpirations(fridge))
openFridge(fridge)
openFridge(
    eatFood("donut",
        [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
        Food("donut", 3), Food("donut", 1), Food("donut", 6)]
    ))