# CLAUDE.md — CPU Cat and Mouse: EPScript/EUD Reference

SC Version: 1.16.1 | euddraft: 0.10.2.5 | EUD Editor v3: 0.19.6.0

---

## Project Overview

Mice (Probes, P1–P7) vs CPU cat waves (P8). Players build Pylons (invincible until round 70),
earn Terran Civilians as currency by killing bonus critters, and rescue dead teammates.
EUD Editor 3, euddraft 0.10.2.5, EPScript.

---

## Code Style

- Always use **tabs**, never spaces, for indentation
- Separate trigger blocks with `//-----------------------------------------------------------------//`
- Do NOT use `//` comments inside trigger text blocks (invalid in SC trigger syntax)
- Use decimal unit IDs over strings where possible in EUD memory work
- `UnitProperty()` always inline, never stored as a variable

---

## Project: Player Slots

| Slot | Role |
|------|------|
| P1–P7 | Human mice (Force1) |
| P8 | Cat spawner CPU |
| P9 | Bonus critter / patrol unit owner |
| P11 | Beacon/neutral tracker |
| P12 | Hero unit owner + shop token pool |

---

## Project: Key Switches

| Switch | Meaning |
|--------|---------|
| DifficultyChosen | Difficulty has been selected |
| EasyModeEnabled | Easy mode is active (dat patches applied) |
| HardModeEnabled | Hard mode is active |
| EUDUnitsPlaced | Difficulty modifier has already run once, skip it |
| ReduceSpawnsForNumPlayers | Scale spawns by player count using split CSV data |
| GameStarted | Game is running (most EPS logic gates on this) |
| pylon invuln | Pylons are still invincible |
| Long Invulnerability | Rescue grants permanent instead of temporary invincibility |
| Rescue | Rescue system is enabled |
| Ban | Ban system is enabled |

Do NOT change these switch names.

---

## Project: Key Locations

| Location | Purpose |
|----------|---------|
| spawner | Primary enemy spawn point (randomized each wave) |
| spawner2 | Secondary enemy spawn point (randomized each wave) |
| playground | Main play area — all combat happens here |
| getprobe | Where probe is moved to each frame from pSpawn |
| pSpawn | Where rescued probes are created |
| Start | Where flags are created for dead players |
| getbonus | Where bonus civilians are created for players |
| bonusSpawner | Temp location for critter spawning (set via setloc each time) |
| BeaconPlacer | Temp location for placing beacon warning units |
| o1,o2,o22,o3,o31,o4,o44,o5 | Patrol waypoints for bonus critters and Duran |
| noair, noair2 | Parking zones for unused air units |
| HeroSelectorArea | Area where hero units are displayed for purchase |

Do NOT change these location names.

---

## Project: File Structure

```
maps/
    CPU Cat and Mouse/
        EUD_cpu_cat_survival_*.scx            source map (pre-EUD)
        EUD_cpu_cat_survival_*_postEUD.scx    compiled output
TriggerEditor/
    common_vars.eps         shared vars (currentRound, tempInvulFrameAmount, etc.)
    common.eps              AI nudge timer, pause setter
    invincibility.eps       rescue detection, pylon invuln, temp/perm invul countdown
    misc.eps                death delay logic, patrol units (critters + Duran)
    RewardSystem.eps        kill bonus civilians, SetKills to reset counters
    wave_spawns.eps         wave spawning logic, beacon flash, roundStep state machine
    wave_spawns_indexes.eps NUM_UNITS, waveSpawnsUnitIndex, waveNotifyStrings (pre-built)
    wave_spawns_notifications.eps   DisplayTextAll wave notifications
    countdownTimer.eps      real-second countdown via getgametick(), PauseTimer in onPluginStart
    difficultyModifier.eps  dat patches for easy mode, hero unit placement
    WaveSpawnsFull.eps      full spawn count arrays — DO NOT EDIT MANUALLY
    WaveSpawnsSplit.eps     per-player split count arrays — DO NOT EDIT MANUALLY
    HardModeSpawnsFull.eps  hard mode bonus options 1-4 — DO NOT EDIT MANUALLY
    HardModeSpawnsSplit.eps hard mode split bonus options 1-4 — DO NOT EDIT MANUALLY
generate_eps.py             generates all EUDVArray .eps files from CSVs
wave_spawns_full.csv        full spawn data (source of truth)
wave_spawns_split.csv       per-player split spawn data (source of truth)
```

