def loading_bar(progress):
    empty_bar = "["
    num = progress // 10
    for i in range(1, 11):
        if i <= num:
            empty_bar += "%"
        else:
            empty_bar += "."
    empty_bar += "]"
    return empty_bar


number = int(input())
status = loading_bar(number)
if number < 100:
    print(f'{number}% {status}')
    print("Still loading...")
else:
    print("100% Complete!")
    print(f'{status}')
