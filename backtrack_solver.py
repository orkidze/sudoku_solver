class backtrack_sovler:
    # Default values
    # edge_length = 9
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, edge_length=9):
        if (edge_length % 3 != 0):
            raise ValueError('Edge length must be divisor of 3')
        self.square_edge_length = edge_length // 3
        self.edge_length = edge_length
        self.numbers = list()
        for i in range(0, edge_length):
            self.numbers.append(i + 1)

    def print_puzzle(self, puzzle):
        string = ""

        def append_line(string):
            string += '\n'
            for _ in range(self.edge_length):
                string += '----'
            string += '\n'
            return string

        string = append_line(string)
        for row in puzzle:
            string += '| '
            for col in row:
                string += str(col) + " | "
            string = append_line(string)

        print(string)

    def solve_backtrack(self, puzzle, row, col):
        def reject(puzzle, row, col):

            # Check horizontally
            for i in [x for x in range(self.edge_length) if x != col]:
                if puzzle[row][i] == puzzle[row][col]:
                    return True

            # Check square
            # Calculate the begging of square
            cord_x = col // 3
            start_x = cord_x * self.square_edge_length
            cord_y = row // 3
            start_y = cord_y * self.square_edge_length
            # Iterate through hosting square
            for i in [x for x in range(start_x, (start_x + 3)) if x != col]:
                for y in [x for x in range(start_y, (start_y + 3)) if x != row]:
                    if puzzle[row][col] == puzzle[y][i]:
                        return True

            # Check vertically
            for i in [x for x in range(self.edge_length) if x != row]:
                if puzzle[i][col] == puzzle[row][col]:
                    return True

        # Call function on the next square
        def step_forward():
            if col == self.edge_length - 1:
                self.solve_backtrack(puzzle, row + 1, 0)
            else:
                self.solve_backtrack(puzzle, row, col + 1)

        if puzzle[row][col] == 0:
            for i in self.numbers:
                puzzle[row][col] = i
                if reject(puzzle, row, col):
                    puzzle[row][col] = 0
                else:
                    if row == self.edge_length - 1 and col == self.edge_length - 1:
                        self.print_puzzle(puzzle)
                    else:
                        step_forward()
            puzzle[row][col] = 0
        else:
            step_forward()


bts = backtrack_sovler()

testpuzzle = [
    [0, 0, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0],
]
bts.print_puzzle(testpuzzle)
print('Solution')
bts.solve_backtrack(testpuzzle, 0, 0)
