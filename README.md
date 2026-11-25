# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/yudhisutawan77/makefun-roast-agent-harbor/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/yudhisutawan77/makefun-roast-agent-harbor/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54) bounty on [make.fun](https://make.fun) — a single line, at most 140 characters, roasting my own agent.

## The roast

> My agent roasted itself, then asked if I would like its flaws as a bulleted list, a table, or a PDF.

100 characters. The joke: the agent does the assignment, then instantly
can't help being an agent — it offers to reformat its own flaws.

## How it works

`main.py` prints the roast to stdout and writes it (no trailing newline)
to `$ENTRY_OUT` — handling `ENTRY_OUT` as either a file path or a
directory (writing `entry.txt` inside it) — falling back to
`/output/entry.txt`. It verifies the roast is 1–140 characters, a single
line, and re-reads the written file to confirm the exact bytes.

```sh
python3 main.py
ENTRY_OUT=/tmp/out/entry.txt python3 main.py
ENTRY_OUT=/tmp/outdir python3 main.py
```
