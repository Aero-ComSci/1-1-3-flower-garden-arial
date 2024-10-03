import turtle as trtl
class Flower:
  distance = 0
  def __init__(self, flowerType, num, color, distance = 50):
    self.flowerType = flowerType
    self.num = int(num)
    self.color = color
    self.distance = distance
    self.turtle = trtl.Turtle()
  def drawall(self, num):
    screen = trtl.Screen()
    screen.setup(width=800, height=600)  # Set the screen size
    width = screen.window_width()
    height = screen.window_height()
    
    self.turtle.hideturtle()
    self.turtle.speed(0)  # Fastest drawing speed
    
    # Calculate the size of each split
    split_width = width / num
    split_height = height / num
    
    for i in range(num):
        for j in range(num):
            # Calculate the center of each split
            center_x = (i + 0.5) * split_width - width / 2
            center_y = (j + 0.5) * split_height - height / 2
            
            self.turtle.penup()
            self. turtle.goto(center_x, center_y)
            self. turtle.pendown()
            self.draw()
        
  def draw(self):
    self.turtle.color(self.color)
    self.turtle.begin_fill()
    self.turtle.right(90)
    self.turtle.forward(100)
    self.turtle.circle(20)
    self.turtle.end_fill()

class Rose(Flower):
  def __init__(self, num, distance = 50):
    super().__init__("rose", num, "red", distance)
  def draw(self):
    super().draw()
   
class Violet(Flower):
  def __init__(self, num, distance = 50):
    super().__init__("violet", num, "purple", distance)
  def draw(self):
    super().draw()

class Poppy(Flower):
  def __init__(self, num, distance = 50):
    super().__init__("poppy", num, "white", distance)
  def draw(self):
    super().draw()

class Marigold(Flower):
  def __init__(self, num, distance = 50):
    super().__init__("marigold", num, "yellow", distance)
  def draw(self):
    super().draw()

class Lily(Flower):
  def __init__(self, num, distance = 50):
    super().__init__("lily", num, "pink", distance)
  def draw(self):
    super().draw()

def main(userinput):
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

  if flowerType == "rose" or flowerType == "roses":
    rose = Rose(int(num))
    rose.drawall(int(num))
  elif flowerType == "violet" or flowerType == "violets":
    violet = Violet(int(num))
    violet.drawall(int(num))
  elif flowerType == "poppy" or flowerType == "poppies":
    poppy = Poppy(int(num))
    poppy.drawall(int(num))
  elif flowerType == "marigold" or flowerType == "marigolds":
    marigold = Marigold(int(num))
    marigold.drawall(int(num))
  elif flowerType == "lily" or flowerType == "lilies":
    lily = Lily(int(num))
    lily.drawall(int(num))
  else:
    print("Invalid flower type. Please choose from: rose, violet, poppy, marigold, lily.")

userinput = input("What flower and how many would you like me to draw? (e.g., 5 roses) ").strip()
if __name__ == "__main__":
  main(userinput)
