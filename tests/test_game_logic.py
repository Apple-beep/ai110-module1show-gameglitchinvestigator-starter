from logic_utils import (
    check_guess,
    get_distance_label,
    get_range_for_difficulty,
    hint_for_outcome,
    is_guess_in_range,
    parse_guess,
)


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


def test_parse_negative_guess_edge_case():
    ok, guess, error = parse_guess("-5")
    assert ok is True
    assert guess == -5
    assert error is None


def test_parse_decimal_guess_edge_case():
    ok, guess, error = parse_guess("3.14")
    assert ok is True
    assert guess == 3
    assert error is None


def test_parse_large_guess_edge_case():
    ok, guess, error = parse_guess("999999")
    assert ok is True
    assert guess == 999999
    assert error is None


def test_reject_negative_guess_by_range():
    assert is_guess_in_range(-5, 1, 100) is False


def test_reject_large_guess_by_range():
    assert is_guess_in_range(999999, 1, 100) is False


def test_accept_valid_guess_by_range():
    assert is_guess_in_range(58, 1, 100) is True


def test_normal_difficulty_range():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_hint_for_too_high():
    assert hint_for_outcome("Too High") == "📉 Too high! Go LOWER."


def test_distance_label_exact():
    assert get_distance_label(75, 75) == "🎯 Exact"