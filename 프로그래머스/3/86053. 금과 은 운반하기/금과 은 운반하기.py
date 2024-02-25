def solution(a, b, g, s, w, t):
    n = len(g)

    def can_get_intime(time):
        total_g = 0
        total_s = 0
        total = 0

        for i in range(n):
            k = mid // t[i]
            if k%2 == 0:
                k = k//2
            else:
                k = k//2+1
            can_get = w[i] * k
            total_g += min(g[i], can_get)
            total_s += min(s[i], can_get)
            total += min(g[i]+s[i], can_get)
        if total >= a + b and total_g >= a and total_s >= b:
            return True
        return False

    l = 0
    r = (2e9) * (2e5)  # 최악의 시간

    while l <= r:
        mid = (l + r) // 2

        if can_get_intime(mid):
            r = mid - 1
        else:
            l = mid + 1

    return l
