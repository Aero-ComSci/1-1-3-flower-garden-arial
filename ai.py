def parse(userinput):
    flowers = ["roses", "rose", "violets", "violet", "poppy", "poppies", "marigold", "marigolds", "lily", "lilies"]
    boingboing = userinput.strip().split(" ")
    flowerType = None
    num = ''
    w = 0
    while w < len(boingboing):
        if boingboing[w].lower() in flowers:
            flowerType = boingboing[w]
            break

        w += 1

    for char in boingboing[w-1]:
        if char.isdigit():
            num += char
            
            if int(num) > 30:
                print("Our max on one run is 30. Sorry for this and thank you for understanding")
                num = 30
            break
    print(flowerType, num)
            

userinput = input("What flower and how many would you like me to draw?").strip()
parse(userinput)


    


