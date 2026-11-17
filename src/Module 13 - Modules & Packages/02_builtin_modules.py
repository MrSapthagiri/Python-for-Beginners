"""Demonstrate useful functions from math, random, and datetime."""

import math
import random
from datetime import date, datetime

# Module 13: Modules & Packages
# Topic 2: Python built-in modules
#
# These modules are included with Python and do not need to be installed.
# random is suitable for games and simulations, not security-sensitive data.


# Example 1: math provides constants and mathematical functions.
print("Example 1 - Circle circumference:", round(2 * math.pi * 3, 2))
print("Example 1 - Square root:", math.sqrt(144))
# Output: Example 1 - Circle circumference: 18.85
# Output: Example 1 - Square root: 12.0

# Example 2: random can choose from a sequence.
random.seed(12)
game_choice = random.choice(["rock", "paper", "scissors"])
print("Example 2 - Game choice is valid:", game_choice in {"rock", "paper", "scissors"})
# Output: Example 2 - Game choice is valid: True

# Example 3: random can generate an inclusive integer range.
die_roll = random.randint(1, 6)
print("Example 3 - Die roll is in range:", 1 <= die_roll <= 6)
# Output: Example 3 - Die roll is in range: True

# Example 4: datetime can create and format a date.
course_start = date(2026, 1, 15)
print("Example 4 - Formatted date:", course_start.strftime("%B %d, %Y"))
# Output: Example 4 - Formatted date: January 15, 2026

# Example 5: datetime can parse text into a date-time object.
meeting = datetime.strptime("2026-01-15 14:30", "%Y-%m-%d %H:%M")
print("Example 5 - Parsed hour:", meeting.hour)
# Output: Example 5 - Parsed hour: 14


# Quick review:
# - math: mathematical constants and operations.
# - random: pseudo-random values for non-security uses.
# - datetime: dates, times, parsing, and formatting.
