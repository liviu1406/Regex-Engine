def get_percentage(number, round_digits=None):
    perc = number * 100
    if round_digits is None:
        return f'{round(perc)}%'
    else:
        return f'{round(perc, round_digits)}%'


# print(get_percentage(0.0123, 10))
