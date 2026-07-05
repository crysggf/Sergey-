def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


result = is_year_leap(2024)
print(f'год {2024}: {result}')
