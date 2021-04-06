def characters_in_range(symbol1, symbol2):
    symbol1 = ord(symbol1)
    symbol2 = ord(symbol2)
    end_result = ""
    for i in range(symbol1 + 1, symbol2):
        end_result += chr(i) + " "
    return end_result


s1 = input()
s2 = input()
a = 5

print(characters_in_range(s1, s2))
