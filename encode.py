########################################################################################################
# V3 code: # V3;width;height;cells;title;                                                              #
# Width and height are in base 74, base numbers 0-73 are:                                              #
#           1111111111222222222233333333334444444444555555555566666666667777                           #
# 01234567890123456789012345678901234567890123456789012345678901234567890123                           #
# --------------------------------------------------------------------------                           #
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}                           #
########################################################################################################
# Cells are encoded with a single base-74 number per cell.                                             #
# Each entry in the table has two base-74 digits. The right digit marks a placeable underneath.        #
# DR\CL| Gen| Cw | Ccw|Mover|Slide|Push|Wall|Enemy|Trash|Empty                                         #
# -----|----|----|----|-----|-----|----|----|-----|-----|-----                                         #
# Right| 01 | 23 | 45 |  67 |  89 | ab | cd |  ef |  gh |  {}                                          #
# Down | ij | kl | mn |  op |  qr | st | uv |  wx |  yz |                                              #
# Left | AB | CD | EF |  GH |  IJ | KL | MN |  OP |  QR |                                              #
# Up   | ST | UV | WX |  YZ |  !$ | %& | +- |  .= |  ?^ |                                              #
########################################################################################################
# Cells are counted starting from bottom-left going row-wise.                                          #
# There is a compression method V3 uses and it can be encoded in 3 different ways: )ab (aa)b (aa(bb)   #
# which says the next b tiles to fill are the last  a+1  tiles filled.                                 #
# The bordermode is a single digit which represents which border mode it is.                           #
# The most common border mode is 0, which represents ungeneratable walls. Here is an example V3 code:  #
# V3;i;5;0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}{)0f;example;       #
# As you can see, the width is i or 18 and the height is 5.                                            #
# All possible cells are in this V3 code in order.                                                     #
# The )0f says that the next 15 cells are filled with the last 1 cell, which is an empty.              #
########################################################################################################
#                                         thanks, uku1928305                                           #
########################################################################################################

V3  = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}")
LB1 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","x"]
V3E = list("{0iAS6oGY24a8qegc")
CELLSDICTIONARY = {"0":"{}", "1":"01", "2":"ij", "3":"AB",
                   "4":"ST", "5":"67", "6":"op", "7":"GH",
                   "8":"YZ", "9":"23klCDUV", "a":"45mnEFWX",
                   "b":"abstKL%&", "c":"89IJ", "d":"qr!$",
                   "e":"efwxOP.=", "f":"ghyzQR?^", "x":"cduvMN+-"}

def CheckCells_V3LB1(CELL,CELLSDICTIONARY):
    listOfConditions = [    CELL in CELLSDICTIONARY["0"], CELL in CELLSDICTIONARY["1"], CELL in CELLSDICTIONARY["2"], CELL in CELLSDICTIONARY["3"],
                            CELL in CELLSDICTIONARY["4"], CELL in CELLSDICTIONARY["5"], CELL in CELLSDICTIONARY["6"], CELL in CELLSDICTIONARY["7"],
                            CELL in CELLSDICTIONARY["8"], CELL in CELLSDICTIONARY["9"], CELL in CELLSDICTIONARY["a"], CELL in CELLSDICTIONARY["b"],
                            CELL in CELLSDICTIONARY["c"], CELL in CELLSDICTIONARY["d"], CELL in CELLSDICTIONARY["e"], CELL in CELLSDICTIONARY["f"], CELL in CELLSDICTIONARY["x"]]
    return listOfConditions.index(True)

def V3_Decode(V3code):
    V3code=V3code.split(";")
    SIZE = [V3code[1],V3code[2]] # x,y
    CELLS = list(V3code[3])
    for i in range(len(CELLS)): CELLS[i]=LB1[CheckCells_V3LB1(CELLS[i],CELLSDICTIONARY)]
    #TODO: size base 74 -> base 10
    return f'LB1 {SIZE[0]} {SIZE[1]} {"".join(CELLS)}'

def V3_Encode(LB1code):
    LB1code=LB1code.split(' ')
    SIZE = [LB1code[1],LB1code[2]] # x,y
    CELLS = list(LB1code[3])
    for i in range(len(CELLS)): CELLS[i]=V3E[LB1.index(CELLS[i])]
    return f'V3;{SIZE[0]};{SIZE[1]};{"".join(CELLS)}'

print(V3_Decode("V3;n;n;{0iAS6oGY24a8qegc{0iAS6oGY24a8qegc{{{aAaA"))
print(V3_Encode("LB1 n n 0123456789abcdefx0123456789abcdefx000b3b3"))
