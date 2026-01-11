# `sys` provides access to interpreter resources (e.g. `stdin`, `stdout`).
# Iterating `sys.stdin` reads lines until end-of-file (EOF), so the loop ends when input is finished.

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b = map(int, line.split())
    print(abs(a - b))