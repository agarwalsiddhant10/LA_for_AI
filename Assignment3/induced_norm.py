import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
import math

def transform(A = None, save_path = None):
    print(A)
    print('Condition Number = ', np.linalg.cond(A))
    if A.shape[0] == A.shape[1]:
        print('Determinant: ', np.linalg.det(A))
    theta = np.random.uniform(low=0, high= 2* np.pi, size= (2000))
    phi = np.random.uniform(low=0, high=np.pi, size=(2000))
    points = np.zeros((A.shape[1], 2000))
    fig = plt.figure(figsize=(20, 40))
    if A.shape[1] == 2:
        points[0] = np.cos(theta)
        points[1] = np.sin(theta)
        ax = fig.add_subplot(1, 2, 1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.scatter(points[0], points[1])
    else:
        points[0] = np.cos(theta) * np.sin(phi)
        points[1] = np.sin(theta) * np.sin(phi)
        points[2] = np.cos(phi)
        
        ax = fig.add_subplot(1, 2, 1, projection='3d')
        ax.set_aspect('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.scatter(points[0], points[1], points[2], zdir='z')

    points = np.dot(A, points)
    if A.shape[0] == 3:
        ax = fig.add_subplot(1, 2, 2, projection='3d')
        ax.set_aspect('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.scatter(points[0], points[1], points[2], zdir='z', c='r')
    else:
        ax = fig.add_subplot(1, 2, 2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.scatter(points[0], points[1], c='r')
    # plt.savefig(save_path)
    plt.show()



transform(A = np.array([[-1/math.sqrt(2), 0], [0, 1/math.sqrt(2)], [-1, 1]]), save_path='plots/a.jpg')
transform(A = np.array([[-2, 1, 2], [0, 2, 0]]), save_path='plots/b.jpg')
transform(A = np.array([[1, 0.9], [0.9, 0.8]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 0], [0, -10]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 1], [1, 10]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 1], [1, 5]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 1], [1, 1]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 1], [1, 0.1]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 1], [1, 0.01]]), save_path='plots/a.jpg')
transform(A = np.array([[1, 1], [1, 0.0001]]), save_path='plots/a.jpg')    
transform(A = np.array([[1, 1], [1, 0]]), save_path='plots/a.jpg')