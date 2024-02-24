def solution(board, h, w):
    answer = 0
    n = len(board)

    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr,nc = h+dr, w+dc
        if 0<=nr<n and 0<=nc<n and board[nr][nc] == board[h][w]:
            answer += 1
                
    return answer