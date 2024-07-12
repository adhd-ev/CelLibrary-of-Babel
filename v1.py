########################################################################################################
# V1 code comes like this: V1;width;height;placeables;cells;title;                                     #
# Width and height are in base 74, base numbers 0-73 are:                                              #
# The placeables are in form X.Y, separated by commas. The X counts from left to right and and Y       #
# counts from bottom to top. The cells are in form type.rot.X.Y, also separated by commas.             #
########################################################################################################
# The cell types are:                                                                                  #
# * 0-generator  * 1-cw rotator * 2-ccw rotator * 3-mover                                              #
# * 4-slide      * 5-push       * 6-wall        * 7-enemy * 8-trash                                    #
########################################################################################################
# The cell direction is right + rot times 90 degrees clockwise (RDLU).
# The X and Y are the same as calculating positions of placeables.
########################################################################################################
# Example V1 level:                                                                                    #
# V1;11;4;3.0,9.0,2.1,4.1,8.1,9.1,1.2,5.2,7.2,9.2,0.3,6.3,9.3;0.1.0.0,3.1.1.0,1.1.2.0,2.1.3.0,5.1.4.0, #
# 4.1.5.0,7.1.6.0,8.1.7.0,6.1.8.0,0.2.0.1,3.2.1.1,1.2.2.1,2.2.3.1,5.2.4.1,4.2.5.1,7.2.6.1,8.2.7.1,6.2. #
# 8.1,0.3.0.2,3.3.1.2,1.3.2.2,2.3.3.2,5.3.4.2,4.3.5.2,7.3.6.2,8.3.7.2,6.3.8.2,0.0.0.3,3.0.1.3,1.0.2.3, #
# 2.0.3.3,5.0.4.3,4.0.5.3,7.0.6.3,8.0.7.3,6.0.8.3;ex-sample;                                           #
########################################################################################################
#                                         thanks, uku1928305                                           #
########################################################################################################

V1CELLSDICTIONARY = {"1": [0.0], "2": [0.1], "3": [0.2], "4": [0.3],
                     "5": [3.0], "6": [3.1], "7": [3.2], "8": [3.3],
                     "9": [1.0, 1.1, 1.2, 1.3], "a": [2.0, 2.1, 2.2, 2.3],
                     "b": [5.0, 5.1, 5.2, 5.3], "c": [4.0, 4.2], "d": [4.1, 4.3],
                     "e": [7.0, 7.1, 7.2, 7.3], "f": [8.0, 8.1, 8.2, 8.3],
                     "x": [6.0, 6.1, 6.2, 6.3]} # Conversion table for V1 to/from LB1

def CheckCells_V1LB1(CELL): return next(lb1 for lb1, list in V1CELLSDICTIONARY.items() if CELL in list)

def V1_Decode(V1code: str):
    V1code = V1code.split(";")
    SIZE = [int(V1code[1]), int(V1code[2])] # x,y
    CELLS = V1code[4].split(",") # Split each cell into its individual code
    CELLAREA = [["0" for i in range(SIZE[0])] for j in range(SIZE[1])] # Setup a blank board

    for cell in CELLS:
        # Split cell into individual parts
        CellData = cell.split(".")
        CellX, CellY = int(CellData[2]), int(CellData[3])

        # Convert cell type into LB1 type
        CellCode = CheckCells_V1LB1(float(f'{CellData[0]}.{CellData[1]}'))

        # Add cell to CELLAREA
        CELLAREA[CellY][CellX] = CellCode
    
    # Return LB1 code
    return f'LB1 {SIZE[0]} {SIZE[1]} {"".join(item for x in CELLAREA for item in x)}'

print(V1_Decode("V1;11;4;3.0,9.0,2.1,4.1,8.1,9.1,1.2,5.2,7.2,9.2,0.3,6.3,9.3;0.1.0.0,3.1.1.0,1.1.2.0,2.1.3.0,5.1.4.0,4.1.5.0,7.1.6.0,8.1.7.0,6.1.8.0,0.2.0.1,3.2.1.1,1.2.2.1,2.2.3.1,5.2.4.1,4.2.5.1,7.2.6.1,8.2.7.1,6.2.8.1,0.3.0.2,3.3.1.2,1.3.2.2,2.3.3.2,5.3.4.2,4.3.5.2,7.3.6.2,8.3.7.2,6.3.8.2,0.0.0.3,3.0.1.3,1.0.2.3,2.0.3.3,5.0.4.3,4.0.5.3,7.0.6.3,8.0.7.3,6.0.8.3;ex-sample;"))
