# I need a function with a return value 
# All the values should be an integer 
# The following code is an example 

input_dict = {
    10: [[5, 34, 23, 125], [13, 0, 7, 58], [21, 47]],
    11: [[0, 22, 25, 547], [13, 4, 63, 75], [22, 52]], 
    12: [[1, 56, 45, 362], [13, 23, 56, 56], [23, 56]],
    13: [[2, 30, 47, 653], [13, 13, 45, 362], [24, 0]],
    14: [[2, 42, 24, 526], [13, 17, 26, 457], [25, 4]],
    15: [[4, 48, 23, 546], [13, 22, ], [26, 7]],
    16: [[6, 40, 24, 452], [13, 26], [0, 9]],
    17: [[1, 16, 56, 568], [14, 26], [2, 9]],
    18: [[1, 10, 45, 498], [14, 26], [2, 9]],
    19: [[3, 45, 23, 362], [14, 26], [2, 9]]
}


# The first number of the first list keeps repeating from 0 1 2 3 4 5 6 0 1 2 3 4 5 6 starting number can be any number 

# expected result 
# output_dict = {
    #10: [[5, 34], [13, 0], [21, 47]],
    #11:                                 because the first number has been skipped and the second is smaller, so repeat the key number 
    #11: [[0, 22], [13, 4], [22, 52]], 
    #12: [[1, 56], [13, 9], [23, 56]],
    #13: [[2, 30], [13, 13], [24, 0]],
    #
    #15: [[4, 48], [13, 22], [26, 7]],
    #16
    #16: [[6, 40], [13, 26], [0, 9]],
    #                                  because the first number has 
    #18: [[1, 10], [14, 26], [2, 9]],
    #19: [[3, 45], [14, 26], [2, 9]] }
