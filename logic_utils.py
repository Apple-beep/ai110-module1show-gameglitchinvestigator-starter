def get_range_for_difficulty(difficulty: str):
    """
    Return the inclusive number range for a selected difficulty.

    Args:
        difficulty: The difficulty label selected in the Streamlit sidebar.

    Returns:
        A tuple containing the lowest and highest valid guesses.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Convert raw user input into an integer guess.

    Args:
        raw: Text entered by the user in the guess input field.

    Returns:
        A tuple of (ok, guess_int, error_message). If parsing succeeds,
        ok is True, guess_int contains the parsed integer, and error_message
        is None. If parsing fails, ok is False and error_message explains why.
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def is_guess_in_range(guess: int, low: int, high: int):
    """
    Check whether a guess is inside the active difficulty range.

    Args:
        guess: The parsed integer guess.
        low: The lowest allowed value.
        high: The highest allowed value.

    Returns:
        True if the guess is inside the range, otherwise False.
    """
    return low <= guess <= high


def check_guess(guess, secret):
    """
    Compare a guess against the secret number.

    Args:
        guess: The user's guess.
        secret: The secret number.

    Returns:
        "Win" when the guess matches the secret, "Too High" when the guess
        is above the secret, and "Too Low" when the guess is below the secret.
    """
    try:
        guess_value = int(guess)
        secret_value = int(secret)
    except Exception:
        guess_value = str(guess)
        secret_value = str(secret)

    if guess_value == secret_value:
        return "Win"

    if guess_value > secret_value:
        return "Too High"

    return "Too Low"


def hint_for_outcome(outcome: str):
    """
    Return a player-facing hint message for a guess outcome.

    Args:
        outcome: The result returned by check_guess.

    Returns:
        A short hint message shown in the Streamlit app.
    """
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Too high! Go LOWER."
    if outcome == "Too Low":
        return "📈 Too low! Go HIGHER."
    return ""


def get_distance_label(guess: int, secret: int):
    """
    Return a hot/cold style hint based on distance from the secret number.

    Args:
        guess: The user's valid guess.
        secret: The secret number.

    Returns:
        A short label describing how close the guess is.
    """
    distance = abs(guess - secret)

    if distance == 0:
        return "🎯 Exact"
    if distance <= 3:
        return "🔥 Very close"
    if distance <= 10:
        return "🌡️ Warm"
    if distance <= 25:
        return "🧊 Cold"

    return "🥶 Very cold"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update the player's score after a valid guess.

    Args:
        current_score: The score before the current guess.
        outcome: The result returned by check_guess.
        attempt_number: The current valid attempt count.

    Returns:
        The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score