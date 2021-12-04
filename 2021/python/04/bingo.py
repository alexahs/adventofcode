import numpy as np

class Board:
    def __init__(self, board):
        self.board = board
        self.size = board.shape[0]
        self.board_inds_set = np.zeros(board.shape)
        self.last_num = -1
        self.has_bingo = False

    def __repr__(self):
        return f"\n{self.board}"


    def update(self, num):
        self.update_set_nums(num)
        return self.calculate_score()

    def is_bingo(self):
        for i in range(self.size):
            if np.sum(self.board_inds_set[i,:]) == self.size:
                return True
        for j in range(self.size):
            if np.sum(self.board_inds_set[:,j]) == self.size:
                return True
        return False

    def calculate_score(self):
        if self.is_bingo():
            score = np.sum(self.board[ self.board_inds_set == 0])
            self.score = score*self.last_num
            self.has_bingo = True
            return self.score
        else:
            return 0
    
    def update_set_nums(self, num):
        self.board_inds_set[ self.board == num ] = 1
        self.last_num = num


def build_boards(inp):
    tmp_board = np.zeros((5, 5))
    cnt = 0
    boards_list = []
    for i in range(2, len(inp)):
        if inp[i] == "\n":
            boards_list.append(Board(tmp_board))
            tmp_board = np.zeros((5, 5))
            cnt += 1
            continue
        y = (i - cnt - 2) % 5
        tmp_board[y, :] = list(map(int, inp[i].split()))


    boards_list.append(Board(tmp_board))
    return boards_list

def build_bingo_nums(inp):
    return list(map(int, inp[0].split(",")))

def run_bingo(boards, nums):
    for num in nums:
        for b in boards:
            score = b.update(num)
            if score != 0:
                print(f"Bingo! score: {score:.0f}")
                return

def run_reverse_bingo(boards, nums):
    num_boads = len(boards)
    won = []
    for num in nums:
        for b in boards:
            if not b.has_bingo:
                score = b.update(num)
                if score != 0:
                    won.append(b)

    print(f"Score of last board: {won[-1].score:.0f}")


def main():
    with open("in", "r") as fp:
        inp = fp.readlines()

    bingo_nums = build_bingo_nums(inp)
    boards = build_boards(inp)

    run_bingo(boards, bingo_nums)
    run_reverse_bingo(boards, bingo_nums)

    
if __name__ == '__main__':
    main()
