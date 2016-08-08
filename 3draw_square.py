import turtle


setup_turtle():
	# creates a screen to place/see the turtle
	window = turtle.Screen()
	window.bgcolor("deep sky blue")

	# instantiates turtle objects from Turtle class and customizes it
	isaac = turtle.Turtle()
	isaac.shape("turtle")
	isaac.shapesize(1,1,1)
	isaac.color("white")

	johanna = turtle.Turtle()
	johanna.shape("turtle")
	johanna.shapesize(1,1,1)
	johanna.color("pink")
	
	# position turtles to the center of screen


def draw_art():
	# draw a triangle
	for i in range(3):
		johanna.forward(100)
		johanna.left(120)
	# draw a square and a circle
	for i in range(5):
		isaac.forward(100)
		isaac.left(90)
	isaac.forward(50)	
	isaac.circle(50)

	# exit on click
	window.exitonclick()

setup_turtle()
draw_art()