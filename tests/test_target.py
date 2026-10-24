import pytest

from target import is_adult


@pytest.mark.parametrize(
    "age, expected",
    [
        (0, False),
        (1, False),
        (17, False),
        (18, True),
        (19, True),
        (100, True),
    ],
)
def test_is_adult_valid_ages(age, expected):
    assert is_adult(age) is expected


def test_is_adult_negative_age():
    with pytest.raises(ValueError, match="age cannot be negative"):
        is_adult(-1)

from target import celsius_to_fahrenheit


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (25, 77.0),
        (37, 98.6),
        (12.345, 54.22),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    result = celsius_to_fahrenheit(celsius)

    assert result == expected
    assert isinstance(result, float)


from target import count_vowels


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("AEIOU", 5),
        ("Python", 1),
        ("rhythm", 0),
        ("", 0),
        ("Education", 5),
        ("Beautiful", 5),
        ("aAaEeIiOoUu", 11),
        ("hello world!", 3),
        ("12345", 0),
    ],
)
def test_count_vowels(text, expected):
    result = count_vowels(text)

    assert result == expected
    assert isinstance(result, int)


@pytest.mark.parametrize(
    "invalid_text",
    [None, 123, 12.5, True, ["hello"], {"text": "hello"}],
)
def test_count_vowels_invalid_type(invalid_text):
    with pytest.raises(TypeError, 
    match="text must be a string"):
        count_vowels(invalid_text)


from target import invert


@pytest.mark.parametrize(
    "flag, expected",
    [
        (True, False),
        (False, True),
    ],
)
def test_invert_valid_boolean(flag, expected):
    result = invert(flag)

    assert result is expected
    assert isinstance(result, bool)


@pytest.mark.parametrize(
    "invalid_flag",
    [0, 1, None, "True", "False", [], {}],
)
def test_invert_invalid_type(invalid_flag):
    with pytest.raises(TypeError, match="flag must be True or False"):
        invert(invalid_flag)

from target import greet


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Mehedi", "Hello, Mehedi!"),
        ("Alice", "Hello, Alice!"),
        (None, "Hello, Guest!"),
        ("", "Hello, Guest!"),
        ("   ", "Hello, Guest!"),
        ("\t", "Hello, Guest!"),
        ("\n", "Hello, Guest!"),
        ("  Mehedi  ", "Hello, Mehedi!"),
        ("0", "Hello, 0!"),
    ],
)
def test_greet(name, expected):
    assert greet(name) == expected


from target import find_max


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 3),
        ([3, 2, 1], 3),
        ([-10, -5, -20], -5),
        ([5], 5),
        ([4, 4, 4], 4),
        ([-1, 0, 1], 1),
        ([1.5, 3.7, 2.2], 3.7),
        ([100, -100, 0], 100),
    ],
)
def test_find_max_valid_lists(numbers, expected):
    assert find_max(numbers) == expected


def test_find_max_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        find_max([])

from target import get_price


@pytest.mark.parametrize(
    "prices, item, expected",
    [
        ({"apple": 10, "banana": 20}, "apple", 10),
        ({"apple": 10, "banana": 20}, "banana", 20),
        ({"laptop": 75000}, "laptop", 75000),
        ({"milk": 0}, "milk", 0),
        ({"apple": 10.5}, "apple", 10.5),
        ({1: 100, 2: 200}, 1, 100),
    ],
)
def test_get_price_existing_items(prices, item, expected):
    assert get_price(prices, item) == expected


def test_get_price_missing_item():
    prices = {"apple": 10, "banana": 20}

    with pytest.raises(KeyError, match="orange not found"):
        get_price(prices, "orange")


def test_get_price_empty_dictionary():
    with pytest.raises(KeyError, match="apple not found"):
        get_price({}, "apple")

from target import swap


@pytest.mark.parametrize(
    "pair, expected",
    [
        ((1, 2), (2, 1)),
        (("a", "b"), ("b", "a")),
        ((10, 20), (20, 10)),
        ((None, "hello"), ("hello", None)),
        ((1, 1), (1, 1)),
        ((1, "two"), ("two", 1)),
    ],
)
def test_swap_valid_pairs(pair, expected):
    result = swap(pair)

    assert result == expected
    assert isinstance(result, tuple)


@pytest.mark.parametrize(
    "pair",
    [
        (),
        (1,),
        (1, 2, 3),
        (1, 2, 3, 4),
    ],
)
def test_swap_invalid_length(pair):
    with pytest.raises(ValueError, match="pair must have exactly 2 values"):
        swap(pair)

