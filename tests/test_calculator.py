"""Unit tests for calculator module."""

from pathlib import Path
import sys

import pytest

# Ensure repository root is on the import path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from calculator import add_numbers, main, parse_arguments


def test_adds_multiple_values():
    assert add_numbers(1, 2, 3) == 6.0


def test_returns_zero_when_no_values():
    assert add_numbers() == 0.0


def test_raises_on_non_numeric():
    with pytest.raises(TypeError):
        add_numbers(1, "two")


def test_parse_arguments():
    args = parse_arguments(["1", "2.5", "3"])
    assert args.numbers == [1.0, 2.5, 3.0]


def test_main_returns_sum_message():
    message = main(["1", "2", "3"])
    assert message == "Sum: 6.0"
