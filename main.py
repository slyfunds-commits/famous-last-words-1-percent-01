"""Famous Last Words at 1 Percent — R1 entry.

The phone speaks in first person about its own dying battery. The keeper
spends its last percent on a goodbye instead of the owner's alarm — the
spending IS the death (P1 self-sealing) and the sacrifice is the cost
(self-sacrifice in machine vocabulary, the Pickup Lines winning device).
The last beat, "Sleep in.", redefines the goodbye: no alarm, so the owner
oversleeps. The reader completes it.

Gate analysis (judge-list-max, full pass recorded in
famous-last-words-1-percent-01-candidates.md): subject gate first beat;
fresh premise (alarm-sacrifice, not a circulating joke); reversal — "Sleep
in." redefines the goodbye; re-read — the alarm is named in beat 1;
action-at-a-cost — the phone gives up its last useful function; second
beat — "Sleep in." is blessing and threat at once; economy — 93 chars,
punch in the last 2 words; truth — true in the fiction, no invented
number. NOT a will reading, NOT a goodbye to the charger, NOT a "1
percent" pun, NOT a low-power-mode joke.
"""

import os
import sys

ENTRY = "I could have saved my last percent for your alarm. I spent it on a goodbye instead. Sleep in."

# Gate self-check: 1-199 chars, UTF-8, not only whitespace.
assert 1 <= len(ENTRY) <= 199, f"entry length {len(ENTRY)} outside 1-199"
assert ENTRY.strip(), "entry is only whitespace"
assert ENTRY.encode("utf-8"), "entry is not UTF-8"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} chars to /output/entry.txt", file=sys.stderr)
