#user input at the very top 

#import turtle as trtl
#painter = trtl.Turtle()

userinput = input("What flower and how many would you like me to draw?").strip()
boingboing = userinput.split(" ")
num = ''
numbers = []
flowerType = None

for char in boingboing:
    if char.isdigit():
        num += char
        
        if int(num) > 30:
            print("Our max on one run is 30. Sorry for this and thank you for understanding")
            num = 30
        break
    else:
        if num:
            numbers.append(num)
            num = ''
        

   

flowers = ["roses", "daisies", "violets", "poppy", "marigold", "lily"]

w = 0
while w < len(boingboing):
    if boingboing[w].lower() in flowers:
        flowerType = boingboing[w]
        break

    w += 1

print(flowerType, num)



# print(num, flowerType)

# def rose(num, type):
#     painter.forward
    

# wn = trtl.Screen()
# wn.mainloop()

# first we make mae a function to draw flower 
#this funciton will have 5 if and elif statements and will change the colors of the petals only base don the case 

# flower funciton has 3 parts 
#circle 
#stem
#pettles, these are the hardest which we keep till end 
