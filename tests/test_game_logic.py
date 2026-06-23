import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, parse_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_high_guess_says_go_lower():
    outcome, message = check_guess(50, 30)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_low_guess_says_go_higher():
    outcome, message = check_guess(20, 30)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_out_of_range_rejected():
    ok, value, err = parse_guess("1000", low=1, high=100)
    assert not ok
    assert value is None
    assert "Out of range" in err
