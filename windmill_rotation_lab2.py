
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

PI=3.14159
current_angle=0
step_angle=0.2

def drawWindblades():
    global current_angle,step_angle
 
    glPushMatrix()   #to save and restore the untranslated coordinate system.
    glTranslatef( 250, 250, 0 )
    glRotatef(current_angle, 0, 0, 10)
    current_angle += step_angle
    glTranslatef(-250, -250, 0)
    
    glBegin(GL_TRIANGLES)           # draw first rotor blade
    glColor3fv([0.5,0.3,0.8])
    glVertex2f(250,250)
    glVertex2f(185,150)
    glVertex2f(150,185)
    glEnd()
    
    glBegin(GL_TRIANGLES)           # draw second rotor blade
    glColor3fv([0.5,0.3,0.8])
    glVertex2f(250,250)
    glVertex2f(220,360)
    glVertex2f(280,360)
    glEnd()
    
    glBegin(GL_TRIANGLES)           # draw third rotor blade
    glColor3fv([0.5,0.3,0.8])
    glVertex2f(250,250)
    glVertex2f(370,230)
    glVertex2f(350,190)
    glEnd()
    glPopMatrix()

def drawCircle(r,color):
    x=250.0                         #to draw the circle at in the middle of the blades
    y=250.0
    radius=r
    traingleAmount=20                   #the triangle as in blade
    twicePI=2.0*PI
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(color)
    glVertex2f(x,y)
    for i in range(0,traingleAmount+1):
        glVertex2f(
            x+(radius*math.cos(i*twicePI/traingleAmount)),
            y+(radius*math.sin(i*twicePI/traingleAmount))
        )
    glEnd()

def Body(v1,v2,v3,v4,color):
    glBegin(GL_POLYGON)
    glColor3fv(color)
    glVertex2fv(v1)
    glVertex2fv(v2)
    glVertex2fv(v3)
    glVertex2fv(v4)
    glEnd()

def myInit():
    glClearColor(0,0,0,1)
    gluOrtho2D(0,500,0,500)
    glMatrixMode(GL_PROJECTION)

def Draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    Body([225,0],[275,0],[275,280],[225,280],[0.1,0.1,0.2])
    drawWindblades()
    drawCircle(5,[0.3,0,0.9])
    glFlush()
    glutSwapBuffers()
    glutPostRedisplay()

def idle():
    glutPostRedisplay()  #since the screen before the display is idle,this function calls the next from the above function call and the work is done. 

def Menu(choice):
    global step_angle
    if choice==1:
        step_angle=0.6
    if choice==2:
        step_angle=0.2
    if choice==3:
        step_angle=0

if __name__=="__main__":
    glutInit()
    glutInitWindowSize(600,600)
    glutInitWindowPosition(300,300)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutCreateWindow("WindMill Rotation")
    myInit()
    glutCreateMenu(Menu)        #Menu to show the user functions of how to rotate the fan and at what speed 
    glutAddMenuEntry("Speed high",1)
    glutAddMenuEntry("Speed low",2)
    glutAddMenuEntry("Stop",3)
    glutAttachMenu(GLUT_LEFT_BUTTON)        #Bring the left button press a box with above menu options 
    glutIdleFunc(idle)
    glutDisplayFunc(Draw)
    glutMainLoop()