from target import common_items


@pytest.mark.parametrize(
    "set_a, set_b, expected",
    [
        ({1, 2, 3}, {2, 3, 4}, {2, 3}),
        ({1, 2}, {3, 4}, set()),
        (set(), {1, 2}, set()),
        ({1, 2}, set(), set()),
        (set(), set(), set()),
        ({"apple", "banana"}, {"banana", "orange"}, {"banana"}),
        ({1}, {1}, {1}),
        ({-1, 0, 1}, {0, 1, 2}, {0, 1}),
    ],
)
def test_common_items(set_a, set_b, expected):
    result = common_items(set_a, set_b)

    assert result == expected
    assert isinstance(result, set)


from target import is_leap_year


@pytest.mark.parametrize(
    "year, expected",
    [
        (1, False),
        (4, True),
        (100, False),
        (400, True),
        (1900, False),
        (2000, True),
        (2023, False),
        (2024, True),
        (2100, False),
        (2400, True),
    ],
)
def test_is_leap_year_valid_years(year, expected):
    result = is_leap_year(year)

    assert result is expected
    assert isinstance(result, bool)


@pytest.mark.parametrize("year", [0, -1, -100])
def test_is_leap_year_invalid_years(year):
    with pytest.raises(ValueError, match="year must be 1 or more"):
        is_leap_year(year)


@pytest.mark.parametrize("year", ["2024", None])
def test_is_leap_year_invalid_types(year):
    with pytest.raises(TypeError):
        is_leap_year(year)


from target import to_int


@pytest.mark.parametrize(
    "value, expected",
    [
        ("10", 10),
        ("0", 0),
        ("-5", -5),
        (10, 10),
        (10.9, 10),
        (-3.8, -3),
        (0.0, 0),
        (" 25 ", 25),
      # handled separately below
    ],
)
def test_to_int_valid_values(value, expected):
    if isinstance(value, bool):
        with pytest.raises(TypeError, match="bool is not allowed"):
            to_int(value)
    else:
        result = to_int(value)
        assert result == expected
        assert isinstance(result, int)


@pytest.mark.parametrize("value", [True, False])
def test_to_int_rejects_booleans(value):
    with pytest.raises(TypeError, match="bool is not allowed"):
        to_int(value)


@pytest.mark.parametrize("value", [None, [], {}])
def test_to_int_invalid_types(value):
    with pytest.raises(TypeError):
        to_int(value)


@pytest.mark.parametrize("value", ["hello", "3.5", ""])
def test_to_int_invalid_strings(value):
    with pytest.raises(ValueError):
        to_int(value)

from target import divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (7, 2, 3.5),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
        (0, 5, 0.0),
        (5.5, 2, 2.75),
    ],
)
def test_divide_valid_values(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("b", [0, 0.0, False])
def test_divide_by_zero(b):
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        divide(10, b)

from target import power


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (5, 2, 25),
        (10, 0, 1),
        (2, 1, 2),
        (-2, 3, -8),
        (-2, 2, 4),
        (2, -2, 0.25),
        (0, 3, 0),
    ],
)
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected

from target import square_root


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0.0),
        (1, 1.0),
        (4, 2.0),
        (9, 3.0),
        (16, 4.0),
        (2, 2 ** 0.5),
        (0.25, 0.5),
    ],
)
def test_square_root_valid_values(x, expected):
    assert square_root(x) == pytest.approx(expected)


@pytest.mark.parametrize("x", [-1, -4, -0.25])
def test_square_root_negative_values(x):
    with pytest.raises(
        ValueError,
        match="cannot take the square root of a negative number",
    ):
        square_root(x)

from target import factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
        (6, 720),
    ],
)
def test_factorial_valid_values(n, expected):
    result = factorial(n)

    assert result == expected
    assert isinstance(result, int)


@pytest.mark.parametrize("n", [-1, -5, -10])
def test_factorial_negative_values(n):
    with pytest.raises(
        ValueError,
        match="factorial is not defined for negative numbers",
    ):
        factorial(n)

from target import average


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2.0),
        ([10, 20, 30], 20.0),
        ([5], 5.0),
        ([0, 0, 0], 0.0),
        ([-1, 0, 1], 0.0),
        ([-2, -4, -6], -4.0),
        ([1.5, 2.5, 3.0], 7 / 3),
        ([1, 2], 1.5),
    ],
)
def test_average_valid_values(numbers, expected):
    assert average(numbers) == pytest.approx(expected)


def test_average_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        average([])

