# CPU Cat and Mouse — EPScript / EUD Editor 3 Development Guide

## Project Overview
StarCraft: Brood War 1.16.1 UMS map using EUD Editor 3 (EPScript / eudplib / euddraft).
Target euddraft version: 0.10.2.5

## IMPORTANT: Always Read Reference Docs Before Writing EPScript
Before writing or modifying ANY .eps file, read the relevant sections at:
	https://havonz.github.io/SCRMapDocs/epScript-Reference/

Key pages:
	Syntax:          https://havonz.github.io/SCRMapDocs/epScript-Reference/Syntax
	Variables:       https://havonz.github.io/SCRMapDocs/epScript-Reference/Use-of-Variables
	Functions:       https://havonz.github.io/SCRMapDocs/epScript-Reference/Use-of-Functions
	Built-in Funcs:  https://havonz.github.io/SCRMapDocs/epScript-Reference/Built-in-Functions

The full docs are also mirrored in: /SCRMapDocs-main/docs/epScript-Reference/

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

Files that are only data (no lifecycle functions) do NOT need to be listed in the .edd file.
They will be found automatically by import if they are in the same TriggerEditor directory.

Files that ARE listed in the .edd AND imported will compile TWICE, causing _1 suffix errors
on all variables. Only list a file in .edd if it has onPluginStart/beforeTriggerExec/afterTriggerExec.

There is no syntax for importing a single member from a module. You must import the whole module.

---

## EPScript: Variable and Constant Declaration

```javascript
const myArray   = EUDArray(10);        // compile-time reference, runtime indexable
const myVar     = EUDVariable(0);      // runtime variable, declared at module scope
var   localVar  = 0;                   // runtime variable, local scope
static var persistentVar = 0;          // retains value across calls
```

- const declares at COMPILE TIME. EUDVariable/EUDArray etc. are runtime objects.
- var is syntactic sugar for EUDVariable. Assignment uses = at runtime.
- All variables have FIXED memory addresses — everything is static internally.
- Module-level consts/vars must be declared BEFORE the functions that use them,
  otherwise EPScript renames them with _1 suffix and they become undefined inside functions.
- Do NOT initialize local vars without a value (var x;) if you want static behavior.
  Always explicitly set initial values (var x = 0;).

---

## EPScript: Arrays

```javascript
// EUDArray — fast for fixed compile-time index, slow for runtime variable index
const a = EUDArray(10);
a[0] = 29;

// EUDVArray — faster for runtime variable index, supports 2D
const b = EUDVArray(4)(list(1, 2, 3, 4));
const c = VArray(1, 2, 3, 4);   // shorthand

// 2D EUDVArray
const d = EUDVArray(60, EUDVArray(27))(list(
	VArray(30, 20, 0, ...),   // Round 1
	VArray(30, 20, 0, ...),   // Round 2
));
var val = d[round][unitIndex];  // runtime 2D access works correctly

// Use EUDVArray when the index is a runtime variable (loops, etc.)
// Use EUDArray when the index is always a compile-time constant
```

---

## EPScript: Functions

```javascript
// Lifecycle functions (only ONE of each per .eps file — duplicates cause compile errors)
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

## EPScript: Player Constants

```javascript
P1  P2  P3  P4  P5  P6  P7  P8   // players 1-8
P9  P10 P11 P12                   // neutral/special slots
AllPlayers
Force1  Force2  Force3  Force4
CurrentPlayer
```

Do NOT use "Player 8", "player 8", or integer 7. Use P8.

---

## EPScript: Unit and Location IDs

```javascript
$U("Terran Marine")     // compile-time unit integer ID — use this in EUDVArrays
$L("Location 1")        // compile-time location integer ID
$B("Terran Marine")     // stat_txt.tbl string index for unit

// String literals in action params are auto-converted at compile time:
CreateUnit(1, "Terran Marine", "Location 1", P1);
// is equivalent to:
CreateUnit(1, 0, someLocIndex, P1);
```

---

## EPScript: Conditions — Parameter Order

```javascript
// Command
Command(player, comparison, count, unit)
Command(P1, AtLeast, 5, "Terran Marine")    // CORRECT
Command(P1, "Terran Marine", AtLeast, 5)    // WRONG