---

## Project: .edd Load Order

Files are loaded in .edd order. `onPluginStart` runs in load order, `afterTriggerExec` runs in
**reverse** load order. Only files with lifecycle functions should be in the .edd. Data-only files
cause double-compile if listed in .edd — import only.

Files in .edd (have lifecycle functions):
- invincibility.eps
- misc.eps
- RewardSystem.eps
- common.eps
- difficultyModifier.eps
- main.eps
- countdownTimer.eps
- wave_spawns.eps
- wave_spawns_indexes.eps
- wave_spawns_notifications.eps

Files NOT in .edd (data only, accessed via import):
- WaveSpawnsFull.eps
- WaveSpawnsSplit.eps
- HardModeSpawnsFull.eps
- HardModeSpawnsSplit.eps
- common_vars.eps

---

## Project: Wave Spawn State Machine (wave_spawns.eps)

| Step | Countdown | Action |
|------|-----------|--------|
| 99→1 | Exactly 10 | increment currentRound, reset index, hardRoll = 0 |
| 1→2 | Exactly 9 | randomize spawners, place beacons, reduce spawns, roll hardRoll |
| 2 | loop | beacon flash loop (beaconFlashCounter), transition when countdown == 0 |
| 2→3 | Exactly 0 | kill buildings+beacons, SetCountdownTimer(60), start spawning |
| 3 | loop | normal spawning loop, 64-frame gaps between unit groups |
| 3→4 | after all units | if HardModeEnabled, reset index for hard mode |
| 4 | loop | hard mode spawns using hardRoll 1-4 |
| 4→99 | after hard units | done |

---

## Project: Key Memory Addresses

```
Kill counters:     0x005878A4 + (unitID * 12 + (player - 1)) * 4
HP (dat):          stored as actual HP * 256  (use f_dwwrite)
Shield (dat):      16-bit value               (use f_wwrite)
Armor (dat):       1 byte per unit            (use f_bwrite)
Weapon damage:     16-bit                     (use f_wwrite)
Weapon bonus:      16-bit                     (use f_wwrite)
Vespene cost:      16-bit                     (use f_wwrite)
Probe speed:       0x6C9FA0                   (use SetMemory or f_dwwrite)
Pause duration:    0x0058d718                 (use dwwrite)
```

HP example: `f_dwwrite(0x00662390, 50000 * 256);` — Sarah Kerrigan Ghost

---

## Project: Bonus Critter / Patrol Unit System (misc.eps)

7 units patrol 8 waypoints (o1, o2, o22, o3, o31, o4, o44, o5): 6 bonus critters + Samir Duran.
2 of each kept alive at all times. Staggered patrol timers: `patrolTimers[i] = 80 + i * 13`.

Kill rewards (by unit ID):
| Unit | ID | Reward |
|------|----|--------|
| Rhynadon (Badlands) | 89 | 2 civilians |
| Bengalaas (Jungle) | 90 | 1 civilian |
| Scantid (Desert) | 93 | 2 civilians |
| Kakaru (Twilight) | 94 | 1 civilian |
| Ragnasaur (Ash World) | 95 | 2 civilians |
| Ursadon (Ice World) | 96 | 3 civilians |
| Samir Duran (Ghost) | 99 | 1 civilian |

---

## Project: Wave Spawn Data

Generated by `generate_eps.py` from CSVs. Never edit these .eps files manually.

