with open("input.txt") as f:
    numbers = list(map(int, f.readline().strip().split(",")))

    boards = {}
    i = -1

    for line in f.readlines():
        line = line.strip()

        new_board = line == ""

        if new_board:
            i += 1
            boards[i] = []
        else:
            boards[i].append(list(map(int, filter(None, line.split(" ")))))


boards_check = {k: [[False for _ in range(5)] for __ in range(5)] for k in boards}

seen = []
for n in numbers:
    for k in boards:
        board = boards[k]
        board_check = boards_check[k]

        for row in range(5):
            cols = list(zip(*board_check))

            for col in range(5):
                if board[row][col] == n:
                    board_check[row][col] = True

                check_col = all(cols[col])

                if check_col:
                    break

            check_row = all(board_check[row])

            if check_row:
                break

        if check_col or check_row:
            if k not in seen:
                seen.append(k)
                sum_unmarkeds = sum(
                    [
                        board[row][col]
                        for col in range(5)
                        for row in range(5)
                        if not board_check[row][col]
                    ]
                )

                print(k, "=>", sum_unmarkeds * n)
