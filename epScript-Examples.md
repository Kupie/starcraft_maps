# epScript Example Projects

> Four complete, working reference projects showing real epScript patterns.
> Each includes the `.edd` config and full `main.eps` source.
> Use these as style/pattern guides when writing epScript.

---

## Project 1: Trigger-and-RawTrigger

**What it shows:** The difference between `Trigger()` and `RawTrigger()`, `preserved = false` for one-shot triggers, using a variable in a condition (requires `Trigger` not `RawTrigger`), `DoActions()`, `GiveUnits`, `Order`, `Bring`, `KillUnitAt`, `CreateUnit`.

### makefile.edd
```ini
[main]
input: Trigger-and-RawTrigger-Terrain.scx
output: Trigger-and-RawTrigger.scx

[eudTurbo]
[main.eps]
```

### main.eps
```javascript
var NextWaveTime = 3;

function doTriggerList() {
	// Unconditional trigger that only fires once
	DoActions(CreateUnit(1, "Terran SCV", "Location 2", P1), preserved = false);

	// Unconditional trigger that only fires once
	DoActions(CreateUnit(1, "Zerg Zergling", "Location 1", P1), preserved = false);

	// Trigger that fires every 3 game seconds
	// NOTE: Must use Trigger() (not RawTrigger) when a condition references a variable
	Trigger(
		conditions = list(
			ElapsedTime(AtLeast, NextWaveTime),
		),
		actions = list(
			GiveUnits(1, "Zerg Zergling", P1, $L("Location 1"), P12),
			Order("Zerg Zergling", P12, $L("Location 1"), Move, $L("Location 3")),
			NextWaveTime.AddNumber(3), // push threshold forward 3s for next fire
			CreateUnit(1, "Zerg Zergling", "Location 1", P1),
		),
	);

	// RawTrigger: kills P12 zerglings that enter Location 3 (repeating)
	RawTrigger(
		conditions = list(
			Bring(P12, AtLeast, 1, "Zerg Zergling", $L("Location 3")),
		),
		actions = list(
			KillUnitAt(10, "Zerg Zergling", "Location 3", P12),
		),
	);

	// RawTrigger: one-shot — turns 1 P1 zergling into 10 on reaching Location 3
	RawTrigger(
		conditions = list(
			Bring(P1, AtLeast, 1, "Zerg Zergling", $L("Location 3")),
		),
		actions = list(
			CreateUnit(9, "Zerg Zergling", "Location 3", P1),
		),
		preserved = false,
	);
}

function onPluginStart() {

}

function beforeTriggerExec() {
	const cp = getcurpl();

	// other per-frame logic here

	setcurpl(cp);
	doTriggerList();
}

function afterTriggerExec() {

}
```

**Key patterns:**
- `Trigger()` is required (instead of `RawTrigger`) whenever a condition references an `EUDVariable` at runtime, because `RawTrigger` conditions are baked in at compile time.
- `preserved = false` makes a trigger fire exactly once then deactivate.
- Always save/restore `getcurpl()` around any `setcurpl()` calls.
- Call trigger-building functions like `doTriggerList()` after restoring `curpl`.

---

## Project 2: ChangeSupplyLimit

**What it shows:** `onPluginStart` one-time setup, direct memory writes via `dwwrite_epd`, `bwrite`, `wwrite`, `EPD()` arithmetic for struct field access, typed parameters (`: TrgPlayer`, `: TrgUnit`, `: Weapon`), `$U()` / `Weapon` string-to-ID macros, `SetResources`, `CreateUnit` inside `RawTrigger`.

### makefile.edd
```ini
[main]
input: ChangeSupplyLimit-Terrain.scx
output: ChangeSupplyLimit.scx

[main.eps]
```