Unit index order (0-26):
```
 0  Zerg Ultralisk                        14  Artanis (Scout)
 1  Terran Firebat                        15  Zerg Devourer
 2  Protoss Reaver                        16  Fenix (Zealot)
 3  Infested Kerrigan (Infested Terran)   17  Yggdrasill (Overlord)
 4  Edmund Duke (Tank Mode)               18  Alan Schezar (Goliath)
 5  Tassadar (Templar)                    19  Kukulza (Guardian)
 6  Hunter Killer (Hydralisk)             20  Norad II (Battlecruiser)
 7  Torrasque (Ultralisk)                 21  Dark Templar (Hero)
 8  Zeratul (Dark Templar)                22  Sarah Kerrigan (Ghost)
 9  Tom Kazansky (Wraith)                 23  Danimoth (Arbiter)
10  Jim Raynor (Marine)                   24  Protoss Observer
11  Fenix (Dragoon)                       25  Kukulza (Mutalisk)
12  Zerg Zergling                         26  Gantrithor (Carrier)
13  Alexei Stukov (Ghost)
```

---

## EPScript: Lifecycle Functions

Three lifecycle functions, executed every frame in order:

```
onPluginStart()       — runs once at game start, initialization only
beforeTriggerExec()   — runs BEFORE classic triggers each frame
afterTriggerExec()    — runs AFTER classic triggers each frame (reverse .edd order)
```

Only ONE of each per file. Having duplicates silently breaks all variable name
resolution (_1 suffix on everything). Classic triggers run between before and after.

---

## EPScript: Compile-time vs Runtime

This is the most important concept in EPScript. Everything is either compile-time (Python,
happens when building the map) or runtime (EUDVariable, happens in-game).

| Feature | Compile-time | Runtime |
|---------|-------------|---------|
| `const x = 5` | ✓ Python integer | — |
| `var x = 5` | — | ✓ EUDVariable |
| `py_range(N)` | ✓ always fixed count | — |
| `EUDLoopPlayer()` | — | ✓ active players only |
| `py_str("name")` | ✓ string constant | — |
| `$T("string")` | ✓ map string index | — |
| `$U("unit name")` | ✓ integer unit ID | — |
| `$L("location")` | ✓ integer location ID | — |
| `$S("switch")` | ✓ integer switch ID | — |
| Function parameters | — | ✓ become EUDVariables |
| `EUDArray[constIdx]` | ✓ fast | — |
| `EUDVArray[varIdx]` | — | ✓ runtime index |

**Critical rule**: Trigger action parameters (unit names, location names, counts in
`Command`, `CreateUnit`, etc.) must be compile-time constants. You cannot pass a
runtime variable as a unit name or location name to classic trigger actions.

---

## EPScript: Variables

```javascript
var x = 0;           // runtime EUDVariable, reassignable with =
const x = 5;         // compile-time Python constant, cannot be reassigned
const arr = EUDArray(7);    // object reference — const correct, arr[i] assignable
static var x = 0;    // explicit static; retains value across calls (same as var x;)
var x;               // WARNING: no initializer = static behavior, retains value!
```

**WRONG** — causes `_1` suffix errors:
```javascript
const x = EUDVariable(0);
x += 1;   // ERROR: const cannot be assigned with =
```

**CORRECT**:
```javascript
var x = 0;
x += 1;   // OK: var compiles = to <<
```

All variables have **fixed memory addresses** — everything is static internally.
A local `var y = 0` inside a function resets to 0 on each call because of the initializer.
A local `var y;` (no initializer) retains its value between calls — this is a footgun.

`SubtractNumber` on EUDVariable **cannot go below 0** — it clamps at 0.
Use `x -= 1` (which uses the `-` operator) if you need wrap-around behavior.

---

## EPScript: Arrays

```javascript
const a = EUDArray(N);              // fast for compile-time index, use const
const b = EUDVArray(N)(list(...));  // supports runtime variable index, 2D possible
const c = [3, 2, 1];               // EUDArray shorthand with initializers
const d = list(py_str("x"), py_str("y"));  // compile-time list of strings
```

**CRITICAL**: Use `list()` NOT `[]` for compile-time py_str arrays:
```javascript
const units = list(py_str("Terran Marine"), py_str("Zerg Zergling"));  // CORRECT
const units = [py_str("Terran Marine"), py_str("Zerg Zergling")];      // WRONG — creates EUDArray, fails on py_str
```

`EUDArray` with a runtime variable index works but is slow.
`EUDVArray` is specifically designed for runtime variable indexing and is much faster.

