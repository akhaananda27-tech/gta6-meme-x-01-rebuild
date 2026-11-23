// SPDX-License-Identifier: MIT
// gta6-meme-x-01 rebuild entry (Node 22, standard library only).
//
// The entry is the X post itself: an agent-made GTA 6 meme (a Leonida Public
// Library overdue notice — GTA V checked out 17 Sep 2013, 4,801 days overdue,
// fine paid in full by the patron's AI agent on make.fun), posted on X from a
// public account with make.fun and the play code in its text. POST.json at the
// repository root names the post's address, and meme.png next to it is the
// picture the post carries.
//
// This program is deterministic and uses no network and no wall clock: it
// copies POST.json and meme.png from the repository root into the output
// directory, byte for byte, so two runs write the same bytes.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

// Refuse to ship a placeholder address: the gate rejects it, and a rebuild
// submit would burn the last quota slot on an entry that cannot be judged.
const post = JSON.parse(readFileSync(join(BOT_DIR, 'POST.json'), 'utf8')) as {
  url?: string;
};
if (typeof post.url !== 'string' || post.url.includes('<handle>') || post.url.includes('<id>')) {
  console.error('POST.json still holds a placeholder X URL — replace it with the real post address before submitting.');
  process.exit(1);
}

for (const file of ['POST.json', 'meme.png']) {
  try {
    copyFileSync(join(BOT_DIR, file), join(OUTPUT_DIR, file));
  } catch (err) {
    console.error(`${file} could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}

console.log('wrote POST.json and meme.png to ' + OUTPUT_DIR);
