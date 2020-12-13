# working with recursion is memory intensive, python has built-in
# limit, so we set this limit higher
import sys

sys.setrecursionlimit(10000)

reg_, test = input().split('|')


# compare a single character
def compare_char(reg, str_) -> bool:
    return reg == str_ or bool(reg == '.' and str_) or not reg


# compare two strings of equal length
def compare_string(reg, str_) -> bool:
    if not reg or (reg == '$' and not str_):  # check for end-pattern '$'
        return True
    elif not str_:
        return False

    # '?' zero or one wildcard
    elif len(reg) > 1 and reg[1] == '?' and reg[0] != '\\':
        return compare_string(reg[2:], str_) or compare_string(reg[2:], str_[1:])

    # '*' zero or more wildcard
    elif len(reg) > 1 and reg[1] == '*' and reg[0] != '\\':
        return compare_string(reg[2:], str_) or compare_string(reg, str_[1:])

    # '+' one ore more wildcard
    elif len(reg) > 1 and reg[1] == '+' and reg[0] != '\\':
        return compare_string(reg.replace('+', '*', 1), str_[1:])

    # regular character comparison
    elif compare_char(reg[0], str_[0]):
        return compare_string(reg[1:].strip('\\'), str_[1:])
    else:
        return False


# compare regex with longer strings
def regex(reg, str_) -> bool:
    if not reg:
        return True
    elif not str_:
        return False
    elif reg[0] == '^':  # check for begin-pattern '^'
        return compare_string(reg[1:].strip('\\'), str_)
    elif compare_string(reg.strip('\\'), str_):
        return True
    else:
        return regex(reg.strip('\\'), str_[1:])


print(regex(reg_, test))