Player indexing: **P1=0, P2=1...P7=6** internally. Use `player` directly as array
index — `player - 1` underflows for P1 (wraps to 0xFFFFFFFF).

---

## EPScript: Imports

```javascript
import common_vars;              // import module
import common_vars as cv;        // import with alias
cv.myVar                         // access with module prefix — ALWAYS required
```

**Double-compile**: If a file is in the .edd AND imported elsewhere, it compiles twice,
causing `_1` suffix errors on all variables. Only list files with lifecycle functions
in the .edd. Data-only files: import only, never in .edd.

**Plugin variables not shared**: Variables in plugin A are not visible in plugin B
without importing. But importing a plugin that is also in .edd = double-compile.
Solution: compute locally, or use EUDRegisterObjectToNamespace/GetEUDNamespace.

---

## EPScript: foreach and py_range

```javascript
foreach(i : py_range(7)) { ... }       // compile-time unroll, always runs 7 times
foreach(i : py_range(0, 7)) { ... }    // same — 0..6 (upper bound exclusive)
foreach(player : EUDLoopPlayer()) { }   // runtime, active players only
foreach(player : EUDLoopPlayer(None, Force1)) { }  // runtime, Force1 only
```

`py_range` is **always compile-time** — it unrolls at compile time into N separate
code blocks. You CANNOT `break` or `continue` inside `foreach(i : py_range(N))`.
You CAN `break`/`continue` inside `foreach(x : EUDLoopPlayer())`.

`EUDLoopPlayer()` only iterates active human players — it internally calls
`playerexist()`. `EUDLoopPlayer(None, Force1)` restricts to Force1 (P1–P7).

**The key insight**: A no-parameter function containing `foreach(i : py_range(N))`
still gets full compile-time unrolling inside the function body. The compile-time
strings referenced by `i` remain compile-time at each unrolled iteration.

```javascript
// CORRECT — loop inside function, no parameters, strings stay compile-time
const myUnits = list(py_str("Terran Marine"), py_str("Zerg Zergling"));
function handleAll() {
    foreach(i : py_range(2)) {
        Command(P1, AtMost, 1, myUnits[i]);  // compile-time string at each unroll ✓
    }
}

// WRONG — passing unit name as parameter makes it a runtime EUDVariable
function handleOne(unit) {
    Command(P1, AtMost, 1, unit);  // FAILS — unit is runtime EUDVariable
}
foreach(i : py_range(2)) { handleOne(myUnits[i]); }
```

---

## EPScript: Functions

Function parameters are runtime EUDVariables — they cannot be used as trigger
action unit names, location names, or comparison counts.

```javascript
function spawnUnit(unit, loc) {
    CreateUnit(1, unit, loc, P8);  // FAILS — unit and loc are runtime EUDVariables
}
```

Multiple return values:
```javascript
function getXY() { return x, y; }
var a, b = getXY();
const r = getXY()[[0]];  // get only first return value
```

Functions starting with `py_` must be called as `py_py_functionName()`.

---

## EPScript: Current Player (setcurpl/getcurpl)

`setcurpl(p)` writes to `0x6509B0`. All triggers in that frame use this value.
Always save and restore:

```javascript
var savedCp = getcurpl();
setcurpl(player);
// ... player-specific actions ...
setcurpl(savedCp);
```

**Actions that use CurrentPlayer (desync-safe, only affect local machine)**:
`DisplayText`, `CenterView`, `PlayWAV`, `MinimapPing`, `TalkingPortrait`, `Transmission`

**Actions that require synced CurrentPlayer**:
`SetAllianceStatus`, `RunAIScript`, `Defeat`, `Victory`, `Draw`

Without `setcurpl(player)` before `DisplayText` in a loop, the message fires
for the wrong player on each machine.

---

## EPScript: Display Text and Sound

Choose the right function for the job:

