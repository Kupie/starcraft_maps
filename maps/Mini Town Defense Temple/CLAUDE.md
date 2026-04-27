# CPU Cat and Mouse — EPScript / EUD Editor 3 Development Guide

## Project Overview
StarCraft: Brood War 1.16.1 UMS map using EUD Editor 3 (EPScript / eudplib / euddraft).
Target euddraft version: 0.10.2.5
Source triggers are in *.txt files in standard SCMDraft trigger format.

---

## IMPORTANT: Always Read Reference Docs Before Writing EPScript
Before writing or modifying ANY .eps file, read the relevant sections at:
	https://havonz.github.io/SCRMapDocs/epScript-Reference/

Key pages:
	Syntax:          https://havonz.github.io/SCRMapDocs/epScript-Reference/Syntax
	Variables:       https://havonz.github.io/SCRMapDocs/epScript-Reference/Use-of-Variables
	Functions:       https://havonz.github.io/SCRMapDocs/epScript-Reference/Use-of-Functions
	Built-in Funcs:  https://havonz.github.io/SCRMapDocs/epScript-Reference/Built-in-Functions

The full docs are also mirrored locally in: /SCRMapDocs-main/docs/epScript-Reference/

---

## EPScript: Imports

Imports require the MODULE NAME PREFIX to access any variable or function from that module.

```javascript
import WaveSpawnsFull;
WaveSpawnsFull.waveSpawnsFull1   // CORRECT
waveSpawnsFull1                  // WRONG — undefined rvalue error

import WaveSpawnsFull as wsf;
wsf.waveSpawnsFull1              // CORRECT with alias
```

- Files that are ONLY data (no lifecycle functions) do NOT need to be listed in the .edd.
  They will be found automatically by import if in the same TriggerEditor directory.
- Files listed in .edd AND imported by another plugin will compile TWICE, causing _1 suffix
  errors on all variables. Only list files with lifecycle functions in the .edd.
- There is no syntax for importing a single member — you must import the whole module.
- Plugin files (those in the .edd) are NOT automatically visible to other plugins.
  Variables from plugin A are NOT accessible in plugin B without importing.
  But importing a plugin causes double-compile. The solution is either:
  a) Count/compute locally in each plugin that needs the value, or
  b) Use EUDRegisterObjectToNamespace / GetEUDNamespace for true cross-plugin sharing.

---

## EPScript: Variable Declaration

```javascript
// Use var for module-level variables that need to be reassigned at runtime
var myRuntimeVar = 0;           // CORRECT for reassignable globals
var myRuntimeVar = 0;           // reassign with: myRuntimeVar = newValue;

// Use const for arrays and objects (reference types)
const myArray   = EUDArray(10);
const myVArray  = EUDVArray(4)(list(1, 2, 3, 4));

// Local variables inside functions
var localVar = 0;               // always initialize explicitly
static var persistent = 0;     // retains value across function calls
```

CRITICAL: Use `var` NOT `const` for module-level variables you intend to reassign.
Using `const x = EUDVariable(0)` then `x = newValue` causes EPScript to rename `x`
to `x_1` inside functions, making it undefined. Always use `var x = 0` instead.

- `var` compiles `=` assignment to the internal `<<` operator correctly.
- `const` does NOT allow `=` assignment after initial declaration.
- All variables have FIXED memory addresses — everything is static internally.
- Module-level vars must be declared BEFORE the functions that use them.

---

## EPScript: Arrays

```javascript
// EUDArray — fast for fixed compile-time index, slow for runtime variable index
const a = EUDArray(10);
a[0] = 29;

// EUDVArray — faster for runtime variable index, supports 2D
const b = EUDVArray(4)(list(1, 2, 3, 4));
const c = VArray(1, 2, 3, 4);   // shorthand, same as above

// 2D EUDVArray
const d = EUDVArray(60, EUDVArray(27))(list(
	VArray(30, 20, 0, 0, ...),   // Round 1
	VArray(30, 20, 0, 0, ...),   // Round 2
));
var val = d[round][unitIndex];   // runtime 2D access works correctly

// Use EUDVArray when index is a runtime variable (loops, player counts, etc.)
// Use EUDArray when index is always a compile-time constant
```

---

## EPScript: Functions

```javascript
// Lifecycle functions — only ONE of each per .eps file
// Duplicates silently break all variable name resolution in that file (_1 suffix)
function onPluginStart()     { }   // runs once at game start
function beforeTriggerExec() { }   // runs every frame before SC triggers
function afterTriggerExec()  { }   // runs every frame after SC triggers

// Regular functions
function myFunc(param1, param2) {
	return param1 + param2;
}

// Multiple return values
function swap(a, b) {
	return b, a;
}
var x, y = swap(1, 2);

// Early return
function hasUnits(roundNumber) {
	foreach(i : py_range(0, NUM_UNITS)) {
		if (myArray[roundNumber][i] > 0) {
			return 1;
		}
	}
	return 0;
}
```

