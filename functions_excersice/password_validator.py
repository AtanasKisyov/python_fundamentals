def password_validation(password):
    is_valid_lenght = False
    is_valid_char = False
    two_digits = 0
    char_range_num = range(48, 58)
    char_range_cap = range(65, 91)
    char_range_sml = range(97, 123)
    if 6 <= len(password) <= 10:
        is_valid_lenght = True
    else:
        is_valid_lenght = False
    for i in range(len(password)):
        current_chr = ord(password[i])
        if current_chr in char_range_cap or current_chr in char_range_sml or current_chr in char_range_num:
            is_valid_char = True
            if current_chr in char_range_num:
                two_digits += 1
        else:
            is_valid_char = False
            break
    return is_valid_char, is_valid_lenght, two_digits


password_input = input()
result_list = list(password_validation(password_input))

if result_list[0] and result_list[1] and result_list[2] >= 2:
    print("Password is valid")
if not result_list[1]:
    print("Password must be between 6 and 10 characters")
if not result_list[0]:
    print("Password must consist only of letters and digits")
if result_list[2] < 2:
    print("Password must have at least 2 digits")
