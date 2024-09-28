def Base40():
    scores = 0
    n = 0
    _score = input('Enter Score: ')
    t = int(input('Enter Total Items: '))
    scores += int(_score)/t
    n += 1
    cmd = input("Continue? [Y/N]: ")
    if cmd == "N":
        if n == 0:
            print("No score is entered.")
            Base40()
        result = (scores/n)*60+40
        if result >= 75:
            print (result, 'Passed')
            return "Passed :>"
        else:
            print (result, 'Failed')
            return "Failed :<"
    Base40()
Base40()

