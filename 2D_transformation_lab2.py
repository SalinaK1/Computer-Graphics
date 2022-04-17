from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

def radian(angle_in_degrees): #caclulates radian for degrees
    return math.pi /180 * angle_in_degrees

def plot_triangle_original(triangle_array): 
    glLineWidth(3.0)
    glColor3f(0.5,0.3,0.8)
    glBegin(GL_TRIANGLES)

    glVertex2f(triangle_array[0],triangle_array[1])
    glVertex2f(triangle_array[3],triangle_array[4])
    glVertex2f(triangle_array[6],triangle_array[7])
    glEnd()
    glFlush()

def plot_triangle(triangle_array): 
    glLineWidth(3.0)
    glColor3f(0.9,0.3,0.8)
    glBegin(GL_TRIANGLES)

    glVertex2f(triangle_array[0],triangle_array[1])
    glVertex2f(triangle_array[3],triangle_array[4])
    glVertex2f(triangle_array[6],triangle_array[7])
    glEnd()
    glFlush()


def translation(triangle_array,tx,ty):
    transformation_matrix = [[1,0,tx],[0,1,ty],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle

def rotation(triangle_array,theta):
    transformation_matrix = [[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle
    
def scaling(triangle_array,sx,sy):
    transformation_matrix = [[sx,0,0],[0,sy,0],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle

def reflection_x_axis(triangle_array):
    transformation_matrix = [[1,0,0],[0,-1,0],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle

def reflection_y_axis(triangle_array):
    transformation_matrix = [[-1,0,0],[0,1,0],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle

def shearing_x_axis(triangle_array,shx):
    transformation_matrix = [[1,shx,0],[0,1,0],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle

def shearing_y_axis(triangle_array,shy):
    transformation_matrix = [[1,0,0],[shy,1,0],[0,0,1]]
    point1=[triangle_array[0],triangle_array[1],1]
    point2=[triangle_array[3],triangle_array[4],1]
    point3=[triangle_array[6],triangle_array[7],1]
    transformed_point1 = np.dot(transformation_matrix,point1)
    transformed_point2 = np.dot(transformation_matrix,point2)
    transformed_point3 = np.dot(transformation_matrix,point3)
    transformed_triangle = np.concatenate((transformed_point1,transformed_point2,transformed_point3), axis=0)
    plot_triangle(transformed_triangle)
    return transformed_triangle



def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("2D Transformation")
    
    glClearColor(0.0,0.0,0.0,0.0)       #Background color of window
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn
    glPointSize(5.0)

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
    userInput = int(input("Enter the transformation you want to perform (Number 1-7).\n 1. Translation\n 2. Rotation\n 3. Scaling\n 4. Reflection about X axis\n 5. Reflection about Y axis\n 6. Shearing about X axis\n 7. Shearing about Y axis.\n => "))
    if userInput == 1:
        tx = int(input("Enter the value of tx: "))
        ty = int(input("Enter the value of ty: "))
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        translation(original_triangle,tx,ty)
    elif userInput == 2:
        rot_angle = int(input("Enter the rotation angle: "))
        rot_angle_radian = radian(rot_angle)
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        rotation(original_triangle,rot_angle_radian)
    elif userInput ==3:
        sx = int(input("Enter the value of sx: "))
        sy = int(input("Enter the value of sy: "))
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        scaling(original_triangle,sx,sy)
    elif userInput ==4:
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        reflection_x_axis(original_triangle)
    elif userInput ==5:
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        reflection_y_axis(original_triangle)
    elif userInput ==6:
        shx = int(input("Enter the value of shx for shearing about x-axis: "))
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        shearing_x_axis(original_triangle,shx)
    elif userInput ==7:
        shy = int(input("Enter the value of shy for shearing about y-axis: "))
        setup()
        original_triangle = [0,0,1,50,50,1,50,0,1]
        glutDisplayFunc(lambda: plot_triangle_original(original_triangle))
        shearing_y_axis(original_triangle,shy)
    else:
        print("Enter the valid option between 1-7")
    glutMainLoop()

