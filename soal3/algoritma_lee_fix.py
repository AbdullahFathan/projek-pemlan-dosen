from queue import Queue

class Maze:
    MOVE = (
        (-1, 0),  # UP
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
    )

    def solve(self, maze, finish, start):
        self.MAZE = maze
        self.SIZE = (len(maze), len(maze[0]))
        self.FINISH = finish

        self.PATH = [[0 for i in range(self.SIZE[1])] for i in range(self.SIZE[0])]
        self.PATH[start[0]][start[1]] = 1

        print("Maze start at", start, "and finish at", finish)
        Maze.display(maze)

        path = self.__lee_algorithm__(start)
        if path:
            print(f"Number of steps taken: {len(path) }")  
            self.PATH = [[0 for i in range(self.SIZE[1])] for i in range(self.SIZE[0])]
            for col,row in path:
                self.PATH[col][row] = '1'
            Maze.display(self.PATH)
        else:
            print("Solution does not exist")

    def display(matrix):
        for r in matrix:
            for c in r:
                code = "#" if c == 0 else "."
                print(code, end=" ")
            print()

    def __lee_algorithm__(self, start):
        #membuat queue kosong 
        queue = Queue()
        #meletakan rute awal
        queue.put((start, [start]))  

        #membuat perulangan jika queue tidak kosong
        while not queue.empty():
            # mendapatkan titik rute dan path 
            (row, col), path = queue.get()

            #jika titik merupakan finis
            if (row, col) == self.FINISH:
                #update path terpendek
                self.__update_path__(path) 
                return path

            #melakukan setiap peregakan yang mungkin
            for move_row, move_col in Maze.MOVE:
                #update nilai koordinat setelah peregakan baru
                new_row, new_col = row + move_row, col + move_col
                #cek apakah valid peregakannya
                if self.__is_valid__(new_row, new_col):
                    #update nilai path dengan +1 sebagai tanda sudah di kunjungi
                    self.PATH[new_row][new_col] = self.PATH[row][col] + 1
                    #memasukan kedalam queue
                    queue.put(((new_row, new_col), path + [(new_row, new_col)]))
        #kembalikan none jika tidak ada rute
        return None

    def __is_valid__(self, row, col):
        return 0 <= row < self.SIZE[0] and 0 <= col < self.SIZE[1] and self.MAZE[row][col] == 1 and self.PATH[row][col] == 0

    def __update_path__(self, path):
        for step, (row, col) in enumerate(path):
            self.PATH[row][col] = step



if __name__ == "__main__":
    solver = Maze()

    maze = [[1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            ]

    newMaze = solver.solve(maze, start=(0, 0), finish=(4, 4))

