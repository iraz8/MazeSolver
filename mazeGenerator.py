def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', action='store', dest='seed', type=int)
    parser.add_argument('--width', action='store', dest='width', default=10, type=int)
    parser.add_argument('--height', action='store', dest='height', default=8, type=int)
    parser.add_argument('--blocks_nr', action='store', dest='blocks_nr', default=1, type=int)
    return parser.parse_args()


def generate_random_coordinates(seed: int, width: int, height: int) -> (int, int):
    import random
    if seed is None:
        random.seed()
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y


def generate_matrix(seed: int, width: int, height: int):
    start = generate_random_coordinates(seed=seed, width=width, height=height)
    finish = generate_random_coordinates(seed=seed, width=width, height=height)
    flame = generate_random_coordinates(seed=seed, width=width, height=height)

    matrix = [[0 for _ in range(0, height)] for _ in range(0, width)]
    matrix[start[0]][start[1]] = 1
    matrix[finish[0]][finish[1]] = 2
    matrix[flame[0]][flame[1]] = -1
    print_matrix(matrix)


def print_matrix(matrix: list):
    for i in range(0, len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    args = parse_args()
    generate_matrix(seed=args.seed, width=args.width, height=args.height)
