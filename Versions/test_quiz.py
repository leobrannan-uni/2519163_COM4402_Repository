# Collects function from python file to test.
from quiz import is_correct


# Sets up a test environment where the choice is correct- to see if score is added.
def test_is_correct_true():
    score = is_correct(choice=2, correct_answers=2, score=0)
    assert score == 1


# Sets up a test environment where the choice is incorrect- to see if score is left untouched.
def test_is_correct_false():
    score = is_correct(choice=1, correct_answers=2, score=0)
    assert score == 0