def ends_with_ab(input_string):
    state = 0 

    for char in input_string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == 'b':
                state = 2
            else:
                state = 0

    return state == 2


test_strings = ["ab", "aab", "abb", "abab", "baab"]
for string in test_strings:
    if ends_with_ab(string):
        print(f"'{string}' ends with 'ab'")
    else:
        print(f"'{string}' does not end with 'ab'")