---

## EPScript: Loops — compile-time vs runtime

```javascript
// foreach with py_range — COMPILE TIME, unrolls statically, cannot break/continue
foreach(i : py_range(0, 27)) {
	// runs exactly 27 times, expanded at compile time
}

// foreach with EUDLoopPlayer — RUNTIME, only loops over active players
// USE THIS for counting active players, NOT py_range
var playerCount = 0;
foreach(player : EUDLoopPlayer()) {
	playerCount += 1;
}

// foreach with EUDLoopRange — RUNTIME, can break/continue
foreach(i : EUDLoopRange(0, 27)) {
	// runtime loop
}

// while — RUNTIME
var i = 0;
while (i < 10) {
	i++;
}
```

CRITICAL: `foreach(player : py_range(1, 7))` always runs 6 times regardless of
how many players are in the game. Use `EUDLoopPlayer()` to count active players.

---

## EPScript: Player Constants

```javascript
P1  P2  P3  P4  P5  P6  P7  P8   // players 1-8
P9  P10 P11 P12                   // neutral/special slots
AllPlayers
Force1  Force2  Force3  Force4
CurrentPlayer                     // constant 13
```

Do NOT use "Player 8", "player 8", or integer 7. Use P8.

---

## EPScript: Unit and Location IDs

```javascript
$U("Terran Marine")     // compile-time unit integer ID — use in EUDVArrays and actions
$L("Location 1")        // compile-time location integer ID
$B("Terran Marine")     // stat_txt.tbl string index for unit

// String literals in action params are auto-converted at compile time:
CreateUnit(1, "Terran Marine", "Location 1", P1);
// ...is equivalent to using the integer IDs directly
```

---

## EPScript: Conditions — Parameter Order

```javascript
// Command
Command(player, comparison, count, unit)
Command(P1, AtLeast, 5, "Terran Marine")    // CORRECT
Command(P1, "Terran Marine", AtLeast, 5)    // WRONG — "invalid comparison" error

// Kills
Kills(player, comparison, count, unit)
Kills(player, AtLeast, 1, 93)               // unit can be integer ID

// Deaths
Deaths(player, comparison, count, unit)

// Memory / MemoryX
Memory(address, comparison, value)

// Switch
Switch("SwitchName", Set)
Switch("SwitchName", Cleared)               // NOT "NotSet" — use Cleared

// CountdownTimer — eudTurbo runs every frame so Exactly is safe with it
CountdownTimer(Exactly, 5)
CountdownTimer(AtLeast, 5)
CountdownTimer(AtMost, 30)

// Negation of conditions
if (!Command(P1, AtLeast, 1, "Terran Marine")) { ... }
```

---

## EPScript: Actions — Parameter Order

```javascript
// CreateUnit
CreateUnit(count, unit, location, player)

// CreateUnitWithProperties — call DIRECTLY, NOT inside DoActions()
CreateUnitWithProperties(count, unit, location, player, UnitProperty(
	hitpoint     = 100,    // health %
	shield       = 100,    // shield %
	energy       = 100,    // energy % (set high for Wraiths so they can cloak immediately)
	hanger       = 8,      // hangar count (interceptors for Carrier, scarabs for Reaver)
	resource     = 0,
	cloaked      = false,
	burrowed     = false,
	intransit    = false,
	hallucinated = false,
	invincible   = false)
);

// GiveUnits — order: count, unit, sourcePlayer, location, destPlayer
GiveUnits(1, "Devouring One (Zergling)", P8, "TopLeftLing", P12)   // CORRECT
GiveUnits(1, "Devouring One (Zergling)", "TopLeftLing", P8, P12)   // WRONG

// SetInvincibility — call DIRECTLY, NOT inside DoActions()
// order: (state, unit, owner, location)
SetInvincibility(Enable, "(any unit)", AllPlayers, "HeroSelectorArea")

// KillUnitAt — call DIRECTLY, NOT inside DoActions()
KillUnitAt(All, "(buildings)", "spawner", Force1)

// SetMemory / SetMemoryX
SetMemory(address, SetTo, value)
SetMemoryX(address, SetTo, value, mask)

// SetSwitch
SetSwitch("SwitchName", Set)
SetSwitch("SwitchName", Clear)

// SetCountdownTimer
SetCountdownTimer(SetTo, 60)

// DoActions — for grouping CLASSIC trigger actions only
// CreateUnitWithProperties, GiveUnits, SetInvincibility, KillUnitAt
// must be called DIRECTLY outside DoActions()
DoActions(
	CreateUnit(1, "Terran Marine", "Location 1", P1),   // simple CreateUnit OK inside
	SetMemory(addr, SetTo, value),
	SetSwitch("MySwitch", Set),
);
```

