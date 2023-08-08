def process_input_dict(input_dict):
    output_dict = {}
    prev_first_num = None
    prev_second_num = None

    for key, sublist in input_dict.items():
        first_num, second_num = sublist[0][:2]

        # task to repeat the key only མཆོངས་ན་ཆུ་ཚོད་ཉུང་བ་ལྷག 

        # if the second number is smaller than while the first number has skipped.
        if prev_first_num is not None and first_num > prev_first_num + 1 and prev_second_num < second_num:
            print("སྔོན་གྱི་གི་ཆུ་ཚོད་ཉུང་བས་ན་སྔོན་གྱི་ཚེས་ལྷག་འདོན་པ།", key, sublist)
            continue 
        if prev_first_num is not None and first_num > prev_first_num + 1 and second_num < prev_second_num:
            print("རྗེས་མའི་ཆུ་ཚོད་ཉུང་བ་ན་རྗེས་མའི་ཚེས་ལྷག་འདོན་པ།", key, sublist)
            continue 


        if prev_first_num == 6 and first_num == 1 and prev_second_num < second_num:
            print("སྔོན་གྱི་ཆུ་ཚོད་ཉུང་བས་ན་སྔོན་གྱི་ཚེས་ལྷག་འདོན་པ།", key, sublist)
            continue 
        if prev_first_num == 6 and first_num == 1 and second_num < prev_second_num:
            print("རྗེས་མའི་ཆུ་ཚོད་ཉུང་བ་ན་རྗེས་མའི་ཚེས་ལྷག་འདོན་པ།", key, sublist)
            continue 


        if prev_first_num == 5 and first_num == 0 and prev_second_num < second_num:
            print("སྔོན་གྱི་ཆུ་ཚོད་ཉུང་བས་ན་སྔོན་གྱི་ཚེས་ལྷག་འདོན་པ།", key, sublist)
            continue 
        if prev_first_num == 5 and first_num == 0 and second_num < prev_second_num:
            print("རྗེས་མའི་ཆུ་ཚོད་ཉུང་བ་ན་རྗེས་མའི་ཚེས་ལྷག་འདོན་པ།", key, sublist)
            continue 


        # task to skip the key-value pair ལྡབ་ན་ཆུ་ཚོད་མང་བ་ཆད།
        if prev_first_num is not None and first_num == prev_first_num and prev_second_num > second_num:
            
            print("སྔོན་གྱི་ཆུ་ཚོད་མང་བས་ན་སྔོན་གྱི་ཚེས་ཆད་འདོན་པ།", key, sublist)
            continue 

        if prev_first_num is not None and first_num == prev_first_num and prev_second_num < second_num:
            print("རྗེས་མའི་ཆུ་ཚོད་མང་བས་ན་རྗེས་མའི་ཚེས་ཆད་འདོན་པ།", key, sublist)
            continue
        
        if key not in output_dict:
            output_dict[key] = []

        output_dict[key].append(sublist)
        prev_first_num = first_num
        prev_second_num = second_num

    return output_dict

input_dict = {
    10: [[5, 34], [13, 0], [21, 47]],
    11: [[0, 22], [13, 4], [22, 52]], 
    12: [[1, 56], [13, 9], [23, 56]],
    13: [[2, 30], [13, 13], [24, 0]],
    14: [[2, 42], [13, 17], [25, 4]],
    15: [[4, 48], [13, 22], [26, 7]],
    16: [[6, 40], [13, 26], [0, 9]],
    17: [[1, 16], [14, 26], [2, 9]],
    18: [[1, 10], [14, 26], [2, 9]],
    19: [[3, 45], [14, 26], [2, 9]]
}
print(process_input_dict(input_dict))


# expected result 

# output_dict = {
    #10: [[5, 34], [13, 0], [21, 47]],
    #11:
    #11: [[0, 22], [13, 4], [22, 52]], 
    #12: [[1, 56], [13, 9], [23, 56]],
    #13: [[2, 30], [13, 13], [24, 0]],
    #
    #15: [[4, 48], [13, 22], [26, 7]],
    #16
    #16: [[6, 40], [13, 26], [0, 9]],
    #
    #18: [[1, 10], [14, 26], [2, 9]],
    #19: [[3, 45], [14, 26], [2, 9]] }