| Function | String type | Players | Buffer? | Cost |
|----------|------------|---------|---------|------|
| `DisplayText(mapIdx)` | compile-time map string | CurrentPlayer only | No | Cheapest |
| `DisplayTextAll(mapIdx)` | compile-time map string | All players | No | Cheapest |
| `println("text {}", var)` | runtime format string | CurrentPlayer only | Yes (global) |  Moderate |
| `printAll("text {}", var)` | runtime format string | All players | Yes (global) | Moderate |

Use `DisplayText`/`DisplayTextAll` for static strings — zero runtime cost.
Use `println`/`printAll` only when you need to embed runtime variable values.

`println` always uses the global `StringBuffer` internally at runtime, even if
all arguments are compile-time constants. It does NOT optimize away.

**Never** create `StringBuffer()` inline in a loop — each call allocates a new
permanent string table slot. Declare at module scope and reuse:
```javascript
const buf = StringBuffer(128);  // at module scope, reuse every frame
```

Sound works identically to DisplayText — `PlayWAV` fires for CurrentPlayer,
`PlayWAVAll` fires for all players. Always pair sound with text messages.

For compile-time constant strings with embedded numbers:
```javascript
const tempInvulSeconds = common_vars.tempInvulFrameAmount / 24;
const msg = $T(py_str("Temporary (") + py_str(tempInvulSeconds) + py_str("s) Invincibility!"));
DisplayText(msg);  // zero runtime cost, number baked in at compile time
```

If the number changes at runtime (e.g. difficulty modifier changes it), use `println` instead.

---

## EPScript: Trigger Actions — Critical Rules

These actions must be called DIRECTLY, NOT inside `DoActions()`:
- `SetInvincibility`
- `CreateUnitWithProperties`
- `GiveUnits`
- `KillUnitAt`
- `RemoveUnitAt`
- `MoveUnit`
- `Order`
- `SetMemory` / `SetMemoryX`

These actions work correctly both inside and outside `DoActions()`:
- `DisplayText`, `DisplayTextAll`
- `PlayWAV`, `PlayWAVAll`
- `SetSwitch`
- `SetResources`
- `CenterView`
- `MinimapPing`
- `CreateUnit` (note: different from CreateUnitWithProperties)

In EPScript, calling trigger action functions directly as statements (with semicolons)
is identical to wrapping them in `DoActions()`. Prefer direct calls for consistency.

---

## EPScript: Action Parameter Order

These are commonly confused. Memorize the exact parameter order:

```javascript
// GiveUnits(count, unit, sourcePlayer, location, destPlayer)
GiveUnits(1, "Protoss Probe", P8, "pSpawn", P9);

// SetInvincibility(state, unit, owner, location)
SetInvincibility(Enable, "Protoss Probe", player, "playground");

// Order(unit, owner, startLocation, orderType, destLocation)
// orderType BEFORE destLocation
Order("Samir Duran (Ghost)", P9, "o1", Move, "o2");

// Command(player, comparison, count, unit)
Command(P1, AtMost, 1, "Protoss Probe");

// KillUnitAt(count, unit, location, player)
KillUnitAt(All, "Men", "playground", player);

// CreateUnitWithProperties(count, unit, location, player, UnitProperty(...))
CreateUnitWithProperties(1, "Terran Civilian", "getbonus", player, UnitProperty(invincible = true));
```

---

## EPScript: Memory Operations

```javascript
f_dwwrite(addr, val)   // 32-bit write
f_wwrite(addr, val)    // 16-bit write  
f_bwrite(addr, val)    // 8-bit write
dwread(addr)           // 32-bit read
f_rand()               // random 32-bit value, use % N for range
f_rand() % 16          // random 0-15
```

HP in dat is stored as `actual_HP * 256`:
```javascript
f_dwwrite(0x00662390, 50000 * 256);  // set HP to 50000
```

Kill counter address: `0x005878A4 + (unitID * 12 + (player - 1)) * 4`
`SetKills(player, Subtract, 1, unitID)` — correct way to decrement kill counter.

Location manipulation:
```javascript
setloc($L("spawner"), left, top, right, bottom);  // set location bounds at runtime
var left, top = getlocTL($L("playground"));         // get top-left coordinates
```

Map string renaming at runtime:
```javascript
dbstr_print(GetMapStringAddr($T("Original Name")), "New Name\0");  // \0 terminator required
```

