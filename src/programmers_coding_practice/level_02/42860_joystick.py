"""
[LINK] https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
[REF] https://bellog.tistory.com/152
[REF] https://velog.io/@jeeseob5761/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
[REF] https://whwl.tistory.com/93
[TITLE] 조이스틱
"""


def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1

    if min_move > 0:
        for idx, each in enumerate(name):
            # 위, 아래 조작 횟수의 최솟값
            answer += min(ord(each) - ord('A'), ord('Z') - ord(each) + 1)

            # 좌, 우 조작 횟수의 최솟값
            next = idx + 1
            while next < len(name) and name[next] == 'A':
                next += 1

            # 한 방향으로만 이동하는 경우, 오른쪽 이동 후 왼쪽으로 이동하는 경우
            min_move = min(min_move, idx + idx + len(name) - next)

            # 처음부터 뒷부분을 먼저 입력하는 것이 더 빠른 경우
            min_move =min(min_move, (len(name) - next) * 2 + idx)

    answer += min_move
    return answer


def solution2(name):
    # 위, 아래 조작 횟수의 최솟값
    moves = [ min(ord(each) - ord('A'), ord('Z') - ord(each) + 1) for each in name ]
    pos = 0
    answer = 0

    while True:
        answer += moves[pos]
        moves[pos] = 0

        if sum(moves) == 0:
            break

        # 좌, 우 조작 횟수 구하기
        left, right = 1, 1
        while moves[pos - left] == 0:
            left += 1
        while moves[pos + right] == 0:
            right += 1

        # 현재 위치 조정
        if left > right:
            answer += right
            pos += right
        else:
            answer += left
            pos -= left

    return answer


def main():
    # name = "JAN"        # return 23
    name = "JEROEN"     # return 56

    print(solution(name))
    # print(solution2(name))    # solution2는 2022년 버전은 해당 안됨


###
main()
