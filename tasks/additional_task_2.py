# from typing import Optional, Tuple
#
# Requirement = Optional[Tuple[int, Optional[int]]]
#
#
# # Необходимо реализовать функцию, которая генерирует случайный пароль по заданным параметрам:
# # min_length - минимальная длина пароля;
# # digits - опциональный параметр, минимальное и максимальное (опционально) число цифровых значений;
# # lower - опциональный параметр, минимальное и максимальное (опционально) число строчных букв;
# # upper - опциональный параметр, минимальное и максимальное (опционально) число прописных букв;
# # special - опциональный параметр, минимальное и максимальное (опционально) число специальных символов;
# def construct_password(min_length: int, /, digits: Requirement = None, lower: Requirement = None,
#                        upper: Requirement = None, special: Requirement = None) -> str:
#     return ''

import random
import string
from typing import Optional, Tuple

Requirement = Optional[Tuple[int, Optional[int]]]


def generate_chars(charset: str, count: int) -> str:
    return ''.join(random.choice(charset) for i in range(count))

def construct_password(min_length: int, digits: Requirement = None, lower: Requirement = None,
                       upper: Requirement = None, special: Requirement = None) -> str:
    password = ''

    if digits:
        digit_count = random.randint(digits[0], digits[1] or digits[0])
        password += generate_chars(string.digits, digit_count)

    if lower:
        lower_count = random.randint(lower[0], lower[1] or lower[0])
        password += generate_chars(string.ascii_lowercase, lower_count)

    if upper:
        upper_count = random.randint(upper[0], upper[1] or upper[0])
        password += generate_chars(string.ascii_uppercase, upper_count)

    if special:
        special_count = random.randint(special[0], special[1] or special[0])
        password += generate_chars(string.punctuation, special_count)

    remaining_length = max(min_length - len(password), 0)
    password += generate_chars(string.ascii_letters + string.digits + string.punctuation, remaining_length)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

password = construct_password(
    min_length=8,
    digits=(2, 4),
    lower=(1, 3),
    upper=(1, 2),
    special=(1, 2)
)

print(password)
