import sys
from collections import Counter

input = sys.stdin.readline

# 단어 저장
words_list = []

# 단어 추가 함수
def add_word(word):
    words_list.append(Counter(word))

# 퍼즐로 단어를 만들 수 있는지 확인
def can_make_word(puzzle_counter, word_counter):
    return all(word_counter[char] <= puzzle_counter.get(char, 0) for char in word_counter)

# 결과 출력 함수
def print_answer(puzzle_count):
    sorted_counts = sorted(puzzle_count.items(), key=lambda x: (x[1], x[0]))
    
    # 최소, 최대값 및 해당 알파벳 추출
    min_count = sorted_counts[0][1]
    max_count = sorted_counts[-1][1]
    
    min_alpha = ''.join([char for char, count in sorted_counts if count == min_count])
    max_alpha = ''.join([char for char, count in sorted_counts if count == max_count])
    
    print(min_alpha, min_count, max_alpha, max_count)

# 단어 입력 처리
while True:
    word = input().strip()
    if word == "-":
        break
    add_word(word)

# 퍼즐 입력 처리
while True:
    puzzle = input().strip()
    if puzzle == "#":
        break

    # 퍼즐 빈도 계산
    puzzle_counter = Counter(puzzle)
    puzzle_count = {char: 0 for char in puzzle_counter.keys()}
    
    for word_counter in words_list:
        if can_make_word(puzzle_counter, word_counter):
            for char in word_counter:
                if char in puzzle_count:
                    puzzle_count[char] += 1

    # 결과 출력
    print_answer(puzzle_count)
