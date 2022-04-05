from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def stopping_criteria(x,y): #stopping criteria
    return x>y

def plot_all_symmetric_pixels(x,y,xc,yc): #plots all the 8 symmetric points for a circle's point
    glColor3f(0.7,0.3,1.0) #sets RGB color for the pixel points
    glPointSize(3.0) #sets point size i.e. size of each pixel that makes a point
    glBegin(GL_POINTS)

    glVertex2f(x+xc, y+yc)
    glVertex2f(-x+xc, y+yc)
    glVertex2f(x+xc, -y+yc)
    glVertex2f(-x+xc, -y+yc)
    glVertex2f(y+xc, x+yc)
    glVertex2f(y+xc, -x+yc)
    glVertex2f(-y+xc, x+yc)
    glVertex2f(-y+xc, -x+yc)
    glEnd() 

def CircleDA(xc, yc, r):
    x = 0
    y = r
    pk = 1-r if isinstance(r,int) else 5/4-r  #decision parameter
    
    while not stopping_criteria(x, y):
        x=x+1
        if pk<0:
            pk = pk + 2*x + 1
            plot_all_symmetric_pixels(x,y, xc, yc)
        else:
            y=y-1
            pk = pk + 2*x - 2*y + 1
            plot_all_symmetric_pixels(x,y, xc, yc)
    
    glFlush()

def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(250, 250)
    glutCreateWindow("Midpoint Circle Drawing Algorithm")
    
    glClearColor(0.0,0.0,0.0,0.0)       #Background color of window
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    # For drawing the axes
    glColor3f(0.0,1.0,1.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glVertex2f(0,-200)
    glEnd()


if __name__ == "__main__":
    center = input("Enter the center of the circle x,y: ").split(',')
    radius = float(input("Enter the radius: "))
    xc,yc = int(center[0]), int(center[1])

    setup()

    glutDisplayFunc(lambda: CircleDA(xc,yc,radius)) 
    glutMainLoop()