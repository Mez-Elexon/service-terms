"""Layout helper: stack a long expression's top-level clauses so it fits a page.

Clauses separated by a top-level \\qquad (outside braces and environments) become lines of a
`gathered` block. Expressions that already use an environment are left as written.
"""
import re


def top_level_split(tex, sep=r"\qquad"):
    parts, depth, i, start = [], 0, 0, 0
    env = 0
    while i < len(tex):
        if tex.startswith(r"\begin", i):
            env += 1
        elif tex.startswith(r"\end", i):
            env -= 1
        ch = tex[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif depth == 0 and env == 0 and tex.startswith(sep, i):
            parts.append(tex[start:i]); i += len(sep); start = i; continue
        i += 1
    parts.append(tex[start:])
    return [p.strip().rstrip(",;").strip() for p in parts if p.strip()]


def stacked(tex):
    """Return the expression with top-level \\qquad clauses on separate lines."""
    if r"\begin" in tex:
        return tex
    parts = top_level_split(tex)
    if len(parts) < 2:
        return tex
    return "\\begin{gathered}\n" + " \\\\\n".join(parts) + "\n\\end{gathered}"
