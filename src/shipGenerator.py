ships = {
    "destroyer":[[[0,0], [0,1]], [[0,0],[1,0]]],
    "submarine":[[[0,0], [0,1], [0,2]], [[0,0],[1,0], [2,0]]],
    "cruiser":  [[[0,0], [0,1], [0,2]], [[0,0],[1,0], [2,0]]],
    "carrier":  [[[0,0], [0,1], [0,2], [0,3], [0,4]], [[0,0],[1,0], [2,0], [3,0], [4,0]]]
}

shipSymbols = {"destroyer":1, "submarine":2, "cruiser":3, "carrier":4}


def matrixAddition(m1, m2):
    m3 = []
    for i in range(int((len(m1)+len(m2))/2)):
        m3.append(m1[i]+m2[i])
    return m3

#ShipName = Str, Origin = List (representing the upper/left most pos of the ship), orientation = Str ("vert", "hori"), array = the mapArray...
def plotShip(shipName, origin, orientation, array):
    if orientation.lower() == "vert": shipData = ships[shipName.lower()][0]
    if orientation.lower() == "hori": shipData = ships[shipName.lower()][1]
    for point in shipData:
        pixelPos = matrixAddition(origin, point)
        if array[pixelPos[1]][pixelPos[0]] == 0:
            try:
                array[pixelPos[1]][pixelPos[0]] = shipSymbols[shipName.lower()]
            except:
                return [f"Failed to plot point {pixelPos[0]}, {pixelPos[1]}"]
        else: return ["Cannot overwrite other ships."]
    return [f"Sucessfully added: {shipName}", array]
