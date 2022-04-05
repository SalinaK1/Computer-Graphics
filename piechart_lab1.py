from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from midpoint_circle_lab1 import CircleDA


def radian(angle_in_degrees): #caclulates radian for degrees
    return - math.pi /180 * angle_in_degrees

def plot_lines(x1, y1, x2, y2): #plots line with openGL function
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def draw(thetas):
    CircleDA(0, 0, 100) #midpoint circle drawing
    x1 = 0
    y1 = 100
    angle = 0
    for i, theta in enumerate(thetas): # for each theta in input, plots lines
        for j in range(angle, angle+theta): #plots lines from previous angle to the next angle
            fill=0
            while fill<1: #plots line at interval of 0.1 pixel
                radian_val = radian(j+fill)
                    #finding point on circle from the degree
                x = round(x1* math.cos(radian_val) - y1* math.sin(radian_val)) 
                y = round(x1* math.sin(radian_val) + y1* math.cos(radian_val))
                    #random RGB value generation
                r = (i+1)%2
                g = (i/2)%2
                b = (i/4)%2
                glColor3f(r,g,b)
                plot_lines(0,0,x,y)
                fill+=0.1

        angle += theta

def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow("Piechart")
    
    glClearColor(0.0,0.0,0.0,0.0)       #Background color of window
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn
    glPointSize(5.0)


if __name__ == "__main__":
    correct_input = True
    thetas = []
    while(correct_input): #take angle inputs from the user
        userInput = input("Enter the values of theta degrees in pie charts separated by space: ")
        userInput = userInput.split()

        for i in userInput:
            thetas.append(int(i))
        
        if sum(thetas) > 360:
            correct_input = False
            print("Sum of angles exceeded 360 degrees. The piechart can't be drawn.")
        else:
            remainings = 360 - sum(thetas)
            thetas.append(int(remainings))
            setup()
            glutDisplayFunc(lambda: draw(thetas))
            glutIdleFunc(lambda: draw(thetas))
            glutMainLoop()