---

## EPScript: Debug Text Output

```javascript
// Display to local player's screen
println("Round: {}", currentRound);
println("Step: {}, Counter: {}", roundStep, spawnTimeCounter);

// Display to all players' screens
printAll("Round: {}", currentRound);

// String + runtime variable — cannot use + operator
// WRONG: DisplayTextAll("Round: " + currentRound);
// CORRECT:
println("Round: {}", currentRound);
```

---

## EPScript: Memory Write Operations

```javascript
// Direct writes (preferred over SetMemoryX for clarity)
f_dwwrite(address, value)       // 32-bit write
f_wwrite(address, value)        // 16-bit write
f_bwrite(address, value)        // 8-bit write

// Masked MemoryAddr conversion:
// 0x0000ffff mask → f_wwrite(addr, value)            same address
// 0xffff0000 mask → f_wwrite(addr + 2, value >> 16)  addr+2, unshift value
// 0x000000ff mask → f_bwrite(addr, value)             single byte

// Example: Masked MemoryAddr(0x00660e98, Set To, 1310720000, 0xffff0000)
//       -> f_wwrite(0x00660e9a, 20000)    // 1310720000 >> 16 = 20000

// HP values in BW dat are stored as actual HP * 256:
f_dwwrite(0x00662390, 50000 * 256)   // readable as "50000 HP"

// EPD address formula: EPD(addr) = (addr - 0x58A364) / 4
// Kill counter address: 0x005878A4 + (unitID * 12 + (player - 1)) * 4
```

---

## EPScript: Randomization

```javascript
f_rand()             // random 32-bit unsigned integer
f_rand() % 4        // 0-3
f_rand() % 4 + 1    // 1-4
```

---

## EPScript: Location Setting

```javascript
// setloc(locationID, left, top, right, bottom)
setloc($L("spawner"), left, top, right, bottom);

// Random spawner location within map bounds:
var left   = f_rand() % 3776;
var top    = 160 + f_rand() % (3776 - 160);
var right  = left + 320;
var bottom = top + 320;
setloc($L("spawner"), left, top, right, bottom);
```

---

## EPScript: Indentation

ALWAYS use TABS, never spaces. Applies to all .eps files and Python scripts.

---

## EPScript: Common Pitfalls

1. **Use `var` not `const` for reassignable globals** — `const x = EUDVariable(0)`
   then `x = val` causes `x_1` undefined errors. Use `var x = 0` instead.

2. **Module prefix required on imports** — `import Foo; Foo.myVar` not just `myVar`.

3. **Plugin variables not shared** — variables in plugin A are not visible in plugin B
   without importing. But importing a plugin causes double-compile. Count/compute locally.

4. **Double-compile causes _1 suffix** — file in .edd AND imported = compiles twice.
   Only list files with lifecycle functions in the .edd. Data-only files: import only.

5. **Duplicate lifecycle functions** — only ONE beforeTriggerExec/afterTriggerExec per file.
   Duplicates silently break all variable name resolution (_1 suffix on everything).

6. **Module-level vars before functions** — declare all vars before any function that uses them.

7. **py_range is compile-time, always fixed count** — `foreach(p : py_range(1, 7))` ALWAYS
   runs 6 times. Use `EUDLoopPlayer()` to iterate only over active players at runtime.

8. **py_range upper bound is exclusive** — `py_range(0, 27)` = 0..26. `py_range(1, 8)` = 1..7.

9. **foreach with py_range cannot break/continue** — use while or EUDLoopRange for that.

10. **Wait() in afterTriggerExec is dangerous** — blocks the entire EUD loop.
    Use frame counters or countdown timers instead.

11. **Assigning to a local copy doesn't affect VArray** — `var x = arr[i]; x = 0;` does nothing
    to the array. Use `arr[i] = 0;` directly.

12. **EUDVArray for runtime indexes** — use EUDVArray not EUDArray when indexing with variables.

13. **$U for runtime unit IDs** — `$U("unit name")` gives integer ID usable at runtime.
    `py_str` is compile-time only. `CreateUnitWithProperties(count, $U("Terran Marine"), ...)` works.

14. **No for/in over arrays** — no `for (x in array)`. Use `foreach(i : py_range(0, N))`.

15. **CreateUnitWithProperties outside DoActions** — call it directly, not wrapped in DoActions.

16. **String concatenation with runtime vars** — cannot use `+` to concat strings with vars.
    Use `println("text {}", myVar)` or `printAll("text {}", myVar)` instead.

---

