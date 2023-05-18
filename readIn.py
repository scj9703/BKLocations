locationNo = 199
rows, cols = (locationNo, 3)
arr = [[0 for i in range(cols)] for j in range(rows)]
def readIn():
    """
    Reads in the locations of 199 Burger Kings into an array, specified in locations.txt
    AUTHOR: Samuel June - scj9703@rit.edu
    :return: A 2-D array of size 199x3
    """
    try:
        file = open("locations.txt", "r")
        firstline = file.readline()
        for i in range(locationNo):
            # Read in each comma separated line into the array.
            line = file.readline()
            line = line.strip()
            values = line.split(",")
            arr[i][0] = values[0]
            arr[i][1] = values[1]
            arr[i][2] = values[2]
        file.close()
        return arr

    except FileNotFoundError:
        print("File not found: locations.txt")
