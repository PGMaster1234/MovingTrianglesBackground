import pygame
import random
import math

screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
print(math.sin(random.randint(1, 1)))

triangle_vertices = []
boid_rects = []
boid_width = 5

for i in range(50):
    triangle_vertices.append([random.randint(0, 1200), random.randint(0, 650),
                              10, 10, random.randint(0, 90), 255])

for boid in triangle_vertices:
    boid_rects.append(pygame.Rect(boid[0], boid[1], boid_width, boid_width))


left_wall = pygame.Rect(0, 0, 5, 650)
top_wall = pygame.Rect(0, 0, 1200, 5)
bottom_wall = pygame.Rect(0, 650, 1200, 5)
right_wall = pygame.Rect(1200, 0, 0, 650)
strength_of_boid = 0.1
sensing_distance = 100
running = True
wall_avoidance_strength = 0.1
while running:

    for boid in triangle_vertices:
        for other_boid in triangle_vertices:
            if abs(other_boid[0] - boid[0]) < sensing_distance:
                if abs(other_boid[1] - boid[1]) < sensing_distance:
                    if other_boid[4] > boid[4]:
                        boid[4] += strength_of_boid
                    else:
                        boid[4] -= strength_of_boid

    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for vert in triangle_vertices:
                vert[4] += 10

    for vert in triangle_vertices:
        pygame.draw.circle(screen, (255, vert[5], vert[5]), (vert[0], vert[1]), boid_width)

        vert[0] += vert[2] * math.sin(vert[4])
        vert[1] += vert[3] * math.cos(vert[4])

        if vert[0] > 1200:
            vert[0] = 1200
        if vert[0] < 0:
            vert[0] = 0
        if vert[1] > 650:
            vert[1] = 650
        if vert[1] < 0:
            vert[1] = 0

        if pygame.draw.line(screen, (200, 200, 200), (vert[0], vert[1]),
                            (vert[0] + (vert[2] + 50) * math.sin(vert[4]),
                             vert[1] + (vert[3] + 50) * math.cos(vert[4])), 5).colliderect(left_wall):
            vert[4] += wall_avoidance_strength
        if pygame.draw.line(screen, (200, 200, 200), (vert[0], vert[1]),
                            (vert[0] + (vert[2] + 50) * math.sin(vert[4]),
                             vert[1] + (vert[3] + 50) * math.cos(vert[4])), 5).colliderect(right_wall):
            vert[4] += wall_avoidance_strength
        if pygame.draw.line(screen, (200, 200, 200), (vert[0], vert[1]),
                            (vert[0] + (vert[2] + 50) * math.sin(vert[4]),
                             vert[1] + (vert[3] + 50) * math.cos(vert[4])), 5).colliderect(top_wall):
            vert[4] += wall_avoidance_strength
        if pygame.draw.line(screen, (200, 200, 200), (vert[0], vert[1]),
                            (vert[0] + (vert[2] + 50) * math.sin(vert[4]),
                             vert[1] + (vert[3] + 50) * math.cos(vert[4])), 5).colliderect(bottom_wall):
            vert[4] += wall_avoidance_strength
        for boid in boid_rects:
            for boid2 in boid_rects:
                if boid.colliderect(boid2):
                    if vert[5] > 1:
                        vert[5] -= 0.1

    pygame.display.update()
    clock.tick(60)