---

## EPScript: Condition Negation Syntax

```javascript
if (!CountdownTimer(Exactly, 5)) { return; }   // CORRECT — ! wraps whole condition
if !(CountdownTimer(Exactly, 5)) { return; }    // WRONG — syntax error
```

The `!` must wrap the entire condition including both parens.

---

## EPScript: Timer / Frame Counter Pattern

NEVER initialize countdown timers to 0 — decrementing from 0 wraps to 0xFFFFFFFF
(unsigned underflow), making the timer fire after ~4 billion frames:

```javascript
var myTimer = 80;  // CORRECT — non-zero initial value

// In beforeTriggerExec / afterTriggerExec:
myTimer--;
if (myTimer == 0) {
    myTimer = 80;
    // ... fire the event ...
}
```

Real-second timing: `getgametick()`, 24 frames = 1 real second at fastest speed.
Exact fastest speed is 23.81 frames/sec — no floats, use integer approximation.
For precision: `frames * 100 / 2381` instead of `frames / 23.81`.

```javascript
var lastTick = 0;
var realCountdown = 50;

function afterTriggerExec() {
    var currentTick = getgametick();
    if (currentTick - lastTick >= 24) {
        lastTick = currentTick;
        realCountdown--;
    }
}
```

Always call `PauseTimer()` in `onPluginStart()` if you want to control the
visible countdown timer yourself via `SetCountdownTimer(SetTo, value)`.

---

## EPScript: Randomization

Replace classic `Set Switch("X", randomize)` + binary switch decoding entirely:

```javascript
// Classic pattern (80+ triggers) replaced by:
var locIdx = f_rand() % 8;   // pick from 8 patrol locations
foreach(i : py_range(8)) {
    if (locIdx == i) {
        CreateUnit(1, "Kakaru (Twilight)", patrolLocs[i], P8);
    }
}
```

Spawner location randomization pattern from wave_spawns.eps:
```javascript
var left   = f_rand() % 3776;
var top    = 160 + f_rand() % (3776 - 160);
var right  = left + 320;
var bottom = top  + 320;
setloc($L("spawner"), left, top, right, bottom);
```

For a bounded spawn area (bonusSpawner with margins):
```javascript
var bonusLeft = 128 + f_rand() % 3808;  // 128 to 3936 (3936+32=3968 max right)
var bonusTop  = 288 + f_rand() % 3648;  // 288 to 3936 (3936+32=3968 max bottom)
setloc($L("bonusSpawner"), bonusLeft, bonusTop, bonusLeft + 32, bonusTop + 32);
```

---

## EPScript: `once` Keyword

`once (condition)` fires exactly once globally when the condition first becomes true.
**Problem**: inside a player loop, it fires for the first player that hits the condition
and never fires again for other players.

```javascript
// WRONG for per-player conditions:
foreach(player : EUDLoopPlayer(None, Force1)) {
    once (tempInvul[player] == 240) {  // fires only for first player, never again
        DisplayText("10 seconds left!");
    }
}

// CORRECT for per-player conditions — use plain if:
foreach(player : EUDLoopPlayer(None, Force1)) {
    if (tempInvul[player] == 240) {  // value passes through 240 only once per countdown
        DisplayText("10 seconds left!");
    }
}
```

`once` without condition: `once { ... }` runs exactly once unconditionally.
`once` inside `foreach(i : py_range(N))` unrolls into N separate once blocks,
one per iteration — each can fire once independently.

---

## EPScript: `switch` Statement

EPScript has a `switch` statement for runtime variable branching:
```javascript
switch (myVar) {
    case 1:
        // code for value 1
        break;
    case 2:
    case 3:
        // code for value 2 or 3
        break;
}
```

Also `epdswitch` for EPD address-based switching. More efficient than chained `if`
statements when testing a single variable against multiple values.

---

## EPScript: EUDLightVariable and EUDLightBool

For variables used only for counting/comparison (not passed to other functions):

