
N = 9
board = [[0] * N] * N

board[0] = [7, 8, 0, 1, 3, 6, 2, 5, 4]
board[1] = [5, 4, 6, 1, 3, 0, 7, 8, 9]
board[2] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board[3] = [9, 8, 7, 6, 5, 4, 3, 2, 1]
board[4] = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def check_array(line):
    if line.count(0) == 1:  # 残り1つだけ埋まっていない場合
        for i in range(N):
            if (i+1 in line) is False:  # 残り1つの数字を特定
                line[line.index(0)] = i+1
                print(line)


def get_line(y):
    return board[y]


def get_column(x):
    col = [c[x] for c in board]
    return col


def get_block(y, x):
    blk = [0] * N
    blk[0:3] = board[y+0][x+0:x+3]
    blk[3:6] = board[y+1][x+0:x+3]
    blk[6:9] = board[y+2][x+0:x+3]
    return blk


def get_block_point(z):
    b_p_y = (int(z / 3)*3)
    b_p_x = (int(z % 3)*3)
    return b_p_y, b_p_x


def get_block_num(x, y):
    x_p = int(x/3)
    y_p = int(y/3)*3
    block_num = x_p + y_p
    return block_num


def main():
    s = 6
    t = 3
    print(get_line(t))
    print(get_column(s))

    block_num = get_block_num(s, t)
    y, x = get_block_point(block_num)
    blk = get_block(y, x)
    print(blk)


if __name__ == '__main__':
    main()


