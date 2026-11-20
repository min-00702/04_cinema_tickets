import pytest

from src.cinema_price import ticket_price


# Requirement 3.1 (1): each ticket costs 1200 cents, total = ticket_count x 1200
@pytest.mark.parametrize("ticket_count, expected", [
    (1, 1200),        # boundary: smallest positive ticket count
    (2, 2400),
    (5, 6000),        # typical purchase
    (100, 120000),    # large purchase
])
def test_valid_ticket_count_returns_total_price_in_cents(ticket_count, expected):
    # Act
    result = ticket_price(ticket_count)

    # Assert
    assert result == expected


# Requirement 3.1 (2): zero tickets costs zero
def test_zero_tickets_returns_zero():
    # Arrange
    ticket_count = 0

    # Act
    result = ticket_price(ticket_count)

    # Assert
    assert result == 0


# Output: the total price is returned as a Python int (whole cents, no decimals)
def test_valid_ticket_count_returns_int():
    # Act
    result = ticket_price(3)

    # Assert
    assert type(result) is int


# General requirement 4: correct type (int) but outside the permitted range -> ValueError
@pytest.mark.parametrize("ticket_count", [
    -1,      # boundary: just below the smallest valid value (0)
    -100,    # far below the range
])
def test_negative_ticket_count_raises_value_error(ticket_count):
    # Act + Assert
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


# General requirements 2 and 3: input must be an int, bool is not a valid int -> TypeError
@pytest.mark.parametrize("ticket_count", [
    2.0,     # float that looks like a whole number
    2.5,     # float with decimals
    "2",     # string
    None,    # no value
    [2],     # list
    True,    # bool is not accepted as an int
    False,   # bool is not accepted as an int
])
def test_non_integer_ticket_count_raises_type_error(ticket_count):
    # Act + Assert
    with pytest.raises(TypeError):
        ticket_price(ticket_count)
