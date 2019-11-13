import string

BASE_LIST = string.digits + string.ascii_letters
BASE_DICT = dict((c, i) for i, c in enumerate(BASE_LIST))


def base_decode(encoded):
    length = len(BASE_DICT)
    ret = 0
    for i, c in enumerate(encoded[::-1]):
        ret += (length ** i) * BASE_DICT[c]

    return ret


def base_encode(integer):
    if integer == 0:
        return BASE_LIST[0]

    length = len(BASE_LIST)
    ret = ''
    while integer != 0:
        ret = BASE_LIST[integer % length] + ret
        integer //= length

    return ret
