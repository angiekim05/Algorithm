def solution(k, room_number):
    answer = []
    next_room = dict()
    for x in room_number:
        if x not in next_room:
            next_room[x] = x+1
            answer.append(x)
        else:
            temp = []
            while x in next_room:
                temp.append(x)
                x = next_room[x]
            next_room[x] = x+1
            answer.append(x)
            for t in temp:
                next_room[t] = x+1
    return answer