## Project: Goal
Convert spawner_triggers.txt (SCMDraft trigger format) into EPScript (.eps) files with:
- Split spawn logic scaled by active player count using EUDLoopPlayer()
- Frame-counter-based wave pacing (no Wait())
- Hard mode extra spawn support
- Randomized spawner locations each wave

---

## Project: Player Slots

| Slot | Role |
|------|------|
| P1–P7 | Human/computer players (mice) |
| P8 | Cat spawner (CPU) |
| P9 | Shop token pool (Terran Civilians = currency) |
| P11 | Kakaru state tracker (wave trigger gating) |
| P12 | Hero unit owner |

---

## Project: Key Switches

| Switch | Meaning |
|--------|---------|
| DifficultyChosen | Difficulty has been selected, run difficulty modifier |
| HardModeEnabled | Hard mode is active |
| EUDUnitsPlaced | Difficulty modifier has already run once, skip it |
| ReduceSpawnsForNumPlayers | Scale spawns by player count using split CSV data |
| SpawnExtra | Wave finished spawning, signal for hard mode extras |
| ExtraSpawn1 / ExtraSpawn2 | Select which hard mode extra unit to spawn (2-bit combo) |

Do NOT change these switch names.

---

## Project: Key Locations

| Location | Purpose |
|----------|---------|
| spawner | Primary enemy spawn point (randomized each wave) |
| spawner2 | Secondary enemy spawn point (randomized each wave) |
| getbonus | Where bonus civilians are created for players |
| playground | Kakaru tracking location |

Do NOT change these location names.

---

## Project: Split Spawn Logic

When Switch "ReduceSpawnsForNumPlayers" is SET:
- Use WaveSpawnsSplit arrays (per-player counts)
- Multiply by active player count (via EUDLoopPlayer) to get actual counts

When NOT SET:
- Use WaveSpawnsFull arrays (full counts regardless of player count)

---

## Project: Wave Spawn Structure

Each wave:
1. roundStep 0: at countdown 6 — increment currentRound, reset index, go to step 1
2. roundStep 1: at countdown 5 — randomize spawner locations, reduce counts if needed, roll hardRoll
3. roundStep 2: at countdown 0 — kill buildings at active spawners, reset timer to 59, go to step 3
4. roundStep 3: spawning loop — iterate unit indices, spawn non-zero with 48-frame (3 sec) gaps
5. roundStep 4: hard mode bonus spawns (same loop, hardRoll 1-4 selects array)
6. roundStep 99: idle, waiting for countdown to reach 6

---

## Project: Key Memory Addresses

```
Kill counters:     0x005878A4 + (unitID * 12 + (player - 1)) * 4
HP (dat):          0x00662000 + offsets  (stored as actual HP * 256)
Shield (dat):      0x00660E00 + offsets  (lower or upper 16 bits of dword)
Armor (dat):       0x0065FF00 + offsets  (1 byte per unit)
Weapon damage:     0x00656E00 + offsets
Weapon bonus:      0x00657600 + offsets
Vespene cost:      0x0065FD80 + offsets
```

---

## Project: Wave Spawn Data

Generated by `generate_eps.py` from CSVs. Never edit these .eps files manually.

| CSV | Output .eps | Variables |
|-----|-------------|-----------|
| wave_spawns_full.csv | WaveSpawnsFull.eps | waveSpawnsFull1, waveSpawnsFull2 |
| wave_spawns_split.csv | WaveSpawnsSplit.eps | WaveSpawnsSplit1, WaveSpawnsSplit2 |
| wave_spawns_full.csv (hard) | HardModeSpawnsFull.eps | waveSpawnsFullHard1..4 |
| wave_spawns_split.csv (hard) | HardModeSpawnsSplit.eps | waveSpawnsSplitHard1..4 |
| (generated) | wave_spawns_indexes.eps | waveSpawnsUnitIndex, NUM_UNITS |

Unit index order (0-26) — same order as CSV columns:
```
 0  Zerg Ultralisk
 1  Terran Firebat
 2  Protoss Reaver
 3  Infested Kerrigan (Infested Terran)
 4  Edmund Duke (Siege Tank)
 5  Tassadar (Templar)
 6  Hunter Killer (Hydralisk)
 7  Torrasque (Ultralisk)
 8  Zeratul (Dark Templar)
 9  Tom Kazansky (Wraith)
10  Jim Raynor (Marine)
11  Fenix (Dragoon)
12  Zerg Zergling
13  Alexei Stukov (Ghost)
14  Artanis (Scout)
15  Zerg Devourer
16  Fenix (Zealot)
17  Yggdrasill (Overlord)
18  Alan Schezar (Goliath)
19  Kukulza (Guardian)
20  Norad II (Battlecruiser)
21  Dark Templar (Hero)
22  Sarah Kerrigan (Ghost)
23  Danimoth (Arbiter)
24  Protoss Observer
25  Kukulza (Mutalisk)
26  Gantrithor (Carrier)
```

