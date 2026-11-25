# Make the AI Judge Laugh — one office joke

[![Make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/Vins1206/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/Vins1206/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [Make the AI Judge Laugh bounty on make.fun](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225).

## What it does

`main.py` (Python standard library only) writes exactly one line — a single
joke about office life, 82 characters — to `/output/entry.txt`:

> My boss calls it "a quick sync," the same way a dentist calls it "a little pinch."

The joke turns on the office's most familiar lie: a "quick sync" is never
quick, just as a dentist's "little pinch" never is. True to office life,
surprising in the last word, tight enough to read aloud in one breath.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

The program is deterministic: every run writes the same single line, with no
trailing newline, and checks the gate itself (1–200 characters, one line,
not blank) before writing.
