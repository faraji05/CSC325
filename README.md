# Ebike & Flying Drone Travel-Time Calculator

This project models a commercial drone's active flight time as payload weight
increases. Standby time is not part of the calculation:

```text
flight time = 180 - (0.1 * payload weight in grams)
```

The result is never negative. Run the test suite with:

```bash
pytest
```

## AI-use disclosure

Used GitHub Copilot Chat (/tests) to generate the initial unit test skeletons
for `calculate_flight_time()`. Rewrote and added tests to cover the
negative-weight error case, the zero-flight boundary, and table validation.
Verified all tests pass with `pytest`.

