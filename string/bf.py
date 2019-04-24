# -*- coding:utf-8 -*-

def bf(string, pattern_s, multi=False):
    n, m = len(string), len(pattern_s)
    if n < m:
        return None
    idxs = []
    for i in range(n - m + 1):
        if string[i : i + m] == pattern_s:
            idxs.append(i)
            if not multi:
                break
    return idxs



if __name__ == '__main__':
    string = 'hello world! this is new life new life'
    pattern_s = 'new'
    print(string)
    print(pattern_s)
    print(bf(string, pattern_s, True))
