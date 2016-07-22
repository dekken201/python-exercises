#Find Cost of Tile to Cover W x H Floor
#Calculate the total cost of tile it would take to cover a floor plan
#of width and height, using a cost entered by the user.
#Taking in account: one tile = 1m x 1m

def findCost():
    price = float(input("Price of the tile: "))
    width = int(input("Width: "))
    height = int(input("Height: "))
    finalcost = (width * height) * price
    print ("The cost will be: ", finalcost)

findCost()
