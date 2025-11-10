def test1(s):
    """
    >>> test1("abcba")
    'Yes'
    >>> test1("Abcba")
    'Yes'
    >>> test1("123321")
    'No'
    >>> test1("a")
    'Yes'
    >>> test1("Ia,aI")
    'No'
    >>> test1("###")
    'No'
    >>> test1("2aa2")
    'No'
    """

    s1 = s.lower()
    s2 = s1[::-1]
    # 检查是否全部是字母
    if not s.isalpha():
        return 'No'
    else:
        if s1 == s2:
            return 'Yes'
        else:
            return 'No'

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)