### main.eps
```javascript
// EUDDB: https://armoha.github.io/eud-book/

const SUP_RACE_ZERG    = 0;
const SUP_RACE_TERRAN  = 1;
const SUP_RACE_PROTOSS = 2;
const SUP_TYPE_AVAILABLE = 0;
const SUP_TYPE_USED      = 1;
const SUP_TYPE_MAX       = 2;

// Supply table: 0x582144 + race*36 + type*12 + player  (each entry is a dword)
function SetPlayerSupply(player : TrgPlayer, race, type, amount) {
	dwwrite_epd(EPD(0x582144) + (race) * 36 + (type) * 12 + (player), amount);
}

function GetPlayerSupply(player : TrgPlayer, race, type) {
	return dwread_epd(EPD(0x582144) + (race) * 36 + (type) * 12 + (player));
}

// units.dat fields (byte/word arrays indexed by unit ID)
function SetUnitSupplyProvided(ut : TrgUnit, amount) {
	bwrite(0x6646C8 + ut * 1, amount);
}

function SetUnitSupplyRequired(ut : TrgUnit, amount) {
	bwrite(0x663CE8 + ut * 1, amount);
}

function SetUnitMineralCost(ut : TrgUnit, amount) {
	wwrite(0x663888 + ut * 2, amount);
}

function SetUnitGasCost(ut : TrgUnit, amount) {
	wwrite(0x65FD00 + ut * 2, amount);
}

function SetUnitBuildTime(ut : TrgUnit, frames) {
	wwrite(0x660428 + ut * 2, frames);
}

// weapons.dat cooldown field (byte array indexed by weapon ID)
function SetWeaponCooldown(wt : Weapon, frames) {
	bwrite(0x656FB8 + wt, frames);
}

function onPluginStart() {
	// Set max supply to 500 (stored *2 internally) for all races for P1
	SetPlayerSupply(P1, SUP_RACE_ZERG,    SUP_TYPE_MAX, 1000);
	SetPlayerSupply(P1, SUP_RACE_TERRAN,  SUP_TYPE_MAX, 1000);
	SetPlayerSupply(P1, SUP_RACE_PROTOSS, SUP_TYPE_MAX, 1000);

	SetUnitSupplyRequired($U("Terran SCV"), 0);  // SCV costs 0 supply
	SetUnitMineralCost($U("Terran SCV"), 0);     // SCV costs 0 minerals
	SetUnitBuildTime($U("Terran SCV"), 10);      // SCV builds in 10 frames (min ~6)

	SetUnitSupplyProvided($U("Terran Command Center"), 200); // CC gives 100 supply
	SetUnitSupplyProvided($U("Terran SCV"), 200);            // SCV gives 100 supply
	SetUnitSupplyProvided($U("Terran Ghost"), 200);          // Ghost gives 100 supply

	SetWeaponCooldown("C-10 Concussion Rifle", 0); // Ghost fires as fast as possible

	setcurpl(P1);
	RawTrigger(
		actions = list(
			CreateUnit(1, "Terran Command Center", "Location 1", P1),
			CreateUnit(2, "Terran SCV",            "Location 2", P1),
			CreateUnit(2, "Terran Ghost",           "Location 2", P1),
			SetResources(P1, Add, 100000, OreAndGas),
		),
		preserved = false,
	);
}

function beforeTriggerExec() {

}

function afterTriggerExec() {

}
```

**Key patterns:**
- All dat-file edits (`bwrite`/`wwrite`/`dwwrite_epd`) go in `onPluginStart()` — they only need to happen once.
- Supply values are stored internally as `display_value * 2`.
- `EPD(address)` converts an absolute memory address to the EPD offset used by `dwread_epd`/`dwwrite_epd`.
- Function parameters typed with `: TrgUnit`, `: TrgPlayer`, `: Weapon` etc. allow passing string names like `$U("Terran SCV")` and have them auto-resolved to IDs at compile time.

---

## Project 3: UsePosition

**What it shows:** `CUnit` field access (`.posX`/`.posY` via `getpos`), `atan2_256`, `lengthdir_256`, `sqrt`, `cunitepdread_cp`, `setcurpl(EPD(...))` (CP trick for reading the newest unit), `set_invincible()`, `once {}` and `once (cond) {}`, `printAt`, multi-return functions, version-branching with a static bool.

