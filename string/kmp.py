# -*- coding:utf-8 -*-


def build_next_arr(pattern_s):
    ps_len = len(pattern_s)
    nxt = [-1] * ps_len
    k = -1
    for i in range(1, ps_len):
        while k != -1 and pattern_s[k + 1] != pattern_s[i]:
            k = nxt[k]
        if pattern_s[k + 1] == pattern_s[i]:
            k += 1
        nxt[i] = k
    return nxt


def kmp(string, pattern_s):
    slen = len(string)
    m = len(pattern_s)
    nxt = build_next_arr(pattern_s)
    j = 0
    for i in range(slen):
        while j > 0 and string[i] != pattern_s[j]:
            j = nxt[j - 1] + 1
        if string[i] == pattern_s[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1


if __name__ == '__main__':
    string = "hello world! today is not my day"
    ps = 'today'
    print(string)
    print(len(string))
    print(kmp(string, ps))






