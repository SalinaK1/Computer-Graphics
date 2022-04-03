from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def BLA(x_s, y_s, x_e, y_e):
    dx = x_e - x_s
    dy = y_e - y_s
    x=x_s
    y=y_s

    #swap lesser and greater points 
    if abs(dx)>abs(dy) and x_e < x_s:
        dx = - dx
        dy = - dy
        x = x_e
        x_e = x_s
        x_s = x
        y = y_e
        y_e = y_s
        y_s = y
    elif abs(dy)>=abs(dx) and y_e < y_s:
        dy = - dy
        dx = - dx
        y = y_e
        y_e = y_s
        y_s = y
        x = x_e
        x_e = x_s
        x_s = x

    glColor3f(0.7,0.3,1.0) #sets RGB color for the pixel points
    glPointSize(3.0) #sets point size i.e. size of each pixel that makes a point
    glBegin(GL_POINTS)

    glVertex2f(x, y) #plot starting point

    if abs(dx)>abs(dy): #for |slope| < 1 
        p=2*dy-dx #decision parameter
        for i in range(abs(dx)+1):
            x+=1
            if (p>=0):
                y = y+1 if y_s < y_e else y-1
                glVertex2f(x, y)
                p = p+2*dy-2*dx if y_s < y_e else p-2*dy-2*dx
            else:
                glVertex2f(x, y)
                p = p+2*dy if y_s < y_e else p-2*dy
        glEnd()

    else: #for |slope|>1
        p=2*dx-dy
        for i in range(0, abs(dy)+1):
            y+=1
            if (p>=0):
                x = x+1 if x_s < x_e else x-1
                glVertex2f(x, y)
                p = p+2*dx-2*dy if x_s < x_e else p-2*dx-2*dy
            else:
                glVertex2f(x, y)
                p = p+2*dx if x_s < x_e else p-2*dx
        glEnd()

    glFlush()

def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow("Bresenham Line Drawing Algorithm")
    
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

    glutDisplayFunc(lambda: BLA(x1, y1, x2, y2))
    glutMainLoop()