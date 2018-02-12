#coding:utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle = 0.0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("回転")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    init(300, 300)
    glutMainLoop()

def init(width, height):
    """初期化"""
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

def display():
    """描画処理"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
    # Y軸に沿ってangleだけ回転
    glRotatef(angle, 0.0, 1.0, 0.0)
    
    # Teapot
    glColor3f(1.0, 0.0, 0.0)
    glutSolidTeapot(1.0)
    
    glutSwapBuffers()  # バッファ切り替え

def idle():
    """アイドル時に呼ばれるコールバック関数"""
    global angle
    angle += 2.0  # 角度を更新
    glutPostRedisplay()  # 再描画

def reshape(width, height):
    """画面サイズの変更時に呼ばれるコールバック関数"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

if __name__ == "__main__":
    main()