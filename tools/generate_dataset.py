"""Génère les départs du 20 octobre 2026 sur quatre lignes de Shinkansen (données fictives).

Un fichier CSV par ligne dans data/inbox, et data/config/lines.json qui décrit les lignes.
delay_s : retard au départ, en secondes (0 si le train part à l'heure).
"""
import csv, json, random
from pathlib import Path

random.seed(2010)
ROOT = Path(__file__).resolve().parent.parent / "data"
(ROOT / "inbox").mkdir(parents=True, exist_ok=True)
(ROOT / "config").mkdir(parents=True, exist_ok=True)
DAY = "2026-10-20"

LINES = [
    # code, nom, trains, (origine, terminus), types, (part à l'heure, retard type si en retard)
    ("tokaido", "Tōkaidō", 132, ("Tokyo", "Shin-Osaka"), ["Nozomi", "Hikari", "Kodama"], 0.985, 95),
    ("sanyo", "Sanyō", 96, ("Shin-Osaka", "Hakata"), ["Nozomi", "Mizuho", "Sakura", "Kodama"], 0.958, 140),
    ("tohoku", "Tōhoku", 104, ("Tokyo", "Shin-Aomori"), ["Hayabusa", "Yamabiko", "Nasuno"], 0.932, 210),
    ("hokkaido", "Hokkaidō", 26, ("Shin-Aomori", "Shin-Hakodate-Hokuto"), ["Hayabusa", "Hayate"], 0.731, 540),
]

config = []
for code, name, n, (o, d), types, p_ok, late in LINES:
    rows = []
    t0 = 6 * 60
    step = (23 * 60 - t0) / n
    for i in range(n):
        m = int(t0 + i * step)
        if random.random() < p_ok:
            delay = random.choice([0, 0, 0, 0, 0, 0, 10, 15, 20, 30, 45])
        else:
            delay = max(60, int(random.expovariate(1 / late)) + 60)
        fwd = i % 2 == 0
        rows.append({
            "train_id": f"{code[:3].upper()}-{i + 1:03d}",
            "train_type": random.choice(types),
            "origin": o if fwd else d,
            "destination": d if fwd else o,
            "sched_dep": f"{DAY} {m // 60:02d}:{m % 60:02d}:00",
            "delay_s": delay,
        })
    f = f"departures_{code}_{DAY}.csv"
    with open(ROOT / "inbox" / f, "w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    config.append({"code": code, "name": name, "file": f})

(ROOT / "config" / "lines.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(config, ensure_ascii=False))
