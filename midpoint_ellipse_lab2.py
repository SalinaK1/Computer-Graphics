from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def stopping_criteria_r1(x,y,rx,ry): #stopping criteria for region 1  
    return 2*ry**2*x >= 2*rx**2*y

def stopping_criteria_r2(y): #stopping criteria for region 2
    return y==0

def plot_all_symmetric_pixels(x,y,xc,yc): #plots all the 4 symmetric points for an ellipse's point
    glColor3f(0.0,1.0,1.0)
    glPointSize(4.0)
    # print(f"({x},{y})")
    # print(f"({x+xc},{y+yc})")
    # print(f"({-x+xc},{y+yc})")
    # print(f"({x+xc},{-y+yc})")
    # print(f"({-x+xc},{-y+yc})")
    glBegin(GL_POINTS)

    glVertex2f(x+xc, y+yc)
    glVertex2f(-x+xc, y+yc)
    glVertex2f(x+xc, -y+yc)
    glVertex2f(-x+xc, -y+yc)
    glEnd() 

def EllipseDA(xc, yc, rx, ry):
    x = 0
    y = ry
    p1k = ry**2 + (rx**2)/4 - ry*rx**2
    
    while not stopping_criteria_r1(x, y,rx,ry):
        x=x+1
        if p1k<0:
            p1k = p1k + 2*x*ry**2 + ry**2
            plot_all_symmetric_pixels(x,y, xc, yc)
        else:
            y=y-1
            p1k = p1k + 2*ry**2*x + ry**2- 2*rx**2*y
            plot_all_symmetric_pixels(x,y, xc, yc)
    
    p2k= ry**2*(x + 0.5)**2 + rx**2*(y-1)**2 - ry**2*rx**2 

    while not stopping_criteria_r2(y):
        y=y-1
        if p2k<0:
            x=x+1
            p2k = p2k + 2*x*ry**2 + rx**2 - 2*rx**2*y
            plot_all_symmetric_pixels(x,y, xc, yc)
        else:
            p2k = p2k + rx**2 - 2*rx**2*y
            plot_all_symmetric_pixels(x,y, xc, yc)
    
    glFlush()

def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("Midpoint Ellipse Drawing Algorithm")
    
    glClearColor(0.0,0.0,0.0,0.0) 
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    glColor3f(1.0,1.0,1.0) #sets RGB color
    glPointSize(1.0) #sets point size

    glBegin(GL_LINES)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glVertex2f(0,-200)
    glEnd()

if __name__ == "__main__":
    center = input("Enter the center coordinate in the form x,y: ").split(',')
    rx = float(input("Enter the rx: "))
    ry = float(input("Enter the ry: "))
    if rx < 0 or ry < 0:
        print("The radius can't be a negative value.")
    else:
        xc,yc = int(center[0]), int(center[1])

        setup()

        glutDisplayFunc(lambda: EllipseDA(xc,yc,rx,ry))
        # glutIdleFunc(lambda: EllipseDA(xc,yc,rx,ry))
        
        glutMainLoop()