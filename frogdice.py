#!/usr/bin/env python3
"""Roll a set of dice and report the results.

This utility is intentionally small and focused, serving as a simple example
script for this repo.
"""

from __future__ import annotations

import argparse
import random
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class RollResult:
    rolls: list[int]

    @property
    def total(self) -> int:
        return sum(self.rolls)


def roll_dice(count: int, sides: int) -> RollResult:
    rolls = [random.randint(1, sides) for _ in range(count)]
    return RollResult(rolls=rolls)


def format_result(result: RollResult) -> str:
    roll_text = " ".join(str(roll) for roll in result.rolls)
    return f"Rolls: {roll_text} (total {result.total})"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Roll a set of dice and print the results.",
    )
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=2,
        help="Number of dice to roll (default: 2).",
    )
    parser.add_argument(
        "sides",
        nargs="?",
        type=int,
        default=6,
        help="Number of sides on each die (default: 6).",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.count < 1:
        raise SystemExit("count must be at least 1")
    if args.sides < 2:
        raise SystemExit("sides must be at least 2")
    result = roll_dice(args.count, args.sides)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