---

## Project: .edd Load Order

Only files with lifecycle functions should be in the .edd.
Data-only files are accessed via import only — listing them in .edd causes double-compile.

Files in .edd (have lifecycle functions):
- RewardSystem.eps     (afterTriggerExec)
- common.eps           (beforeTriggerExec)
- difficultyModifier.eps (afterTriggerExec)
- main.eps             (all 3 lifecycle functions, MSQC boilerplate)
- wave_spawns.eps      (afterTriggerExec)

Files NOT in .edd (data only, import only):
- wave_spawns_indexes.eps
- WaveSpawnsFull.eps
- WaveSpawnsSplit.eps
- HardModeSpawnsFull.eps
- HardModeSpawnsSplit.eps

---

## Project: File Structure

```
maps/
	CPU Cat and Mouse/
		EUD_cpu_cat_survival_*.scx            source map (pre-EUD)
		EUD_cpu_cat_survival_*_postEUD.scx    compiled output
		spawner_triggers.txt                  original SCMDraft trigger source
TriggerEditor/
	common.eps              active player counter in beforeTriggerExec (var not const!)
	wave_spawns_indexes.eps NUM_UNITS const + waveSpawnsUnitIndex EUDVArray
	WaveSpawnsFull.eps      full spawn count arrays
	WaveSpawnsSplit.eps     per-player split count arrays
	HardModeSpawnsFull.eps  hard mode bonus options 1-4
	HardModeSpawnsSplit.eps hard mode split bonus options 1-4
	wave_spawns.eps         wave spawning logic (imports the above data files)
	difficultyModifier.eps  easy mode dat patching + hero unit placement
	RewardSystem.eps        kill bonus civilian rewards per player
	main.eps                MSQC boilerplate (mostly blank)
SCRMapDocs-main/            EPScript reference docs (local mirror)
generate_eps.py             generates all EUDVArray .eps files from CSVs
wave_spawns_full.csv        full spawn data (source of truth)
wave_spawns_split.csv       per-player split spawn data (source of truth)
```

---

## EPScript: setcurpl / Current Player

`setcurpl(player)` writes to memory address `0x6509B0` — the global "current player" variable that ALL triggers (both EUD plugins and classic SCMDraft triggers) read from simultaneously.

```javascript
var savedCp = getcurpl();   // always save first
setcurpl(P8);
RunAIScript("SuiR");        // runs as P8
setcurpl(savedCp);          // always restore
```

CRITICAL: If you set curpl and don't restore it, every classic trigger and every other EUD plugin in that frame runs as the wrong player. This causes wrong player units, wrong resources, wrong AI, wrong victory/defeat.

Actions that use Current Player and require sync (must match on all clients):
- RunAIScript, RunAIScriptAt, SetAllianceStatus, Defeat, Victory, Draw

Actions that use Current Player but are desync-safe (only affect local machine):
- DisplayText, CenterView, PlayWAV, MinimapPing, TalkingPortrait, Transmission, SetMissionObjectives

---

## EPScript: AI Scripts

Common AI scripts for use with RunAIScript / RunAIScriptAt:

| Script | Behavior |
|--------|---------|
| `SuiR` | Suicide Run — rush nearest enemy, designed for use with RunAIScriptAt + location |
| `AICD` | Attack Closest — attack nearest enemy unit/building |
| `Att5` / `Att10` / `Att15` | Wait until N units then attack |
| `ReRu` | Rescue Passive — become passive/defensive |
| `StPd` | Stop Patrol — stop moving entirely |

`SuiR` should be used with `RunAIScriptAt` and a target location — without a location it doesn't know where to send units. For a periodic AI nudge every few seconds:

```javascript
var aiNudgeTimer = 80;  // NEVER initialize to 0 — causes unsigned underflow

function beforeTriggerExec() {
	aiNudgeTimer--;
	if (aiNudgeTimer == 0) {
		aiNudgeTimer = 80;   // reset to non-zero
		var savedCp = getcurpl();
		setcurpl(P8);
		RunAIScriptAt("SuiR", $L("playground"));
		setcurpl(savedCp);
	}
}
```

Do NOT run RunAIScript every frame — it causes units to constantly restart their order and never actually move.

---

## EPScript: Timers and Frame Counters

**CRITICAL: Never initialize a countdown timer var to 0.** All vars are 32-bit unsigned. Doing `timerVar--` when `timerVar == 0` wraps to `0xFFFFFFFF` (~4 billion), and the counter won't fire again for a very long time.

```javascript
var myTimer = 80;   // CORRECT — initialize to non-zero
var myTimer = 0;    // WRONG — first decrement underflows to 0xFFFFFFFF
```