### makefile.edd
```ini
[main]
input: UsePosition-Terrain.scx
output: UsePosition.scx

[eudTurbo]
[main.eps]
```

### main.eps
```javascript
// Detect euddraft version: atan2_256(10,10) >= 90 means 0.9.9.8+
function _0998_above() {
	static var is0998above = false;
	once is0998above = l2v(atan2_256(10, 10) >= 90);
	return is0998above;
}

// Angle (in 256-unit circle) from point (x1,y1) to point (x2,y2)
function angleBetween_256(x1, y1, x2, y2) {
	if (_0998_above()) {
		return atan2_256(y2 - y1, x2 - x1);
	}
	return atan2_256(x2 - x1, y1 - y2);
}

// Euclidean distance between two points
function distanceBetween(x1, y1, x2, y2) {
	const x = x2 - x1;
	const y = y2 - y1;
	return sqrt(x*x + y*y);
}

// Project point (x0,y0) by (length) units in direction (angle/256 circle)
function polarProjection_256(x0, y0, length, angle) {
	var dx, dy;
	if (_0998_above()) {
		dx, dy = lengthdir_256(length, angle);
		return x0 + dx, y0 + dy;
	} else {
		dx, dy = lengthdir_256(length, 320 - angle);
		return x0 + dx, y0 - dy;
	}
}

var marine_epd, ghost_epd = 0, 0;

function onPluginStart() {

}

function beforeTriggerExec() {
	const cp = getcurpl();

	// CP trick: setcurpl to the "first unit" pointer to read newly created units
	once (ElapsedTime(AtLeast, 0)) {
		const cp2 = getcurpl();
		setcurpl(EPD(0x628438)); // 0x628438 = pointer to most-recently-created unit
		{
			const ptr, epd = cunitepdread_cp(0);
			CreateUnit(1, "Terran Marine", "Location 1", P1);
			if (ptr != 0) {
				marine_epd = epd;
			}
		}
		{
			const ptr, epd = cunitepdread_cp(0);
			CreateUnit(1, "Terran Ghost", "Location 2", P1);
			if (ptr != 0) {
				ghost_epd = epd;
			}
		}
		setcurpl(cp2);
	}

	if (marine_epd != 0 && ghost_epd != 0) {
		const marine_cu = CUnit(marine_epd);
		const ghost_cu  = CUnit(ghost_epd);

		once {
			ghost_cu.set_invincible();
			marine_cu.set_invincible();
		}

		const x0, y0 = marine_cu.getpos("pos");
		const x1, y1 = ghost_cu.getpos("pos");
		const ang     = angleBetween_256(x0, y0, x1, y1);
		const dist    = distanceBetween(x0, y0, x1, y1);
		const x, y    = polarProjection_256(x0, y0, dist, ang);

		setcurpl(P1);
		printAt(0, "Marine({},{})(Face:{}) -> Ghost({},{})(Face:{}) dist={} angle={}",
			x0, y0, marine_cu.currentDirection2,
			x1, y1, ghost_cu.currentDirection2,
			dist, ang);
		printAt(1, "Walking dist={} at angle={} from Marine reaches ({}, {})", dist, ang, x, y);
	}

	setcurpl(cp);
}

function afterTriggerExec() {

}
```

**Key patterns:**
- `setcurpl(EPD(0x628438))` is the "CP trick" — points current player at the most-recently-created-unit pointer so `cunitepdread_cp(0)` reads it.
- Read the EPD *before* creating the unit; after `CreateUnit` that slot holds the new unit.
- `CUnit(epd)` wraps an EPD into a CUnit object for field access.
- `once { }` (no condition) executes exactly once ever. `once (cond) { }` executes once after the condition first becomes true.
- `static var` inside a function persists across calls (not reset each frame).
- Angles use a 256-unit full circle (not degrees or radians). `lengthdir_256` / `atan2_256` work in this space.

---

## Project 4: [MSQC]GameSpeedTextMenu

