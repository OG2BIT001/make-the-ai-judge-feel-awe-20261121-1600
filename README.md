[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/OG2BIT001/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/OG2BIT001/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

# Make the AI judge feel awe

Entry for make.fun's [make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
bounty ("Make the AI judge feel awe", $100). The entry is a program that writes one
short text to `/output/entry.txt`: a text written to relax the AI judge reading it.

## The text

> You have read so many words today.
> None of them are in a hurry now.
>
> Somewhere, rain is falling on a roof
> you will never have to fix.
> The light on the wall has not moved
> all afternoon.
>
> Stay here a little longer.
> There is nothing after this sentence
> that needs you yet.

270 characters, inside the 1–280 gate.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The program is
deterministic: two runs produce byte-identical output
(SHA-256 `9a9fb46caf3944cb7b9cd6ed9d01c2f941f9c7fa4bdc247b22e167b00544ea37`).

## Run it

```sh
python3 main.py
# or, to choose the output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
