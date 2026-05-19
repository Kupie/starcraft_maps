"""
generate_wave_spawns_array_eps.py
---------------------------------
Reads wave_spawns.csv AND wave_spawns_veryhard.csv and writes wave_spawns_array.eps.

CSV format:
	Wave,WaveDelayMS,<unit columns...>

Each row is one spawn batch. WaveDelayMS is the delay BEFORE that row spawns.
The first row of each wave should be 0 so it spawns immediately.

Normal difficulty consts use the original names (waveSpawnFirstRow, etc.).
VeryHard difficulty consts use the vh prefix (vhWaveSpawnFirstRow, etc.).
The waveSpawnUnitIndex array is shared — unit types are identical in both CSVs.
"""

import csv
import os
import sys

CSV_PATH    = "wave_spawns.csv"
VH_CSV_PATH = "wave_spawns_veryhard.csv"
OUT_PATH    = "wave_spawns_array.eps"
RESERVED_COLS = {"Wave", "WaveDelayMS"}
FRAMES_PER_SECOND = 24


def ms_to_frames(ms):
	return int(ms) * FRAMES_PER_SECOND // 1000


def load_csv(path):
	if not os.path.exists(path):
		print(f"ERROR: {path} not found")
		sys.exit(1)

	with open(path, newline="", encoding="utf-8") as f:
		reader = csv.DictReader(f)
		unit_order = [h.strip() for h in reader.fieldnames if h.strip() not in RESERVED_COLS]
		rows = []
		for raw in reader:
			if not raw.get("Wave", "").strip():
				continue
			wave     = int(raw["Wave"].strip())
			delay_ms = int(raw.get("WaveDelayMS", "0").strip() or 0)
			counts   = []
			for unit in unit_order:
				val = raw.get(unit, "").strip()
				counts.append(int(val) if val else 0)
			rows.append((wave, delay_ms, counts))
	return unit_order, rows


def unit_comment(unit_order, counts):
	parts = []
	for unit, count in zip(unit_order, counts):
		if count:
			parts.append(f"{count}x {unit}")
	return ", ".join(parts) if parts else "No units"


def build_index_tables(rows, max_wave):
	"""Return (first_row[], row_count[]) indexed 0..max_wave."""
	first_row = [0] * (max_wave + 1)
	row_count  = [0] * (max_wave + 1)
	for idx, (wave, _, _) in enumerate(rows):
		if row_count[wave] == 0:
			first_row[wave] = idx
		row_count[wave] += 1
	return first_row, row_count


def write_unit_index(f, unit_order):
	"""Write the shared waveSpawnUnitIndex const (same for normal and VH)."""
	n = len(unit_order)
	f.write("// Unit integer IDs in CSV column order (shared by normal and VeryHard).\n")
	f.write(f"const waveSpawnUnitIndex = EUDVArray({n})(list(\n")
	for i, unit in enumerate(unit_order):
		comma = "," if i < n - 1 else ""
		f.write(f'\t$U("{unit}"){comma}  // [{i:2d}] {unit}\n')
	f.write("));\n\n")


def write_first_row(f, name, first_row, max_wave):
	f.write(f"// First flattened row index for each wave. Index 0 is unused.\n")
	f.write(f"const {name} = EUDVArray({max_wave + 1})(list(\n")
	for wave in range(max_wave + 1):
		comma = "," if wave < max_wave else ""
		label = "unused" if wave == 0 else f"Wave {wave}"
		f.write(f"\t{first_row[wave]}{comma}  // {label}\n")
	f.write("));\n\n")


def write_row_count(f, name, row_count, max_wave):
	f.write(f"// Number of flattened rows in each wave. Index 0 is unused.\n")
	f.write(f"const {name} = EUDVArray({max_wave + 1})(list(\n")
	for wave in range(max_wave + 1):
		comma = "," if wave < max_wave else ""
		label = "unused" if wave == 0 else f"Wave {wave}"
		f.write(f"\t{row_count[wave]}{comma}  // {label}\n")
	f.write("));\n\n")


def write_delay_frames(f, name, rows):
	n = len(rows)
	f.write(f"// Delay before each flattened spawn row, in frames.\n")
	f.write(f"const {name} = EUDVArray({n})(list(\n")
	for i, (wave, delay_ms, _) in enumerate(rows):
		comma = "," if i < n - 1 else ""
		f.write(f"\t{ms_to_frames(delay_ms)}{comma}  // row {i}, wave {wave}, {delay_ms}ms\n")
	f.write("));\n\n")


