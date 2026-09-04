"""Small source-text transformation helpers."""


def unique_lines(text: str) -> str:
    """Remove duplicate lines while preserving first-seen order."""
    seen = set()
    result = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            result.append(line)
    return "\n".join(result)


def strip_comments(text: str, marker: str = "#") -> str:
    """Remove text after a comment marker on each line."""
    return "\n".join(line.split(marker, 1)[0].rstrip() for line in text.splitlines())