// Kills
Kills(player, comparison, count, unit)
Kills(player, AtLeast, 1, 93)

// Deaths
Deaths(player, comparison, count, unit)

// Memory
Memory(address, comparison, value)

// Switch
Switch("SwitchName", Set)
Switch("SwitchName", NotSet)

// CountdownTimer
CountdownTimer(AtLeast, 5)    // use AtLeast/AtMost, NOT Exactly
CountdownTimer(AtMost, 30)    // Exactly can be missed since triggers don't poll every frame
                               // (unless using eudTurbo which runs every frame — then Exactly is safe)
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
	energy       = 100,    // energy %
	hanger       = 8,      // hangar count (interceptors/scarabs)
	resource     = 0,
	cloaked      = false,
	burrowed     = false,
	intransit    = false,
	hallucinated = false,
	invincible   = false)
);

// GiveUnits
GiveUnits(count, unit, sourcePlayer, location, destPlayer)
GiveUnits(1, "Terran Marine", P8, "TopLeftLing", P12)   // CORRECT
GiveUnits(1, "Terran Marine", "TopLeftLing", P8, P12)   // WRONG

// SetInvincibility — call DIRECTLY, NOT inside DoActions()
SetInvincibility(Enable, "(any unit)", AllPlayers, "HeroSelectorArea")
// order: (state, unit, owner, location)

// KillUnitAt — call DIRECTLY, NOT inside DoActions()
KillUnitAt(All, "(buildings)", "spawner", Force1)

// SetMemory / SetMemoryX
SetMemory(address, SetTo, value)
SetMemoryX(address, SetTo, value, mask)    // masked write

// SetSwitch
SetSwitch("SwitchName", Set)
SetSwitch("SwitchName", Clear)

// SetCountdownTimer
SetCountdownTimer(SetTo, 60)

// DoActions — use for grouping CLASSIC trigger actions only
// Actions like CreateUnitWithProperties, GiveUnits, SetInvincibility,
// KillUnitAt should be called DIRECTLY outside DoActions()
DoActions(
	CreateUnit(1, "Terran Marine", "Location 1", P1),   // simple CreateUnit can go inside
	SetMemory(addr, SetTo, value),
);
```

---

## EPScript: Memory Operations

```javascript
// Direct writes (preferred over SetMemoryX for clarity)
f_dwwrite(address, value)       // 32-bit write
f_wwrite(address, value)        // 16-bit write
f_bwrite(address, value)        // 8-bit write

// For upper 16 bits of a dword (0xffff0000 mask):
f_wwrite(address + 2, value)    // write to addr+2 with unshifted value
// e.g. Masked MemoryAddr(0x00660e98, Set To, 1310720000, 0xffff0000)
//   -> f_wwrite(0x00660e9a, 20000)   // 1310720000 >> 16 = 20000

// For lower 16 bits (0x0000ffff mask):
f_wwrite(address, value)        // same address, no shift needed

// For single byte (0x000000ff mask):
f_bwrite(address, value)

// HP values in BW dat are stored as HP * 256:
f_dwwrite(0x00662390, 50000 * 256)   // readable — 50000 actual HP

// EPD address formula: EPD(addr) = (addr - 0x58A364) / 4
// Kill counter address: 0x005878A4 + (unitID * 12 + (player - 1)) * 4
```

---

## EPScript: Randomization

```javascript
f_rand()            // returns random 32-bit unsigned integer
f_rand() % 4       // 0-3
f_rand() % 4 + 1   // 1-4
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

ALWAYS use TABS, never spaces.

---

## EPScript: Common Pitfalls

1. **Duplicate lifecycle functions** — only ONE beforeTriggerExec/afterTriggerExec per file.
   Duplicates break all variable name resolution in that file.

2. **Module prefix required** — `import Foo; Foo.myVar` not `myVar`.

3. **Consts before functions** — module-level consts must appear before functions that reference them.

4. **for/in loop doesn't exist** — no `for (unit in array)`. Use `foreach(i : py_range(0, N))`.

5. **py_range upper bound is exclusive** — `py_range(1, 7)` = players 1,2,3,4,5,6 (NOT 7).

6. **Wait() in afterTriggerExec is dangerous** — blocks the entire EUD loop.
   Use frame counters (spawnTimeCounter--) or countdown timers instead.

