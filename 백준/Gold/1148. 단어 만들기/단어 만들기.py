# import sys
# input = sys.stdin.readline
#
# # 단어를 알파벳 빈도 리스트로 변환하여 저장
# def add_word(word):
#     temp = [0] * 26
#     for x in word:
#         temp[ord(x) - 65] += 1
#     words_list.append(temp)
#
# # 퍼즐로 단어를 만들 수 있는지 확인
# def can_make_word(puzzle, word):
#     for i in range(26):
#         if word[i] > puzzle[i]:
#             return False
#     return True
#
# # 결과 출력 함수
# def print_answer(puzzle_count):
#     ans = [(chr(i + 65), puzzle_count[i]) for i in range(26) if puzzle_count[i] > -1]
#     ans.sort(key=lambda x: (x[1], x[0]))  # 개수, 알파벳 순으로 정렬
#     min_, max_ = ans[0][1], ans[-1][1]
#     min_alpha = ''.join([x for x, cnt in ans if cnt == min_])
#     max_alpha = ''.join([x for x, cnt in ans if cnt == max_])
#     print(min_alpha, min_, max_alpha, max_)
#
# # 단어 입력 처리
# words_list = []
# words = set()
# while True:
#     word = input().strip()
#     if word == "-":
#         break
#     if word in words:
#         continue
#     add_word(word)
#
# # 퍼즐 입력 처리
# while True:
#     puzzle = input().strip()
#     if puzzle == "#":
#         break
#
#     # 퍼즐의 알파벳 빈도 리스트 생성
#     puzzle_alpha = [0] * 26
#     for x in puzzle:
#         puzzle_alpha[ord(x) - 65] += 1
#
#     # 퍼즐에 포함된 단어의 알파벳 개수 계산
#     puzzle_count = [0 if puzzle_alpha[i] else -1 for i in range(26)]
#     for word_ in words_list:
#         if can_make_word(puzzle_alpha, word_):
#             for i in range(26):
#                 if word_[i] > 0:
#                     puzzle_count[i] += 1
#
#     # 결과 출력
#     print_answer(puzzle_count)

import sys
input = sys.stdin.readline

words_dict = dict()
def add_word(word):
    temp = dict()
    for x in word:
        if x in temp:
            temp[x] += 1
        else:
            temp[x] = 1
    words_dict[word] = temp
    return

def can_make_word(puzzle, word):
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

    puzzle_count = {t:0 for t in puzzle_dict.keys()}
    for word_dict in words_dict.values():
        if can_make_word(puzzle_dict, word_dict):
            for x in word_dict:
                puzzle_count[x] += 1

    print_answer(puzzle_count)