import os
import subprocess
import glob

# --- config ---
EUDDRAFT_EXE = r"E:\Downloads\Admin\Scmdraft 2 - 2020.06.24(W)\EUDShiz\euddraft0.10.2.5\euddraft.exe"
MAPS_DIR     = r"C:\Users\Admin\Documents\StarCraft\Maps\CoopCampaign_v1.2.3.35"
EDS_TEMPLATE = r"E:\Downloads\Admin\Scmdraft 2 - 2020.06.24(W)\EUDShiz\EUD.Editor.3.0.19.6.0\Data\temp\BuildData_Campaign_Edits_CheatsOnly\eudplibData\EUDEditor.eds"
EDS_DIR      = os.path.dirname(EDS_TEMPLATE)

# --- read template ---
with open(EDS_TEMPLATE, 'r', encoding='utf-8') as f:
	template = f.read()

# --- find all .scx recursively, skip already processed ---
map_files = glob.glob(os.path.join(MAPS_DIR, "**", "*.scx"), recursive=True)
map_files = [f for f in map_files if "_modded" not in f and "_HT_Cheats" not in f]

print(f"Found {len(map_files)} map(s) to process")

for map_path in sorted(map_files):
	map_name = os.path.basename(map_path)
	stem     = os.path.splitext(map_name)[0]
	out_path = os.path.join(os.path.dirname(map_path), stem + "_HT_Cheats.scx")

	lines = template.splitlines()
	new_lines = []
	for line in lines:
		if line.startswith("input:"):
			new_lines.append(f"input: {map_path}")
		elif line.startswith("output:"):
			new_lines.append(f"output: {out_path}")
		else:
			new_lines.append(line)

	# write temp .eds into eudplibData folder so relative plugin paths resolve
	temp_eds = os.path.join(EDS_DIR, "_temp.eds")
	with open(temp_eds, 'w', encoding='utf-8') as f:
		f.write('\n'.join(new_lines))

	print(f"Processing {map_path}")
	print(f"       --> {out_path}")

	result = subprocess.run(
		[EUDDRAFT_EXE, temp_eds],
		capture_output=True, text=True,
		input="\n",
		creationflags=subprocess.CREATE_NO_WINDOW
	)

	if result.returncode == 0:
		print(f"  OK\n")
	else:
		print(f"  FAILED")
		print(result.stdout[-1000:])
		print(result.stderr[-500:])
		print()

	os.remove(temp_eds)

print("All done.")
