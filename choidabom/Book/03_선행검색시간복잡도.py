def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while  i < n:
        if a[i] == key:
            return i    # 검색에 성공하여 인덱스를 반환
        i += 1
    return -1   # 검색에 실패하여 -1을 반환