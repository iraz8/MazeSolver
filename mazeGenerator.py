import cells

NR_SPECIAL_CELL_TYPES = 4
MAX_GENERATE_MATRIX_ATTEMPS = 5


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', action='store', dest='seed', type=int)
    parser.add_argument('--width', action='store', dest='width', default=6, type=int)
    parser.add_argument('--height', action='store', dest='height', default=4, type=int)
    parser.add_argument('--nr_blocks', action='store', dest='nr_blocks', default=2, type=int)
    return parser.parse_args()


def generate_random_coordinates(seed: int, width: int, height: int) -> (int, int):
    import random
    if seed is None:
        random.seed()
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y


def generate_special_cells_coordinates(seed: int, width: int, height: int, nr_blocks: int):
    start = generate_random_coordinates(seed=seed, width=width, height=height)
    finish = generate_random_coordinates(seed=seed, width=width, height=height)
    blocks = [generate_random_coordinates(seed=seed, width=width, height=height) for _ in range(0, nr_blocks)]
    flame = generate_random_coordinates(seed=seed, width=width, height=height)
    return start, finish, blocks, flame


def generate_matrix(seed: int, width: int, height: int, nr_blocks: int):
    start, finish, blocks, flame = generate_special_cells_coordinates(seed=seed, width=width, height=height,
                                                                      nr_blocks=nr_blocks)
    matrix = [[0 for _ in range(0, height)] for _ in range(0, width)]
    matrix[start[0]][start[1]] = cells.START
    matrix[finish[0]][finish[1]] = cells.FINISH
    matrix[flame[0]][flame[1]] = cells.FLAME
    for i in range(0, len(blocks)):
        matrix[blocks[i][0]][blocks[i][1]] = cells.BLOCK
    return matrix


def get_generated_matrix(seed: int, width: int, height: int, nr_blocks: int):
    generated_matrix = generate_matrix(seed=seed, width=width, height=height, nr_blocks=nr_blocks)
    i = 0
    while matrix_validator(matrix=generated_matrix, nr_blocks=nr_blocks) is False:
        if i > MAX_GENERATE_MATRIX_ATTEMPS:
            raise Exception('MAX ATTEMPTS TO GENERATE MATRIX REACHED!')
        generated_matrix = generate_matrix(seed=seed, width=width, height=height, nr_blocks=nr_blocks)
        i += 1

    return generated_matrix


def print_matrix(matrix: list):
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix)):
            print(matrix[j][i], end='   ')
        print()


def matrix_validator(matrix: list, nr_blocks: int):
    nr_types_detected = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] != cells.EMPTY:
                nr_types_detected += 1
    if nr_types_detected == (NR_SPECIAL_CELL_TYPES - 1 + nr_blocks):
        return True
    return False


if __name__ == "__main__":
    args = parse_args()
    matrix = get_generated_matrix(seed=args.seed, width=args.width, height=args.height, nr_blocks=args.nr_blocks)
    print_matrix(matrix)
