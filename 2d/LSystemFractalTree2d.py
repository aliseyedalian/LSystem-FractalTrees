import turtle
import re

BROWN = "#694D23"
GREEN = "#41A441"

def makeTree(axiom,rules,n_generations):
    generations = [axiom]  
    n = n_generations
    for _ in range(n):
        current_gen = generations[-1]
        next_gen = [getRule(char,rules) for char in current_gen]     
        generations.append(''.join(next_gen))
    last_gen = generations[-1]
    return last_gen

def getRule(char,rules):
    if char in rules:
        return rules[char]
    return char 

def drawTree(turtle,stepsize,tree,turnangle):
    memory = []
    for char in tree:
        turtle.pd()
        if char == "F": # forward with drawing
            turtle.forward(stepsize)
        elif char == "L": # Leaf -> green
            turtle.pencolor(GREEN)
            turtle.width(2)
        elif char == "S": # Stem -> brown
            turtle.pencolor(BROWN)
            turtle.width(1.5)
        elif char == "+": # heading Right
            turtle.right(turnangle)
        elif char == "-": # heading left
            turtle.left(turnangle)
        elif char == "[": # Save the current state of the turtle, that is, the turtle position and orientation:
            memory.append((turtle.position(), turtle.heading()))
        elif char == "]": # Restore the state of the turtle using the last saved state:
            turtle.pu()  
            position, heading = memory.pop()
            turtle.goto(position)
            turtle.setheading(heading)
        elif char == "A": #draw flower
            turtle.pencolor("red")
            turtle.circle(2)
        elif char == "B": #draw flower
            turtle.pencolor("purple")
            turtle.circle(2)
            
def init_turtle(heading , speed):
    myturtle = turtle.Turtle()  
    myturtle.speed(speed) 
    myturtle.setheading(heading)
    return myturtle
  
def init_turtle_screen(size):
    screen = turtle.Screen() 
    screen.screensize(size, size)
    screen.title("L-System Fractal Tree")
    return screen

def readInputs(fileName):
    f = open(fileName, "r")
    content = f.read()
    f.close()
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    rules = {}
    for line in lines:
        rule = line.rstrip().split("->")
        if len(rule)==2 :
            key = rule[0]
            value = rule[1]
            rules[key] = value
    axiom = re.search("^AXIOM : (\w+)", content, re.MULTILINE).group(1)
    n = int(re.search("^N : (\d+)$", content, re.MULTILINE).group(1))
    alpha0 = int(re.search("^ALPHA0 : (\d+)$", content, re.MULTILINE).group(1))
    angle = int(re.search("^ANGLE : (\d+)$", content, re.MULTILINE).group(1))
    return axiom ,rules , n , alpha0 , angle

if __name__ == "__main__":
    inputs_path = "inputs.txt"
    axiom , rules , n  , alpha0 , angle = readInputs(fileName = inputs_path)
    tree = makeTree(axiom = axiom, rules=rules, n_generations = n)  
    raphael = init_turtle(heading = alpha0 , speed = 0)  
    window = init_turtle_screen(size=2000)
    drawTree(turtle = raphael, stepsize = 10, tree = tree, turnangle = angle) 
    window.exitonclick()