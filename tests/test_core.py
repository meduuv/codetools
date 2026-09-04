from codetools import strip_comments, unique_lines


def test_unique_lines():
    assert unique_lines("a\nb\na") == "a\nb"


def test_strip_comments():
    assert strip_comments("x # note\ny") == "x\ny"
