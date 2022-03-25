import re


def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace('.', '\.').replace('*', '.?').replace('?', '.')
    result = re.findall(pattern, filename)
    if len(result) != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # print("Example:")
    # print(unix_match("l.txt", "???*"))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert unix_match('somefile.txt', '*') == True
    # assert unix_match('other.exe', '*') == True
    # assert unix_match('my.exe', '*.txt') == False
    # assert unix_match('log1.txt', 'log?.txt') == True
    # assert unix_match('log12.txt', 'log?.txt') == False
    # assert unix_match('log12.txt', 'log??.txt') == True
    # assert unix_match("l.txt", "???*") == True
    assert unix_match("12apache1", "*.*") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
