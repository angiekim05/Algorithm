def solution(video_len, pos, op_start, op_end, commands):    
    def prev(t):
        return max(0, t-10)
    
    def post(t):
        return min(video_len, t+10)
    
    def jump(t):
        if op_start <= t <= op_end:
            return op_end
        return t
    
    def s2t(s):
        mm,ss = map(int,s.split(":"))
        return mm*60+ss
    
    def t2s(t):
        mm,ss = divmod(t,60)
        return f'{mm:02d}:{ss:02d}'
    
    
    video_len, pos, op_start, op_end = map(s2t,[video_len, pos, op_start, op_end])
    pos = jump(pos)
    for command in commands:
        if command == "prev":
            pos = prev(pos)
        else:
            pos = post(pos)
        pos = jump(pos)
            
    answer = t2s(pos)
    return answer