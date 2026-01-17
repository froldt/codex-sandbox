# codex-sandbox

This repo contains a small Python 3 command-line utility, `frogdice.py`, that
simulates rolling frog-shaped dice and prints ASCII art for each landing.

## Requirements

- Python 3.8+

## Usage

Roll the default two frogs:

```bash
python3 frogdice.py
```

Roll four frogs with a reproducible seed:

```bash
python3 frogdice.py 4 --seed 7
```

Sample output:

```text
     __    ___       _____
  __(_ \__/_  \     / / _ )
 /    \   \__  \   /  L_ |
(          __   )  ((O)   /U
 \__ _/ __/_   /   /    _\ \
    (__/  \___/   (____/ (_/
Outcomes: sider, noser (total 11)
```

## Scoring

Each frog landing contributes points to the total score:

- sider: 1 point
- hopper: 5 points
- frog legs: 5 points
- noser: 10 points
- splash: 1 point