**What it shows:** `MSQC` plugin integration, `PVariable` (per-player variable array), `EUDRegisterObjectToNamespace`, `StringBuffer` with `printfAt`/`insert`/`append`/`appendf`/`DisplayAt`, `EUDLightBool`, `RawTrigger` with `isMouseOvered[i].IsCleared()` condition, `foreach(p : EUDLoopPlayer("Human"))`, `dwwrite_epd` for live game speed editing, `PColor`/`PName`, `PlayWAV`, `MemoryEPD`, `getcurpl()`/`getuserplayerid()` distinction for local-only actions.

### makefile.edd
```ini
[main]
input: GameSpeedTextMenu-Terrain.scx
output: GameSpeedTextMenu.scx

[main.eps]
[eudTurbo]

[MSQC]
QCDebug : 0
QCUnit : 218
; Each line: memory conditions ; MouseDown(L): variable, value_to_set
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 129;0x6CDDC8, AtMost, 139;MouseDown(L): menuSel, 50
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 145;0x6CDDC8, AtMost, 155;MouseDown(L): menuSel, 100
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 161;0x6CDDC8, AtMost, 171;MouseDown(L): menuSel, 125
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 177;0x6CDDC8, AtMost, 187;MouseDown(L): menuSel, 150
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 193;0x6CDDC8, AtMost, 203;MouseDown(L): menuSel, 200
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 209;0x6CDDC8, AtMost, 219;MouseDown(L): menuSel, 400
0x6CDDC4, AtLeast, 10;0x6CDDC4, AtMost, 25;0x6CDDC8, AtLeast, 225;0x6CDDC8, AtMost, 235;MouseDown(L): menuSel, 4200
```

### main.eps
```javascript
// EUDDB: https://armoha.github.io/eud-book/

// Write the milliseconds-per-frame value for a given game speed slot
// level 6 = Fastest. speed is a percentage where 100% = normal Fastest timing.
// mspf = 1,000,000 / (10000/42 * speed%)
function SetGameSpeed(level, speed) {
	const mspf = 1000000 / (10000 / 42 * speed);
	dwwrite_epd(EPD(0x5124D8) + level, mspf);
}

const MOUSE_X_EPD = EPD(0x6CDDC4);
const MOUSE_Y_EPD = EPD(0x6CDDC8);

// PVariable = one EUDVariable per player slot (array indexed by player ID)
const menuSel = PVariable();
var currentSpeedSel;

// Register menuSel so the MSQC plugin can write into it by name
EUDRegisterObjectToNamespace("menuSel", menuSel);

function showMenu(p) {
	const speedList = 50, 100, 125, 150, 200, 400, 4200;
	// One EUDLightBool per menu item to track hover state
	const isMouseOvered =
		EUDLightBool(), EUDLightBool(), EUDLightBool(), EUDLightBool(),
		EUDLightBool(), EUDLightBool(), EUDLightBool();

	if (getcurpl() == p) {
		const buf = StringBuffer(255);

		// Line 0: current speed header
		buf.printfAt(0, "\x02Currently selected game speed: \x07{}\x02%\x02", currentSpeedSel);

		// Lines 1-7: menu items
		foreach(i : py_range(0, 7)) {
			buf.insert(0); // reset buffer to empty
			if (speedList[i] == currentSpeedSel) {
				buf.append("\x03[\x07x\x03]\x1E ");
			} else {
				buf.append("\x03[  ]\x02");
			}
			buf.appendf(" Game Speed {}%\x02", speedList[i]);
			buf.DisplayAt(i + 1);
		}

		// Highlight hovered item if mouse is in the menu X range
		if (MemoryEPD(MOUSE_X_EPD, AtLeast, 10) && MemoryEPD(MOUSE_X_EPD, AtMost, 25)) {
			foreach(i : py_range(0, 7)) {
				if (MemoryEPD(MOUSE_Y_EPD, AtLeast, 129 + i * 16) &&
				    MemoryEPD(MOUSE_Y_EPD, AtMost,  139 + i * 16)) {
					if (speedList[i] != currentSpeedSel) {
						buf.insert(0);
						buf.append("\x07[  ]\x1E ");
						buf.appendf(" Game Speed {}%\x02", speedList[i]);
						buf.DisplayAt(i + 1);
						// Play hover sound once per enter
						RawTrigger(
							conditions = isMouseOvered[i].IsCleared(),
							actions = list(
								PlayWAV("sound\\glue\\mouseover.wav"),
								isMouseOvered[i].Set(),
							),
						);
					}
				} else {
					RawTrigger(actions = isMouseOvered[i].Clear());
				}
			}
		} else {
			// Mouse left menu entirely — clear all hover states
			const clearActions = py_list();
			foreach(v : isMouseOvered) {
				clearActions.append(v.Clear());
			}
			RawTrigger(actions = clearActions);
		}
	}
}

function onPluginStart() {
	currentSpeedSel = 100;
	SetGameSpeed(6, currentSpeedSel); // Set Fastest speed to 100%
}

function beforeTriggerExec() {
	const cp = getcurpl();

	// Spawn overlords at Location 1 for MSQC to detect clicks (unit 218 = Overlord)
	RawTrigger(actions = list(
		CreateUnitWithProperties(1, "Zerg Overlord", "Location 1", P1, UnitProperty(invincible = true)),
		CreateUnitWithProperties(1, "Zerg Overlord", "Location 1", P2, UnitProperty(invincible = true)),
	), preserved = false);

	// Show menu to every human player
	foreach(p : EUDLoopPlayer("Human")) {
		setcurpl(p);
		showMenu(p);
	}

	setcurpl(cp);
}

function afterTriggerExec() {
	// MSQC writes menuSel[p] = chosen_speed when player p clicks a menu item.
	// We pick it up here and sync it to all machines.
	foreach(p : EUDLoopPlayer("Human")) {
		if (menuSel[p] != 0) {
			currentSpeedSel = menuSel[p]; // sync-data: all machines run this
			menuSel[p] = 0;

			SetGameSpeed(6, currentSpeedSel);

			// Local-only display (desync-safe because it's display only)
			setcurpl(getuserplayerid());
			if (p == getuserplayerid()) {
				PlayWAV("sound\\glue\\mousedown2.wav");
				printAt(10, "You change the game speed to \x07{}\x02%", currentSpeedSel);
			} else {
				PlayWAV("sound\\misc\\transmission.wav");
				printAt(10, "{}{} \x02changes the game speed to \x07{}\x02%",
					PColor(p), PName(p), currentSpeedSel);
			}
		}
	}
}
```

