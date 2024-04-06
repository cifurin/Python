import pygame
import numpy as np
from math import cos, sin, pi

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600

scale = 100
origin = [WIDTH / 2, HEIGHT / 2]

angle = 0

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

vertices = [n for n in range(9)]

vertices[0] = np.matrix([[-1], [1], [1]])
vertices[1] = np.matrix([[1], [1], [1]])
vertices[2] = np.matrix([[1], [-1], [1]])
vertices[3] = np.matrix([[-1], [-1], [1]])
vertices[4] = np.matrix([[-1], [1], [-1]])
vertices[5] = np.matrix([[1], [1], [-1]])
vertices[6] = np.matrix([[1], [-1], [-1]])
vertices[7] = np.matrix([[-1], [-1], [-1]])
vertices[8] = np.matrix([[-0.5], [1], [1]])

projection_matrix = np.matrix([[1, 0, 0], [0, 1, 0]])


def generate_rot_x(theta):
    # theta MUST be in Radians
    return np.matrix(
        [[1, 0, 0], [0, cos(theta), -sin(theta)], [0, sin(theta), cos(theta)]]
    )


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    rot_z = np.matrix(
        [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
    )

    rot_y = np.matrix(
        [[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]]
    )

    rot_x = np.matrix(
        [[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]]
    )

    # print(vertices[0])
    # print(np.dot(rot_x, vertices[0]))

    angle += 0.01
    # print(angle)

    # angle = pi/4

    window.fill(WHITE)

    render_points = []

    for point in vertices:
        #
        rotated = np.dot(rot_x, point)

        # This rotation is 180 degrees about the x-axis to account for the x-y axis used by Pygame, where y is downwards +ve
        # rotated = np.dot(generate_rot_x(pi), rotated)
        # This projects the 3D point on to the 2D surface, This is effectively just removing the z component
        projected2D = np.dot(projection_matrix, rotated)
        # print(projected2D)

        x = int(projected2D[0][0] * scale) + origin[0]
        y = int(projected2D[1][0] * scale) + origin[1]

        # x = int(projected2D[0][0])
        # y = int(projected2D[1][0])

        render_points.append((x, y))

    # x,y = render_points[0]
    # pygame.draw.circle(window, BLACK, (x, y), 5)

    for x, y in render_points:
        pygame.draw.circle(window, BLACK, (x, y), 5)

        pygame.draw.line(window, RED, render_points[4], render_points[5])
        pygame.draw.line(window, RED, render_points[5], render_points[6])
        pygame.draw.line(window, RED, render_points[6], render_points[7])
        pygame.draw.line(window, RED, render_points[7], render_points[4])
        pygame.draw.line(window, RED, render_points[0], render_points[4])
        pygame.draw.line(window, RED, render_points[1], render_points[5])
        pygame.draw.line(window, RED, render_points[2], render_points[6])
        pygame.draw.line(window, RED, render_points[3], render_points[7])
        # draw a diagonal line on face so that it can be identified
        # pygame.draw.line(window, RED, render_points[0], render_points[2])
        # pygame.draw.line(window, BLACK, render_points[5], render_points[7])

        pygame.draw.line(window, RED, render_points[0], render_points[1])
        pygame.draw.line(window, RED, render_points[1], render_points[2])
        pygame.draw.line(window, RED, render_points[2], render_points[3])
        pygame.draw.line(window, RED, render_points[3], render_points[0])

    pygame.display.update()
