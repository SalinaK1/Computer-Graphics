from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else: 
        steps = abs(dy)
    x_inc = dx/steps
    y_inc = dy/steps
    x = x1
    y = y1

    glColor3f(0.7,0.3,1.0) #sets RGB color for the pixel points
    glPointSize(3.0) #sets point size i.e. size of each pixel that makes a point
    glBegin(GL_POINTS)
    
    for j in range(steps+1):
        glVertex2i(round(x), round(y))  #draws point
        x = x + x_inc
        y = y + y_inc
    glEnd()
    glFlush()       #shift to new window for drawing.

def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow("DDA Line Drawing Algorithm")
    
    glClearColor(0.0,0.0,0.0,0.0)       #Background color of window
    gluOrtho2D(-100,100,-100,100)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    # For drawing the axes
    glColor3f(0.0,1.0,1.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

if __name__ == "__main__":
    starting_point = input("Enter the starting point of line x1,y1: ").split(',')
    end_point = input("Enter the end point of line x2,y2: ").split(',')
    x1,y1 = int(starting_point[0]), int(starting_point[1])
    x2,y2 = int(end_point[0]), int(end_point[1])

    setup()

    glutDisplayFunc(lambda: DDA(x1, y1, x2, y2))
    # glutIdleFunc(lambda: DDA(x1, y1, x2, y2))
    glutMainLoop()