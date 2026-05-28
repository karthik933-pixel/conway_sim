
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((900,700))

running = True

rows = 20
cols = 20

grid = []
for row in range(rows):

    current_row = []

    for col in range(cols):

        life = random.choice([0,1])

        current_row.append(life)

    grid.append(current_row)

cell_size = 20

clock = pygame.time.Clock()

def count_neighbors(grid,col,row):

    count = 0

    for i in [-1,0,1]:
        for j in [-1,0,1]:

            if i == 0 and j == 0:
                continue

            n_row = row + i
            n_col = col + j

            if 0 <= n_col < cols and 0 <= n_row < rows:

                count += grid[n_row][n_col]

    return count

while running:

    screen.fill((0,0,0))

    for row in range(rows):
        for col in range(cols):

            x = (col * cell_size) + 200
            y = (row * cell_size) + 100

            if grid[row][col] == 1:
                color = (200,200,200)
            else:
                color = (30,30,30)

            pygame.draw.rect(
                screen,
                color,
                (x,y,cell_size,cell_size)
            )

            pygame.draw.rect(
                screen,
                (0,0,0),
                (x,y,cell_size,cell_size),
                2
            )

    new_grid = []

    for row in range(rows):

        current_row = []

        for col in range(cols):

            neighbors = count_neighbors(grid,col,row)

            cell = grid[row][col]

            if cell == 1:

                if neighbors == 2 or neighbors == 3:
                    current_row.append(1)
                else:
                    current_row.append(0)

            else:

                if neighbors == 3:
                    current_row.append(1)
                else:
                    current_row.append(0)

        new_grid.append(current_row)

    grid = new_grid

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    clock.tick(24)

pygame.quit()