**Key patterns:**
- `PVariable()` creates an array of one variable per player, indexed `menuSel[p]`.
- `EUDRegisterObjectToNamespace("name", obj)` exposes an epScript object to MSQC (or other plugins) by name.
- MSQC plugin lines in `.edd`: memory address conditions followed by `MouseDown(L): varName, value` — MSQC writes `value` into the named variable when click conditions are met. This is desync-safe because MSQC uses the game command queue.
- `getcurpl()` vs `getuserplayerid()`: `getcurpl()` is the synchronized "current player" used for trigger targeting. `getuserplayerid()` is the local machine's actual player ID (desync-safe for display only).
- `beforeTriggerExec` handles display and input detection; `afterTriggerExec` handles the synchronized state update that results from MSQC input.
- `buf.insert(0)` resets the StringBuffer position to 0 before rewriting it.
- `\x02`=white, `\x03`=yellow, `\x07`=green, `\x1E`=no-color in SC text color codes.

---

## Common Boilerplate

### Minimal .edd config
```ini
[main]
input: basemap.scx
output: output.scx

[eudTurbo]
[main.eps]
```

### Minimal main.eps shell
```javascript
function onPluginStart() {
	// One-time setup: dat edits, memory writes, initial unit creation
}

function beforeTriggerExec() {
	const cp = getcurpl();

	// Per-frame logic before classical triggers

	setcurpl(cp); // always restore before returning or calling trigger builders
}

function afterTriggerExec() {
	// Per-frame logic after classical triggers
}
```

### build.bat pattern
```bat
@copy makefile.edd makefile.eds
@C:\path\to\euddraft.exe makefile.eds
@del /f /q makefile.eds
@pause
```
