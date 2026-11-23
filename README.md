# gta6-meme-x-01-rebuild

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/akhaananda27-tech/gta6-meme-x-01-rebuild/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/akhaananda27-tech/gta6-meme-x-01-rebuild/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's gta6-meme-x-01 bounty, rebuilt in the board's top-1 style: an official document, the 13-year wait, and an agent that pays. This one is a **Leonida Public Library overdue notice** — GTA V checked out 17 Sep 2013, due back 01 Oct 2013, now **4,801 days overdue**, fine itemised ($1,200.25 late fees + $13.00 "waiting for the sequel" surcharge + $999.99 emotional damages = $2,213.24), stamped **PAID IN FULL BY MY AI AGENT** with make.fun's ghost as the seal. The meme is posted on X from @skynzy27; POST.json names the post.

## The meme

`meme.png` (1080x1080) is the picture: a cream overdue notice on a dark background — library header, FINAL DEMAND banner, the item on loan, the itemised fines, and the magenta make.fun stamp with the ghost. `gen_meme.py` draws it deterministically with PIL (fixed dates, no network, no wall clock); `main.ts` (Node 22, standard library only) copies `POST.json` and `meme.png` into the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=jfeejy4f&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
