from logic_utils import check_guess, parse_guess, get_range_for_difficulty


def test_winning_guess():
    result = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_valid_guess():
    ok, guess, error = parse_guess("58")
    assert ok is True
    assert guess == 58
    assert error is None


def test_parse_blank_guess():
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."


def test_parse_non_number_guess():
    ok, guess, error = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."


def test_normal_difficulty_range():
    assert get_range_for_difficulty("Normal") == (1, 100)