7. **count = 0 does nothing to a VArray** — to zero out a slot:
   `myVArray[round][index] = 0;`  not  `var count = myVArray[...]; count = 0;`

8. **Double-compile causes _1 suffix** — if a file is in the .edd AND imported by another plugin,
   it compiles twice and all its variables get renamed. Fix: remove it from .edd.

9. **EUDVArray for runtime indexes** — use EUDVArray, not EUDArray, when indexing with variables.

10. **py_str vs $U** — `$U("unit name")` gives the integer unit ID usable at runtime.
    `py_str` is compile-time only and cannot be used directly in runtime actions.
    `CreateUnitWithProperties(count, $U("Terran Marine"), ...)` works.

11. **foreach with py_range is compile-time** — it unrolls at compile time.
    Cannot use break/continue inside. For runtime loops use while or EUDLoopRange.

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
| DifficultyChosen | Difficulty has been selected |
| HardModeEnabled | Hard mode is active |
| EUDUnitsPlaced | Difficulty modifier has already run |
| ReduceSpawnsForNumPlayers | Use split spawn counts scaled by player count |
| SpawnExtra | Wave has finished spawning, signal for hard mode extras |
| ExtraSpawn1 / ExtraSpawn2 | Used to select which hard mode extra unit to spawn |

---

## Project: Key Memory Addresses

```
Kill counters:     0x005878A4 + (unitID * 12 + (player - 1)) * 4
HP (dat):          0x00662000 + offsets (HP stored as actual * 256)
Shield (dat):      0x00660E00 + offsets (stored as actual value, lower or upper 16 bits)
Armor (dat):       0x0065FF00 + offsets (1 byte per unit)
Weapon damage:     0x00656E00 + offsets
Weapon bonus:      0x00657600 + offsets
Vespene cost:      0x0065FD80 + offsets
```

---

## Project: Wave Spawn System

Wave data is generated by `generate_eps.py` from CSVs:
- `wave_spawns_full.csv` → `WaveSpawnsFull.eps` (waveSpawnsFull1, waveSpawnsFull2)
- `wave_spawns_split.csv` → `WaveSpawnsSplit.eps` (WaveSpawnsSplit1, WaveSpawnsSplit2)
- Hard mode options → `HardModeSpawnsFull.eps`, `HardModeSpawnsSplit.eps`
- Unit index lookup → `wave_spawns_indexes.eps` (waveSpawnsUnitIndex, NUM_UNITS)

Unit index order (0-26):
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

Spawn logic (wave_spawns.eps):
- roundStep 1: randomize spawner locations, reduce counts if ReduceSpawnsForNumPlayers
- roundStep 2: kill buildings at active spawners, begin spawning
- roundStep 3: loop through unit indices, spawn non-zero with 48-frame (3 sec) gaps
- roundStep 4: hard mode bonus spawns (same loop, uses hardRoll 1-4 to pick array)
- roundStep 99: idle, waiting for next round reset

---

## Project: File Structure

```
maps/
	CPU Cat and Mouse/
		EUD_cpu_cat_survival_*.scx        (pre-EUD source map)
		EUD_cpu_cat_survival_*_postEUD.scx (compiled output)
TriggerEditor/
	common.eps              shared vars (numActivePlayers), beforeTriggerExec
	wave_spawns_indexes.eps NUM_UNITS constant + waveSpawnsUnitIndex array
	WaveSpawnsFull.eps      full spawn counts (spawner1 + spawner2)
	WaveSpawnsSplit.eps     per-player split counts
	HardModeSpawnsFull.eps  hard mode bonus options 1-4
	HardModeSpawnsSplit.eps hard mode split bonus options 1-4
	wave_spawns.eps         wave spawning logic
	difficultyModifier.eps  easy mode dat patching + hero unit placement
	RewardSystem.eps        kill bonus civilian rewards
	main.eps                MSQC boilerplate, mostly blank
SCRMapDocs-main/            EPScript reference documentation (local mirror)
generate_eps.py             Python script — generates all EUDVArray .eps from CSVs
wave_spawns_full.csv        full spawn data per round
wave_spawns_split.csv       split (per-player) spawn data per round
```
