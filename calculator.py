"""Simple addition calculator module and CLI."""
from __future__ import annotations

import argparse
from typing import Sequence


def add_numbers(*numbers: float) -> float:
    """Return the sum of the provided numbers.

    Parameters
    ----------
    *numbers: float
        A variable number of numeric values to add together. Non-numeric
        arguments raise a ``TypeError``.

    Returns
    -------
    float
        The total of all provided numbers. If no numbers are supplied, ``0.0``
        is returned.
    """

    total = 0.0
    for value in numbers:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Unsupported value for addition: {value!r}")
        total += float(value)
    return total


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments for the calculator.

    Parameters
    ----------
    argv: Sequence[str] | None
        Optional list of arguments to parse (useful for testing). Defaults to
        ``None`` to parse arguments from ``sys.argv``.
    """

    parser = argparse.ArgumentParser(description="Add numbers together.")
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="Numbers to add together",
    )
    return parser.parse_args(args=argv)


def main(argv: Sequence[str] | None = None) -> str:
    """Compute a sum from CLI arguments and return a human-friendly message."""

    args = parse_arguments(argv)
    result = add_numbers(*args.numbers)
    return f"Sum: {result}"


if __name__ == "__main__":
    print(main())
