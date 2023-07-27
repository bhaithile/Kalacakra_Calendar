input_dict = {
    10: [[6, 12, 25, 2, 31, 295], [13, 0, 20, 0, 0], [21, 47, 54, 3, 35, 412]],
    11: [[1, 6, 27, 0, 56, 660], [13, 4, 40, 0, 0], [22, 52, 12, 5, 10, 47]],
    12: [[3, 0, 28, 5, 15, 318], [13, 9, 0, 0, 0], [23, 56, 31, 0, 51, 389]],
    13: [[4, 54, 30, 3, 40, 683], [13, 13, 20, 0, 0], [24, 0, 49, 2, 26, 24]],
    14: [[5, 48, 49, 5, 47, 240], [13, 17, 40, 0, 0], [25, 4, 50, 0, 19, 467]],
    15: [[6, 44, 11, 5, 61, 504], [13, 22, 2, 4, 8], [26, 7, 50, 4, 13, 203]],
    16: [[0, 40, 35, 1, 20, 61], [13, 26, 26, 3, 27], [0, 9, 51, 2, 6, 646]],
    17: [[2, 40, 35, 1, 20, 61], [14, 26, 26, 3, 27], [2, 9, 51, 2, 6, 646]]
}

prev_first_num = None

for key, sublist in input_dict.items():
    first_num = sublist[0][0]

    if prev_first_num is not None:
        skipped = first_num - prev_first_num - 1
        if skipped > 0:
            for i in range(1, skipped+1):
                repeated_first_num = prev_first_num + i
                print(f"{key}: # between the key numbers {key-1} and {key}, {repeated_first_num} number has skipped of the first number of the first list and the second is smaller")
                print(f"{key}: [[{repeated_first_num}, {' ,'.join(str(num) for num in sublist[0][1:])}], {sublist[1]}, {sublist[2]}]")
    
    prev_first_num = first_num
    print(f"{key}: {sublist}")