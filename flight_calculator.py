"""Utilities for estimating an e-bike or drone payload's active flight time."""


def calculate_flight_time(weight_grams: float) -> float:
    """Return active flight time in minutes for a payload weight.

    Args:
        weight_grams: Payload weight in grams; it must be non-negative.

    Returns:
        The active flight time in minutes, floored at zero.

    Raises:
        ValueError: If ``weight_grams`` is negative.
    """
    if weight_grams < 0:
        raise ValueError("Payload weight must be non-negative.")

    # Copilot suggested the linear formula; edited it to enforce the zero floor.
    return max(0, 180 - 0.1 * weight_grams)


def flight_time_table(
    max_weight_grams: float, step_grams: float
) -> list[tuple[float, float]]:
    """Return flight-time pairs from zero through a maximum payload weight.

    Args:
        max_weight_grams: Largest payload weight to include; it must be non-negative.
        step_grams: Positive increment between payload weights.

    Returns:
        A list of ``(weight, flight_time)`` pairs.

    Raises:
        ValueError: If the maximum weight is negative or the step is not positive.
    """
    if max_weight_grams < 0:
        raise ValueError("Maximum payload weight must be non-negative.")
    if step_grams <= 0:
        raise ValueError("Weight step must be positive.")

    table = []
    weight = 0.0
    while weight <= max_weight_grams:
        table.append((weight, calculate_flight_time(weight)))
        weight += step_grams
    return table

