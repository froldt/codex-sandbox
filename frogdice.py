#!/usr/bin/env python3
"""Roll frog dice and print ASCII art for each landing.

Each frog can land on one of several sides, and each result has an associated
score. The frog faces are rendered using ASCII art inspired by the original
Python 2 implementation.
"""

from __future__ import annotations

import argparse
import random
import sys
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class FrogOutcome:
    name: str
    points: int
    art: tuple[str, ...]


OUTCOMES: tuple[FrogOutcome, ...] = (
    FrogOutcome(
        name="sider",
        points=1,
        art=(
            "     __    ___",
            "  __(_ \\__/_  \\",
            " /    \\   \\__  \\",
            "(          __   )",
            " \\__ _/ __/_   /",
            "    (__/  \\___/",
        ),
    ),
    FrogOutcome(
        name="sider",
        points=1,
        art=(
            "   ___    __",
            "  /  _\\__/ _)__",
            " /    /   /    \\",
            "(               )",
            " \\   _\\__ \\_ __/",
            "  \\___/  \\__)",
        ),
    ),
    FrogOutcome(
        name="hopper",
        points=5,
        art=(
            " _((O)",
            "(_    \\_______",
            "  \\           \\",
            "   \\ \\ \\   /   )",
            "    -/ /--(  _/",
            "   ((_/ ((__/",
        ),
    ),
    FrogOutcome(
        name="frog legs",
        points=5,
        art=(
            "  _/   )) / ))",
            " /    )--/ /-",
            "(    /   \\ \\ ",
            " \\________    \\_",
            "          \\    _)",
            "           (0))",
        ),
    ),
    FrogOutcome(
        name="noser",
        points=10,
        art=(
            "       _____",
            "      / / _ )",
            "     /  L_ |",
            "  ((O)   /U",
            " /    _\\ \\",
            "(____/ (_/",
        ),
    ),
    FrogOutcome(
        name="splash",
        points=1,
        art=(
            " ____    )))  __",
            "(_  _\\__(((__/ _)__",
            "  /  /   )))  /    \\",
            " (      (((         )",
            " _\\ _\\___)))_ \\_ __/",
            "(____/  (((  \\__)",
        ),
    ),
)


@dataclass(frozen=True)
class FrogRoll:
    outcome: FrogOutcome


@dataclass(frozen=True)
class RollResult:
    rolls: tuple[FrogRoll, ...]

    @property
    def total(self) -> int:
        return sum(roll.outcome.points for roll in self.rolls)


def pick_outcome(rng: random.Random) -> FrogOutcome:
    return rng.choice(OUTCOMES)


def roll_frogs(count: int, rng: random.Random) -> RollResult:
    return RollResult(tuple(FrogRoll(pick_outcome(rng)) for _ in range(count)))


def format_summary(result: RollResult) -> str:
    names = ", ".join(roll.outcome.name for roll in result.rolls)
    return f"Outcomes: {names} (total {result.total})"


def render_rolls(result: RollResult) -> list[str]:
    art_lines = [roll.outcome.art for roll in result.rolls]
    if not art_lines:
        return []
    combined: list[str] = []
    for rows in zip(*art_lines):
        combined.append("   ".join(rows))
    return combined


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Roll frog dice and show ASCII art for each landing.",
    )
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=2,
        help="Number of frogs to roll (default: 2).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Optional random seed for reproducible rolls.",
    )
    return parser.parse_args(argv)


def validate_count(count: int) -> None:
    if count < 1:
        raise SystemExit("count must be at least 1")


def print_lines(lines: Iterable[str]) -> None:
    for line in lines:
        print(line)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    validate_count(args.count)
    rng = random.Random(args.seed)
    result = roll_frogs(args.count, rng)
    print_lines(render_rolls(result))
    print(format_summary(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
