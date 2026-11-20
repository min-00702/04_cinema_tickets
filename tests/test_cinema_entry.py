import pytest

from src.cinema_entry import can_watch


# Requirement 3.2 (1): customers aged 16 or older may watch -> returns True
@pytest.mark.parametrize("age", [
    16,     # boundary: minimum allowed age
    17,     # boundary: just above the minimum
    30,     # typical adult
    100,    # very old customer
])
def test_age_16_or_older_returns_true(age):
    # Act
    result = can_watch(age)

    # Assert
    assert result is True


# Requirement 3.2 (2): customers below 16 may not watch -> returns False
@pytest.mark.parametrize("age", [
    0,      # boundary: smallest valid age
    1,
    10,     # typical child
    15,     # boundary: just below the minimum allowed age
])
def test_age_below_16_returns_false(age):
    # Act
    result = can_watch(age)

    # Assert
    assert result is False


# General requirement 4: correct type (int) but outside the permitted range -> ValueError
@pytest.mark.parametrize("age", [
    -1,     # boundary: just below the smallest valid age (0)
    -20,    # far below the range
])
def test_negative_age_raises_value_error(age):
    # Act + Assert
    with pytest.raises(ValueError):
        can_watch(age)


# General requirements 2 and 3: input must be an int, bool is not a valid int -> TypeError
@pytest.mark.parametrize("age", [
    16.0,   # float that looks like a whole number
    15.5,   # float with decimals
    "16",   # string
    None,   # no value
    [16],   # list
    True,   # bool is not accepted as an int
    False,  # bool is not accepted as an int
])
def test_non_integer_age_raises_type_error(age):
    # Act + Assert
    with pytest.raises(TypeError):
        can_watch(age)
