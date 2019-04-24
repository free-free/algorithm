# -*- coding:utf-8 -*-


def rk(main, pattern, multi=False):
    """
        @param:
            main: str, input string
            pattern: str,  pattern string
            multi: bool, multi position searching
        @return:
            idxs: list, idxs of where pattern string match with main string

    """
    n, m = len(main), len(pattern)
    idxs = []
    if n < m:
        return idxs
    unique_chrs = set(main)
    unique_chr_num = len(unique_chrs)
    chr_map = {char : idx for idx, char in enumerate(unique_chrs)}
    precompute_power = {val: unique_chr_num ** val 
            for val in range(m)}
    pttrn_hash = sum([precompute_power[idx] * chr_map[char] 
        for idx, char in enumerate(pattern[::-1])])
    pre_hash = sum([precompute_power[idx] *  chr_map[char]
        for idx , char in enumerate(main[:m][::-1])])
    if pre_hash == pttrn_hash:
        idxs = [0]
        return idxs
    for i in range(1, n - m + 1):
        pre_char = main[i - 1]
        chr_hash = (pre_hash - chr_map[pre_char] * precompute_power[m - 1]) * \
                unique_chr_num + chr_map[main[i + m -1]]
        if chr_hash == pttrn_hash:
            idxs.append(i)
            if not multi:
                break
        pre_hash = chr_hash
    return idxs



if __name__ == '__main__':
    main = "我是hello 小明 world! This is the New life new life!"
    pattern = '小明'
    print(main)
    print(pattern)
    print(rk(main, pattern, True))
        
    
