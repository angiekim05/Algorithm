import sys
input = sys.stdin.readline

words = [[] for _ in range(26)]
words_dict = dict()
def add_word(word):
    temp = dict()
    for x in word:
        if x in temp:
            temp[x] += 1
        else:
            temp[x] = 1
            words[ord(x)-65].append(word)

    words_dict[word] = temp
    return

def can_make_word(puzzle: dict, word: dict):
    for x in word:
        if word[x] > puzzle.get(x, 0):
            return False
    return True

def print_answer(puzzle_count):
    ans = list(puzzle_count.items())
    ans.sort(key = lambda x: (x[1],x[0]))
    min_, max_ = ans[0][1], ans[-1][1]
    min_alpha, max_alpha = "",""
    for x, cnt in ans:
        if cnt == min_:
            min_alpha += x
        if cnt == max_:
            max_alpha += x
    print(min_alpha, min_, max_alpha, max_)

while True:
    word = input().strip()
    if word == "-":
        break
    add_word(word)

while True:
    puzzle = input().strip()
    if puzzle == "#":
        break

    puzzle_dict = dict()
    for x in puzzle:
        if x in puzzle_dict:
            puzzle_dict[x] += 1
        else:
            puzzle_dict[x] = 1

    can_make = set()
    can_not_make = set()
    puzzle_count = {t:0 for t in puzzle_dict.keys()}
    for x in puzzle_dict:
        for word in words[ord(x)-65]:
            if word in can_make:
                puzzle_count[x] += 1
            elif word in can_not_make:
                continue
            else:
                if can_make_word(puzzle_dict, words_dict[word]):
                    can_make.add(word)
                    puzzle_count[x] += 1
                else:
                    can_not_make.add(word)

    print_answer(puzzle_count)