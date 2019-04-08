# -*- coding:utf-8 -*-


def build_bad_char_map(pattern_s, sz=256):
    bcmap = [-1] * sz
    for i,s in enumerate(pattern_s):
        bcmap[ord(s)] = i
    return bcmap

def build_good_suffix_prefix_map(pattern_s):
    m = len(pattern_s)
    prefix, suffix = [False] * m, [-1] * m
    for i in range(m - 1):
        j = i
        k = 0
        while j >= 0 and pattern_s[j] == pattern_s[m - k - 1]:
            k += 1
            suffix[k] = j
            j -= 1
        if j < 0:
            prefix[k] = True
    return prefix, suffix
           
def move_forward_by_gsp(bc_p, m, suffix, prefix):
    k = m - 1 - j
    if suffix[k] != -1:
        return j - suffix[k] + 1
    r = j + 2
    while r < m:
        if prefix[m - r] == True:
            return r


def bm(string, pattern_s):
    m = len(pattern_s)
    n = len(string)
    step_num = n - m + 1
    bcmap = build_bad_char_map(pattern_s)
    prefix, suffix = build_good_suffix_prefix_map(pattern_s)
    i = 0
    while i < step_num:
        j = m - 1
        while j >= 0 and string[i + j] == pattern_s[j]:
            j -= 1
        if j < 0:
            return i
        x = (j - bcmap[ord(string[i + j])])
        y = 0
        if j < (m - 1):
            y = move_forward_by_gsp(j, m, suffix, prefix)
        i += max(x, y)
    return -1

if __name__ == '__main__':
    string = "hello world! today is not my day"
    ps = 'today'
    print(string)
    print(len(string))
    print(bm(string, ps))


