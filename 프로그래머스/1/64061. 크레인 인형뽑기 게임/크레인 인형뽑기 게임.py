def solution(board, moves):
    # 사라진 인형 개수
    answer = 0
    
    # 인형을 꺼내기 쉽도록 배열 재배치
    n,m = len(board), len(board[0])
    new_board = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if board[n-i-1][j] != 0:
                new_board[j].append(board[n-i-1][j])
    
    
    # 인형 뽑기 시작
    bag = []
    for move in moves:
        move -= 1
        if new_board[move]:
            x = new_board[move].pop()
            if bag and bag[-1] == x:
                bag.pop()
                answer += 2
            else:
                bag.append(x)

    return answer