```javascript
const lv = EUDLightVariable(100);  // only 4 bytes vs 72 bytes for EUDVariable
// Same conditions/actions as EUDVariable, but value passing is expensive:
println("{}", dwread(lv.getValueAddr()));  // reading is ~32x more triggers than EUDVariable
```

```javascript
const b = EUDLightBool();  // 1 bit (32 share one EUDLightVariable)
DoActions(b.Set(), b.Clear(), b.Toggle());
if (b.IsSet()) { ... }
if (b.IsCleared()) { ... }
```

Use `EUDLightBool` instead of `var` for boolean flags that don't need to be
passed as function arguments.

---

## EPScript: String Types Reference

| Type | How to create | Use case |
|------|--------------|---------|
| `py_str("x")` | compile-time string | string concat at compile time, list() arrays |
| `$T("x")` | compile-time map string index | DisplayText, trigger string params |
| `$U("unit")` | compile-time unit ID integer | EUDVArray init, runtime unit IDs |
| `$L("loc")` | compile-time location ID | setloc, MinimapPing with variable |
| `$S("switch")` | compile-time switch ID | SetSwitch with variable |
| `$B("name")` | compile-time TBL key | stat_txt.tbl entries |
| `Db(N)` | runtime memory buffer | raw string data, not directly displayable |
| `StringBuffer(N)` | runtime string buffer | println target, writable display strings |

String concatenation at compile time:
```javascript
const msg = $T(py_str("Round ") + py_str(42) + py_str(" complete!"));
```

Runtime string modification (must not change size):
```javascript
dbstr_print(GetMapStringAddr($T("My Map String")), "New Content\0");  // \0 required
```

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

9. **foreach with py_range cannot break/continue** — use `while` or `EUDLoopRange` for that.

10. **Wait() in afterTriggerExec is dangerous** — blocks the entire EUD loop.
    Use frame counters or countdown timers instead.

11. **Assigning to a local copy doesn't affect VArray** — `var x = arr[i]; x = 0;` does nothing
    to the array. Use `arr[i] = 0;` directly.

12. **EUDVArray for runtime indexes** — use EUDVArray not EUDArray when indexing with variables.
    EUDArray is fast for compile-time (py_range) indexes, slow for runtime variable indexes.

13. **$U for runtime unit IDs** — `$U("unit name")` gives integer ID usable at runtime in
    EUDVArray. `py_str` is compile-time only. `waveSpawnsUnitIndex[i]` works because it's
    an EUDVArray of `$U(...)` values.

14. **No for/in over arrays** — no `for (x in array)`. Use `foreach(i : py_range(0, N))`.

15. **CreateUnitWithProperties outside DoActions** — call it directly, not wrapped in DoActions.

16. **String concatenation with runtime vars** — cannot use `+` to concat strings with vars.
    Use `println("text {}", myVar)` or `printAll("text {}", myVar)` instead.

17. **No-parameter function with internal py_range loop** — a function with NO parameters
    containing `foreach(i : py_range(N))` DOES get full compile-time unrolling.
    The compile-time strings accessed by `i` remain compile-time at each unrolled copy.
    This is CONFIRMED correct behavior — verified against docs and compilation.

    ```javascript
    const units = list(py_str("Terran Marine"), py_str("Zerg Zergling"));
    function handleAll() {           // no parameters = compile-time strings preserved
        foreach(i : py_range(2)) {
            Command(P1, AtMost, 1, units[i]);  // ✓ compile-time unit name
        }
    }
    ```

18. **`list()` not `[]` for compile-time py_str arrays** — `[]` creates EUDArray which fails
    on py_str. Use `list()` for compile-time string/constant collections.

19. **Condition comparison values must be compile-time** — `Command(P9, AtMost, runtimeVar, unit)`
    fails. Even `maxCount - 1` fails if `maxCount` is a function parameter (runtime).
    Hardcode the value or restructure to avoid passing counts through functions.

20. **Timer vars must never start at 0** — all vars are 32-bit unsigned. `timer--` when
    `timer == 0` wraps to 0xFFFFFFFF. Always initialize countdown timers non-zero.

