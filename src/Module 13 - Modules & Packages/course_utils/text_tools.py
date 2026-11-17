"""Text helpers for the course_utils package."""


def normalize_name(name):
    """Strip surrounding whitespace and capitalize each name part."""
    return " ".join(part.capitalize() for part in name.split())


def count_words(text):
    """Return the number of whitespace-separated words in text."""
    return len(text.split())
