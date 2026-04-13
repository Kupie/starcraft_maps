# CPU Cat and Mouse — EDScript Conversion Project

## Context
StarCraft: Brood War 1.16.1 UMS map using EUD Editor 3 (EDScript / eudplib).
Source triggers are in *.txt in standard SCMDraft trigger format.

## EPScript Reference
See /SCRMapDocs-main/docs/epScript-Reference/epScript-Reference.md for correct syntax.
Key gotchas discovered so far:
- Player format: P1-P8, not "Player 1" or 0-indexed
- Command() order: Command(player, comparison, count, unit)
- No Wait() in afterTriggerExec safely
- Negation with !Condition() inside if()

## Goal
Convert spawner_triggers.txt into EDScript (.eps) files.

## Key Rules
- EDScript uses: const, foreach, py_range, DoActions(), EUDVariable
- foreach loop syntax: foreach(player : py_range(1, 7))
- Global vars declared at file scope as: const varName = EUDVariable(0);
- Waits and spawns go in afterTriggerExec()
- numActivePlayers is a global EUDVariable maintained in globalvars.eps
- Player 8 = the spawner/cat player (CPU)
- Player 9 = shop token pool (Terran Civilians = currency)
- Player 11 = the Kakaru state tracker unit

## Split Spawn Logic
When Switch "ReduceSpawnsForNumPlayers" is SET:
  - Divide unit counts by numActivePlayers (round down, minimum 1)
When NOT SET:
  - Use full counts from original trigger

## Wave Spawn Structure
Each wave trigger becomes a function in wavespawn.eps:
  - Check the same Conditions (Kakaru position, civilian count, switches)
  - if ReduceSpawnsForNumPlayers set: spawn (count / numActivePlayers) per player
  - else: spawn full count
  - Always end with Set Switch SpawnExtra

## Hard Mode Extra Spawns
hardmode_extra.eps should collapse the 200+ triggers into a single
foreach loop using civilian count and ExtraSpawn1/2 switch states
to determine which unit to spawn.

## Do Not Change
- Switch names (SpawnExtra, ExtraSpawn1, ExtraSpawn2, HardModeEnabled, ReduceSpawnsForNumPlayers)
- Location names ("spawner", "getbonus")
- Unit names (exact strings must match)