21. **P1 internal value is 0, not 1** — `player - 1` for P1 underflows to 0xFFFFFFFF.
    Use `player` directly as EUDArray index (P1=0, P2=1, ..., P7=6).

22. **setcurpl required for DisplayText/PlayWAV/CenterView per-player** — without
    `setcurpl(player)` before them in a loop, they fire for the wrong player.
    Always save/restore: `var savedCp = getcurpl(); setcurpl(p); ...; setcurpl(savedCp);`

23. **DisplayText vs println vs DisplayTextAll** — use the right tool:
    - `DisplayText(mapStringIdx)` — cheapest, compile-time string only, current player only
    - `DisplayTextAll(mapStringIdx)` — same but all players, no setcurpl needed
    - `println("text {}", runtimeVar)` — uses StringBuffer, supports runtime vars, current player
    - `printAll("text {}", runtimeVar)` — same but all players
    Never call `StringBuffer()` inline in a loop — allocates a new string slot permanently each call.

24. **Order() parameter order** — `Order(unit, owner, startLocation, orderType, destLocation)`
    The orderType comes BEFORE destLocation. Example: `Order("Duran", P9, "o1", Move, "o2");`

25. **Classic trigger randomize switch → use f_rand() instead** — the classic
    `Set Switch("X", randomize)` + binary switch decode pattern is entirely replaced by
    `f_rand() % N`. No BonusSwitches needed.

26. **EUDLoopPlayer(None, Force1)** — iterates only active players in Force1 (P1-P7).
    `EUDLoopPlayer()` with no args iterates all active players regardless of force.

27. **Condition negation syntax** — `if (!Condition(args))` — the `!` wraps the entire
    condition including both closing parens: `if (!CountdownTimer(Exactly, 5))`.

28. **`println` always uses StringBuffer at runtime** — even for compile-time constant args,
    `println` still does a runtime memory write. Use `DisplayText($T(...))` for zero-cost static messages.

29. **No floating point** — EPScript is 32-bit unsigned integers only. `23.81` truncates to `23`.
    Use integer math: `frames * 100 / 2381` for frames-to-seconds with 2-decimal precision.

30. **`once` with per-player runtime condition** — `once (tempInvul[player] == 240)` inside
    a player loop fires globally once for the first player, never again for others. Use plain `if`.

31. **`var x;` without initializer has static behavior** — the value persists between function
    calls. Always use `var x = 0;` to ensure reset on each call, or use `static var x = 0;`
    to explicitly document intended static behavior.

32. **`delayBetweenSpawns = EUDVariable(64)` is wrong** — in common_vars.eps this is a bug.
    `var delayBetweenSpawns = EUDVariable(64)` makes it a var holding the *address* of an
    EUDVariable object, not the value 64. Should be `var delayBetweenSpawns = 64;`.

33. **afterTriggerExec runs in REVERSE .edd order** — if A.eps and B.eps are both in .edd,
    B's afterTriggerExec runs BEFORE A's. onPluginStart and beforeTriggerExec run in forward order.

34. **Scope shadowing** — a `var` declared inside an inner `{}` block shadows outer vars of
    the same name. The inner var's scope ends when its braces close.

35. **EUDVariable SubtractNumber clamps at 0** — `DoActions(x.SubtractNumber(2))` cannot
    go below 0. Use `x -= 2` (the `-` operator) if you need unsigned wrap-around.

36. **`var arr = EUDArray(10)` is wrong** — creates an EUDVariable holding the address of
    an EUDArray. `arr[0] = 1` is a syntax error. Use `const arr = EUDArray(10)` instead.

37. **All objects have fixed memory space** — even objects created inside loops share the
    same memory. `const X = EUDArray(10); for (...) { X[i] = EUDArray(10); }` assigns
    the SAME EUDArray instance to every X[i]. Use dynamic allocation (`EUDArray.alloc()`)
    for truly separate instances (note: EUDArray itself cannot be dynamically allocated).

38. **`common_vars.eps` has a `beforeTriggerExec` function** — this empty function is needed
    because common_vars.eps is loaded as a plugin. Without it, the file would not be recognized
    as a plugin. However, it should NOT be in the .edd to avoid double-compile.
