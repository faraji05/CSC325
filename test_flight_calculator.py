import pytest

from flight_calculator import calculate_flight_time, flight_time_table


def test_zero_payload_has_three_hours_of_active_flight_time():
    assert calculate_flight_time(0) == 180


def test_typical_payload_reduces_flight_time_linearly():
    assert calculate_flight_time(250) == 155


def test_payload_at_boundary_has_zero_flight_time():
    assert calculate_flight_time(1800) == 0


def test_payload_above_boundary_stays_at_zero():
    assert calculate_flight_time(2000) == 0


def test_negative_payload_raises_value_error():
    with pytest.raises(ValueError, match="non-negative"):
        calculate_flight_time(-1)


def test_flight_time_table_includes_zero_and_maximum_weight():
    assert flight_time_table(100, 50) == [(0.0, 180.0), (50.0, 175.0), (100.0, 170.0)]


def test_flight_time_table_rejects_invalid_step():
    with pytest.raises(ValueError, match="positive"):
        flight_time_table(100, 0)