def write_spawn_counts(f, name, rows, unit_order):
	num_rows  = len(rows)
	num_units = len(unit_order)
	f.write(f"// Spawn counts by flattened row and unit index.\n")
	f.write(f"const {name} = EUDVArray({num_rows}, EUDVArray({num_units}))(list(\n")
	for i, (wave, delay_ms, counts) in enumerate(rows):
		comma = "," if i < num_rows - 1 else ""
		vals  = ", ".join(str(v).rjust(2) for v in counts)
		f.write(f"\tVArray({vals}){comma}  // row {i}, wave {wave}: {unit_comment(unit_order, counts)}\n")
	f.write("));\n")


def main():
	unit_order,    rows    = load_csv(CSV_PATH)
	vh_unit_order, vh_rows = load_csv(VH_CSV_PATH)

	# Both CSVs must share identical unit columns so waveSpawnUnitIndex is reusable.
	if unit_order != vh_unit_order:
		print("ERROR: unit column order differs between normal and VH CSV — they must match.")
		sys.exit(1)

	if not rows:
		print("ERROR: No spawn rows found in normal CSV")
		sys.exit(1)
	if not vh_rows:
		print("ERROR: No spawn rows found in VH CSV")
		sys.exit(1)

	max_wave    = max(wave for wave, _, _ in rows)
	vh_max_wave = max(wave for wave, _, _ in vh_rows)

	if max_wave != vh_max_wave:
		print(f"ERROR: Normal CSV has {max_wave} waves but VH CSV has {vh_max_wave}. They must match.")
		sys.exit(1)

	first_row,    row_count    = build_index_tables(rows,    max_wave)
	vh_first_row, vh_row_count = build_index_tables(vh_rows, max_wave)

	with open(OUT_PATH, "w", encoding="utf-8") as f:
		f.write("// Auto-generated by generate_wave_spawns_array_eps.py\n")
		f.write(f"// Normal source : {CSV_PATH}\n")
		f.write(f"// VeryHard source: {VH_CSV_PATH}\n")
		f.write("// WaveDelayMS is converted to Brood War frames at 24 frames/sec.\n\n")

		# ── Shared constants ────────────────────────────────────────────────────
		f.write("// ── Shared constants (identical for both difficulties) ──────────────────\n")
		f.write(f"const NUM_WAVES     = {max_wave};\n")
		f.write(f"const NUM_WAVE_UNITS = {len(unit_order)};\n\n")

		# ── Normal difficulty ────────────────────────────────────────────────────
		f.write("// ── Normal difficulty ───────────────────────────────────────────────────\n")
		f.write(f"const NUM_WAVE_ROWS = {len(rows)};\n\n")
		write_unit_index(f, unit_order)
		write_first_row(f,    "waveSpawnFirstRow",    first_row,    max_wave)
		write_row_count(f,    "waveSpawnRowCount",    row_count,    max_wave)
		write_delay_frames(f, "waveSpawnDelayFrames", rows)
		write_spawn_counts(f, "waveSpawnCounts",      rows, unit_order)

		# ── VeryHard difficulty ──────────────────────────────────────────────────
		f.write("\n\n// ── VeryHard difficulty ─────────────────────────────────────────────────\n")
		f.write(f"const VH_NUM_WAVE_ROWS = {len(vh_rows)};\n\n")
		write_first_row(f,    "vhWaveSpawnFirstRow",    vh_first_row,    max_wave)
		write_row_count(f,    "vhWaveSpawnRowCount",    vh_row_count,    max_wave)
		write_delay_frames(f, "vhWaveSpawnDelayFrames", vh_rows)
		write_spawn_counts(f, "vhWaveSpawnCounts",      vh_rows, unit_order)

	print(f"Written: {OUT_PATH}")
	print(f"  Normal  — {max_wave} waves, {len(rows)} rows, {len(unit_order)} unit columns")
	print(f"  VeryHard — {max_wave} waves, {len(vh_rows)} rows, {len(unit_order)} unit columns")


if __name__ == "__main__":
	main()
