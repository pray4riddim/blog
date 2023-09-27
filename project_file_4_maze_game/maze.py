import pygame
import random

# 迷宫尺寸和单元格大小
maze_width = 600
maze_height = 600
cell_size = 20

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 初始化Pygame
pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((maze_width, maze_height))
pygame.display.set_caption("Maze_game by 212241816129 普洲")

clock = pygame.time.Clock()


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = [True, True, True, True]
        self.path_visited = False


def create_maze():
    stack = []
    current_cell = cells[0][0]
    visited_cells = 1

    while visited_cells < rows * cols:
        neighbors = []
        row = current_cell.row
        col = current_cell.col

        if row > 0 and not cells[row - 1][col].visited:
            neighbors.append(cells[row - 1][col])
        if row < rows - 1 and not cells[row + 1][col].visited:
            neighbors.append(cells[row + 1][col])
        if col > 0 and not cells[row][col - 1].visited:
            neighbors.append(cells[row][col - 1])
        if col < cols - 1 and not cells[row][col + 1].visited:
            neighbors.append(cells[row][col + 1])

        if len(neighbors) > 0:
            next_cell = random.choice(neighbors)
            stack.append(current_cell)

            if next_cell.row < current_cell.row:
                current_cell.walls[0] = False
                next_cell.walls[2] = False
            elif next_cell.row > current_cell.row:
                current_cell.walls[2] = False
                next_cell.walls[0] = False
            elif next_cell.col < current_cell.col:
                current_cell.walls[3] = False
                next_cell.walls[1] = False
            elif next_cell.col > current_cell.col:
                current_cell.walls[1] = False
                next_cell.walls[3] = False

            current_cell = next_cell
            current_cell.visited = True
            visited_cells += 1
        elif len(stack) > 0:
            current_cell = stack.pop()


def draw_maze():
    screen.fill(BLACK)
    for row in cells:
        for cell in row:
            x = cell.col * cell_size
            y = cell.row * cell_size

            if cell.walls[0]:
                pygame.draw.line(screen, WHITE, (x, y), (x + cell_size, y), 1)
            if cell.walls[1]:
                pygame.draw.line(
                    screen, WHITE, (x + cell_size, y), (x + cell_size, y + cell_size), 1
                )
            if cell.walls[2]:
                pygame.draw.line(
                    screen,
                    WHITE,
                    (x + cell_size, y + cell_size),
                    (x, y + cell_size),
                    1,
                )
            if cell.walls[3]:
                pygame.draw.line(screen, WHITE, (x, y + cell_size), (x, y), 1)

            if cell == cells[0][0] or cell == cells[rows - 1][cols - 1]:
                pygame.draw.rect(screen, GREEN, (x, y, cell_size, cell_size))

            if cell.path_visited:
                pygame.draw.circle(
                    screen,
                    GREEN,
                    (x + cell_size // 2, y + cell_size // 2),
                    cell_size // 6,
                )


def astar_algorithm():
    open_list = []
    closed_list = []
    start = cells[0][0]
    end = cells[rows - 1][cols - 1]

    g = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    f = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    g[start.row][start.col] = 0
    f[start.row][start.col] = heuristic(start, end)
    open_list.append(start)

    while len(open_list) > 0:
        current = min(open_list, key=lambda cell: f[cell.row][cell.col])

        if current == end:
            return reconstruct_path(parent, end)

        open_list.remove(current)
        closed_list.append(current)

        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            if neighbor in closed_list:
                continue

            tentative_g = g[current.row][current.col] + 1

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= g[neighbor.row][neighbor.col]:
                continue

            parent[neighbor.row][neighbor.col] = current
            g[neighbor.row][neighbor.col] = tentative_g
            f[neighbor.row][neighbor.col] = g[neighbor.row][neighbor.col] + heuristic(
                neighbor, end
            )

    return None


def get_neighbors(cell):
    neighbors = []

    if not cell.walls[0]:
        neighbors.append(cells[cell.row - 1][cell.col])
    if not cell.walls[1]:
        neighbors.append(cells[cell.row][cell.col + 1])
    if not cell.walls[2]:
        neighbors.append(cells[cell.row + 1][cell.col])
    if not cell.walls[3]:
        neighbors.append(cells[cell.row][cell.col - 1])

    return neighbors


def heuristic(cell, end):
    return abs(cell.row - end.row) + abs(cell.col - end.col)


def reconstruct_path(parent, current):
    path = []
    while current is not None:
        path.append(current)
        current = parent[current.row][current.col]

    return path[::-1]


# 创建迷宫单元格
rows = maze_height // cell_size
cols = maze_width // cell_size

cells = [[Cell(row, col) for col in range(cols)] for row in range(rows)]

create_maze()
draw_maze()
running = True
start_algorithm = False
move_start = False
player_row = 0
player_col = 0
path = astar_algorithm()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and path:
                move_start = True
            elif event.key == pygame.K_UP:
                if cells[player_row - 1][player_col].walls[2] == False:
                    player_row -= 1
            elif event.key == pygame.K_DOWN:
                if cells[player_row][player_col].walls[2] == False:
                    player_row += 1
            elif event.key == pygame.K_LEFT:
                if cells[player_row][player_col - 1].walls[1] == False:
                    player_col -= 1
            elif event.key == pygame.K_RIGHT:
                if cells[player_row][player_col].walls[1] == False:
                    player_col += 1
            elif event.key == pygame.K_SPACE:
                move_start = True

    if move_start:
        if len(path) > 1:
            current = path.pop(0)
            next_cell = path[0]

            screen.fill(BLACK)
            draw_maze()

            x = current.col * cell_size + cell_size // 2
            y = current.row * cell_size + cell_size // 2
            pygame.draw.circle(screen, GREEN, (x, y), cell_size // 4)

            x = next_cell.col * cell_size + cell_size // 2
            y = next_cell.row * cell_size + cell_size // 2
            pygame.draw.circle(screen, GREEN, (x, y), cell_size // 4)
            start_algorithm = True
        else:
            move_start = False

    if start_algorithm:
        path = astar_algorithm()

        if path is not None:
            for cell in path:
                cell.path_visited = True

            # 自动移动到终点并留下路线痕迹
            for cell in path:
                draw_maze()
                pygame.display.flip()
                clock.tick(10)
                if cell != cells[rows - 1][cols - 1]:
                    next_cell = path[path.index(cell) + 1]
                    if next_cell.col > cell.col:
                        player_col += 1
                    elif next_cell.col < cell.col:
                        player_col -= 1
                    elif next_cell.row > cell.row:
                        player_row += 1
                    elif next_cell.row < cell.row:
                        player_row -= 1

    else:
        screen.fill(BLACK)
        draw_maze()

        # 绘制玩家位置
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (
                player_col * cell_size + cell_size // 4,
                player_row * cell_size + cell_size // 4,
                cell_size // 2,
                cell_size // 2,
            ),
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