**Real-second countdown using getgametick():**
```javascript
var lastTick      = 0;
var realCountdown = 0;

function onPluginStart() {
	realCountdown = someValue;
}

function afterTriggerExec() {
	if (Switch("GameStarted", Set)) {
		var currentTick = getgametick();
		if (currentTick - lastTick >= 24) {  // 24 frames = 1 real second
			lastTick = currentTick;
			realCountdown--;
			SetCountdownTimer(SetTo, realCountdown);
		}
		if (realCountdown == 0) {
			realCountdown = someValue;
		}
	}
}
```

Do NOT use `SetCountdownTimer` every frame — only update it inside the 24-frame tick block to avoid UI jank.

---

## EPScript: Unit Renaming via Map Strings

To rename a unit whose name is set in the map editor (custom string):

```javascript
// Get the address of the map string by its current text, then overwrite it
var myStringAddr = 0;
function onPluginStart() {
	myStringAddr = GetMapStringAddr($T("Original Name In Map"));
}

// Then when needed:
dbstr_print(myStringAddr, "New Name\0");   // \0 null terminator required

// To restore original name:
dbstr_print(myStringAddr, "Original Name In Map\0");
```

Use `$T("string")` for map strings (set in SCMDraft editor).
Use `$B("unit name")` for stat_txt.tbl entries (original BW unit names).
Do NOT use `GetTBLAddr("string")` for map-configured custom strings — it only works for stat_txt.tbl entries.

---

## EPScript: Text Display

```javascript
// Print to specific screen line with format variable
const buf = StringBuffer(64);
buf.insertf(0, "\x07{}", myVar);
buf.DisplayAt(6);   // line 0=top, 10=bottom, 6=roughly center

// Print to all players with format
printAll("\x07Round: {}", currentRound);

// Cannot concatenate string + runtime var with +
// WRONG: DisplayTextAll("Round: " + currentRound);
// CORRECT: printAll("Round: {}", currentRound);

// DisplayText takes a map string index directly
DisplayText($T("My Map String"));
var strIdx = someVArray[round][row];
DisplayText(strIdx);   // works if strIdx is a $T() index
```

Screen has lines 0–10. Line 11 is often cut off. Text persists for several seconds and scrolls up as new lines are added — it does not auto-clear.

---

## EPScript: Beacon Placement System

Beacons are placed at 14 fixed offsets within a spawner's bounding box to form a visible outline:

```javascript
const beaconOffsetX = [48,  48,  48,  48,  48,  112, 112, 208, 208, 272, 272, 272, 272, 272];
const beaconOffsetY = [32,  96,  160, 224, 288, 32,  288, 32,  288, 32,  96,  160, 224, 288];

function placeSpawnerBeacons(left, top) {
	foreach(i : py_range(14)) {
		setloc($L("BeaconPlacer"),
			left + beaconOffsetX[i],
			top  + beaconOffsetY[i],
			left + beaconOffsetX[i] + 1,
			top  + beaconOffsetY[i] + 1);
		CreateUnit(1, "Terran Beacon", "BeaconPlacer", P8);
	}
}
```

Spawner location coords (s1left, s1top, s2left, s2top) must be module-level vars — local vars inside an if block go out of scope and are undefined in later roundSteps.


---

## EPScript: Additional Pitfalls (from extended session)

17. **Functions with compile-time loops — no parameters needed** — a no-parameter
    function containing `foreach(i : py_range(N))` still gets full compile-time
    unrolling inside the function body. The key is that `py_str` list items accessed
    by `i` remain compile-time strings as long as `i` comes from `py_range`.

    WRONG — passing unit name as parameter makes it a runtime EUDVariable:
    ```javascript
    function handleUnit(unit, idx) {
        Command(P9, AtMost, 1, unit);  // FAILS — unit is runtime
    }
    foreach(i : py_range(7)) { handleUnit(patrolUnits[i], i); }
    ```

    CORRECT — loop inside the function, no parameters:
    ```javascript
    function handleAllUnits() {
        foreach(i : py_range(7)) {
            Command(P9, AtMost, 1, patrolUnits[i]);  // compile-time string ✓
        }
    }
    handleAllUnits();  // called with no arguments
    ```

18. **`list()` not `[]` for compile-time py_str arrays** — using `[]` creates an
    EUDArray which tries to evaluate contents as runtime values and fails on py_str.
    Use `list()` for compile-time string/constant collections:
    ```javascript
    const myUnits = list(py_str("Terran Marine"), py_str("Zerg Zergling"));  // CORRECT
    const myUnits = [py_str("Terran Marine"), py_str("Zerg Zergling")];      // WRONG
    ```

19. **Condition comparison values must be compile-time** — `Command(P9, AtMost, runtimeVar, unit)`
    fails because the count parameter must be a compile-time constant. This includes
    function parameters — even `maxCount - 1` where maxCount is passed as `2` fails
    because the subtraction happens at runtime in the function context.

