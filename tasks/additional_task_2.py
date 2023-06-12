from typing import Optional, Tuple

Requirement = Optional[Tuple[int, Optional[int]]]


# Необходимо реализовать функцию, которая генерирует случайный пароль по заданным параметрам:
# min_length - минимальная длина пароля;
# digits - опциональный параметр, минимальное и максимальное (опционально) число цифровых значений;
# lower - опциональный параметр, минимальное и максимальное (опционально) число строчных букв;
# upper - опциональный параметр, минимальное и максимальное (опционально) число прописных букв;
# special - опциональный параметр, минимальное и максимальное (опционально) число специальных символов;
def construct_password(min_length: int, /, digits: Requirement = None, lower: Requirement = None,
                       upper: Requirement = None, special: Requirement = None) -> str:
    return ''
