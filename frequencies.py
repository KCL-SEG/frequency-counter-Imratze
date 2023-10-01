"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if isinstance(item, str):
            key = item
        else:
            key = str(item)

        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1

    return frequencies