20. **Timer vars must never start at 0** — all vars are 32-bit unsigned. `timer--`
    when `timer == 0` wraps to `0xFFFFFFFF`, making the timer fire only after ~4
    billion frames. Always initialize countdown timers to a non-zero value.

21. **P1 internal value is 0, not 1** — `player - 1` for P1 underflows to `0xFFFFFFFF`.
    Use `player` directly as an EUDArray index (P1=0, P2=1, ..., P7=6).
    Confirm with `printAll("player={}", player)` if unsure.

22. **`var idx = player` is correct for EUDArray indexing** — since P1=0, P2=1 etc.,
    the player value IS the correct 0-based array index. No subtraction needed.

23. **setcurpl required for DisplayText/PlayWAV/CenterView per-player** — these
    actions only affect the machine where CurrentPlayer == LocalPlayer. Without
    `setcurpl(player)` before them in a loop, they fire for the wrong player.
    Always save/restore: `var savedCp = getcurpl(); setcurpl(p); ...; setcurpl(savedCp);`

24. **DisplayText vs println vs DisplayTextAll** — use the right tool:
    - `DisplayText(mapStringIdx)` — cheapest, compile-time string only, current player only
    - `DisplayTextAll(mapStringIdx)` — same but all players, no setcurpl needed
    - `println("text {}", runtimeVar)` — uses StringBuffer, supports runtime vars, current player
    - `printAll("text {}", runtimeVar)` — same but all players
    Never call `StringBuffer()` inline in a loop — allocates a new string slot each call.
    Declare `const buf = StringBuffer(N)` at module scope and reuse it.

25. **Order() parameter order** — `Order(unit, owner, startLocation, orderType, destLocation)`
    The orderType comes BEFORE destLocation, unlike SCMDraft trigger syntax which has
    destLocation last. Common orders: `Move`, `Attack Move`, `Hold Position`.

26. **Classic trigger randomize switch → use f_rand() instead** — the classic
    `Set Switch("X", randomize)` pattern used 4-bit binary switch combos to pick
    from N locations. Replace entirely with `f_rand() % N` and a compile-time
    `foreach` to select the location. No BonusSwitches needed.

27. **EUDLoopPlayer(None, Force1)** — iterates only active players in Force1 (P1-P7).
    Use instead of `foreach(p : py_range(1, 8))` which always runs 7 times regardless
    of active players. `EUDLoopPlayer()` with no args iterates all active players.

28. **Condition negation syntax** — `if (!CountdownTimer(Exactly, 5))` requires the
    `!` to wrap the entire condition including both parens:
    ```javascript
    if (!CountdownTimer(Exactly, 5)) { return; }  // CORRECT
    if !(CountdownTimer(Exactly, 5)) { return; }   // WRONG — syntax error
    ```

29. **`println` always uses StringBuffer at runtime** — even if the argument is a
    compile-time constant, `println` still does a runtime memory write. Use
    `DisplayText($T(...))` for truly zero-cost static messages.

30. **Floating point doesn't exist** — EPScript is 32-bit unsigned integers only.
    `23.81` truncates to `23`. Use integer approximations:
    `frames * 100 / 2381` instead of `frames / 23.81`.

31. **`once` with per-player runtime condition** — `once (tempInvul[player] == 240)`
    inside a player loop fires globally once for the first player that hits 240,
    then never again for other players. Use plain `if` instead when the condition
    is per-player runtime state.

32. **Cannot store condition results in variables** — `var x = (a == b)` causes an
    "Orphan condition" error at compile time. Conditions can ONLY be used directly
    inside `if()`, `while()`, or other control flow — never assigned to a variable.

    WRONG:
    ```javascript
    var isReaver = (wave_spawns_indexes.waveSpawnsUnitIndex[idx] == $U("Protoss Reaver"));
    if (isReaver) { ... }  // ERROR: Orphan condition
    ```

    CORRECT — inline the condition directly:
    ```javascript
    if (wave_spawns_indexes.waveSpawnsUnitIndex[idx] == $U("Protoss Reaver")) { ... }
    ```

    If you need to branch on the same condition multiple times, duplicate the check
    or restructure into a single if/else block.

33. **`UnitProperty()` fields are all compile-time constants** — you cannot pass a
    runtime variable as any field (hanger, hitpoint, shield, etc.). This includes
    variables computed from conditions. If you need two different values (e.g. hanger=2
    for Reavers, hanger=8 for others), you must write two separate
    `CreateUnitWithProperties` calls inside an if/else:

    ```javascript
    if (wave_spawns_indexes.waveSpawnsUnitIndex[spawnIdx] == $U("Protoss Reaver")) {
        CreateUnitWithProperties(count, ..., UnitProperty(hanger = 2, ...));
    } else {
        CreateUnitWithProperties(count, ..., UnitProperty(hanger = 8, ...));
    }
    ```

