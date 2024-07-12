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