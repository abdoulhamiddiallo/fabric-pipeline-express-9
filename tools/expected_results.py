"""Résultats attendus du pipeline 9 : ce que Score line doit renvoyer pour chaque ligne."""
import csv, json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"
r1 = lambda x: Decimal(str(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
for line in json.loads((ROOT / "config" / "lines.json").read_text(encoding="utf-8")):
    d = [int(r["delay_s"]) for r in csv.DictReader(open(ROOT / "inbox" / line["file"], encoding="utf-8"))]
    pct, avg = r1(100 * sum(x < 60 for x in d) / len(d)), r1(sum(d) / len(d))
    print(f"{line['code']:9} {len(d):4} départs  {pct:>5} % à l'heure  moyenne {avg:>5} s  max {max(d):5} s")
    print(f"          {line['name']} {pct} % à l'heure ({len(d)} départs, max {max(d)} s)")