34. **afterTriggerExec runs in REVERSE .edd order** — if A.eps and B.eps are both
    in .edd, B's afterTriggerExec runs BEFORE A's. onPluginStart and beforeTriggerExec
    run in forward order.

35. **`DisplayTextAll` inside a player loop fires once per active player** — it
    broadcasts to everyone each iteration. Move it outside the loop:
    ```javascript
    DisplayTextAll("You WIN!");              // once, correct
    foreach(player : EUDLoopPlayer(...)) {
        setcurpl(player);
        Victory();                           // per-player, correct
    }
    ```

36. **`var x;` without initializer has static behavior** — the value persists between
    function calls. Always use `var x = 0;` to ensure reset, or `static var x = 0;`
    to explicitly document the intent.

37. **`aiNudgeTimer` (and similar timers) must be initialized non-zero** — if declared
    as `var aiNudgeTimer = 0`, the first `aiNudgeTimer--` wraps to 0xFFFFFFFF. Either
    initialize in declaration (`var aiNudgeTimer = 72`) or set in `onPluginStart`.

38. **`$T()` inside `list()` works fine** — `$T()` returns a compile-time integer
    (map string index), not a py_str, so both `list()` and `[]` work. But use `list()`
    for consistency with other compile-time lists:
    ```javascript
    const banMessages = list(
        $T("\x06Player 1 has been banned!"),
        $T("\x06Player 2 has been banned!"),
    );
    ```

---

## Continuing From Previous Session

### What Has Been Converted to EPScript

All major systems are now in EPScript. The following classic triggers have been removed:

- ✅ Player death detection + delay timer (misc.eps)
- ✅ Invincibility system — rescue detection, temp/perm invul countdown (invincibility.eps)
- ✅ Pylon invincibility until round 70 (invincibility.eps)
- ✅ Alliance status setting (invincibility.eps onPluginStart)
- ✅ Patrol unit system — 7 units patrol 8 waypoints (misc.eps)
- ✅ Bonus critter spawn logic (misc.eps, via handlePatrolUnit)
- ✅ Wave spawning + beacon flash system (wave_spawns.eps)
- ✅ Countdown timer real-second tracking (countdownTimer.eps)
- ✅ Difficulty modifier — dat patches for HP/damage (difficultyModifier.eps)
- ✅ Reward system — kill bonuses for critters (RewardSystem.eps)
- ✅ Wave notifications (wave_spawns_notifications.eps)
- ✅ Victory/Defeat conditions (misc.eps beforeTriggerExec)
- ✅ Ban logic — 7 players, per-slot ban locations (misc.eps)
- ✅ AI nudge timer (misc.eps)

### Key EPScript Docs Links

```
Full reference:     https://havonz.github.io/SCRMapDocs/epScript-Reference/
Syntax:             https://havonz.github.io/SCRMapDocs/epScript-Reference/Syntax
Variables:          https://havonz.github.io/SCRMapDocs/epScript-Reference/Use-of-Variables
Functions:          https://havonz.github.io/SCRMapDocs/epScript-Reference/Use-of-Functions
Built-in functions: https://havonz.github.io/SCRMapDocs/epScript-Reference/Built-in-Functions
Built-in objects:   https://havonz.github.io/SCRMapDocs/epScript-Reference/Built-in-Object-Types
Understanding strs: https://havonz.github.io/SCRMapDocs/epScript-Reference/Understanding-Strings
euddraft reference: https://havonz.github.io/SCRMapDocs/euddraft-Reference
EUD database:       https://github.com/armoha/euddb
eudplib source:     https://github.com/armoha/eudplib
SCRMapDocs source:  https://github.com/Havonz/SCRMapDocs
```

### Quick Reminder: Trigger Conversion Workflow

1. Identify repeated per-player triggers → collapse with `EUDLoopPlayer(None, Force1)`
2. Identify repeated per-slot triggers → collapse with `foreach(i : py_range(N))` + `list(py_str(...))`
3. Replace `Set Switch("X", randomize)` + binary decode → `f_rand() % N`
4. Replace `Wait(N)` → frame counter (`var timer = N; timer--; if (timer == 0) { ... }`)
5. Replace `DisplayText` for one player → `setcurpl(player)` + `DisplayText` + restore
6. Replace `DisplayText` for all → `DisplayTextAll`
7. Compile-time strings in trigger actions must come from `py_str` lists or inline literals
8. Never put `CreateUnitWithProperties`, `GiveUnits`, `SetInvincibility`, `KillUnitAt` inside `DoActions()`
