# I need a function with a return value 
# All the values should be an integer 
# The following code is an example 
input_dict = {
    10: [[6, 34, 23, 125], [13, 0, 7, 58], [21, 47, 56, 456]],
    11: [[0, 22, 25, 547], [13, 4, 63, 75], [22, 52, 36, 456]], 
    12: [[1, 56, 45, 362], [13, 23, 56, 56], [23, 56, 42, 654]],
    13: [[3, 30, 47, 653], [13, 13, 45, 362], [24, 0, 15, 362]],
    14: [[4, 42, 24, 526], [13, 17, 26, 457], [25, 4, 54, 435]],
    15: [[5, 41, 23, 546], [13, 22, 65, 98], [26, 7, 68, 478]],
    16: [[5, 48, 24, 452], [13, 26, 52, 563], [0, 9, 45, 316]],
    17: [[0, 16, 56, 568], [14, 26, 45, 236], [2, 9, 62, 416]],
    18: [[1, 10, 45, 498], [14, 26, 56, 785 [2, 9, 49, 186]],
    19: [[2, 45, 23, 362], [14, 26, 45, 456], [2, 9, 67, 198]]
    20: [[4, 10, 45, 498], [14, 26, 56, 785 [2, 9, 49, 186]],
}
# The first number of the first list keeps repeating from 0 1 2 3 4 5 6 0 1 2 3 4 5 6 starting number can be any number 
# task is to do with number of first list. 
# expected result 
# output_dict = {10: [[6, 34, 23, 125], [13, 0, 7, 58], [21, 47, 56, 456]],
    11: [[0, 22, 25, 547], [13, 4, 63, 75], [22, 52, 36, 456]], 
    12: [[1, 56, 45, 362], [13, 23, 56, 56], [23, 56, 42, 654]],
    13: #  because 2 number has skipped and the second is smaller 
    13: [[3, 30, 47, 653], [13, 13, 45, 362], [24, 0, 15, 362]],
    14: [[4, 42, 24, 526], [13, 17, 26, 457], [25, 4, 54, 435]],
    15: [[5, 41, 23, 546], [13, 22, 65, 98], [26, 7, 68, 478]],
    # 16: [[5, 48, 24, 452], [13, 26, 52, 563], [0, 9, 45, 316]], the first number is repeated and second number is greater. this should store in a new variable and remove from this line 
    17: [[0, 16, 56, 568], [14, 26, 45, 236], [2, 9, 62, 416]],
    18: [[1, 10, 45, 498], [14, 26, 56, 785 [2, 9, 49, 186]],
    19: [[2, 45, 23, 362], [14, 26, 45, 456], [2, 9, 67, 198]]
    20: [[4, 10, 45, 498], [14, 26, 56, 785 [2, 9, 49, 186]],
}

# at the end of dict_value I need the record of skipped number and repeated number and variable that was stored.


