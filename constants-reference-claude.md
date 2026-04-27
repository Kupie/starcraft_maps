# epScript Constants Reference

> All constant tables for epScript (euddraft/eudplib).
> String names are resolved at compile time — they are NOT inserted into the map at runtime.
> Use $U("name"), $B("name"), $T("name"), $L("name") macros to get IDs at compile time.

---


---
sidebar_position: 8
---

# epScript Constants Reference

## TrgCount

```JavaScript
All: 0
Other integers
```

## TrgModifier

```JavaScript
SetTo: 7    // =
Add: 8      // +=
Subtract: 9 // -= (It can be reduced to zero at most, even if a number greater than the current value is subtracted)
```

## TrgComparison

```JavaScript
AtLeast: 0  // >=
AtMost: 1   // <=
Exactly: 10 // ==
```

## TrgSwitchState

```JavaScript
Set: 2
Cleared: 3
```

## TrgSwitchAction

```JavaScript
Set: 4
Clear: 5
Toggle: 6
Random: 11
```

## TrgResource

```JavaScript
Ore: 0
Gas: 1
OreAndGas: 2
```

## TrgAllyStatus

```JavaScript
Enemy: 0
Ally: 1
AlliedVictory: 2
```

## TrgOrder

```JavaScript
Move: 0
Patrol: 1
Attack: 2
```

## TrgPropState

```JavaScript
Enable: 4
Disable: 5
Toggle: 6
```

## TrgScore

```JavaScript
Total: 0
Units: 1
Buildings: 2
UnitsAndBuildings: 3
Kills: 4
Razings: 5
KillsAndRazings: 6
Custom: 7
```

## TrgLocation
```JavaScript
// There are a total of 255 locations/areas, numbered from 0 to 63, 65 to 255
// No. 64 means Anywhere
"Location 1~64": 0~63
"Anywhere": 64
"Location 66~256": 65~255
// When euddraft compiles, it will remove all location/area names from the map string table, that is, location/area names do not exist at runtime and are only used by map developers to distinguish 
```

## TrgSwitch

```JavaScript
// There are a total of 256 switches, numbered 0 to 255
"Switch 1~256": 0~255
// When euddraft compiles, it will remove all switch names from the map string table, that is, switch names do not exist at runtime and are only used by map developers to distinguish
```




## TrgPlayer

```JavaScript
P1: 0
P2: 1
P3: 2
P4: 3
P5: 4
P6: 5
P7: 6
P8: 7
P9: 8
P10: 9
P11: 10
P12: 11
Player1: 0
Player2: 1
Player3: 2
Player4: 3
Player5: 4
Player6: 5
Player7: 6
Player8: 7
Player9: 8
Player10: 9
Player11: 10
Player12: 11
CurrentPlayer: 13
Foes: 14
Allies: 15
NeutralPlayers: 16
AllPlayers: 17
Force1: 18
Force2: 19
Force3: 20
Force4: 21
NonAlliedVictoryPlayers: 26
```

  





## TrgUnit

```JavaScript
"Terran Marine": 0
"Terran Ghost": 1
"Terran Vulture": 2
"Terran Goliath": 3
"Goliath Turret": 4
"Terran Siege Tank (Tank Mode)": 5
"Siege Tank Turret (Tank Mode)": 6
"Tank Turret type   1": 6
"Terran SCV": 7
"Terran Wraith": 8
"Terran Science Vessel": 9
"Gui Montag": 10
"Gui Montag (Firebat)": 10
"Terran Dropship": 11
"Terran Battlecruiser": 12
"Spider Mine": 13
"Vulture Spider Mine": 13
"Nuclear Missile": 14
"Terran Civilian": 15
"Sarah Kerrigan": 16
"Sarah Kerrigan (Ghost)": 16
"Alan Schezar": 17
"Alan Schezar (Goliath)": 17
"Alan Schezar Turret": 18
"Alan Turret": 18
"Jim Raynor (Vulture)": 19
"Jim Raynor (Marine)": 20
"Tom Kazansky": 21
"Tom Kazansky (Wraith)": 21
"Magellan": 22
"Magellan (Science Vessel)": 22
"Edmund Duke (Tank Mode)": 23
"Edmund Duke (Siege Tank)": 23
"Edmund Duke Turret (Tank Mode)": 24
"Duke Turret type   1": 24
"Edmund Duke (Siege Mode)": 25
"Edmund Duke Turret (Siege Mode)": 26
"Duke Turret type   2": 26
"Arcturus Mengsk": 27
"Arcturus Mengsk (Battlecruiser)": 27
"Hyperion": 28
"Hyperion (Battlecruiser)": 28
"Norad II (Battlecruiser)": 29
"Terran Siege Tank (Siege Mode)": 30
"Siege Tank Turret (Siege Mode)": 31
"Tank Turret type   2": 31
"Terran Firebat": 32
"Scanner Sweep": 33
"Terran Medic": 34
"Zerg Larva": 35
"Zerg Egg": 36
"Zerg Zergling": 37
"Zerg Hydralisk": 38
"Zerg Ultralisk": 39
"Zerg Broodling": 40
"Zerg Drone": 41
"Zerg Overlord": 42
"Zerg Mutalisk": 43
"Zerg Guardian": 44
"Zerg Queen": 45
"Zerg Defiler": 46
"Zerg Scourge": 47
"Torrasque": 48
"Torrasque (Ultralisk)": 48
"Matriarch": 49
"Matriarch (Queen)": 49
"Infested Terran": 50
"Infested Kerrigan": 51
"Infested Kerrigan (Infested Terran)": 51
"Unclean One": 52
"Unclean One (Defiler)": 52
"Hunter Killer": 53
"Hunter Killer (Hydralisk)": 53
"Devouring One": 54
"Devouring One (Zergling)": 54
"Kukulza (Mutalisk)": 55
"Kukulza (Guardian)": 56
"Yggdrasill": 57
"Yggdrasill (Overlord)": 57
"Terran Valkyrie": 58
"Mutalisk Cocoon": 59
"Cocoon": 59
"Protoss Corsair": 60
"Protoss Dark Templar": 61
"Protoss Dark Templar (Unit)": 61
"Zerg Devourer": 62
"Protoss Dark Archon": 63
"Protoss Probe": 64
"Protoss Zealot": 65
"Protoss Dragoon": 66
"Protoss High Templar": 67
"Protoss Archon": 68
"Protoss Shuttle": 69
"Protoss Scout": 70
"Protoss Arbiter": 71
"Protoss Carrier": 72
"Protoss Interceptor": 73
"Dark Templar": 74
"Dark Templar (Hero)": 74
"Protoss Dark Templar (Hero)": 74
"Zeratul": 75
"Zeratul (Dark Templar)": 75
"Tassadar/Zeratul": 76
"Tassadar/Zeratul (Archon)": 76
"Fenix (Zealot)": 77
"Fenix (Dragoon)": 78
"Tassadar": 79
"Tassadar (Templar)": 79
"Mojo": 80
"Mojo (Scout)": 80
"Warbringer": 81
"Warbringer (Reaver)": 81
"Gantrithor": 82
"Gantrithor (Carrier)": 82
"Protoss Reaver": 83
"Protoss Observer": 84
"Protoss Scarab": 85
"Danimoth": 86
"Danimoth (Arbiter)": 86
"Aldaris": 87
"Aldaris (Templar)": 87
"Artanis": 88
"Artanis (Scout)": 88
"Rhynadon": 89
"Rhynadon (Badlands)": 89
"Rhynadon (Badlands Critter)": 89
"Bengalaas": 90
"Bengalaas (Jungle)": 90
"Bengalaas (Jungle Critter)": 90
"Cargo Ship": 91
"Cargo Ship (Unused)": 91
"Unused type   1": 91
"Unused type   2": 92
"Mercenary Gunship": 92
"Mercenary Gunship (Unused)": 92
"Scantid": 93
"Scantid (Desert)": 93
"Scantid (Desert Critter)": 93
"Kakaru": 94
"Kakaru (Twilight)": 94
"Kakaru (Twilight Critter)": 94
"Ragnasaur": 95
"Ragnasaur (Ashworld)": 95
"Ragnasaur (Ashworld Critter)": 95
"Ursadon": 96
"Ursadon (Ice World)": 96
"Ursadon (Ice World Critter)": 96
"Lurker Egg": 97
"Zerg Lurker Egg": 97
"Raszagal": 98
"Raszagal (Corsair)": 98
"Samir Duran": 99
"Samir Duran (Ghost)": 99
"Alexei Stukov": 100
"Alexei Stukov (Ghost)": 100
"Map Revealer": 101
"Gerard DuGalle": 102
"Gerard DuGalle (Ghost)": 102
"Gerard DuGalle (BattleCruiser)": 102
"Zerg Lurker": 103
"Infested Duran": 104
"Infested Duran (Infested Terran)": 104
"Disruption Web": 105
"Disruption Field": 105
"Terran Command Center": 106
"Terran Comsat Station": 107
"Terran Nuclear Silo": 108
"Terran Supply Depot": 109
"Terran Refinery": 110
"Terran Barracks": 111
"Terran Academy": 112
"Terran Factory": 113
"Terran Starport": 114
"Terran Control Tower": 115
"Terran Science Facility": 116
"Terran Covert Ops": 117
"Terran Physics Lab": 118
"Starbase": 119
"Starbase (Unused)": 119
"Unused Terran Bldg type   1": 119
"Terran Machine Shop": 120
"Repair Bay": 121
"Repair Bay (Unused)": 121
"Unused Terran Bldg type   2": 121
"Terran Engineering Bay": 122
"Terran Armory": 123
"Terran Missile Turret": 124
"Terran Bunker": 125
"Norad II (Crashed)": 126
"Norad II (Crashed Battlecruiser)": 126
"Ion Cannon": 127
"Uraj Crystal": 128
"Khalis Crystal": 129
"Infested Command Center": 130
"Zerg Hatchery": 131
"Zerg Lair": 132
"Zerg Hive": 133
"Zerg Nydus Canal": 134
"Zerg Hydralisk Den": 135
"Zerg Defiler Mound": 136
"Zerg Greater Spire": 137
"Zerg Queen's Nest": 138
"Zerg Evolution Chamber": 139
"Zerg Ultralisk Cavern": 140
"Zerg Spire": 141
"Zerg Spawning Pool": 142
"Zerg Creep Colony": 143
"Zerg Spore Colony": 144
"Unused Zerg Bldg": 145
"Unused Zerg Building1": 145
"Zerg Sunken Colony": 146
"Zerg Overmind (With Shell)": 147
"Zerg Overmind": 148
"Zerg Extractor": 149
"Mature Chrysalis": 150
"Mature Crysalis": 150
"Zerg Cerebrate": 151
"Zerg Cerebrate Daggoth": 152
"Unused Zerg Building2": 153
"Protoss Nexus": 154
"Protoss Robotics Facility": 155
"Protoss Pylon": 156
"Protoss Assimilator": 157
"Protoss Unused type   1": 158
"Unused Protoss Building1": 158
"Protoss Observatory": 159
"Protoss Gateway": 160
"Protoss Unused type   2": 161
"Unused Protoss Building2": 161
"Protoss Photon Cannon": 162
"Protoss Citadel of Adun": 163
"Protoss Cybernetics Core": 164
"Protoss Templar Archives": 165
"Protoss Forge": 166
"Protoss Stargate": 167
"Stasis Cell/Prison": 168
"Protoss Fleet Beacon": 169
"Protoss Arbiter Tribunal": 170
"Protoss Robotics Support Bay": 171
"Protoss Shield Battery": 172
"Khaydarin Crystal Formation": 173
"Protoss Temple": 174
"Xel'Naga Temple": 175
"Mineral Field (Type 1)": 176
"Mineral Field (Type 2)": 177
"Mineral Field (Type 3)": 178
"Cave": 179
"Cave (Unused)": 179
"Cave-in": 180
"Cave-in (Unused)": 180
"Cantina": 181
"Cantina (Unused)": 181
"Mining Platform": 182
"Mining Platform (Unused)": 182
"Independent Command Center": 183
"Independent Command Center (Unused)": 183
"Independent Starport": 184
"Independent Starport (Unused)": 184
"Jump Gate": 185
"Independent Jump Gate (Unused)": 185
"Ruins": 186
"Ruins (Unused)": 186
"Kyadarin Crystal Formation": 187
"Khaydarin Crystal Formation (Unused)": 187
"Vespene Geyser": 188
"Warp Gate": 189
"Psi Disrupter": 190
"Zerg Marker": 191
"Terran Marker": 192
"Protoss Marker": 193
"Zerg Beacon": 194
"Terran Beacon": 195
"Protoss Beacon": 196
"Zerg Flag Beacon": 197
"Terran Flag Beacon": 198
"Protoss Flag Beacon": 199
"Power Generator": 200
"Overmind Cocoon": 201
"Dark Swarm": 202
"Floor Missile Trap": 203
"Floor Hatch (Unused)": 204
"Floor Hatch (UNUSED)": 204
"Left Upper Level Door": 205
"Right Upper Level Door": 206
"Left Pit Door": 207
"Right Pit Door": 208
"Floor Gun Trap": 209
"Left Wall Missile Trap": 210
"Left Wall Flame Trap": 211
"Right Wall Missile Trap": 212
"Right Wall Flame Trap": 213
"Start Location": 214
"Flag": 215
"Young Chrysalis": 216
"Psi Emitter": 217
"Data Disc": 218
"Khaydarin Crystal": 219
"Mineral Chunk (Type 1)": 220
"Mineral Chunk (Type 2)": 221
"Mineral Cluster Type 1": 220
"Mineral Cluster Type 2": 221
"Vespene Orb (Protoss Type 1)": 222
"Vespene Orb (Protoss Type 2)": 223
"Protoss Vespene Gas Orb Type 1": 222
"Protoss Vespene Gas Orb Type 2": 223
"Vespene Sac (Zerg Type 1)": 224
"Vespene Sac (Zerg Type 2)": 225
"Zerg Vespene Gas Sac Type 1": 224
"Zerg Vespene Gas Sac Type 2": 225
"Vespene Tank (Terran Type 1)": 226
"Vespene Tank (Terran Type 2)": 227
"Terran Vespene Gas Tank Type 1": 226
"Terran Vespene Gas Tank Type 2": 227
"Unused unit 228": 228
"Unused228": 228
"None": 228
"Any unit": 229
"(any unit)": 229
"Men": 230
"(men)": 230
"Buildings": 231
"(buildings)": 231
"Factories": 232
"(factories)": 232
```

  



The AI script number is in the form of a little-endian four-character code, which is essentially a 32-bit unsigned integer.

b"TMCu" represents the number 1967344980. This method of using four characters to represent a number is called [Four-Character Codes](https://en.wikipedia.org/wiki/FourCC), and on the x86 platform it is usually little-endian. 

```JavaScript
println("{} == {}", py_int().from_bytes(b"+Vi0", "little"), EncodeAIScript("Turn ON Shared Vision for Player 1")); // 812209707 == 812209707
RunAIScript(b2i4(b"ZMCu"));
```

```Python
def f_b2i4(bytes):
  return int.from_bytes(bytes, "little")

print(f_b2i4(b"TMCu")) # 1967344980
```

## AI Scripts

```Python
# Custom AI Scripts
b"Terran Custom Level": b"TMCu"
b"Zerg Custom Level": b"ZMCu"
b"Protoss Custom Level": b"PMCu"
b"Terran Expansion Custom Level": b"TMCx"
b"Zerg Expansion Custom Level": b"ZMCx"
b"Protoss Expansion Custom Level": b"PMCx"
b"Terran Campaign Easy": b"TLOf"
b"Terran Campaign Medium": b"TMED"
b"Terran Campaign Difficult": b"THIf"
b"Terran Campaign Insane": b"TSUP"
b"Terran Campaign Area Town": b"TARE"
b"Zerg Campaign Easy": b"ZLOf"
b"Zerg Campaign Medium": b"ZMED"
b"Zerg Campaign Difficult": b"ZHIf"
b"Zerg Campaign Insane": b"ZSUP"
b"Zerg Campaign Area Town": b"ZARE"
b"Protoss Campaign Easy": b"PLOf"
b"Protoss Campaign Medium": b"PMED"
b"Protoss Campaign Difficult": b"PHIf"
b"Protoss Campaign Insane": b"PSUP"
b"Protoss Campaign Area Town": b"PARE"
b"Expansion Terran Campaign Easy": b"TLOx"
b"Expansion Terran Campaign Medium": b"TMEx"
b"Expansion Terran Campaign Difficult": b"THIx"
b"Expansion Terran Campaign Insane": b"TSUx"
b"Expansion Terran Campaign Area Town": b"TARx"
b"Expansion Zerg Campaign Easy": b"ZLOx"
b"Expansion Zerg Campaign Medium": b"ZMEx"
b"Expansion Zerg Campaign Difficult": b"ZHIx"
b"Expansion Zerg Campaign Insane": b"ZSUx"
b"Expansion Zerg Campaign Area Town": b"ZARx"
b"Expansion Protoss Campaign Easy": b"PLOx"
b"Expansion Protoss Campaign Medium": b"PMEx"
b"Expansion Protoss Campaign Difficult": b"PHIx"
b"Expansion Protoss Campaign Insane": b"PSUx"
b"Expansion Protoss Campaign Area Town": b"PARx"
b"Send All Units on Strategic Suicide Missions": b"Suic"
b"Send All Units on Random Suicide Missions": b"SuiR"
b"Switch Computer Player to Rescue Passive": b"Rscu"
b"Turn ON Shared Vision for Player 1": b"+Vi0"
b"Turn ON Shared Vision for Player 2": b"+Vi1"
b"Turn ON Shared Vision for Player 3": b"+Vi2"
b"Turn ON Shared Vision for Player 4": b"+Vi3"
b"Turn ON Shared Vision for Player 5": b"+Vi4"
b"Turn ON Shared Vision for Player 6": b"+Vi5"
b"Turn ON Shared Vision for Player 7": b"+Vi6"
b"Turn ON Shared Vision for Player 8": b"+Vi7"
b"Turn OFF Shared Vision for Player 1": b"-Vi0"
b"Turn OFF Shared Vision for Player 2": b"-Vi1"
b"Turn OFF Shared Vision for Player 3": b"-Vi2"
b"Turn OFF Shared Vision for Player 4": b"-Vi3"
b"Turn OFF Shared Vision for Player 5": b"-Vi4"
b"Turn OFF Shared Vision for Player 6": b"-Vi5"
b"Turn OFF Shared Vision for Player 7": b"-Vi6"
b"Turn OFF Shared Vision for Player 8": b"-Vi7"
b"Move Dark Templars to Region": b"MvTe"
b"Clear Previous Combat Data": b"ClrC"
b"Set Player to Enemy": b"Enmy"
b"Set Player to Ally  ": b"y   "
b"Value This Area Higher": b"VluA"
b"Enter Closest Bunker": b"EnBk"
b"Set Generic Command Target": b"StTg"
b"Make These Units Patrol": b"StPt"
b"Enter Transport": b"EnTr"
b"Exit Transport": b"ExTr"
b"AI Nuke Here": b"NuHe"
b"AI Harass Here": b"HaHe"
b"Set Unit Order To: Junk Yard Dog": b"JYDg"
b"Disruption Web Here": b"DWHe"
b"Recall Here": b"ReHe"

# StarCraft AI Scripts
b"Terran 3 - Zerg Town": b"Ter3"
b"Terran 5 - Terran Main Town": b"Ter5"
b"Terran 5 - Terran Harvest Town": b"Te5H"
b"Terran 6 - Air Attack Zerg": b"Ter6"
b"Terran 6 - Ground Attack Zerg": b"Te6b"
b"Terran 6 - Zerg Support Town": b"Te6c"
b"Terran 7 - Bottom Zerg Town": b"Ter7"
b"Terran 7 - Right Zerg Town": b"Te7s"
b"Terran 7 - Middle Zerg Town": b"Te7m"
b"Terran 8 - Confederate Town": b"Ter8"
b"Terran 9 - Light Attack": b"Tr9L"
b"Terran 9 - Heavy Attack": b"Tr9H"
b"Terran 10 - Confederate Towns": b"Te10"
b"Terran 11 - Zerg Town": b"T11z"
b"Terran 11 - Lower Protoss Town": b"T11a"
b"Terran 11 - Upper Protoss Town": b"T11b"
b"Terran 12 - Nuke Town": b"T12N"
b"Terran 12 - Phoenix Town": b"T12P"
b"Terran 12 - Tank Town": b"T12T"
b"Terran 1 - Electronic Distribution": b"TED1"
b"Terran 2 - Electronic Distribution": b"TED2"
b"Terran 3 - Electronic Distribution": b"TED3"
b"Terran 1 - Shareware": b"TSW1"
b"Terran 2 - Shareware": b"TSW2"
b"Terran 3 - Shareware": b"TSW3"
b"Terran 4 - Shareware": b"TSW4"
b"Terran 5 - Shareware": b"TSW5"
b"Zerg 1 - Terran Town": b"Zer1"
b"Zerg 2 - Protoss Town": b"Zer2"
b"Zerg 3 - Terran Town": b"Zer3"
b"Zerg 4 - Right Terran Town": b"Zer4"
b"Zerg 4 - Lower Terran Town": b"Ze4S"
b"Zerg 6 - Protoss Town": b"Zer6"
b"Zerg 7 - Air Town": b"Zr7a"
b"Zerg 7 - Ground Town": b"Zr7g"
b"Zerg 7 - Support Town": b"Zr7s"
b"Zerg 8 - Scout Town": b"Zer8"
b"Zerg 8 - Templar Town": b"Ze8T"
b"Zerg 9 - Teal Protoss": b"Zer9"
b"Zerg 9 - Left Yellow Protoss": b"Z9ly"
b"Zerg 9 - Right Yellow Protoss": b"Z9ry"
b"Zerg 9 - Left Orange Protoss": b"Z9lo"
b"Zerg 9 - Right Orange Protoss": b"Z9ro"
b"Zerg 10 - Left Teal (Attack": b"Z10a"
b"Zerg 10 - Right Teal (Support": b"Z10b"
b"Zerg 10 - Left Yellow (Support": b"Z10c"
b"Zerg 10 - Right Yellow (Attack": b"Z10d"
b"Zerg 10 - Red Protoss": b"Z10e"
b"Protoss 1 - Zerg Town": b"Pro1"
b"Protoss 2 - Zerg Town": b"Pro2"
b"Protoss 3 - Air Zerg Town": b"Pr3R"
b"Protoss 3 - Ground Zerg Town": b"Pr3G"
b"Protoss 4 - Zerg Town": b"Pro4"
b"Protoss 5 - Zerg Town Island": b"Pr5I"
b"Protoss 5 - Zerg Town Base": b"Pr5B"
b"Protoss 7 - Left Protoss Town": b"Pro7"
b"Protoss 7 - Right Protoss Town": b"Pr7B"
b"Protoss 7 - Shrine Protoss": b"Pr7S"
b"Protoss 8 - Left Protoss Town": b"Pro8"
b"Protoss 8 - Right Protoss Town": b"Pr8B"
b"Protoss 8 - Protoss Defenders": b"Pr8D"
b"Protoss 9 - Ground Zerg": b"Pro9"
b"Protoss 9 - Air Zerg": b"Pr9W"
b"Protoss 9 - Spell Zerg": b"Pr9Y"
b"Protoss 10 - Mini-Towns": b"Pr10"
b"Protoss 10 - Mini-Town Master": b"P10C"
b"Protoss 10 - Overmind Defenders": b"P10o"

# Brood Wars AI Scripts
b"Brood Wars Protoss 1 - Town A": b"PB1A"
b"Brood Wars Protoss 1 - Town B": b"PB1B"
b"Brood Wars Protoss 1 - Town C": b"PB1C"
b"Brood Wars Protoss 1 - Town D": b"PB1D"
b"Brood Wars Protoss 1 - Town E": b"PB1E"
b"Brood Wars Protoss 1 - Town F": b"PB1F"
b"Brood Wars Protoss 2 - Town A": b"PB2A"
b"Brood Wars Protoss 2 - Town B": b"PB2B"
b"Brood Wars Protoss 2 - Town C": b"PB2C"
b"Brood Wars Protoss 2 - Town D": b"PB2D"
b"Brood Wars Protoss 2 - Town E": b"PB2E"
b"Brood Wars Protoss 2 - Town F": b"PB2F"
b"Brood Wars Protoss 3 - Town A": b"PB3A"
b"Brood Wars Protoss 3 - Town B": b"PB3B"
b"Brood Wars Protoss 3 - Town C": b"PB3C"
b"Brood Wars Protoss 3 - Town D": b"PB3D"
b"Brood Wars Protoss 3 - Town E": b"PB3E"
b"Brood Wars Protoss 3 - Town F": b"PB3F"
b"Brood Wars Protoss 4 - Town A": b"PB4A"
b"Brood Wars Protoss 4 - Town B": b"PB4B"
b"Brood Wars Protoss 4 - Town C": b"PB4C"
b"Brood Wars Protoss 4 - Town D": b"PB4D"
b"Brood Wars Protoss 4 - Town E": b"PB4E"
b"Brood Wars Protoss 4 - Town F": b"PB4F"
b"Brood Wars Protoss 5 - Town A": b"PB5A"
b"Brood Wars Protoss 5 - Town B": b"PB5B"
b"Brood Wars Protoss 5 - Town C": b"PB5C"
b"Brood Wars Protoss 5 - Town D": b"PB5D"
b"Brood Wars Protoss 5 - Town E": b"PB5E"
b"Brood Wars Protoss 5 - Town F": b"PB5F"
b"Brood Wars Protoss 6 - Town A": b"PB6A"
b"Brood Wars Protoss 6 - Town B": b"PB6B"
b"Brood Wars Protoss 6 - Town C": b"PB6C"
b"Brood Wars Protoss 6 - Town D": b"PB6D"
b"Brood Wars Protoss 6 - Town E": b"PB6E"
b"Brood Wars Protoss 6 - Town F": b"PB6F"
b"Brood Wars Protoss 7 - Town A": b"PB7A"
b"Brood Wars Protoss 7 - Town B": b"PB7B"
b"Brood Wars Protoss 7 - Town C": b"PB7C"
b"Brood Wars Protoss 7 - Town D": b"PB7D"
b"Brood Wars Protoss 7 - Town E": b"PB7E"
b"Brood Wars Protoss 7 - Town F": b"PB7F"
b"Brood Wars Protoss 8 - Town A": b"PB8A"
b"Brood Wars Protoss 8 - Town B": b"PB8B"
b"Brood Wars Protoss 8 - Town C": b"PB8C"
b"Brood Wars Protoss 8 - Town D": b"PB8D"
b"Brood Wars Protoss 8 - Town E": b"PB8E"
b"Brood Wars Protoss 8 - Town F": b"PB8F"
b"Brood Wars Terran 1 - Town A": b"TB1A"
b"Brood Wars Terran 1 - Town B": b"TB1B"
b"Brood Wars Terran 1 - Town C": b"TB1C"
b"Brood Wars Terran 1 - Town D": b"TB1D"
b"Brood Wars Terran 1 - Town E": b"TB1E"
b"Brood Wars Terran 1 - Town F": b"TB1F"
b"Brood Wars Terran 2 - Town A": b"TB2A"
b"Brood Wars Terran 2 - Town B": b"TB2B"
b"Brood Wars Terran 2 - Town C": b"TB2C"
b"Brood Wars Terran 2 - Town D": b"TB2D"
b"Brood Wars Terran 2 - Town E": b"TB2E"
b"Brood Wars Terran 2 - Town F": b"TB2F"
b"Brood Wars Terran 3 - Town A": b"TB3A"
b"Brood Wars Terran 3 - Town B": b"TB3B"
b"Brood Wars Terran 3 - Town C": b"TB3C"
b"Brood Wars Terran 3 - Town D": b"TB3D"
b"Brood Wars Terran 3 - Town E": b"TB3E"
b"Brood Wars Terran 3 - Town F": b"TB3F"
b"Brood Wars Terran 4 - Town A": b"TB4A"
b"Brood Wars Terran 4 - Town B": b"TB4B"
b"Brood Wars Terran 4 - Town C": b"TB4C"
b"Brood Wars Terran 4 - Town D": b"TB4D"
b"Brood Wars Terran 4 - Town E": b"TB4E"
b"Brood Wars Terran 4 - Town F": b"TB4F"
b"Brood Wars Terran 5 - Town A": b"TB5A"
b"Brood Wars Terran 5 - Town B": b"TB5B"
b"Brood Wars Terran 5 - Town C": b"TB5C"
b"Brood Wars Terran 5 - Town D": b"TB5D"
b"Brood Wars Terran 5 - Town E": b"TB5E"
b"Brood Wars Terran 5 - Town F": b"TB5F"
b"Brood Wars Terran 6 - Town A": b"TB6A"
b"Brood Wars Terran 6 - Town B": b"TB6B"
b"Brood Wars Terran 6 - Town C": b"TB6C"
b"Brood Wars Terran 6 - Town D": b"TB6D"
b"Brood Wars Terran 6 - Town E": b"TB6E"
b"Brood Wars Terran 6 - Town F": b"TB6F"
b"Brood Wars Terran 7 - Town A": b"TB7A"
b"Brood Wars Terran 7 - Town B": b"TB7B"
b"Brood Wars Terran 7 - Town C": b"TB7C"
b"Brood Wars Terran 7 - Town D": b"TB7D"
b"Brood Wars Terran 7 - Town E": b"TB7E"
b"Brood Wars Terran 7 - Town F": b"TB7F"
b"Brood Wars Terran 8 - Town A": b"TB8A"
b"Brood Wars Terran 8 - Town B": b"TB8B"
b"Brood Wars Terran 8 - Town C": b"TB8C"
b"Brood Wars Terran 8 - Town D": b"TB8D"
b"Brood Wars Terran 8 - Town E": b"TB8E"
b"Brood Wars Terran 8 - Town F": b"TB8F"
b"Brood Wars Zerg 1 - Town A": b"ZB1A"
b"Brood Wars Zerg 1 - Town B": b"ZB1B"
b"Brood Wars Zerg 1 - Town C": b"ZB1C"
b"Brood Wars Zerg 1 - Town D": b"ZB1D"
b"Brood Wars Zerg 1 - Town E": b"ZB1E"
b"Brood Wars Zerg 1 - Town F": b"ZB1F"
b"Brood Wars Zerg 2 - Town A": b"ZB2A"
b"Brood Wars Zerg 2 - Town B": b"ZB2B"
b"Brood Wars Zerg 2 - Town C": b"ZB2C"
b"Brood Wars Zerg 2 - Town D": b"ZB2D"
b"Brood Wars Zerg 2 - Town E": b"ZB2E"
b"Brood Wars Zerg 2 - Town F": b"ZB2F"
b"Brood Wars Zerg 3 - Town A": b"ZB3A"
b"Brood Wars Zerg 3 - Town B": b"ZB3B"
b"Brood Wars Zerg 3 - Town C": b"ZB3C"
b"Brood Wars Zerg 3 - Town D": b"ZB3D"
b"Brood Wars Zerg 3 - Town E": b"ZB3E"
b"Brood Wars Zerg 3 - Town F": b"ZB3F"
b"Brood Wars Zerg 4 - Town A": b"ZB4A"
b"Brood Wars Zerg 4 - Town B": b"ZB4B"
b"Brood Wars Zerg 4 - Town C": b"ZB4C"
b"Brood Wars Zerg 4 - Town D": b"ZB4D"
b"Brood Wars Zerg 4 - Town E": b"ZB4E"
b"Brood Wars Zerg 4 - Town F": b"ZB4F"
b"Brood Wars Zerg 5 - Town A": b"ZB5A"
b"Brood Wars Zerg 5 - Town B": b"ZB5B"
b"Brood Wars Zerg 5 - Town C": b"ZB5C"
b"Brood Wars Zerg 5 - Town D": b"ZB5D"
b"Brood Wars Zerg 5 - Town E": b"ZB5E"
b"Brood Wars Zerg 5 - Town F": b"ZB5F"
b"Brood Wars Zerg 6 - Town A": b"ZB6A"
b"Brood Wars Zerg 6 - Town B": b"ZB6B"
b"Brood Wars Zerg 6 - Town C": b"ZB6C"
b"Brood Wars Zerg 6 - Town D": b"ZB6D"
b"Brood Wars Zerg 6 - Town E": b"ZB6E"
b"Brood Wars Zerg 6 - Town F": b"ZB6F"
b"Brood Wars Zerg 7 - Town A": b"ZB7A"
b"Brood Wars Zerg 7 - Town B": b"ZB7B"
b"Brood Wars Zerg 7 - Town C": b"ZB7C"
b"Brood Wars Zerg 7 - Town D": b"ZB7D"
b"Brood Wars Zerg 7 - Town E": b"ZB7E"
b"Brood Wars Zerg 7 - Town F": b"ZB7F"
b"Brood Wars Zerg 8 - Town A": b"ZB8A"
b"Brood Wars Zerg 8 - Town B": b"ZB8B"
b"Brood Wars Zerg 8 - Town C": b"ZB8C"
b"Brood Wars Zerg 8 - Town D": b"ZB8D"
b"Brood Wars Zerg 8 - Town E": b"ZB8E"
b"Brood Wars Zerg 8 - Town F": b"ZB8F"
b"Brood Wars Zerg 9 - Town A": b"ZB9A"
b"Brood Wars Zerg 9 - Town B": b"ZB9B"
b"Brood Wars Zerg 9 - Town C": b"ZB9C"
b"Brood Wars Zerg 9 - Town D": b"ZB9D"
b"Brood Wars Zerg 9 - Town E": b"ZB9E"
b"Brood Wars Zerg 9 - Town F": b"ZB9F"
b"Brood Wars Zerg 10 - Town A": b"ZB0A"
b"Brood Wars Zerg 10 - Town B": b"ZB0B"
b"Brood Wars Zerg 10 - Town C": b"ZB0C"
b"Brood Wars Zerg 10 - Town D": b"ZB0D"
b"Brood Wars Zerg 10 - Town E": b"ZB0E"
b"Brood Wars Zerg 10 - Town F": b"ZB0F"
```

  





## Weapon

```JavaScript
"Gauss Rifle": 0
"Gauss Rifle (Raynor)": 1
"C-10 Concussion Rifle": 2
"C-10 Concussion Rifle (Kerrigan)": 3
"Fragmentation Grenade": 4
"Fragmentation Grenade (Raynor)": 5
"Spider Mines": 6
"Twin Autocannons": 7
"Hellfire Missile Pack": 8
"Twin Autocannons (Schezar)": 9
"Hellfire Missile Pack (Schezar)": 10
"Arclite Cannon": 11
"Arclite Cannon (Duke)": 12
"Fusion Cutter": 13
"Fusion Cutter (Harvest)": 14
"Gemini Missiles": 15
"Burst Lasers": 16
"Gemini Missiles (Kazansky)": 17
"Burst Lasers (Kazansky)": 18
"ATS Laser Battery": 19
"ATA Laser Battery": 20
"ATS Laser Battery (Norad II+Mengsk+DuGalle)": 21
"ATA Laser Battery (Norad II+Mengsk+DuGalle)": 22
"ATS Laser Battery (Norad II)": 21
"ATA Laser Battery (Norad II)": 22
"ATS Laser Battery (Mengsk)": 21
"ATA Laser Battery (Mengsk)": 22
"ATS Laser Battery (DuGalle)": 21
"ATA Laser Battery (DuGalle)": 22
"ATS Laser Battery (Hyperion)": 23
"ATA Laser Battery (Hyperion)": 24
"Flame Thrower": 25
"Flame Thrower (Montag)": 26
"Arclite Shock Cannon": 27
"Arclite Shock Cannon (Duke)": 28
"Longbolt Missiles": 29
"Yamato Gun": 30
"Nuclear Missile": 31
"Lockdown": 32
"EMP Shockwave": 33
"Irradiate": 34
"Claws": 35
"Claws (Devouring One)": 36
"Claws (Infested Kerrigan)": 37
"Needle Spines": 38
"Needle Spines (Hunter Killer)": 39
"Kaiser Blades": 40
"Kaiser Blades (Torrasque)": 41
"Toxic Spores": 42
"Spines": 43
"Spines (Harvest)": 44
"Acid Spray": 45
"Acid Spore": 46
"Acid Spore (Kukulza)": 47
"Glave Wurm": 48
"Glave Wurm (Kukulza)": 49
"Venom": 50
"Venom (Unclean One)": 51
"Seeker Spores": 52
"Subterranean Tentacle": 53
"Suicide (Infested Terran)": 54
"Suicide (Scourge)": 55
"Parasite": 56
"Spawn Broodlings": 57
"Ensnare": 58
"Dark Swarm": 59
"Plague": 60
"Consume": 61
"Particle Beam": 62
"Particle Beam (Harvest)": 63
"Psi Blades": 64
"Psi Blades (Fenix)": 65
"Phase Disruptor": 66
"Phase Disruptor (Fenix)": 67
"Psi Assault": 68
"Psi Assault (Tassadar)": 69
"Psionic Shockwave": 70
"Psionic Shockwave (Tassadar/Zeratul)": 71
"Unused72": 72
"Dual Photon Blasters": 73
"Anti-matter Missiles": 74
"Dual Photon Blasters (Mojo)": 75
"Anti-matter Missiles (Mojo)": 76
"Phase Disruptor Cannon": 77
"Phase Disruptor Cannon (Danimoth)": 78
"Pulse Cannon": 79
"STS Photon Cannon": 80
"STA Photon Cannon": 81
"Scarab": 82
"Stasis Field": 83
"Psi Storm": 84
"Warp Blades (Zeratul)": 85
"Warp Blades (Hero)": 86
"Missiles": 87
"Laser Battery1": 88
"Tormentor Missiles": 89
"Bombs": 90
"Raider Gun": 91
"Laser Battery2": 92
"Laser Battery3": 93
"Dual Photon Blasters": 94
"Flechette Grenade": 95
"Twin Autocannons (Floor Trap)": 96
"Hellfire Missile Pack (Wall Trap)": 97
"Flame Thrower (Wall Trap)": 98
"Hellfire Missile Pack (Floor Trap)": 99
"Neutron Flare": 100
"Disruption Web": 101
"Restoration": 102
"Halo Rockets": 103
"Corrosive Acid": 104
"Mind Control": 105
"Feedback": 106
"Optical Flare": 107
"Maelstrom": 108
"Subterranean Spines": 109
"Gauss Rifle0": 110
"Unused110": 110
"Warp Blades": 111
"C-10 Concussion Rifle (Duran)": 112
"C-10 Concussion Rifle (Infested Duran)": 113
"Dual Photon Blasters (Artanis)": 114
"Anti-matter Missiles (Artanis)": 115
"C-10 Concussion Rifle (Stukov)": 116
"Gauss Rifle1": 117
"Gauss Rifle2": 118
"Gauss Rifle3": 119
"Gauss Rifle4": 120
"Gauss Rifle5": 121
"Gauss Rifle6": 122
"Gauss Rifle7": 123
"Gauss Rifle8": 124
"Gauss Rifle9": 125
"Gauss Rifle10": 126
"Gauss Rifle11": 127
"Gauss Rifle12": 128
"Gauss Rifle13": 129
"Unused117": 117
"Unused118": 118
"Unused119": 119
"Unused120": 120
"Unused121": 121
"Unused122": 122
"Unused123": 123
"Unused124": 124
"Unused125": 125
"Unused126": 126
"Unused127": 127
"Unused128": 128
"Unused129": 129
"None": 130
```

  



## Tech

```JavaScript
"Stim Packs": 0
"Lockdown": 1
"EMP Shockwave": 2
"Spider Mines": 3
"Scanner Sweep": 4
"Tank Siege Mode": 5
"Defensive Matrix": 6
"Irradiate": 7
"Yamato Gun": 8
"Cloaking Field": 9
"Personnel Cloaking": 10
"Burrowing": 11
"Infestation": 12
"Spawn Broodlings": 13
"Dark Swarm": 14
"Plague": 15
"Consume": 16
"Ensnare": 17
"Parasite": 18
"Psionic Storm": 19
"Hallucination": 20
"Recall": 21
"Stasis Field": 22
"Archon Warp": 23
"Restoration": 24
"Disruption Web": 25
"Unused26": 26
"Mind Control": 27
"Dark Archon Meld": 28
"Feedback": 29
"Optical Flare": 30
"Maelstrom": 31
"Lurker Aspect": 32
"Unused33": 33
"Healing": 34
"Unused35": 35
"Unused36": 36
"Unused37": 37
"Unused38": 38
"Unused39": 39
"Unused40": 40
"Unused41": 41
"Unused42": 42
"Unused43": 43
```

  



## Upgrade

```JavaScript
"Terran Infantry Armor": 0
"Terran Vehicle Plating": 1
"Terran Ship Plating": 2
"Zerg Carapace": 3
"Zerg Flyer Carapace": 4
"Protoss Armor": 5
"Protoss Plating": 6
"Terran Infantry Weapons": 7
"Terran Vehicle Weapons": 8
"Terran Ship Weapons": 9
"Zerg Melee Attacks": 10
"Zerg Missile Attacks": 11
"Zerg Flyer Attacks": 12
"Protoss Ground Weapons": 13
"Protoss Air Weapons": 14
"Protoss Plasma Shields": 15
"U-238 Shells": 16
"Ion Thrusters": 17
"Burst Lasers (Unused)": 18
"Titan Reactor (SV +50)": 19
"Ocular Implants": 20
"Moebius Reactor (Ghost +50)": 21
"Apollo Reactor (Wraith +50)": 22
"Colossus Reactor (BC +50)": 23
"Ventral Sacs": 24
"Antennae": 25
"Pneumatized Carapace": 26
"Metabolic Boost": 27
"Adrenal Glands": 28
"Muscular Augments": 29
"Grooved Spines": 30
"Gamete Meiosis (Queen +50)": 31
"Metasynaptic Node (Defiler +50)": 32
"Singularity Charge": 33
"Leg Enhancements": 34
"Scarab Damage": 35
"Reaver Capacity": 36
"Gravitic Drive": 37
"Sensor Array": 38
"Gravitic Boosters": 39
"Khaydarin Amulet (HT +50)": 40
"Apial Sensors": 41
"Gravitic Thrusters": 42
"Carrier Capacity": 43
"Khaydarin Core (Arbiter +50)": 44
"Unused45": 45
"Unused46": 46
"Argus Jewel (Corsair +50)": 47
"Unused48": 48
"Argus Talisman (DA +50)": 49
"Unused50": 50
"Caduceus Reactor (Medic +50)": 51
"Chitinous Plating": 52
"Anabolic Synthesis": 53
"Charon Booster": 54
"Unused55": 55
"Unused56": 56
"Unused57": 57
"Unused58": 58
"Unused59": 59
"Unused60": 60,
```

  



## UnitOrder

```Python
"Die": 0,  # Causes the unit to die. Normal units run the death iscript animation,
# while hallucinated units have the sound/sprite spawned and then are removed.
"Stop": 1,  # Normal unit stop command. Stops current order chain, and then goes to idle.
"Guard": 2,  # Generic Guard order. Determines what guard command a unit uses.
"Guard (Normal)": 2,
"Player Guard": 3,  # Attacking Mobile unit guard order.
"Guard (Player)": 3,
"Turret Guard": 4,  # Attacking unit turret guard.
"Guard (Subunit)": 4,
"Bunker Guard": 5,  # Transport building guard. Set when a building picks up a unit.
"Guard (Bunker)": 5,
"Move": 6,  # Unit move. Ignores enemies on way to destination.
"Ignore (Normal)": 6,
"Reaver Stop": 7,  # Stop order for the reaver.
"Stop (Reaver)": 7,
"Attack1": 8,  # Generic attack order.
"Attack": 8,
"Attack2": 9,  # Move to attack shrouded building.
"Attack (Obscured)": 9,
"Attack Unit": 10,  # Mobile unit attacking a unit/building.
"Attack Unit (Normal)": 10,
"Attack Fixed Range": 11,  # Attack for an immobile unit. Lurker attack.
"Attack In Range": 11,
"Attack Tile": 12,
"Attack Ground (Unused)": 12,
"Hover": 13,
"Hover (Unused)": 13,
"Attack Move": 14,  # Unit move, attack enemies along path to target.
"Infest Mine 1": 15,  # Ran when a unit is being infested.
"Building Is Being Infested": 15,
"Nothing 1": 16,
"Nothing 1 (Unused)": 16,
"Powerup 1": 17,  # Unknown. Speculated to be a Powerup being built order.
"Power-Up (Unused)": 17,
"Tower Guard": 18,  # Building tower guard.
"Guard (Building)": 18,
"Tower Attack": 19,  # Building tower attack.
"Attack (Building)": 19,
"Vulture Mine": 20,  # Spidermine idle order.
"Script (Spider Mine)": 20,
"Stay In Range": 21,  # Mobile unit base attack.
"Turret Attack": 22,  # Mobile Unit Turret attack.
"Attack (Subunit)": 22,
"Nothing 2": 23,  # Do nothing, next order.
"Nothing 2 (Normal)": 23,
"Nothing 3": 24,  # Unknown, used when a unit is changing state between siege <-> normal.
"Nothing 3 (Unused)": 24,
"Drone Start Build": 25,  # Move to target position and run drone build.
"Drone Start Mutate": 25,
"Drone Build": 26,  # Check resources and run drone land.
"Drone Mutate": 26,
"Infest Mine 2": 27,  # Move to Infest a unit.
"Cast Spell (Infest 1)": 27,
"Infest Mine 3": 28,  # Move to Infest shrouded unit
"Cast Spell (Infest 2)": 28,
"Infest Mine 4": 29,  # Infest Unit. Hides unit, runs infest 1 on target, then reshows unit.
"Infest (Queen)": 29,
"Build Terran": 30,  # Move/Start Terran Building.
"Build (SCV)": 30,
"Build Protoss 1": 31,  # Full Protoss Building order.
"Build (Probe)": 31,
"Build Protoss 2": 32,  # Creates the Protoss Building.
"Create Building (Probe)": 32,
"Constructing Building": 33,  # SCV is building.
"Is Building (SCV)": 33,
"Repair 1": 34,  # Repair Unit.
"Repair Unit (SCV)": 34,
"Repair 2": 35,  # Move to repair shrouded building.
"Repair Unit (Obscured)": 35,
"Place Add-On": 36,  # Move and start addon.
"Build Add-On": 37,  # Building Addon.
"Train": 38,  # Training Unit.
"Train (Normal)": 38,
"Rally Point 1": 39,  # Rally to Visible Unit. Causes units to follow the selected unit.
"Rally to Visible Unit": 39,
"Rally Point 2": 40,  # Rally to tile.
"Rally to Ground Tile": 40,
"Zerg Birth": 41,  # Unit is being born.
"Morph 1": 42,  # Unit Morph
"Unit Morph": 42,
"Morph 2": 43,  # Building Morph
"Building Morph": 43,
"Build Self 1": 44,  # Terran Building, Is being built.
"Building Is Constructed (Terran)": 44,
"Zerg Build Self": 45,  # Zerg Building build order.
"Build 5": 46,  # Nydus canal exit build order.
"Build (Nydus Canal Exit)": 46,
"Enter Nydus Canal": 47,  # Enter/transport through nydus canal
"Enter (Nydus Canal)": 47,
"Build Self 2": 48,  # Protoss Building being built order.
"Building Is Constructed (Protoss)": 48,
"Follow": 49,  # Move to/with unit or building. Causes units to load into transports
# or enter nydus canal or recharge shields.
"Carrier": 50,  # Idle command for the carrier.
"Idle (Carrier)": 50,
"Carrier Ignore 1": 51,  # Carrier move command. Ignores enemies
"Move (Carrier&Reaver)": 51,
"Carrier Stop": 52,  # Carrier stop command. Runs idle.
"Stop (Carrier)": 52,
"Carrier Attack 1": 53,  # Generic Carrier attack command.
"Attack (Carrier)": 53,
"Carrier Attack 2": 54,  # Move to attack shrouded building.
"Attack Obscured (Carrier)": 54,
"Carrier Ignore 2": 55,  # Unknown. Possibly a secondary move.
"Ignore 2 (Carrier)": 55,
"Carrier Fight": 56,  # Carrier Attack Unit.
"Attack Unit (Carrier)": 56,
"Carrier Hold": 57,  # Carrier Hold Position.
"Hold Position 1": 57,
"Hold Position (Carrier)": 57,
"Reaver": 58,  # Reaver Idle order.
"Idle (Reaver)": 58,
"Reaver Attack 1": 59,  # Generic reaver attack order.
"Attack (Reaver)": 59,
"Reaver Attack 2": 60,  # Move to attack shrouded building
"Attack Obscured (Reaver)": 60,
"Reaver Fight": 61,  # Reaver attack unit.
"Attack Unit (Reaver)": 61,
"Reaver Hold": 62,  # Reaver hold position.
"Hold Position (Reaver)": 62,
"Train Fighter": 63,  # Training subunit(scarab, interceptor).
# Causes all interceptors within a carrier to be healed when not attacking.
"Training (Subunit)": 63,
"Strafe Unit 1": 64,  # Interceptor move and attack.
"Move&Attack (Interceptor)": 64,
"Strafe Unit 2": 65,  # Scarab move and attack.
"Move&Attack (Scarab)": 65,
"Recharge Shields 1": 66,  # Unit recharge shields.
"Recharge Shields (Unit)": 66,
"Recharge Shields 2": 67,  # Shield Battery, recharge shield cast on unit or ground.
# Unit runs recharge shields 1, shield battery runs shield battery.
# If cast on ground, recharges all units within rechargeable radius.
"Recharge Shields (Global)": 67,
"Shield Battery": 68,  # Shield Battery, is recharging.
"Shield Battery Is Recharging": 68,
"Return": 69,  # Interceptor return to parent.
"Return To Parent (Interceptor)": 69,
"Drone Land": 70,  # Drone landing order. Used when building.
"Land (Drone)": 70,
"Building Land": 71,  # Building land order.
"Land (Building)": 71,
"Building Lift Off": 72,  # Begin Building Liftoff
"Lift Off (Building)": 72,
"Drone Lift Off": 73,  # Begin Drone liftoff
"Lift Off (Drone)": 73,
"Lift Off": 74,  # Unit is lifting off.
"Is Lifting Off": 74,
"Research Tech": 75,  # Building researching tech.
"Is Researching Technology": 75,
"Upgrade": 76,  # Building researching upgrade.
"Is Performing Upgrade": 76,
"Larva": 77,  # Idle order for larva. Make sure it stays on creep,
# dies if off, and says within the range of the parent it came from.
"Idle (Larva)": 77,
"Spawning Larva": 78,  # Building is spawning larva.
"Is Spawning Larva": 78,
"Harvest 1": 79,  # Generic move to harvest order.
"Move to Harvest": 79,
"Harvest 2": 80,  # Move to harvest shrouded minerals/gas
"Move to Harvest Obscured": 80,
"Harvest Gas 1": 81,  # Move to harvest gas.
"Move to Harvest Gas": 81,
"Harvest Gas 2": 82,  # Check if it can enter the gas mine(no unit in it).
"Can Enter Gas Mine": 82,
"Harvest Gas 3": 83,  # Enter/exit mine, set return order.
"Enter/Exit Gas Mine": 83,
"Return Gas": 84,  # Return order, has gas.
"Harvest Minerals 1": 85,  # Move to harvest minerals.
"Move to Minerals": 85,
"Move to Harvest Minerals": 85,
"Harvest Minerals 2": 86,  # Can harvest minerals(one unit per field).
"Can Harvest Minerals": 86,
"Harvest Minerals 3": 87,  # Harvesting minerals. Runs iscript to spawn weapon.
"Mining Minerals": 87,
"Harvesting Minerals": 87,
"Harvest 3": 88,  # Harvesting minerals is interrupted.
"Harvesting Minerals Interrupted": 88,
"Harvest 4": 89,  # Unknown harvest command.
"Harvest 4 (Unknown)": 89,
"Return Minerals": 90,  # Return resources /B Has minerals.
"Harvest 5": 91,  # Harvest Interrupt /B recharge shields.
"Harvesting Interrupted - Recharge Shields": 91,
"Enter Transport": 92,  # Move/enter a transport.
"Move/Enter Transport": 92,
"Pick Up 1": 93,  # Transport Idle command.
"Idle (Transport)": 93,
"Pick Up 2": 94,  # Mobile Transport unit pickup.
"Load Unit (Mobile Transport)": 94,
"Pick Up 3": 95,  # Building pickup.
"Load Unit (Bunker)": 95,
"Pick Up 4": 96,  # Unknown /B AI pickup?
"Load Unit (Unknown)": 96,
"Powerup 2": 97,  # Idle for powerups.
"Idle (Power-Up)": 97,
"Siege Mode": 98,  # Switch to Siege mode.
"Tank Mode": 99,  # Switch to Tank mode.
"Watch Target": 100,  # Immobile Unit base, watch the target.
"Initing Creep Growth": 101,  # Start Spreading Creep.
"Script (Starting Creep Growth)": 101,
"Spread Creep": 102,  # Spreads creep. If it is a larva producer, runs that order also.
"Script (Spread Creep&Spawn Larva)": 102,
"Stopping Creep Growth": 103,  # Stops creep growth.
"Script (Stopping Creep Growth)": 103,
"Guardian Aspect": 104,  # Unused, Morph 1 is used for unit morphing.
"Guardian Aspect (Unused)": 104,
"Warping Archon": 105,  # Move and start archon merge.
"Move and Morph Archon": 105,
"Completing Archon Summon": 106,  # Archon build self order.
"Hold Position 2": 107,  # Attacking Unit hold position.
"Hold Position (Normal)": 107,
"Hold Position 3": 108,  # Queen Hold position.
"Hold Position (Queen)": 108,
"Cloak": 109,  # Cloak Unit.
"Decloak": 110,  # Decloak Unit.
"Unload": 111,  # Unload a unit from the transport.
"Unload Unit (Transport)": 111,
"Move Unload": 112,  # Move to unload site and run unload order.
"Move&Unload Unit (Transport)": 112,
"Fire Yamato Gun 1": 113,  # Cast Spell: Yamato.
"Cast Spell (Yamato Gun)": 113,
"Fire Yamato Gun 2": 114,  # Move to cast spell on shrouded building.
"Cast Spell On Obscured (Yamato Gun)": 114,
"Magna Pulse": 115,  # Cast Spell: Lockdown.
"Cast Spell (Lockdown)": 115,
"Burrow": 116,  # Burrow Unit.
"Burrowed": 117,  # Burrowed Unit idle.
"Idle (Burrowed)": 117,
"Unburrow": 118,  # Unburrow unit.
"Dark Swarm": 119,  # Cast Spell: Dark Swarm.
"Cast Spell (Dark Swarm)": 119,
"Cast Parasite": 120,  # Cast Spell: Parasite.
"Cast Spell (Parasite)": 120,
"Summon Broodlings": 121,  # Cast Spell: Spawn Broodings.
"Cast Spell (Spawn Broodling)": 121,
"EMP Shockwave": 122,  # Cast Spell: EMP Shockwave.
"Cast Spell (EMP Shockwave)": 122,
"Nuke Wait": 123,  # Unknown.
"Unknown": 123,
"Nuke Train": 124,  # Silo Idle
"Idle (Nuclear Silo)": 124,
"Nuke Launch": 125,  # Launch for nuclear missile.
"Attack (Nuke)": 125,
"Nuke Paint": 126,  # Move to and set nuke target.
"Move&Paint Nuke Target": 126,
"Nuke Unit": 127,  # Nuke the ground location of the unit.
"Attack Unit (Nuke)": 127,
"Nuke Ground": 128,  # Nuke ground.
"Attack Ground (Nuke)": 128,
"Nuke Track": 129,  # Ghost order during nuke.
"Nuke Track (Ghost)": 129,
"Initializing Arbiter": 130,  # Run nearby cloaking.
"Script (Cloak Nearby Units)": 130,
"Cloaking nearby units": 131,  # Cloak non arbiters within range.
"Cloak Nearby Units (Freezes the casting unit)": 131,
"Place Mine": 132,  # Place spider mine.
"Place Spider Mine": 132,
"Right Click Action": 133,  # right click, sets correct order based on target.
"Script (Right-Click Action)": 133,
"Sap Unit": 134,  # Suicide Attack Unit.
"Attack Unit (Infested Terran)": 134,
"Sap Location": 135,  # Suicide Attack tile.
"Attack Ground (Infested Terran)": 135,
"Hold Position 4": 136,  # Suicide Hold Position.
"Hold Position (Suicide Units)": 136,
"Teleport": 137,  # Recall(units within range of target pos).
"Cast Spell (Recall)": 137,
"Teleport to Location": 138,  # Causes units to teleport when being recalled.
"Teleport To Location (Freezes the casting unit)": 138,
"Place Scanner": 139,  # Place Scanner Sweep Unit at position.
"Cast Spell (Scanner Sweep)": 139,
"Scanner": 140,  # Scanner Sweep Unit idle.
"Idle (Scanner Sweep)": 140,
"Defensive Matrix": 141,  # Defensive Matrix cast on target.
"Cast Spell (Defensive Matrix)": 141,
"Psionic Storm": 142,  # Cast Spell: Psi Storm.
"Cast Spell (Psionic Storm)": 142,
"Irradiate": 143,  # Cast Spell: Irradiate.
"Cast Spell (Irradiate)": 143,
"Plague": 144,  # Cast Spell: Plague.
"Cast Spell (Plague)": 144,
"Consume": 145,  # Cast Spell: Consume.
"Cast Spell (Consume)": 145,
"Ensnare": 146,  # Cast Spell: Ensnare.
"Cast Spell (Ensnare)": 146,
"Stasis Field": 147,  # Cast Spell: Stasis Field.
"Cast Spell (Stasis Field)": 147,
"Hallucination 1": 148,  # Hallucination Cast on target.
"Cast Spell (Hallucination)": 148,
"Hallucination 2": 149,  # Kill Halluciation on spell cast.
"Script (Hallucination)": 149,
"Reset Collision 1": 150,  # Collision Reset between 2 units.
"Reset Collision (2 Units)": 150,
"Reset Collision 2": 151,  # Collision reset between harvester and mine.
"Reset Collision (Harvester&Mine)": 151,
"Patrol": 152,  # Patrol to target, queue patrol to original position.
"Patrol (Normal)": 152,
"CTF COP Init": 153,  # CTF Initialization
"CTF COP (Initialize)": 153,
"CTF COP 1": 154,  # CTF Idle
"Idle (CTF COP)": 154,
"CTF COP 2": 155,  # Unknown? Reset COP?
"Unknown CTF COP 2": 155,
"Computer AI": 156,  # AI Control.
"Script (Computer)": 156,
"Atk Move EP": 157,  # AI Attack Move?
"Attack Move (Computer)": 157,
"Harass Move": 158,  # Aggressive Attack Move? Units won't give up on a target.
# If they see it, they will attack it, even worse than attack move. Might be a computer attack move?
"Move (Harass)": 158,
"AI Patrol": 159,  # Moves units to the center of the current area that they are at?
# Not sure if the spacing is meant to allow for detectors to cover an area or not.
"Patrol (Computer)": 159,
"Guard Post": 160,  # Immobile Unit Guard.
"Guard (Computer)": 160,
"Rescuable Passive": 161,  # Rescuable unit idle.
"Idle (Rescuable)": 161,
"Neutral": 162,  # Neutral Unit idle.
"Idle (Neutral)": 162,
"Computer Return": 163,  # Return computer units to defensive position?
# Was seen returning units that had followed a unit outside of a base and killed it.
"Return To Base (Computer)": 163,
"Initing Psi Provider": 164,  # Init Psi Provider. Adds to some kind of linked list.
"Script (PSI Provider)": 164,
"Self Destrucing": 165,  # Remove unit.
"Fatal (Scarab)": 165,
"Critter": 166,  # Critter idle.
"Idle (Critter)": 166,
"Hidden Gun": 167,  # Trap idle order.
"Idle (Trap)": 167,
"Open Door": 168,  # Opens the door.
"Close Door": 169,  # Closes the door.
"Hide Trap": 170,  # Trap return to idle.
"Stop (Trap)": 170,
"Reveal Trap": 171,  # Trap attack.
"Attack (Trap)": 171,
"Enable Doodad": 172,  # Enable Doodad State.
"Disable Doodad": 173,  # Disable Doodad State.
"Warp In": 174,  # Unused. Left over from unit warp in which now exists in Starcraft 2.
"Warp In (Unused)": 174,
"Medic": 175,  # Idle command for the Terran Medic.
"Idle (Medic)": 175,
"Medic Heal 1": 176,  # Heal cast on target.
"Cast Spell (Heal)": 176,
"Heal Move": 177,  # Attack move command for the Terran Medic.
"Move (Medic)": 177,
"Medic Hold Position": 178,  # Holds Position for Terran Medics, heals units within range.
"Hold Position&Heal (Medic)": 178,
"Medic Heal 2": 179,  # Return to idle after heal.
"Return To Idle After Heal": 179,
"Restoration": 180,  # Cast Spell: Restoration.
"Cast Spell (Restoration)": 180,
"Cast Disruption Web": 181,  # Cast Spell: Disruption Web.
"Cast Spell (Disruption Web)": 181,
"Cast Mind Control": 182,  # Mind Control Cast on Target.
"Cast Spell (Mind Control)": 182,
"Warping Dark Archon": 183,  # Dark Archon Meld.
"Dark Archon Meld": 183,
"Cast Feedback": 184,  # Feedback cast on target.
"Cast Spell (Feedback)": 184,
"Cast Optical Flare": 185,  # Cast Spell: Optical Flare.
"Cast Spell (Optical Flare)": 185,
"Cast Maelstrom": 186,  # Cast Spell: Maelstrom.
"Cast Spell (Maelstrom)": 186,
"Junk Yard Dog": 187,  # Junk yard dog movement.
"Move (Junk Yard Dog)": 187,
"Fatal": 188,  # Nothing.
```

  



## Flingy

```JavaScript
"Scourge": 0
"Broodling": 1
"Infested Terran": 2
"Guardian Cocoon": 3
"Defiler": 4
"Drone": 5
"Egg": 6
"Guardian": 7
"Hydralisk": 8
"Infested Kerrigan": 9
"Larva": 10
"Mutalisk": 11
"Overlord": 12
"Queen": 13
"Ultralisk": 14
"Zergling": 15
"Cerebrate": 16
"Infested Command Center": 17
"Spawning Pool": 18
"Mature Chrysalis": 19
"Evolution Chamber": 20
"Creep Colony": 21
"Hatchery": 22
"Hive": 23
"Lair": 24
"Sunken Colony": 25
"Greater Spire": 26
"Defiler Mound": 27
"Queen's Nest": 28
"Nydus Canal": 29
"Overmind With Shell": 30
"Overmind Without Shell": 31
"Ultralisk Cavern": 32
"Extractor": 33
"Hydralisk Den": 34
"Spire": 35
"Spore Colony": 36
"Arbiter": 37
"Archon Energy": 38
"Carrier": 39
"Dragoon": 40
"Interceptor": 41
"Probe": 42
"Scout": 43
"Shuttle": 44
"High Templar": 45
"Dark Templar (Hero)": 46
"Reaver": 47
"Scarab": 48
"Zealot": 49
"Observer": 50
"Templar Archives": 51
"Assimilator": 52
"Observatory": 53
"Citadel of Adun": 54
"Forge": 55
"Gateway": 56
"Cybernetics Core": 57
"Khaydarin Crystal Formation": 58
"Nexus": 59
"Photon Cannon": 60
"Arbiter Tribunal": 61
"Pylon": 62
"Robotics Facility": 63
"Shield Battery": 64
"Stargate": 65
"Stasis Cell/Prison": 66
"Robotics Support Bay": 67
"Protoss Temple": 68
"Fleet Beacon": 69
"Battlecruiser": 70
"Civilian": 71
"Dropship": 72
"Firebat": 73
"Ghost": 74
"Goliath Base": 75
"Goliath Turret": 76
"Sarah Kerrigan": 77
"Marine": 78
"Scanner Sweep": 79
"Wraith": 80
"SCV": 81
"Siege Tank (Tank) Base": 82
"Siege Tank (Tank) Turret": 83
"Siege Tank (Siege) Base": 84
"Siege Tank (Siege) Turret": 85
"Science Vessel (Base)": 86
"Science Vessel (Turret)": 87
"Vulture": 88
"Spider Mine": 89
"Academy": 90
"Barracks": 91
"Armory": 92
"Comsat Station": 93
"Command Center": 94
"Supply Depot": 95
"Control Tower": 96
"Factory": 97
"Covert Ops": 98
"Ion Cannon": 99
"Machine Shop": 100
"Missile Turret (Base)": 101
"Crashed Battlecruiser": 102
"Physics Lab": 103
"Bunker": 104
"Refinery": 105
"Immobile Barracks": 106
"Science Facility": 107
"Nuke Silo": 108
"Nuclear Missile": 109
"Starport": 110
"Engineering Bay": 111
"Terran Construction (Large)": 112
"Terran Construction (Small)": 113
"Ragnasaur (Ashworld)": 114
"Rhynadon (Badlands)": 115
"Bengalaas (Jungle)": 116
"Vespene Geyser": 117
"Mineral Field Type1": 118
"Mineral Field Type2": 119
"Mineral Field Type3": 120
"Independent Starport (Unused)": 121
"Zerg Beacon": 122
"Terran Beacon": 123
"Protoss Beacon": 124
"Dark Swarm": 125
"Flag": 126
"Young Chrysalis": 127
"Psi Emitter": 128
"Data Disc": 129
"Khaydarin Crystal": 130
"Mineral Chunk Type1": 131
"Mineral Chunk Type2": 132
"Protoss Gas Orb Type1": 133
"Protoss Gas Orb Type2": 134
"Zerg Gas Sac Type1": 135
"Zerg Gas Sac Type2": 136
"Terran Gas Tank Type1": 137
"Terran Gas Tank Type2": 138
"Map Revealer": 139
"Start Location": 140
"Fusion Cutter Hit": 141
"Gauss Rifle Hit": 142
"C-10 Canister Rifle Hit": 143
"Gemini Missiles": 144
"Fragmentation Grenade": 145
"Lockdown/LongBolt/Hellfire Missile": 146
"Unused Lockdown": 147
"ATS/ATA Laser Battery": 148
"Burst Lasers": 149
"Arclite Shock Cannon Hit": 150
"EMP Missile": 151
"Dual Photon Blasters Hit": 152
"Particle Beam Hit": 153
"Anti-Matter Missile": 154
"Pulse Cannon": 155
"Psionic Shockwave Hit": 156
"Psionic Storm": 157
"Yamato Gun": 158
"Phase Disruptor": 159
"STA/STS Cannon Overlay": 160
"Sunken Colony Tentacle": 161
"Venom (Unused Zerg Weapon)": 162
"Acid Spore": 163
"Unknown164": 164
"Glave Wurm": 165
"Seeker Spores": 166
"Queen Spell Carrier": 167
"Plague Cloud": 168
"Consume": 169
"Ensnare": 170
"Needle Spine Hit": 171
"White Circle (Invisible)": 172
"Left Upper Level Door": 173
"Right Upper Level Door": 174
"Substructure Left Door": 175
"Substructure Right Door": 176
"Substructure Opening Hole": 177
"Floor Gun Trap": 178
"Floor Missile Trap": 179
"Wall Missile Trap": 180
"Wall Missile Trap2": 181
"Wall Flame Trap": 182
"Wall Flame Trap2": 183
"Lurker Egg": 184
"Devourer": 185
"Lurker": 186
"Dark Archon Energy": 187
"Dark Templar (Unit)": 188
"Medic": 189
"Valkyrie": 190
"Corsair": 191
"Disruption Web": 192
"Overmind Cocoon": 193
"Psi Disrupter": 194
"Warp Gate": 195
"Power Generator": 196
"Xel'Naga Temple": 197
"Scantid (Desert)": 198
"Kakaru (Twilight)": 199
"Ursadon (Ice)": 200
"Optical Flare Grenade": 201
"Halo Rockets": 202
"Subterranean Spines": 203
"Corrosive Acid Shot": 204
"Corrosive Acid Hit": 205
"Neutron Flare": 206
"Uraj": 207
"Khalis": 208
```

  



## Image

```JavaScript
"Scourge": 0
"Scourge Shadow": 1
"Scourge Birth": 2
"Scourge Death": 3
"Scourge Explosion": 4
"Broodling": 5
"Broodling Shadow": 6
"Broodling Remnants": 7
"Infested Terran": 8
"Infested Terran Shadow": 9
"Infested Terran Explosion": 10
"Guardian Cocoon": 11
"Guardian Cocoon Shadow": 12
"Defiler": 13
"Defiler Shadow": 14
"Defiler Birth": 15
"Defiler Remnants": 16
"Drone": 17
"Drone Shadow": 18
"Drone Birth": 19
"Drone Remnants": 20
"Egg": 21
"Egg Shadow": 22
"Egg Spawn": 23
"Egg Remnants": 24
"Guardian": 25
"Guardian Shadow": 26
"Guardian Birth": 27
"Guardian Death": 28
"Hydralisk": 29
"Hydralisk Shadow": 30
"Hydralisk Birth": 31
"Hydralisk Remnants": 32
"Infested Kerrigan": 33
"Infested Kerrigan Shadow": 34
"Needle Spines": 35
"Larva": 36
"Larva Remnants": 37
"Mutalisk": 38
"Mutalisk Shadow": 39
"Mutalisk Birth": 40
"Mutalisk Death": 41
"Overlord": 42
"Overlord Shadow": 43
"Overlord Birth": 44
"Overlord Death": 45
"Queen": 46
"Queen Shadow": 47
"Queen Death": 48
"Queen Birth": 49
"Ultralisk": 50
"Ultralisk Shadow": 51
"Ultralisk Birth": 52
"Ultralisk Remnants": 53
"Zergling": 54
"Zergling Shadow": 55
"Zergling Birth": 56
"Zergling Remnants": 57
"Zerg Air Death Explosion (Large)": 58
"Zerg Air Death Explosion (Small)": 59
"Zerg Building Explosion": 60
"Cerebrate": 61
"Cerebrate Shadow": 62
"Infested Command Center": 63
"Spawning Pool": 64
"Spawning Pool Shadow": 65
"Evolution Chamber": 66
"Evolution Chamber Shadow": 67
"Creep Colony": 68
"Creep Colony Shadow": 69
"Hatchery": 70
"Hatchery Shadow": 71
"Hive": 72
"Hive Shadow": 73
"Lair": 74
"Lair Shadow": 75
"Sunken Colony": 76
"Sunken Colony Shadow": 77
"Mature Chrysalis": 78
"Mature Chrysalis Shadow": 79
"Greater Spire": 80
"Greater Spire Shadow": 81
"Defiler Mound": 82
"Defiler Mound Shadow": 83
"Queen's Nest": 84
"Queen Nest Shadow": 85
"Nydus Canal": 86
"Nydus Canal Shadow": 87
"Overmind With Shell": 88
"Overmind Remnants": 89
"Overmind Without Shell": 90
"Ultralisk Cavern": 91
"Ultralisk Cavern Shadow": 92
"Extractor": 93
"Extractor Shadow": 94
"Hydralisk Den": 95
"Hydralisk Den Shadow": 96
"Spire": 97
"Spire Shadow": 98
"Spore Colony": 99
"Spore Colony Shadow": 100
"Infested Command Center Overlay": 101
"Zerg Construction (Large)": 102
"Zerg Building Morph": 103
"Zerg Construction (Medium)": 104
"Zerg Construction (Small)": 105
"Zerg Building Construction Shadow": 106
"Zerg Building Spawn (Small)": 107
"Zerg Building Spawn (Medium)": 108
"Zerg Building Spawn (Large)": 109
"Zerg Building Rubble (Small)": 110
"Zerg Building Rubble (Large)": 111
"Carrier": 112
"Carrier Shadow": 113
"Carrier Engines": 114
"Carrier Warp Flash": 115
"Interceptor": 116
"Interceptor Shadow": 117
"Shuttle": 118
"Shuttle Shadow": 119
"Shuttle Engines": 120
"Shuttle Warp Flash": 121
"Dragoon": 122
"Dragoon Shadow": 123
"Dragoon Remnants": 124
"Dragoon Warp Flash": 125
"High Templar": 126
"High Templar Shadow": 127
"High Templar Warp Flash": 128
"Dark Templar (Hero)": 129
"Arbiter": 130
"Arbiter Shadow": 131
"Arbiter Engines": 132
"Arbiter Warp Flash": 133
"Archon Energy": 134
"Archon Being": 135
"Archon Swirl": 136
"Probe": 137
"Probe Shadow": 138
"Probe Warp Flash": 139
"Scout": 140
"Scout Shadow": 141
"Scout Engines": 142
"Scout Warp Flash": 143
"Reaver": 144
"Reaver Shadow": 145
"Reaver Warp Flash": 146
"Scarab": 147
"Observer": 148
"Observer Shadow": 149
"Observer Warp Flash": 150
"Zealot": 151
"Zealot Shadow": 152
"Zealot Death": 153
"Zealot Warp Flash": 154
"Templar Archives": 155
"Templar Archives Warp Flash": 156
"Templar Archives Shadow": 157
"Assimilator": 158
"Assimilator Warp Flash": 159
"Assimilator Shadow": 160
"Observatory": 161
"Observatory Warp Flash": 162
"Observatory Shadow": 163
"Citadel of Adun": 164
"Citadel of Adun Warp Flash": 165
"Citadel of Adun Shadow": 166
"Forge": 167
"Forge Overlay": 168
"Forge Warp Flash": 169
"Forge Shadow": 170
"Gateway": 171
"Gateway Warp Flash": 172
"Gateway Shadow": 173
"Cybernetics Core": 174
"Cybernetics Core Warp Flash": 175
"Cybernetics Core Overlay": 176
"Cybernetics Core Shadow": 177
"Khaydarin Crystal Formation": 178
"Nexus": 179
"Nexus Warp Flash": 180
"Nexus Overlay": 181
"Nexus Shadow": 182
"Photon Cannon": 183
"Photon Cannon Shadow": 184
"Photon Cannon Warp Flash": 185
"Arbiter Tribunal": 186
"Arbiter Tribunal Warp Flash": 187
"Arbiter Tribunal Shadow": 188
"Pylon": 189
"Pylon Warp Flash": 190
"Pylon Shadow": 191
"Robotics Facility": 192
"Robotics Facility Warp Flash": 193
"Robotics Facility Shadow": 194
"Shield Battery": 195
"Shield Battery Overlay": 196
"Shileld Battery Warp Flash": 197
"Shield Battery Shadow": 198
"Stargate": 199
"Stargate Overlay": 200
"Stargate Warp Flash": 201
"Stargate Shadow": 202
"Stasis Cell/Prison": 203
"Robotics Support Bay": 204
"Robotics Support Bay Warp Flash": 205
"Robotics Support Bay Shadow": 206
"Protoss Temple": 207
"Fleet Beacon": 208
"Fleet Beacon Warp Flash": 209
"Warp Texture": 210
"Warp Anchor": 211
"Fleet Beacon Shadow": 212
"Explosion1 (Small)": 213
"Explosion1 (Medium)": 214
"Explosion (Large)": 215
"Protoss Building Rubble (Small)": 216
"Protoss Building Rubble (Large)": 217
"Battlecruiser": 218
"Battlecruiser Shadow": 219
"Battlecruiser Engines": 220
"Civilian": 221
"Civilian Shadow": 222
"Dropship": 223
"Dropship Shadow": 224
"Dropship Engines": 225
"Firebat": 226
"Firebat Shadow": 227
"Ghost": 228
"Ghost Shadow": 229
"Ghost Remnants": 230
"Ghost Death": 231
"Nuke Beam": 232
"Nuke Target Dot": 233
"Goliath Base": 234
"Goliath Turret": 235
"Goliath Shadow": 236
"Sarah Kerrigan": 237
"Sarah Kerrigan Shadow": 238
"Marine": 239
"Marine Shadow": 240
"Marine Remnants": 241
"Marine Death": 242
"Wraith": 243
"Wraith Shadow": 244
"Wraith Engines": 245
"Scanner Sweep": 246
"SCV": 247
"SCV Shadow": 248
"SCV Glow": 249
"Siege Tank (Tank) Base": 250
"Siege Tank (Tank) Turret": 251
"Siege Tank (Tank) Base Shadow": 252
"Siege Tank (Siege) Base": 253
"Siege Tank (Siege) Turret": 254
"Siege Tank (Siege) Base Shadow": 255
"Vulture": 256
"Vulture Shadow": 257
"Spider Mine": 258
"Spider Mine Shadow": 259
"Science Vessel (Base)": 260
"Science Vessel (Turret)": 261
"Science Vessel Shadow": 262
"Terran Academy": 263
"Academy Overlay": 264
"Academy Shadow": 265
"Barracks": 266
"Barracks Shadow": 267
"Armory": 268
"Armory Overlay": 269
"Armory Shadow": 270
"Comsat Station": 271
"Comsat Station Connector": 272
"Comsat Station Overlay": 273
"Comsat Station Shadow": 274
"Command Center": 275
"Command Center Overlay": 276
"Command Center Shadow": 277
"Supply Depot": 278
"Supply Depot Overlay": 279
"Supply Depot Shadow": 280
"Control Tower": 281
"Control Tower Connector": 282
"Control Tower Overlay": 283
"Control Tower Shadow": 284
"Factory": 285
"Factory Overlay": 286
"Factory Shadow": 287
"Covert Ops": 288
"Covert Ops Connector": 289
"Covert Ops Overlay": 290
"Covert Ops Shadow": 291
"Ion Cannon": 292
"Machine Shop": 293
"Machine Shop Connector": 294
"Machine Shop Shadow": 295
"Missile Turret (Base)": 296
"Missile Turret (Turret)": 297
"Missile Turret (Base) Shadow": 298
"Crashed Batlecruiser": 299
"Crashed Battlecruiser Shadow": 300
"Physics Lab": 301
"Physics Lab Connector": 302
"Physics Lab Shadow": 303
"Bunker": 304
"Bunker Shadow": 305
"Bunker Overlay": 306
"Refinery": 307
"Refinery Shadow": 308
"Science Facility": 309
"Science Facility Overlay": 310
"Science Facility Shadow": 311
"Nuclear Silo": 312
"Nuclear Silo Connector": 313
"Nuclear Silo Overlay": 314
"Nuclear Silo Shadow": 315
"Nuclear Missile": 316
"Nuclear Missile Shadow": 317
"Nuke Hit": 318
"Starport": 319
"Starport Overlay": 320
"Starport Shadow": 321
"Engineering Bay": 322
"Engineering Bay Overlay": 323
"Engineering Bay Shadow": 324
"Terran Construction (Large)": 325
"Terran Construction (Large) Shadow": 326
"Terran Construction (Medium)": 327
"Terran Construction (Medium) Shadow": 328
"Addon Construction": 329
"Terran Construction (Small)": 330
"Terran Construction (Small) Shadow": 331
"Explosion2 (Small)": 332
"Explosion2 (Medium)": 333
"Building Explosion (Large)": 334
"Terran Building Rubble (Small)": 335
"Terran Building Rubble (Large)": 336
"Dark Swarm": 337
"Ragnasaur (Ash)": 338
"Ragnasaur (Ash) Shadow": 339
"Rhynadon (Badlands)": 340
"Rhynadon (Badlands) Shadow": 341
"Bengalaas (Jungle)": 342
"Bengalaas (Jungle) Shadow": 343
"Vespene Geyser": 344
"Vespene Geyser2": 345
"Vespene Geyser Shadow": 346
"Mineral Field Type1": 347
"Mineral Field Type1 Shadow": 348
"Mineral Field Type2": 349
"Mineral Field Type2 Shadow": 350
"Mineral Field Type3": 351
"Mineral Field Type3 Shadow": 352
"Independent Starport (Unused)": 353
"Zerg Beacon": 354
"Zerg Beacon Overlay": 355
"Terran Beacon": 356
"Terran Beacon Overlay": 357
"Protoss Beacon": 358
"Protoss Beacon Overlay": 359
"Unknown360": 360
"Lockdown Field (Small)": 361
"Lockdown Field (Medium)": 362
"Lockdown Field (Large)": 363
"Stasis Field Hit": 364
"Stasis Field (Small)": 365
"Stasis Field (Medium)": 366
"Stasis Field (Large)": 367
"Recharge Shields (Small)": 368
"Recharge Shields (Medium)": 369
"Recharge Shields (Large)": 370
"Defensive Matrix Front (Small)": 371
"Defensive Matrix Front (Medium)": 372
"Defensive Matrix Front (Large)": 373
"Defensive Matrix Back (Small)": 374
"Defensive Matrix Back (Medium)": 375
"Defensive Matrix Back (Large)": 376
"Defensive Matrix Hit (Small)": 377
"Defensive Matrix Hit (Medium)": 378
"Defensive Matrix Hit (Large)": 379
"Irradiate (Small)": 380
"Irradiate (Medium)": 381
"Irradiate (Large)": 382
"Ensnare Cloud": 383
"Ensnare Overlay (Small)": 384
"Ensnare Overlay (Medium)": 385
"Ensnare Overlay (Large)": 386
"Plague Cloud": 387
"Plague Overlay (Small)": 388
"Plague Overlay (Medium)": 389
"Plague Overlay (Large)": 390
"Recall Field": 391
"Flag": 392
"Young Chrysalis": 393
"Psi Emitter": 394
"Data Disc": 395
"Khaydarin Crystal": 396
"Mineral Chunk Type1": 397
"Mineral Chunk Type2": 398
"Protoss Gas Orb Type1": 399
"Protoss Gas Orb Type2": 400
"Zerg Gas Sac Type1": 401
"Zerg Gas Sac Type2": 402
"Terran Gas Tank Type1": 403
"Terran Gas Tank Type2": 404
"Mineral Chunk Shadow": 405
"Protoss Gas Orb Shadow": 406
"Zerg Gas Sac Shadow": 407
"Terran Gas Tank Shadow": 408
"Data Disk Shadow (Ground)": 409
"Data Disk Shadow (Carried)": 410
"Flag Shadow (Ground)": 411
"Flag Shadow (Carried)": 412
"Crystal Shadow (Ground)": 413
"Crystal Shadow (Carried)": 414
"Young Chrysalis Shadow (Ground)": 415
"Young Chrysalis Shadow (Carried)": 416
"Psi Emitter Shadow (Ground)": 417
"Psi Emitter Shadow (Carried)": 418
"Acid Spray (Unused)": 419
"Unknown420": 420
"FlameThrower": 421
"Longbolt/Gemini Missiles Trail": 422
"Burrowing Dust": 423
"Shield Overlay": 424
"Unknown425": 425
"Double Explosion": 426
"Phase Disruptor Hit": 427
"Nuclear Missile Death": 428
"Spider Mine Death": 429
"Vespene Geyser Smoke1": 430
"Vespene Geyser Smoke2": 431
"Vespene Geyser Smoke3": 432
"Vespene Geyser Smoke4": 433
"Vespene Geyser Smoke5": 434
"Unknown435": 435
"Unknown436": 436
"Unknown437": 437
"Unknown438": 438
"Unknown439": 439
"Fragmentation Grenade Hit": 440
"Grenade Shot Smoke": 441
"Anti-Matter Missile Hit": 442
"Scarab/Anti-Matter Missile Overlay": 443
"Scarab Hit": 444
"Cursor Marker": 445
"Battlecruiser Attack Overlay": 446
"Burst Lasers Hit": 447
"Unknown448": 448
"High Templar Glow": 449
"Flames1 Type1 (Small)": 450
"Flames1 Type2 (Small)": 451
"Flames1 Type3 (Small)": 452
"Flames2 Type3 (Small)": 453
"Flames3 Type3 (Small)": 454
"Flames4 Type3 (Small)": 455
"Flames5 Type3 (Small)": 456
"Flames6 Type3 (Small)": 457
"Bleeding Variant1 Type1 (Small)": 458
"Bleeding Variant1 Type2 (Small)": 459
"Bleeding Variant1 Type3 (Small)": 460
"Bleeding Variant1 Type4 (Small)": 461
"Bleeding Variant2 Type1 (Small)": 462
"Bleeding Variant2 Type2 (Small)": 463
"Bleeding Variant2 Type3 (Small)": 464
"Bleeding Variant2 Type4 (Small)": 465
"Flames2 Type1 (Small)": 466
"Flames2 Type2 (Small)": 467
"Flames7 Type3 (Small)": 468
"Flames3 Type1 (Small)": 469
"Flames3 Type2 (Small)": 470
"Flames8 Type3 (Small)": 471
"Flames1 Type1 (Large)": 472
"Flames1 Type2 (Large)": 473
"Flames1 Type3 (Large)": 474
"Flames2 Type3 (Large)": 475
"Flames3 Type3 (Large)": 476
"Flames4 Type3 (Large)": 477
"Flames5 Type3 (Large)": 478
"Flames6 Type3 (Large)": 479
"Bleeding Variant1 Type1 (Large)": 480
"Bleeding Variant1 Type2 (Large)": 481
"Bleeding Variant1 Type3 (Large)": 482
"Bleeding Variant1 Type4 (Large)": 483
"Bleeding Variant2 Type1 (Large)": 484
"Bleeding Variant2 Type3 (Large)": 485
"Bleeding Variant3 Type3 (Large)": 486
"Bleeding Variant2 Type4 (Large)": 487
"Flames2 Type1 (Large)": 488
"Flames2 Type2 (Large)": 489
"Flames7 Type3 (Large)": 490
"Flames3 Type1 (Large)": 491
"Flames3 Type2 (Large)": 492
"Flames8 Type3 (Large)": 493
"Building Landing Dust Type1": 494
"Building Landing Dust Type2": 495
"Building Landing Dust Type3": 496
"Building Landing Dust Type4": 497
"Building Landing Dust Type5": 498
"Building Lifting Dust Type1": 499
"Building Lifting Dust Type2": 500
"Building Lifting Dust Type3": 501
"Building Lifting Dust Type4": 502
"White Circle": 503
"Needle Spine Hit": 504
"Unknown505": 505
"Sunken Colony Tentacle": 506
"Venom (Unused Zerg Weapon)": 507
"Venom Hit (Unused)": 508
"Acid Spore": 509
"Acid Spore Hit": 510
"Glave Wurm": 511
"Glave Wurm/Seeker Spores Hit": 512
"Glave Wurm Trail": 513
"Seeker Spores Overlay": 514
"Seeker Spores": 515
"Queen Spell Holder": 516
"Consume": 517
"Guardian Attack Overlay": 518
"Dual Photon Blasters Hit": 519
"Particle Beam Hit": 520
"Anti-Matter Missile": 521
"Pulse Cannon": 522
"Phase Disruptor": 523
"STA/STS Photon Cannon Overlay": 524
"Psionic Storm": 525
"Fusion Cutter Hit": 526
"Gauss Rifle Hit": 527
"Gemini Missiles": 528
"Lockdown/LongBolt/Hellfire Missile": 529
"Gemini Missiles Explosion": 530
"C-10 Canister Rifle Hit": 531
"Fragmentation Grenade": 532
"Arclite Shock Cannon Hit": 533
"ATS/ATA Laser Battery": 534
"Burst Lasers": 535
"Siege Tank(Tank) Turret Attack Overlay": 536
"Siege Tank(Siege) Turret Attack Overlay": 537
"Science Vessel Overlay (Part1)": 538
"Science Vessel Overlay (Part2)": 539
"Science Vessel Overlay (Part3)": 540
"Yamato Gun": 541
"Yamato Gun Trail": 542
"Yamato Gun Overlay": 543
"Yamato Gun Hit": 544
"Hallucination Hit": 545
"Scanner Sweep Hit": 546
"Unknown547": 547
"Psionic Shockwave Hit": 548
"Archon Beam": 549
"Psionic Storm Part1": 550
"Psionic Storm Part2": 551
"Psionic Storm Part3": 552
"Psionic Storm Part4": 553
"EMP Shockwave Missile": 554
"EMP Shockwave Hit (Part1)": 555
"EMP Shockwave Hit (Part2)": 556
"Hallucination Death1": 557
"Hallucination Death2": 558
"Hallucination Death3": 559
"Circle Marker1": 560
"Selection Circle (22pixels)": 561
"Selection Circle (32pixels)": 562
"Selection Circle (48pixels)": 563
"Selection Circle (62pixels)": 564
"Selection Circle (72pixels)": 565
"Selection Circle (94pixels)": 566
"Selection Circle (110pixels)": 567
"Selection Circle (122pixels)": 568
"Selection Circle (146pixels)": 569
"Selection Circle (224pixels)": 570
"Selection Circle Dashed (22pixels)": 571
"Selection Circle Dashed (32pixels)": 572
"Selection Circle Dashed (48pixels)": 573
"Selection Circle Dashed (62pixels)": 574
"Selection Circle Dashed (72pixels)": 575
"Selection Circle Dashed (94pixels)": 576
"Selection Circle Dashed (110pixels)": 577
"Selection Circle Dashed (122pixels)": 578
"Selection Circle Dashed (146pixels)": 579
"Selection Circle Dashed (224pixels)": 580
"Circle Marker2": 581
"Map Revealer": 582
"Circle Marker3": 583
"Psi Field1 (Right Upper)": 584
"Psi Field1 (Right Lower)": 585
"Psi Field2 (Right Upper)": 586
"Psi Field2 (Right Lower)": 587
"Start Location": 588
"2/38 Ash": 589
"2/38 Ash Shadow": 590
"2/39 Ash": 591
"2/39 Ash Shadow": 592
"2/41 Ash": 593
"2/41 Ash Shadow": 594
"2/40 Ash": 595
"2/40 Ash Shadow": 596
"2/42 Ash": 597
"2/42 Ash Shadow": 598
"2/43 Ash": 599
"2/44 Ash": 600
"2/1 Ash": 601
"2/4 Ash": 602
"2/5 Ash": 603
"2/30 Ash": 604
"2/28 Ash": 605
"2/29 Ash": 606
"4/1 Ash": 607
"4/2 Ash": 608
"4/3 Ash": 609
"4/56 Jungle": 610
"4/56 Jungle Shadow": 611
"4/57 Jungle": 612
"4/57 Jungle Shadow": 613
"4/58 Jungle": 614
"4/58 Jungle Shadow": 615
"4/59 Jungle": 616
"4/59 Jungle Shadow": 617
"9/5 Jungle": 618
"9/5 Jungle Shadow": 619
"9/6 Jungle": 620
"9/6 Jungle Shadow": 621
"9/7 Jungle": 622
"9/7 Jungle Shadow": 623
"4/51 Jungle": 624
"4/51 Jungle Shadow": 625
"4/52 Jungle": 626
"4/52 Jungle Shadow": 627
"4/54 Jungle": 628
"4/54 Jungle Shadow": 629
"4/53 Jungle": 630
"4/53 Jungle Shadow": 631
"9/1 Jungle": 632
"9/1 Jungle Shadow": 633
"9/2 Jungle": 634
"9/2 Jungle Shadow": 635
"9/3 Jungle": 636
"9/3 Jungle Shadow": 637
"9/4 Jungle": 638
"9/4 Jungle Shadow": 639
"4/12 Jungle": 640
"4/13 Jungle": 641
"4/1 Jungle": 642
"4/3 Jungle": 643
"4/2 Jungle": 644
"4/5 Jungle": 645
"4/4 Jungle": 646
"4/9 Jungle": 647
"4/10 Jungle": 648
"5/5 Jungle": 649
"5/7 Jungle": 650
"5/6 Jungle": 651
"5/9 Jungle": 652
"5/8 Jungle": 653
"4/6 Jungle": 654
"4/7 Jungle": 655
"4/17 Jungle": 656
"13/4 Jungle": 657
"11/5 Jungle": 658
"11/6 Jungle": 659
"11/7 Jungle": 660
"11/8 Jungle": 661
"11/10 Jungle": 662
"11/11 Jungle": 663
"11/12 Jungle": 664
"7/4 Platform": 665
"7/4 Platform Shadow": 666
"7/5 Platform": 667
"7/5 Platform Shadow": 668
"7/6 Platform": 669
"7/6 Platform Shadow": 670
"7/1 Platform": 671
"7/1 Platform Shadow": 672
"7/2 Platform": 673
"7/2 Platform Shadow": 674
"7/3 Platform": 675
"7/3 Platform Shadow": 676
"7/9 Platform": 677
"7/10 Platform": 678
"7/8 Platform": 679
"7/7 Platform": 680
"7/26 Platform": 681
"7/24 Platform": 682
"7/28 Platform": 683
"7/27 Platform": 684
"7/25 Platform": 685
"7/29 Platform": 686
"7/30 Platform": 687
"7/31 Platform": 688
"12/1 Platform": 689
"9/27 Platform": 690
"5/54 Badlands": 691
"5/54 Badlands Shadow": 692
"5/55 Badlands": 693
"5/55 Badlands Shadow": 694
"5/56 Badlands": 695
"5/56 Badlands Shadow": 696
"5/57 Badlands": 697
"5/57 Badlands Shadow": 698
"6/16 Badlands": 699
"6/17 Badlands": 700
"6/20 Badlands": 701
"6/21 Badlands": 702
"5/10 Badlands": 703
"5/50 Badlands": 704
"5/50 Badlands Shadow": 705
"5/52 Badlands": 706
"5/52 Badlands Shadow": 707
"5/53 Badlands": 708
"5/53 Badlands Shadow": 709
"5/51 Badlands": 710
"5/51 Badlands Shadow": 711
"6/3 Badlands": 712
"11/3 Badlands": 713
"11/8 Badlands": 714
"11/6 Badlands": 715
"11/7 Badlands": 716
"11/9 Badlands": 717
"11/10 Badlands": 718
"11/11 Badlands": 719
"11/12 Badlands": 720
"11/13 Badlands": 721
"11/14 Badlands": 722
"1/13 Badlands": 723
"1/9 Badlands": 724
"1/11 Badlands": 725
"1/14 Badlands": 726
"1/10 Badlands": 727
"1/12 Badlands": 728
"1/15 Badlands": 729
"1/7 Badlands": 730
"1/5 Badlands": 731
"1/16 Badlands": 732
"1/8 Badlands": 733
"1/6 Badlands": 734
"Floor Gun Trap": 735
"Floor Missile Trap": 736
"Floor Missile Trap Turret": 737
"Wall Missile Trap": 738
"Wall Missile Trap2": 739
"Wall Flame Trap": 740
"Wall Flame Trap2": 741
"Left Upper Level Door": 742
"Right Upper Level Door": 743
"4/15 Installation1": 744
"4/15 Installation2": 745
"3/9 Installation": 746
"3/10 Installation": 747
"3/11 Installation": 748
"3/12 Installation": 749
"Substructure Left Door": 750
"Substructure Right Door": 751
"3/1 Installation": 752
"3/2 Installation": 753
"Substructure Opening Hole": 754
"7/21 Twilight": 755
"Unknown Twilight": 756
"7/13 Twilight": 757
"7/14 Twilight": 758
"7/16 Twilight": 759
"7/15 Twilight": 760
"7/19 Twilight": 761
"7/20 Twilight": 762
"7/17 Twilight": 763
"6/1 Twilight": 764
"6/2 Twilight": 765
"6/3 Twilight": 766
"6/4 Twilight": 767
"6/5 Twilight": 768
"8/3 Twilight1": 769
"8/3 Twilight2": 770
"9/29 Ice": 771
"9/29 Ice Shadow": 772
"9/28 Ice": 773
"9/28 Ice Shadow": 774
"12/38 Ice": 775
"12/38 Ice Shadow": 776
"12/37 Ice": 777
"12/37 Ice Shadow": 778
"12/33 Ice1": 779
"12/33 Ice1 Shadow": 780
"9/21 Ice": 781
"9/21 Ice Shadow": 782
"9/15 Ice": 783
"9/15 Ice Shadow": 784
"9/16 Ice": 785
"9/16 Ice Shadow": 786
"Unknown787": 787
"Unknown788": 788
"12/9 Ice1": 789
"12/10 Ice1": 790
"9/24 Ice": 791
"9/24 Ice Shadow": 792
"9/23 Ice": 793
"9/23 Ice Shadow": 794
"Unknown795": 795
"Unknown Ice Shadow": 796
"12/7 Ice": 797
"12/7 Ice Shadow": 798
"12/8 Ice": 799
"12/8 Ice Shadow": 800
"12/9 Ice2": 801
"12/9 Ice2 Shadow": 802
"12/10 Ice2": 803
"12/10 Ice2 Shadow": 804
"12/40 Ice": 805
"12/40 Ice Shadow": 806
"12/41 Ice": 807
"12/41 Ice Shadow": 808
"12/42 Ice": 809
"12/42 Ice Shadow": 810
"12/5 Ice": 811
"12/5 Ice Shadow": 812
"12/6 Ice": 813
"12/6 Ice Shadow": 814
"12/36 Ice": 815
"12/36 Ice Shadow": 816
"12/32 Ice": 817
"12/32 Ice Shadow": 818
"12/33 Ice2": 819
"12/33 Ice2 Shadow": 820
"12/34 Ice": 821
"12/34 Ice Shadow": 822
"12/24 Ice1": 823
"12/24 Ice1 Shadow": 824
"12/25 Ice1": 825
"12/25 Ice1 Shadow": 826
"12/30 Ice1": 827
"12/30 Ice1 Shadow": 828
"12/31 Ice": 829
"12/31 Ice Shadow": 830
"12/20 Ice": 831
"12/30 Ice2": 832
"12/30 Ice2 Shadow": 833
"9/22 Ice": 834
"9/22 Ice Shadow": 835
"12/24 Ice2": 836
"12/24 Ice2 Shadow": 837
"12/25 Ice2": 838
"12/25 Ice2 Shadow": 839
"Unknown840": 840
"4/1 Ice": 841
"6/1 Ice": 842
"5/6 Ice": 843
"5/6 Ice Shadow": 844
"5/7 Ice": 845
"5/7 Ice Shadow": 846
"5/8 Ice": 847
"5/8 Ice Shadow": 848
"5/9 Ice": 849
"5/9 Ice Shadow": 850
"10/10 Desert1": 851
"10/12 Desert1": 852
"10/12 Desert1 Shadow": 853
"10/8 Desert1": 854
"10/8 Desert1 Shadow": 855
"10/9 Desert1": 856
"10/9 Desert1 Shadow": 857
"6/10 Desert": 858
"6/10 Desert Shadow": 859
"6/13 Desert1": 860
"6/13 Desert1 Shadow": 861
"Unknown Desert": 862
"Unknown Desert Shadow": 863
"10/12 Desert2": 864
"10/12 Desert2 Shadow": 865
"10/9 Desert2": 866
"10/9 Desert2 Shadow": 867
"10/10 Desert2": 868
"10/10 Desert2 Shadow": 869
"10/11 Desert": 870
"10/11 Desert Shadow": 871
"10/14 Desert": 872
"10/14 Desert Shadow": 873
"10/41 Desert": 874
"10/41 Desert Shadow": 875
"10/39 Desert": 876
"1/39 Desert Shadow": 877
"10/8 Desert2": 878
"10/8 Desert2 Shadow": 879
"10/6 Desert": 880
"10/7 Desert": 881
"10/7 Desert Shadow": 882
"4/6 Desert": 883
"4/6 Desert Shadow": 884
"4/11 Desert": 885
"4/11 Desert Shadow": 886
"4/10 Desert": 887
"4/10 Desert Shadow": 888
"4/9 Desert": 889
"4/7 Desert": 890
"4/7 Desert Shadow": 891
"4/12 Desert": 892
"4/12 Desert Shadow": 893
"4/8 Desert": 894
"4/13 Desert": 895
"4/13 Desert Shadow": 896
"4/17 Desert": 897
"4/15 Desert1": 898
"4/15 Desert1 Shadow": 899
"10/23 Desert": 900
"10/23 Desert Shadow": 901
"10/5 Desert": 902
"10/5 Desert Shadow": 903
"6/13 Desert2": 904
"6/13 Desert2 Shadow": 905
"6/20 Desert": 906
"4/15 Desert2": 907
"4/15 Desert2 Shadow": 908
"8/23 Desert": 909
"8/23 Desert Shadow": 910
"12/1 Desert Overlay": 911
"11/3 Desert": 912
"Unknown913": 913
"Lurker Egg": 914
"Devourer": 915
"Devourer Shadow": 916
"Devourer Birth": 917
"Devourer Death": 918
"Lurker Birth": 919
"Lurker Remnants": 920
"Lurker": 921
"Lurker Shadow": 922
"Overmind Cocoon": 923
"Overmind Cocoon Shadow": 924
"Dark Archon Energy": 925
"Dark Archon Being": 926
"Dark Archon Swirl": 927
"Dark Archon Death": 928
"Corsair": 929
"Corsair Shadow": 930
"Corsair Engines": 931
"Corsair Attack Overlay (Unused)": 932
"Dark Templar (Unit)": 933
"Warp Gate": 934
"Warp Gate Shadow": 935
"Warp Gate Overlay": 936
"Xel'Naga Temple": 937
"Xel'Naga Temple Shadow": 938
"Valkyrie": 939
"Valkyrie Shadow": 940
"Valkyrie Engines": 941
"Valkyrie Engines2 (Unused)": 942
"Valkyrie Afterburners (Unused)": 943
"Medic": 944
"Medic Shadow": 945
"Medic Remnants": 946
"Psi Disrupter": 947
"Psi Disrupter Shadow": 948
"Power Generator": 949
"Power Generator Shadow": 950
"Disruption Web": 951
"Scantid (Desert)": 952
"Scantid (Desert) Shadow": 953
"Kakaru (Twilight)": 954
"Kakaru (Twilight) Shadow": 955
"Ursadon (Ice)": 956
"Ursadon (Ice) Shadow": 957
"Uraj": 958
"Khalis": 959
"Halo Rockets Trail": 960
"Subterranean Spines": 961
"Coroosive Acid Shot": 962
"Corrosive Acid Hit": 963
"Neutron Flare": 964
"Halo Rockets": 965
"Optical Flare Grenade": 966
"Restoration Hit (Small)": 967
"Restoration Hit (Medium)": 968
"Restoration Hit (Large)": 969
"Heal (Small)": 970
"Heal (medium)": 971
"Heal (Large)": 972
"Mind Control Hit (Small)": 973
"Mind Control Hit (Medium)": 974
"Mind Control Hit (Large)": 975
"Optical Flare Hit (Small)": 976
"Optical Flare Hit (Medium)": 977
"Optical Flare Hit (Large)": 978
"Feedback (Small)": 979
"Feedback (Medium)": 980
"Feedback Hit (Large)": 981
"Maelstorm Overlay (Small)": 982
"Maelstorm Overlay (Medium)": 983
"Maelstorm Overlay (Large)": 984
"Unknown985": 985
"Acid Spores (1) Overlay (Small)": 986
"Acid Spores (2-3) Overlay (Small)": 987
"Acid Spores (4-5) Overlay (Small)": 988
"Acid Spores (6-9) Overlay (Small)": 989
"Acid Spores (1) Overlay (Medium)": 990
"Acid Spores (2-3) Overlay (Medium)": 991
"Acid Spores (4-5) Overlay (Medium)": 992
"Acid Spores (6-9) Overlay (Medium)": 993
"Acid Spores (1) Overlay (Large)": 994
"Acid Spores (2-3) Overlay (Large)": 995
"Acid Spores (4-5) Overlay (Large)": 996
"Acid Spores (6-9) Overlay (Large)": 997
"Maelstorm Hit": 998
```

  



## Icon

```JavaScript
"Marine": 0
"Ghost": 1
"Vulture": 2
"Goliath": 3
"Blank (Goliath Turret)": 4
"Siege Tank (Tank Mode)": 5
"Blank (Tank Turret)": 6
"SCV": 7
"Wraith": 8
"Science Vessel": 9
"Gui Montag (Firebat)": 10
"Dropship": 11
"Battlecruiser": 12
"Vulture Spider Mine": 13
"Nuclear Missile": 14
"Civilian": 15
"Sarah Kerrigan (Ghost)": 16
"Alan Schezar (Goliath)": 17
"Blank (Alan Turret)": 18
"Jim Raynor (Vulture)": 19
"Jim Raynor (Marine)": 20
"Tom Kazansky (Wraith)": 21
"Magellan (Science Vessel)": 22
"Edmund Duke (Siege Tank)": 23
"Blank (Duke Turret)": 24
"Edmund Duke (Siege Mode)": 25
"Blank (Duke Turret)": 26
"Blank (Arcturus Mengsk)": 27
"Hyperion (Battlecruiser)": 28
"Norad II (Battlecruiser)": 29
"Terran Siege Tank (Siege Mode)": 30
"Blank (Siege Tank Turret)": 31
"Firebat": 32
"Marine (Scanner Sweep)": 33
"Medic": 34
"Larva": 35
"Radioactive (Zerg Egg)": 36
"Zergling": 37
"Hydralisk": 38
"Ultralisk": 39
"Broodling": 40
"Drone": 41
"Overlord": 42
"Mutalisk": 43
"Guardian": 44
"Queen": 45
"Defiler": 46
"Scourge": 47
"Torrarsque (Ultralisk)": 48
"Matriarch (Queen)": 49
"Infested Terran": 50
"Infested Kerrigan (Infested Terran)": 51
"Unclean One (Defiler)": 52
"Hunter Killer (Hydralisk)": 53
"Devouring One (Zergling)": 54
"Kukulza (Mutalisk)": 55
"Kukulza (Guardian)": 56
"Yggdrasill (Overlord)": 57
"Valkyrie": 58
"Mutalisk/Guardian Cocoon": 59
"Corsair": 60
"Dark Templar (Unit)": 61
"Devourer": 62
"Dark Archon": 63
"Probe": 64
"Zealot": 65
"Dragoon": 66
"High Templar": 67
"Archon": 68
"Shuttle": 69
"Scout": 70
"Arbiter": 71
"Carrier": 72
"Interceptor": 73
"Dark Templar (Hero)": 74
"Zeratul (Dark Templar)": 75
"Tassadar/Zeratul (Archon)": 76
"Fenix (Zealot)": 77
"Fenix (Dragoon)": 78
"Tassadar (Templar)": 79
"Mojo (Scout)": 80
"Warbringer (Reaver)": 81
"Gantrithor (Carrier)": 82
"Reaver": 83
"Observer": 84
"Scarab": 85
"Danimoth (Arbiter)": 86
"Blank (Aldaris)": 87
"Artanis (Scout)": 88
"Rhynadon (Badlands Critter)": 89
"Bengalaas (Jungle Critter)": 90
"Lurker (Cargo Ship - Unused)": 91
"Mercenary Gunship (Unused)": 92
"Scantid (Desert Critter)": 93
"Kakaru (Twilight Critter)": 94
"Ragnasaur (Ashworld Critter)": 95
"Ursadon (Ice Critter)": 96
"Blank (Zerg Lurker Egg)": 97
"Blank (Raszagal)": 98
"Samir Duran (Ghost)": 99
"Alexei Stukov (Ghost)": 100
"Map Revealer": 101
"Blank (Gerard DuGalle)": 102
"Lurker": 103
"Infested Duran (Infested Terran)": 104
"Blank (Disruption Field)": 105
"Command Center": 106
"Comsat Station": 107
"Nuclear Silo": 108
"Supply Depot": 109
"Refinery": 110
"Barracks": 111
"Academy": 112
"Factory": 113
"Starport": 114
"Control Tower": 115
"Science Facility": 116
"Covert Ops": 117
"Physics Lab": 118
"Blank (Starbase - Unused)": 119
"Machine Shop": 120
"Repair Bay (Unused)": 121
"Engineering Bay": 122
"Armory": 123
"Missile Tower": 124
"Bunker": 125
"Crashed Norad II": 126
"Ion Cannon": 127
"Uraj": 128
"Khalis": 129
"Infested Command Center": 130
"Hatchery": 131
"Lair": 132
"Hive": 133
"Nydus Canal": 134
"Hydralisk Den": 135
"Defiler Mound": 136
"Greater Spire": 137
"Queen's Nest": 138
"Evolution Chamber": 139
"Ultralisk Cavern": 140
"Spire": 141
"Spawning Pool": 142
"Creep Colony": 143
"Spore Colony": 144
"Radioactive (Zerg Bldg1 - Unused)": 145
"Sunken Colony": 146
"Overmind (Without Shell)": 147
"Overmind (With Shell)": 148
"Extractor": 149
"Mature Chrysalis": 150
"Cerebrate": 151
"Cerebrate Daggoth": 152
"Blank (Zerg Bldg2 - Unused)": 153
"Nexus": 154
"Robotics Facility": 155
"Pylon": 156
"Assimilator": 157
"Blank (Protoss Bldg1 - Unused)": 158
"Observatory": 159
"Gateway": 160
"Blank (Protoss Bldg2 - Unused)": 161
"Photon Cannon": 162
"Citadel of Adun": 163
"Cybernetics Core": 164
"Templar Archives": 165
"Forge": 166
"Stargate": 167
"Stasis Cell/Prison": 168
"Fleet Beacon": 169
"Arbiter Tribunal": 170
"Robotics Support Bay": 171
"Shield Battery": 172
"Khaydarin Crystal Formation": 173
"Protoss Temple": 174
"Xel'Naga Temple": 175
"Mineral Cluster (Type 1)": 176
"Mineral Cluster (Type 2)": 177
"Mineral Cluster (Type 3)": 178
"Blank (Cave - Unused)": 179
"Blank (Cave-in - Unused)": 180
"Blank (Cantina - Unused)": 181
"Blank (Mining Platform - Unused)": 182
"Blank (Independent CC - Unused)": 183
"Blank (Independent Starport - Unused)": 184
"Blank (Jump Gate - Unused)": 185
"Blank (Ruins - Unused)": 186
"Blank (Khayd. Crystal Form. - Unused)": 187
"Vespene Geyser": 188
"Warp Gate": 189
"Psi Disrupter": 190
"Blank (Zerg Marker)": 191
"Blank (Terran Marker)": 192
"Blank (Protoss Marker)": 193
"Zerg Beacon": 194
"Terran Beacon": 195
"Protoss Beacon": 196
"Zerg Flag Beacon": 197
"Terran Flag Beacon": 198
"Protoss Flag Beacon": 199
"Power Generator": 200
"Overmind Cocoon": 201
"Blank (Dark Swarm)": 202
"Blank (Floor Missile Trap)": 203
"Blank (Floor Hatch - Unused)": 204
"Blank (Left Upper Level Door)": 205
"Blank (Right Upper Level Door)": 206
"Blank (Left Pit Door)": 207
"Blank (Right Pit Door)": 208
"Blank (Floor Gun Trap)": 209
"Blank (Left Wall Missile Trap)": 210
"Blank (Left Wall Flame Trap)": 211
"Infested Mine (Unused)": 212
"Blank (Right Wall Flame Trap)": 213
"Start Location": 214
"Flag": 215
"Young Chrysalis": 216
"Psi Emitter": 217
"Data Disc": 218
"Khaydarin Crystal": 219
"Blank (Mineral Chunk Type 1)": 220
"Blank (Mineral Chunk Type 2)": 221
"Blank (Protoss Vespene Orb Type 1)": 222
"Blank (Protoss Vespene Orb Type 2)": 223
"Blank (Zerg Vespene Sac Type 1)": 224
"Blank (Zerg Vespene Sac Type 2)": 225
"Blank (Terran Vespene Tank Type 1)": 226
"Blank (Terran Vespene Tank Type 2)": 227
"Move": 228
"Stop": 229
"Attack": 230
"Gather": 231
"Repair": 232
"Return Resources": 233
"Terran Basic Buildings": 234
"Terran Advanced Buildings": 235
"Cancel": 236
"Use Stimpack": 237
"U-238 Shells": 238
"Burst Lasers (Unused)": 239
"Lockdown": 240
"EMP Shockwave": 241
"Irradiate": 242
"Use Spider Mines": 243
"Afterburners (Unused Terran Upgrade)": 244
"Siege Mode": 245
"Tank Mode": 246
"Defensive Matrix": 247
"Titan Reactor": 248
"Ocular Implants": 249
"Scanner Sweep": 250
"Yamato Gun": 251
"Cloak": 252
"Decloak": 253
"Patrol": 254
"Hold Position": 255
"Moebius Reactor": 256
"Zerg Basic Buildings": 257
"Zerg Advanced Buildings": 258
"Burrow": 259
"Unburrow": 260
"Ventral Sacs": 261
"Antennae": 262
"Metabolic Boost": 263
"Adrenal Glands": 264
"Plague": 265
"Muscular Augments": 266
"Ensnare": 267
"Grooved Spines": 268
"Roar (Unused Zerg Upgrade)": 269
"Dark Swarm": 270
"Parasite": 271
"Protoss Basic Buildings": 272
"Protoss Advanced Buildings": 273
"Mind Control (SC Beta - Unused)": 274
"Psionic Storm": 275
"Gravitic Boosters": 276
"Hallucination": 277
"Stasis Field": 278
"Blank": 279
"Recall": 280
"Singularity Charge": 281
"Lift off": 282
"Land": 283
"Apollo Reactor": 284
"Colossus Reactor": 285
"Set Rally Point": 286
"Ion Thrusters": 287
"Infantry Weapons": 288
"Vehicle Weapons": 289
"Ship Weapons": 290
"Ship Plating": 291
"Infantry Armor": 292
"Vehicle Armor": 293
"Gamete Meiosis": 294
"Metasynaptic Node": 295
"Pneumatized Caparace": 296
"Zerg Caparace": 297
"Flyer Caparace": 298
"Melee Attacks": 299
"Missile Attacks": 300
"Flyer Attacks": 301
"Consume": 302
"Ground Armor": 303
"Air Plating": 304
"Ground Weapons": 305
"Air Weapons": 306
"Leg Enhancements": 307
"Recharge Shields": 308
"Load (into Transport)": 309
"Plasma Shields": 310
"Nuclear Strike": 311
"Unload All (from Transport/Bunker)": 312
"Infest Command Center": 313
"Scarab Damage": 314
"Reaver Capacity": 315
"Gravitic Drive": 316
"Sensor Array": 317
"Khaydarin Amulet": 318
"Apial Sensors": 319
"Gravitic Thrusters": 320
"Carrier Capacity": 321
"Khaydarin Core": 322
"Gauss Rifle": 323
"C-10 Canister Rifle": 324
"Fragmentation Grenade": 325
"Twin Autocannons": 326
"Hellfire Missile Pack": 327
"Arclite Cannon": 328
"Fusion Cutter": 329
"Fusion Cutter (Harvest)": 330
"Gemini Missiles": 331
"Burst Lasers": 332
"ATS Laser Battery": 333
"ATA Laser Battery": 334
"Flame Thrower": 335
"Arclite Shock Cannon": 336
"Longbolt Missile": 337
"Claws": 338
"Needle Spines": 339
"Kaiser Blades": 340
"Toxic Spores": 341
"Spines": 342
"Flyer Attack": 343
"Acid Spore": 344
"Glave Wurm": 345
"Venom (Unused Zerg Weapon)": 346
"Seeker Spores": 347
"Subterranean Tentacle": 348
"Suicide (Infested Terran)": 349
"Suicide (Scourge)": 350
"Particle Beam": 351
"Particle Beam (Harvest)": 352
"Psi/Warp Blades": 353
"Phase Disruptor": 354
"Psi Assault": 355
"Psionic Shockwave": 356
"Radioactive (Unused)": 357
"Dual Photon Blasters": 358
"Anti-matter Missiles": 359
"Phase Disruptor Cannon": 360
"Pulse Cannon": 361
"Photon Cannon": 362
"Radioactive (Unused)": 363
"Spider Mine": 364
"Heal": 365
"Restoration": 366
"Restoration": 367
"Disruption Web": 368
"Disruption Web": 369
"Unknown371": 370
"Mind Control": 371
"Feedback": 372
"Optical Flare": 373
"Afterburners ON (Unused)": 374
"Afterburners OFF (Unused)": 375
"Lurker Aspect": 376
"Unknown378": 377
"Anabolic Synthesis": 378
"Chitinous Plating": 379
"Charon Boosters": 380
"Maelstrom": 381
"Subterranean Spines": 382
"Argus Jewel": 383
"Caduceus Reactor": 384
"Argus Talisman": 385
"Play (Replay)": 386
"Pause (Replay)": 387
"Speed Up (Replay)": 388
"Slow Down (Replay": 389
```

  



## Iscript

```JavaScript
"Scourge": 0
"Unknown1": 1
"Scourge Death": 2
"Scourge Explosion": 3
"Broodling": 4
"Broodling Remnants": 5
"Infested Terran": 6
"Infested Terran Explosion": 7
"Guardian Cocoon": 8
"Defiler": 9
"Defiler Remnants": 10
"Drone": 11
"Drone Remnants": 12
"Egg": 13
"Egg Remnants": 14
"Guardian": 15
"Guardian Birth": 16
"Guardian Death": 17
"Hydralisk": 18
"Hydralisk Remnants": 19
"Infested Kerrigan": 20
"Larva": 21
"Larva Remnants": 22
"Mutalisk": 23
"Mutalisk Death": 24
"Overlord": 25
"Overlord Death": 26
"Queen": 27
"Queen Death": 28
"Ultralisk": 29
"Ultralisk Remnants": 30
"Zergling": 31
"Zergling Remnants": 32
"Zerg Air Death Explosion": 33
"Zerg Building Explosion": 34
"Unknown35": 35
"Zerg Birth": 36
"Egg Spawn": 37
"Cerebrate": 38
"Infested Command Center": 39
"Spawning Pool": 40
"Evolution Chamber": 41
"Creep Colony": 42
"Hatchery": 43
"Hive": 44
"Lair": 45
"Sunken Colony": 46
"Mature Chrysalis": 47
"Greater Spire": 48
"Defiler Mound": 49
"Queen Nest": 50
"Nydus Canal": 51
"Overmind(with Shell)": 52
"Overmind Remnants": 53
"Overmind(without Shell)": 54
"Ultralisk Cavern": 55
"Extractor": 56
"Hydralisk Den": 57
"Spire": 58
"Spore Colony": 59
"Infested Command Center Overlay": 60
"Zerg Construction(Small)": 61
"Zerg Construction(Medium)": 62
"Zerg Building Morph": 63
"Zerg Construction(Large)": 64
"Zerg Building Spawn": 65
"Battlecruiser": 66
"Civilian": 67
"Dropship": 68
"Firebat": 69
"Ghost": 70
"Ghost Remnants": 71
"Ghost Death": 72
"Nuke Beam": 73
"Nuke Target Dot": 74
"Goliath(Base)": 75
"Goliath(Turret)": 76
"Sarah Kerrigan": 77
"Marine": 78
"Marine Remnants": 79
"Marine Death": 80
"Scanner Sweep": 81
"Wraith": 82
"Wraith Afterburners": 83
"SCV": 84
"Unknown85": 85
"Vulture": 86
"Spider Mine": 87
"Science Vessel(Base)": 88
"Science Vessel(Turret)": 89
"Siege Tank(Tank) Base": 90
"Siege Tank(Tank) Turret": 91
"Siege Tank(Siege) Base": 92
"Siege Tank(Siege) Turret": 93
"Academy": 94
"Academy Overlay": 95
"Barracks": 96
"Armory": 97
"Armory Overlay": 98
"Comsat Station": 99
"Comsat Connector": 100
"Comsat Overlay": 101
"Command Center": 102
"Command Center Overlay": 103
"Crashed Battlecruiser": 104
"Supply Depot": 105
"Supply Depot Overlay": 106
"Control Tower": 107
"Control Tower Connector": 108
"Control Tower Overlay": 109
"Unknown110": 110
"Factory": 111
"Factory Overlay": 112
"Covert Ops": 113
"Covert Ops Connector": 114
"Covert Ops Overlay": 115
"Ion Cannon": 116
"Machine Shop": 117
"Machine Shop Connector": 118
"Missile Turret(Base)": 119
"Missile Turret(Turret)": 120
"Physics Lab": 121
"Physics Lab Connector": 122
"Bunker": 123
"Bunker Overlay": 124
"Refinery": 125
"Science Facility": 126
"Science Facility Overlay": 127
"Nuclear Silo": 128
"Nuclear Silo Connector": 129
"Nuclear Silo Overlay": 130
"Nuclear Missile": 131
"Unknown132": 132
"Nuke Explosion": 133
"Starport": 134
"Starport Overlay": 135
"Engineering Bay": 136
"Engineering Bay Overlay": 137
"Terran Construction(Large)": 138
"Terran Construction(Medium)": 139
"Terran Construction(Small)": 140
"Addon Construction": 141
"Explosion(Small)": 142
"Explosion(Medium)": 143
"Explosion(Large)": 144
"Building Rubble Header": 145
"Arbiter": 146
"Archon Energy": 147
"Archon Being": 148
"Archon Swirl": 149
"Unknown150": 150
"Carrier": 151
"Dark Templar(Hero)": 152
"Dragoon": 153
"Dragoon Remnants": 154
"Interceptor": 155
"Probe": 156
"Shuttle": 157
"High Templar": 158
"Reaver": 159
"Scarab": 160
"Scout": 161
"Scout Engines": 162
"Zealot": 163
"Zealot Death": 164
"Observer": 165
"Templar Archives": 166
"Assimilator": 167
"Observatory": 168
"Unknown169": 169
"Citadel Of Adun": 170
"Forge": 171
"Forge Overlay": 172
"Gateway": 173
"Cybernetics Core": 174
"Cybrnetics Core Overlay": 175
"Khaydarin Crystal Formation": 176
"Nexus": 177
"Nexus Overlay": 178
"Photon Cannon": 179
"Arbiter Tribunal": 180
"Pylon": 181
"Robotics Facility": 182
"Shield Battery": 183
"Shield Battery Overlay": 184
"Stargate": 185
"Stargate Overlay": 186
"Stasis Cell/Prison": 187
"Robotics Support Bay": 188
"Temple": 189
"Fleet Beacon": 190
"Warp Anchor": 191
"Warp Flash Header": 192
"Warp Texture": 193
"Unknown194": 194
"Unknown195": 195
"Unknown196": 196
"Unknown197": 197
"Ragnasaur(Ashworld Critter)": 198
"Rhynadon(Badlands Critter)": 199
"Bengalaas(Jungle Critter)": 200
"Vespene Geyser": 201
"Vespene Geyser2": 202
"Vespene Geyser Shadow": 203
"Mineral Field Type1": 204
"Mineral Field Type2": 205
"Mineral Field Type3": 206
"Unknown207": 207
"Zerg Beacon Overlay": 208
"Terran Beacon Overlay": 209
"Protoss Beacon Overlay": 210
"Zerg Beacon": 211
"Protoss Beacon": 212
"Terran Beacon": 213
"Unknown214": 214
"Powerups Shadow Header": 215
"Flag": 216
"Psi Emitter": 217
"Data Disk": 218
"Crystals Shadows": 219
"Young Chrysalis": 220
"Ore Chunk": 221
"Ore Chunk2": 222
"Gas Sac": 223
"Gas Sac2": 224
"Gas Orb": 225
"Gas Orb2": 226
"Gas Tank": 227
"Gas Tank2": 228
"Archon Overlay": 229
"Particle Beam Hit": 230
"Dual Photon Blaster Hit": 231
"Anti-Matter Missile": 232
"Pulse Cannon": 233
"Phase Disruptor": 234
"STA/STS Photon Cannon Overlay": 235
"Psionic Storm": 236
"Fusion Cutter Hit": 237
"Gauss Rifle Hit": 238
"Gemini Missiles": 239
"Longbolt Missile": 240
"C-10 Canister Rifle Hit": 241
"Fragmentation Grenade": 242
"ATA/ATS Laser Battery/Burst Lasers": 243
"Unknown244": 244
"Lockdown Hit": 245
"Arclite Shock Cannon Hit": 246
"Yamato Gun": 247
"Yamato Gun Trail": 248
"Lockdown/EMP Shockwave Missile": 249
"Siege Tank(Tank) Turret Overlay": 250
"Siege Tank(Siege) Turret Overlay": 251
"Science Vessel Overlay": 252
"Hallucination Hit": 253
"Unknown254": 254
"Unknown255": 255
"Needle Spines Hit": 256
"Venom (Unused)": 257
"Subterranean Tentacle": 258
"Venom Hit (Unused)": 259
"Acid Spore": 260
"Acid Spore Hit": 261
"Guardian Attack Overlay": 262
"Unknown263": 263
"Glave Wurm": 264
"Glave Wurm Hit": 265
"Seeker Spores": 266
"Queen Spell Holder": 267
"Psionic Shockwave Hit": 268
"Glave Wurm Trail": 269
"Seeker Spores Overlay": 270
"Acid Spray": 271
"Unknown272": 272
"Longbolt\Halo\Gemini Missiles Trail": 273
"Burowing Dust": 274
"Shadow Header": 275
"Shield Overlay": 276
"Unknown277": 277
"Double Explosion": 278
"Nuclear Missile Death": 279
"Spider Mine Explosion": 280
"Vespene Geyser Smokes": 281
"Unknown282": 282
"Fragmentation Grenade Hit": 283
"Grenade Shot Smoke": 284
"Phase Disruptor/Anti-Matter Missile Hit": 285
"Scarab/Anti-Matter Missile Overlay": 286
"Scarab Hit": 287
"Cursor Marker": 288
"Circle Marker": 289
"Carrier Engines": 290
"Engines/Glow Header": 291
"White Circle": 292
"Battlecruiser Attack Overlay": 293
"ATA/ATS Laser Battery/Burst Lasers Hit": 294
"Unknown295": 295
"Plague Cloud": 296
"Plague Overlay": 297
"Consume": 298
"Dark Swarm": 299
"Defensive Matrix Overlay": 300
"Defensive Matrix Hit": 301
"Ensnare": 302
"Ensnare Overlay": 303
"Irradiate": 304
"Recall Field": 305
"Stasis Field Overlay": 306
"Stasis Field Hit": 307
"Recharge Shields(Large)": 308
"Recharge Shields(Small)": 309
"High Templar Glow": 310
"Needle Spines Overlay": 311
"Flamethrower": 312
"Gemini Missiles Explosion": 313
"Yamato Gun Overlay": 314
"Yamato Gun Hit": 315
"Unknown316": 316
"Psionic Storm Part Variant1": 317
"Psionic Storm Part Variant2": 318
"EMP Shockwave Hit(Part1)": 319
"EMP Shockwave Hit(Part2)": 320
"Hallucination Death": 321
"Flames(Small)": 322
"Unknown323": 323
"Bleeding(Small) Variant1": 324
"Bleeding(Small) Variant2": 325
"Flames(Large)": 326
"Unknown327": 327
"Bleeding(Large) Variant1": 328
"Bleeding(Large) Variant2": 329
"Dust Variant1": 330
"Dust Variant2": 331
"Confirm Circle": 332
"Psi Field Type1": 333
"Psi Field Type2": 334
"Start Location": 335
"Doodad Header": 336
"Doodad Header(secondary)": 337
"Space Platform Doodad": 338
"Space Platform Doodad2": 339
"Installation Doodad": 340
"Installation Doodad2": 341
"Installation Right Wall Fans": 342
"Installation Left Wall Fans": 343
"Installation Gear": 344
"Floor Missile Trap": 345
"Floor Missile Trap Turret": 346
"Floor Gun Trap": 347
"Wall Missile Trap Type1": 348
"Wall Missile Trap Typet2": 349
"Wall Flame Trap Type1": 350
"Wall Flame Trap Type2": 351
"Map Revealer": 352
"Lurker Egg": 353
"Lurker": 354
"Unknown355": 355
"Lurker Remnants": 356
"Devourer": 357
"Devourer Birth": 358
"Devourer Death": 359
"Medic": 360
"Medic Remnants": 361
"Valkyrie": 362
"Unknown363": 363
"Unknown364": 364
"Dark Archon Energy": 365
"Dark Archon Being": 366
"Dark Archon Swirl": 367
"Dark Archon Death": 368
"Corsair": 369
"Corsair Engines": 370
"Unknown371": 371
"Dark Templar(Unit)": 372
"Neutron Flare": 373
"Disruption Web": 374
"Scantid(Desert Critter)": 375
"Kakaru(Twilight Critter)": 376
"Ursadon(Ice Critter)": 377
"Halo Rocket": 378
"Optical Flare": 379
"Subterranean Spines": 380
"Corrosive Acid": 381
"Corrosive Acid Hit": 382
"Acid Spores (1) Overlay": 383
"Acid Spores (2-3) Overlay": 384
"Acid Spores (4-5) Overlay": 385
"Acid Spores (6-9) Overlay": 386
"Ice Doodad": 387
"Doodad Shadows Header (BW)": 388
"Restoration Hit": 389
"Mind Control Hit": 390
"Optical Flare Hit": 391
"Feedback": 392
"Maelstorm Overlay": 393
"Unknown394": 394
"Unknown395": 395
"Desert Doodad": 396
"Desert Doodad2": 397
"Desert Doodad3": 398
"Desert Doodad Overlay": 399
"Desert Doodad": 400
"Twilight Doodad": 401
"Twilight Doodad": 402
"Twilight Doodad": 403
"Twilight Doodad": 404
"Overmind Cocoon": 405
"Warp Gate": 406
"Psi Disrupter": 407
"Power Generator": 408
"Warp Gate Overlay": 409
"Xel'Naga Temple": 410
"Maelstrom Hit": 411
```

  



## Portrait

```JavaScript
"Marine": 0
"Ghost": 1
"Firebat ": 2
"Vulture ": 3
"Spider Mine": 4
"Goliath": 5
"Siege Tank": 6
"SCV": 7
"Wraith": 8
"Science Vessel": 9
"Dropship": 10
"Battlecruiser": 11
"Sarah Kerrigan": 12
"Jim Raynor ": 13
"Edmund Duke": 14
"Civilian": 15
"Arcturus Mengsk": 16
"Terran Advisor": 17
"Larva": 18
"Egg": 19
"Zergling": 20
"Hydralisk": 21
"Ultralisk": 22
"Broodling": 23
"Drone": 24
"Overlord": 25
"Mutalisk": 26
"Guardian": 27
"Queen": 28
"Defiler": 29
"Scourge": 30
"Cocoon": 31
"Mature Chrysalis": 32
"Infested Terran": 33
"Zasz": 34
"Daggoth": 35
"Infested Kerrigan": 36
"Hunter Killer": 37
"Overmind": 38
"Probe": 39
"Zealot": 40
"Dragoon": 41
"High Templar": 42
"Archon": 43
"Shuttle": 44
"Scout": 45
"Arbiter": 46
"Carrier": 47
"Interceptor": 48
"Dark Templar": 49
"Fenix (Zealot)": 50
"Fenix (Dragoon)": 51
"Zeratul": 52
"Tassadar": 53
"Gantrithor": 54
"Observer": 55
"Reaver": 56
"Scarab": 57
"Khaydarin Crystal Formation": 58
"Aldaris": 59
"Protoss Advisor": 60
"Merc Biker": 61
"Rhynadon": 62
"Bengalaas": 63
"Ragnasaur": 64
"Cargo Ship": 65
"Merc Gunship": 66
"Raider": 67
"Grom Biker": 68
"Space Critter": 69
"Sally": 70
"Greedo": 71
"Boskk": 72
"Peter": 73
"Independent Advisor": 74
"Terran Gas Tank": 75
"Protoss Gas Orb": 76
"Zerg Gas Sac": 77
"Mineral Cluster": 78
"Data Disc": 79
"Psi Emitter": 80
"Khaydarin Crystal": 81
"Flag P1": 82
"Flag P2": 83
"Flag P3": 84
"Flag P4": 85
"Flag P5": 86
"Flag P6": 87
"Flag P7": 88
"Flag P8": 89
"Medic": 90
"Valkyrie": 91
"Dugalle": 92
"Stukov": 93
"Duran": 94
"Artanis": 95
"Raszagal": 96
"Devourer": 97
"Lurker": 98
"Dark Archon": 99
"Corsair": 100
"Scantid": 101
"Kakaru": 102
"Ursadon": 103
"Uraj Crystal": 104
"Khalis Crystal": 105
"Flag P9": 106
"Flag P10": 107
"Flag P11": 108
"Flag P12": 109
"Marine - Talking": 110
"Ghost - Talking": 111
"Firebat - Talking": 112
"Vulture - Talking": 113
"Spider Mine - Talking": 114
"Goliath - Talking": 115
"Siege Tank - Talking": 116
"SCV - Talking": 117
"Wraith - Talking": 118
"Science Vessel - Talking": 119
"Dropship - Talking": 120
"Battlecruiser - Talking": 121
"Sarah Kerrigan - Talking": 122
"Jim Raynor  - Talking": 123
"Edmund Duke - Talking": 124
"Civilian - Talking": 125
"Arcturus Mengsk - Talking": 126
"Terran Advisor - Talking": 127
"Larva - Talking": 128
"Egg - Talking": 129
"Zergling - Talking": 130
"Hydralisk - Talking": 131
"Ultralisk - Talking": 132
"Broodling - Talking": 133
"Drone - Talking": 134
"Overlord - Talking": 135
"Mutalisk - Talking": 136
"Guardian - Talking": 137
"Queen - Talking": 138
"Defiler - Talking": 139
"Scourge - Talking": 140
"Cocoon - Talking": 141
"Mature Chrysalis - Talking": 142
"Infested Terran - Talking": 143
"Zasz - Talking": 144
"Daggoth - Talking": 145
"Infested Kerrigan - Talking": 146
"Hunter Killer - Talking": 147
"Overmind - Talking": 148
"Probe - Talking": 149
"Zealot - Talking": 150
"Dragoon - Talking": 151
"High Templar - Talking": 152
"Archon - Talking": 153
"Shuttle - Talking": 154
"Scout - Talking": 155
"Arbiter - Talking": 156
"Carrier - Talking": 157
"Interceptor - Talking": 158
"Dark Templar - Talking": 159
"Fenix (Zealot) - Talking": 160
"Fenix (Dragoon) - Talking": 161
"Zeratul - Talking": 162
"Tassadar - Talking": 163
"Gantrithor - Talking": 164
"Observer - Talking": 165
"Reaver - Talking": 166
"Scarab - Talking": 167
"Khaydarin Crystal Formation - Talking": 168
"Aldaris - Talking": 169
"Protoss Advisor - Talking": 170
"Merc Biker - Talking": 171
"Rhynadon - Talking": 172
"Bengalaas - Talking": 173
"Ragnasaur - Talking": 174
"Cargo Ship - Talking": 175
"Merc Gunship - Talking": 176
"Raider - Talking": 177
"Grom Biker - Talking": 178
"Space Critter - Talking": 179
"Sally - Talking": 180
"Greedo - Talking": 181
"Boskk - Talking": 182
"Peter - Talking": 183
"Independent Advisor - Talking": 184
"Terran Gas Tank - Talking": 185
"Protoss Gas Orb - Talking": 186
"Zerg Gas Sac - Talking": 187
"Mineral Cluster - Talking": 188
"Data Disc - Talking": 189
"Psi Emitter - Talking": 190
"Khaydarin Crystal - Talking": 191
"Flag P1 - Talking": 192
"Flag P2 - Talking": 193
"Flag P3 - Talking": 194
"Flag P4 - Talking": 195
"Flag P5 - Talking": 196
"Flag P6 - Talking": 197
"Flag P7 - Talking": 198
"Flag P8 - Talking": 199
"Medic - Talking": 200
"Valkyrie - Talking": 201
"Dugalle - Talking": 202
"Stukov - Talking": 203
"Duran - Talking": 204
"Artanis - Talking": 205
"Raszagal - Talking": 206
"Devourer - Talking": 207
"Lurker - Talking": 208
"Dark Archon - Talking": 209
"Corsair - Talking": 210
"Scantid - Talking": 211
"Kakaru - Talking": 212
"Ursadon - Talking": 213
"Uraj Crystal - Talking": 214
"Khalis Crystal - Talking": 215
"Flag P9 - Talking": 216
"Flag P10 - Talking": 217
"Flag P11 - Talking": 218
"Flag P12 - Talking": 219
"None": 65535
```

  



## Sprites

```Python
"2/38 Ash": 0
"2/39 Ash": 1
"2/41 Ash": 2
"2/40 Ash": 3
"2/42 Ash": 4
"2/43 Ash": 5
"2/44 Ash": 6
"2/1 Ash": 7
"2/4 Ash": 8
"2/5 Ash": 9
"2/30 Ash": 10
"2/28 Ash": 11
"2/29 Ash": 12
"4/1 Ash": 13
"4/2 Ash": 14
"4/3 Ash": 15
"4/56 Jungle": 16
"4/57 Jungle": 17
"4/58 Jungle": 18
"4/59 Jungle": 19
"9/5 Jungle": 20
"9/6 Jungle": 21
"9/7 Jungle": 22
"4/51 Jungle": 23
"4/52 Jungle": 24
"4/54 Jungle": 25
"4/53 Jungle": 26
"9/1 Jungle": 27
"9/2 Jungle": 28
"9/3 Jungle": 29
"9/4 Jungle": 30
"4/12 Jungle": 31
"4/13 Jungle": 32
"4/1 Jungle": 33
"4/3 Jungle": 34
"4/2 Jungle": 35
"4/5 Jungle": 36
"4/4 Jungle": 37
"4/9 Jungle": 38
"4/10 Jungle": 39
"5/5 Jungle": 40
"5/7 Jungle": 41
"5/6 Jungle": 42
"5/9 Jungle": 43
"5/8 Jungle": 44
"4/6 Jungle": 45
"4/7 Jungle": 46
"4/17 Jungle": 47
"13/4 Jungle": 48
"11/5 Jungle": 49
"11/6 Jungle": 50
"11/7 Jungle": 51
"11/8 Jungle": 52
"11/10 Jungle": 53
"11/11 Jungle": 54
"11/12 Jungle": 55
"7/4 Platform": 56
"7/5 Platform": 57
"7/6 Platform": 58
"7/1 Platform": 59
"7/2 Platform": 60
"7/3 Platform": 61
"7/9 Platform": 62
"7/10 Platform": 63
"7/8 Platform": 64
"7/7 Platform": 65
"7/26 Platform": 66
"7/24 Platform": 67
"7/28 Platform": 68
"7/27 Platform": 69
"7/25 Platform": 70
"7/29 Platform": 71
"7/30 Platform": 72
"7/31 Platform": 73
"12/1 Platform": 74
"9/27 Platform": 75
"5/54 Badlands": 76
"5/55 Badlands": 77
"5/56 Badlands": 78
"5/57 Badlands": 79
"6/16 Badlands": 80
"6/17 Badlands": 81
"6/20 Badlands": 82
"6/21 Badlands": 83
"5/10 Badlands": 84
"5/50 Badlands": 85
"5/52 Badlands": 86
"5/53 Badlands": 87
"5/51 Badlands": 88
"6/3 Badlands": 89
"11/3 Badlands": 90
"11/8 Badlands": 91
"11/6 Badlands": 92
"11/7 Badlands": 93
"11/9 Badlands": 94
"11/10 Badlands": 95
"11/11 Badlands": 96
"11/12 Badlands": 97
"11/13 Badlands": 98
"11/14 Badlands": 99
"1/13 Badlands": 100
"1/9 Badlands": 101
"1/11 Badlands": 102
"1/14 Badlands": 103
"1/10 Badlands": 104
"1/12 Badlands": 105
"1/15 Badlands": 106
"1/7 Badlands": 107
"1/5 Badlands": 108
"1/16 Badlands": 109
"1/8 Badlands": 110
"1/6 Badlands1": 111
"1/6 Badlands2": 112
"1/6 Badlands3": 113
"1/6 Badlands4": 114
"1/6 Badlands5": 115
"1/6 Badlands6": 116
"1/6 Badlands7": 117
"1/6 Badlands8": 118
"4/15 Installation1": 119
"4/15 Installation2": 120
"3/9 Installation": 121
"3/10 Installation": 122
"3/11 Installation": 123
"3/12 Installation": 124
"1/6 Badlands9": 125
"1/6 Badlands10": 126
"3/1 Installation": 127
"3/2 Installation": 128
"1/6 Badlands11": 129
"Scourge": 130
"Scourge Death": 131
"Scourge Explosion": 132
"Broodling": 133
"Broodling Remnants": 134
"Infested Terran": 135
"Infested Terran Explosion": 136
"Guardian Cocoon": 137
"Defiler": 138
"Defiler Remnants": 139
"Drone": 140
"Drone Remnants": 141
"Egg": 142
"Egg Remnants": 143
"Guardian": 144
"Guardian Death": 145
"Hydralisk": 146
"Hydralisk Remnants": 147
"Infested Kerrigan": 148
"Larva": 149
"Larva Remnants": 150
"Mutalisk": 151
"Mutalisk Death": 152
"Overlord": 153
"Overlord Death": 154
"Queen": 155
"Queen Death": 156
"Ultralisk": 157
"Ultralisk Remnants": 158
"Zergling": 159
"Zergling Remnants": 160
"Cerebrate": 161
"Infested Command Center": 162
"Spawning Pool": 163
"Mature Chrysalis": 164
"Evolution Chamber": 165
"Creep Colony": 166
"Hatchery": 167
"Hive": 168
"Lair": 169
"Sunken Colony": 170
"Greater Spire": 171
"Defiler Mound": 172
"Queen's Nest": 173
"Nydus Canal": 174
"Overmind With Shell": 175
"Overmind Without Shell": 176
"Ultralisk Cavern": 177
"Extractor": 178
"Hydralisk Den": 179
"Spire": 180
"Spore Colony": 181
"Zerg Building Spawn (Small)": 182
"Zerg Building Spawn (Medium)": 183
"Zerg Building Spawn (Large)": 184
"Zerg Building Explosion": 185
"Zerg Building Rubble (Small)": 186
"Zerg Building Rubble (Large)": 187
"Arbiter": 188
"Archon Energy": 189
"Carrier": 190
"Dragoon": 191
"Dragoon Remnants": 192
"Interceptor": 193
"Probe": 194
"Scout": 195
"Shuttle": 196
"High Templar": 197
"Dark Templar (Hero)": 198
"Reaver": 199
"Scarab": 200
"Zealot": 201
"Observer": 202
"Templar Archives": 203
"Assimilator": 204
"Observatory": 205
"Citadel of Adun": 206
"Forge": 207
"Gateway": 208
"Cybernetics Core": 209
"Khaydarin Crystal Formation": 210
"Nexus": 211
"Photon Cannon": 212
"Arbiter Tribunal": 213
"Pylon": 214
"Robotics Facility": 215
"Shield Battery": 216
"Stargate": 217
"Stasis Cell/Prison": 218
"Robotics Support Bay": 219
"Protoss Temple": 220
"Fleet Beacon": 221
"Explosion (Large)": 222
"Protoss Building Rubble (Small)": 223
"Protoss Building Rubble (Large)": 224
"Battlecruiser": 225
"Civilian": 226
"Dropship": 227
"Firebat": 228
"Ghost": 229
"Ghost Remnants": 230
"Nuke Target Dot": 231
"Goliath Base": 232
"Goliath Turret": 233
"Sarah Kerrigan": 234
"Marine": 235
"Marine Remnants": 236
"Scanner Sweep": 237
"Wraith": 238
"SCV": 239
"Siege Tank (Tank) Base": 240
"Siege Tank (Tank) Turret": 241
"Siege Tank (Siege) Base": 242
"Siege Tank (Siege) Turret": 243
"Vulture": 244
"Spider Mine": 245
"Science Vessel (Base)": 246
"Science Vessel (Turret)": 247
"Terran Academy": 248
"Barracks": 249
"Armory": 250
"Comsat Station": 251
"Command Center": 252
"Supply Depot": 253
"Control Tower": 254
"Factory": 255
"Covert Ops": 256
"Ion Cannon": 257
"Machine Shop": 258
"Missile Turret (Base)": 259
"Crashed Batlecruiser": 260
"Physics Lab": 261
"Bunker": 262
"Refinery": 263
"Science Facility": 264
"Nuclear Silo": 265
"Nuclear Missile": 266
"Nuke Hit": 267
"Starport": 268
"Engineering Bay": 269
"Terran Construction (Large)": 270
"Terran Construction (Small)": 271
"Building Explosion (Large)": 272
"Terran Building Rubble (Small)": 273
"Terran Building Rubble (Large)": 274
"Vespene Geyser": 275
"Ragnasaur (Ash)": 276
"Rhynadon (Badlands)": 277
"Bengalaas (Jungle)": 278
"Mineral Field Type1": 279
"Mineral Field Type2": 280
"Mineral Field Type3": 281
"Independent Starport (Unused)": 282
"Zerg Beacon": 283
"Terran Beacon": 284
"Protoss Beacon": 285
"Dark Swarm": 286
"Flag": 287
"Young Chrysalis": 288
"Psi Emitter": 289
"Data Disc": 290
"Khaydarin Crystal": 291
"Mineral Chunk Type1": 292
"Mineral Chunk Type2": 293
"Protoss Gas Orb Type1": 294
"Protoss Gas Orb Type2": 295
"Zerg Gas Sac Type1": 296
"Zerg Gas Sac Type2": 297
"Terran Gas Tank Type1": 298
"Terran Gas Tank Type2": 299
"White Circle (Invisible)": 300
"Start Location": 301
"Map Revealer": 302
"Floor Gun Trap": 303
"Wall Missile Trap": 304
"Wall Missile Trap2": 305
"Wall Flame Trap": 306
"Wall Flame Trap2": 307
"Floor Missile Trap": 308
"Longbolt/Gemini Missiles Trail": 309
"Grenade Shot Smoke": 310
"Vespene Geyser Smoke1": 311
"Vespene Geyser Smoke2": 312
"Vespene Geyser Smoke3": 313
"Vespene Geyser Smoke4": 314
"Vespene Geyser Smoke5": 315
"Unknown316": 316
"Double Explosion": 317
"Cursor Marker": 318
"Egg Spawn": 319
"High Templar Glow": 320
"Psi Field (Right Upper)": 321
"Burrowing Dust": 322
"Building Landing Dust Type1": 323
"Building Landing Dust Type2": 324
"Building Landing Dust Type3": 325
"Building Landing Dust Type4": 326
"Building Landing Dust Type5": 327
"Building Lifting Dust Type1": 328
"Building Lifting Dust Type2": 329
"Building Lifting Dust Type3": 330
"Building Lifting Dust Type4": 331
"Needle Spines": 332
"Dual Photon Blasters Hit": 333
"Particle Beam Hit": 334
"Anti-Matter Missile": 335
"Pulse Cannon": 336
"Phase Disruptor": 337
"STA/STS Photon Cannon Overlay": 338
"Psionic Storm": 339
"Fusion Cutter Hit": 340
"Gauss Rifle Hit": 341
"Gemini Missiles": 342
"Fragmentation Grenade": 343
"Unknown344": 344
"Lockdown/LongBolt/Hellfire Missile": 345
"C-10 Canister Rifle Hit": 346
"ATS/ATA Laser Battery": 347
"Burst Lasers": 348
"Arclite Shock Cannon Hit": 349
"Yamato Gun": 350
"Yamato Gun Trail": 351
"EMP Shockwave Missile": 352
"Needle Spine Hit": 353
"Unknown354": 354
"Sunken Colony Tentacle": 355
"Venom (Unused Zerg Weapon)": 356
"Acid Spore": 357
"Glave Wurm": 358
"Seeker Spores": 359
"Queen Spell Holder": 360
"Stasis Field Hit": 361
"Plague Cloud": 362
"Consume": 363
"Ensnare": 364
"Glave Wurm/Seeker Spores Hit": 365
"Psionic Shockwave Hit": 366
"Glave Wurm Trail": 367
"Seeker Spores Overlay": 368
"Phase Disruptor (Unused)": 369
"White Circle": 370
"Acid Spray (Unused)": 371
"Unknown372": 372
"Scarab/Anti-Matter Missile Overlay": 373
"Hallucination Death1": 374
"Hallucination Death2": 375
"Hallucination Death3": 376
"Bunker Overlay": 377
"FlameThrower": 378
"Recall Field": 379
"Scanner Sweep Hit": 380
"Left Upper Level Door": 381
"Right Upper Level Door": 382
"Substructure Left Door": 383
"Substructure Right Door": 384
"Substructure Opening Hole": 385
"7/13 Twilight": 386
"7/14 Twilight": 387
"7/16 Twilight": 388
"7/15 Twilight": 389
"7/19 Twilight": 390
"7/20 Twilight": 391
"7/21 Twilight": 392
"Unknown Twilight": 393
"7/17 Twilight": 394
"6/1 Twilight": 395
"6/2 Twilight": 396
"6/3 Twilight": 397
"6/4 Twilight": 398
"6/5 Twilight": 399
"8/3 Twilight": 400
"8/3 Twilight": 401
"9/29 Ice": 402
"9/28 Ice": 403
"12/38 Ice": 404
"12/37 Ice": 405
"12/33 Ice": 406
"9/21 Ice": 407
"9/15 Ice": 408
"9/16 Ice": 409
"Unknown410": 410
"Unknown411": 411
"12/9 Ice1": 412
"12/10 Ice": 413
"9/24 Ice": 414
"9/23 Ice": 415
"Unknown416": 416
"12/7 Ice": 417
"12/8 Ice": 418
"12/9 Ice2": 419
"12/10 Ice": 420
"12/40 Ice": 421
"12/41 Ice": 422
"12/42 Ice": 423
"12/5 Ice": 424
"12/6 Ice": 425
"12/36 Ice": 426
"12/32 Ice": 427
"12/33 Ice": 428
"12/34 Ice": 429
"12/24 Ice": 430
"12/25 Ice": 431
"9/22 Ice": 432
"12/31 Ice": 433
"12/20 Ice": 434
"12/24 Ice": 435
"12/25 Ice": 436
"12/30 Ice": 437
"12/30 Ice": 438
"Unknown439": 439
"4/1 Ice": 440
"6/1 Ice": 441
"5/6 Ice": 442
"5/7 Ice": 443
"5/8 Ice": 444
"5/9 Ice": 445
"10/10 Desert1": 446
"10/12 Desert1": 447
"10/8 Desert": 448
"10/9 Desert1": 449
"6/10 Desert": 450
"6/13 Desert": 451
"Unknown Desert": 452
"10/12 Desert2": 453
"10/9 Desert2": 454
"10/10 Desert2": 455
"10/11 Desert": 456
"10/14 Desert": 457
"10/41 Desert": 458
"10/39 Desert": 459
"10/8 Desert": 460
"10/6 Desert": 461
"10/7 Desert": 462
"4/6 Desert": 463
"4/11 Desert": 464
"4/10 Desert": 465
"4/9 Desert": 466
"4/7 Desert": 467
"4/12 Desert": 468
"4/8 Desert": 469
"4/13 Desert": 470
"6/13 Desert": 471
"4/17 Desert": 472
"6/20 Desert": 473
"4/15 Desert1": 474
"4/15 Desert2": 475
"10/23 Desert": 476
"8/23 Desert": 477
"10/5 Desert": 478
"12/1 Desert Overlay": 479
"11/3 Desert": 480
"Lurker Egg": 481
"Devourer": 482
"Devourer Death": 483
"Lurker Remnants": 484
"Lurker": 485
"Dark Archon Energy": 486
"Corsair": 487
"Dark Templar (Unit)": 488
"Medic": 489
"Medic Remnants": 490
"Valkyrie": 491
"Scantid (Desert)": 492
"Kakaru (Twilight)": 493
"Ursadon (Ice)": 494
"Overmind Cocoon": 495
"Power Generator": 496
"Xel'Naga Temple": 497
"Psi Disrupter": 498
"Warp Gate": 499
"Feedback Hit (Small)": 500
"Feedback Hit (Medium)": 501
"Feedback Hit (Large)": 502
"Disruption Web": 503
"White Circle": 504
"Halo Rockets Trail": 505
"Neutron Flare": 506
"Corsair Attack Overlay (Unused)": 507
"Optical Flare Grenade": 508
"Halo Rockets": 509
"Subterranean Spines Hit": 510
"Subterranean Spines": 511
"Corrosive Acid Shot": 512
"Corrosive Acid Hit": 513
"Maelstrom Hit": 514
"Uraj": 515
"Khalis": 516
```

  





## StatText

```Python
# Units
'Terran Marine': 1
'Terran Ghost': 2
'Terran Vulture': 3
'Terran Goliath': 4
'Goliath Turret': 5
'Terran Siege Tank (Tank Mode)': 6
'Siege Tank Turret (Tank Mode)': 7
'Tank Turret type 1': 7
'Terran SCV': 8
'Terran Wraith': 9
'Terran Science Vessel': 10
'Gui Montag': 11
'Gui Montag (Firebat)': 11
'Terran Dropship': 12
'Terran Battlecruiser': 13
'Spider Mine': 14
'Vulture Spider Mine': 14
'Nuclear Missile': 15
'Terran Civilian': 16
'Sarah Kerrigan': 17
'Sarah Kerrigan (Ghost)': 17
'Alan Schezar': 18
'Alan Schezar (Goliath)': 18
'Alan Schezar Turret': 19
'Alan Turret': 19
'Jim Raynor (Vulture)': 20
'Jim Raynor (Marine)': 21
'Tom Kazansky': 22
'Tom Kazansky (Wraith)': 22
'Magellan': 23
'Magellan (Science Vessel)': 23
'Edmund Duke (Tank Mode)': 24
'Edmund Duke (Siege Tank)': 24
'Edmund Duke Turret (Tank Mode)': 25
'Duke Turret type 1': 25
'Edmund Duke (Siege Mode)': 26
'Edmund Duke Turret (Siege Mode)': 27
'Duke Turret type 2': 27
'Arcturus Mengsk': 28
'Arcturus Mengsk (Battlecruiser)': 28
'Hyperion': 29
'Hyperion (Battlecruiser)': 29
'Norad II (Battlecruiser)': 30
'Terran Siege Tank (Siege Mode)': 31
'Siege Tank Turret (Siege Mode)': 32
'Tank Turret type 2': 32
'Terran Firebat': 33
'Scanner Sweep (Unit)': 34
'Terran Medic': 35
'Zerg Larva': 36
'Zerg Egg': 37
'Zerg Zergling': 38
'Zerg Hydralisk': 39
'Zerg Ultralisk': 40
'Zerg Broodling': 41
'Zerg Drone': 42
'Zerg Overlord': 43
'Zerg Mutalisk': 44
'Zerg Guardian': 45
'Zerg Queen': 46
'Zerg Defiler': 47
'Zerg Scourge': 48
'Torrasque': 49
'Torrasque (Ultralisk)': 49
'Matriarch': 50
'Matriarch (Queen)': 50
'Infested Terran': 51
'Infested Kerrigan': 52
'Infested Kerrigan (Infested Terran)': 52
'Unclean One': 53
'Unclean One (Defiler)': 53
'Hunter Killer': 54
'Hunter Killer (Hydralisk)': 54
'Devouring One': 55
'Devouring One (Zergling)': 55
'Kukulza (Mutalisk)': 56
'Kukulza (Guardian)': 57
'Yggdrasill': 58
'Yggdrasill (Overlord)': 58
'Terran Valkyrie': 59
'Mutalisk Cocoon': 60
'Cocoon': 60
'Protoss Corsair': 61
'Protoss Dark Templar': 62
'Protoss Dark Templar (Unit)': 62
'Zerg Devourer': 63
'Protoss Dark Archon': 64
'Protoss Probe': 65
'Protoss Zealot': 66
'Protoss Dragoon': 67
'Protoss High Templar': 68
'Protoss Archon': 69
'Protoss Shuttle': 70
'Protoss Scout': 71
'Protoss Arbiter': 72
'Protoss Carrier': 73
'Protoss Interceptor': 74
'Dark Templar': 75
'Dark Templar (Hero)': 75
'Protoss Dark Templar (Hero)': 75
'Zeratul': 76
'Zeratul (Dark Templar)': 76
'Tassadar/Zeratul': 77
'Tassadar/Zeratul (Archon)': 77
'Fenix (Zealot)': 78
'Fenix (Dragoon)': 79
'Tassadar (Unit)': 80
'Tassadar (Templar)': 80
'Mojo': 81
'Mojo (Scout)': 81
'Warbringer': 82
'Warbringer (Reaver)': 82
'Gantrithor': 83
'Gantrithor (Carrier)': 83
'Protoss Reaver': 84
'Protoss Observer': 85
'Protoss Scara': 86
'Danimoth': 87
'Danimoth (Arbiter)': 87
'Aldaris': 88
'Aldaris (Templar)': 88
'Artanis': 89
'Artanis (Scout)': 89
'Rhynadon': 90
'Rhynadon (Badlands)': 90
'Rhynadon (Badlands Critter)': 90
'Bengalaas': 91
'Bengalaas (Jungle)': 91
'Bengalaas (Jungle Critter)': 91
'Cargo Ship': 92
'Cargo Ship (Unused)': 92
'Unused type 1': 92
'Unused type 2': 93
'Mercenary Gunship': 93
'Mercenary Gunship (Unused)': 93
'Scantid': 94
'Scantid (Desert)': 94
'Scantid (Desert Critter)': 94
'Kakaru': 95
'Kakaru (Twilight)': 95
'Kakaru (Twilight Critter)': 95
'Ragnasaur': 96
'Ragnasaur (Ashworld)': 96
'Ragnasaur (Ashworld Critter)': 96
'Ursadon': 97
'Ursadon (Ice World)': 97
'Ursadon (Ice World Critter)': 97
'Lurker Egg': 98
'Zerg Lurker Egg': 98
'Raszagal': 99
'Raszagal (Corsair)': 99
'Samir Duran': 100
'Samir Duran (Ghost)': 100
'Alexei Stukov': 101
'Alexei Stukov (Ghost)': 101
'Map Revealer': 102
'Gerard DuGalle': 103
'Gerard DuGalle (Ghost)': 103
'Gerard DuGalle (BattleCruiser)': 103
'Zerg Lurker': 104
'Infested Duran': 105
'Infested Duran (Infested Terran)': 105
'Disruption Web (Unit)': 106
'Disruption Field': 106
'Terran Command Center': 107
'Terran Comsat Station': 108
'Terran Nuclear Silo': 109
'Terran Supply Depot': 110
'Terran Refinery': 111
'Terran Barracks': 112
'Terran Academy': 113
'Terran Factory': 114
'Terran Starport': 115
'Terran Control Tower': 116
'Terran Science Facility': 117
'Terran Covert Ops': 118
'Terran Physics La': 119
'Starbase': 120
'Starbase (Unused)': 120
'Unused Terran Bldg type 1': 120
'Terran Machine Shop': 121
'Repair Bay': 122
'Repair Bay (Unused)': 122
'Unused Terran Bldg type 2': 122
'Terran Engineering Bay': 123
'Terran Armory': 124
'Terran Missile Turret': 125
'Terran Bunker': 126
'Norad II (Crashed)': 127
'Norad II (Crashed Battlecruiser)': 127
'Ion Cannon': 128
'Uraj Crystal': 129
'Khalis Crystal': 130
'Infested Command Center': 131
'Zerg Hatchery': 132
'Zerg Lair': 133
'Zerg Hive': 134
'Zerg Nydus Canal': 135
'Zerg Hydralisk Den': 136
'Zerg Defiler Mound': 137
'Zerg Greater Spire': 138
"Zerg Queen's Nest": 139
'Zerg Evolution Chamber': 140
'Zerg Ultralisk Cavern': 141
'Zerg Spire': 142
'Zerg Spawning Pool': 143
'Zerg Creep Colony': 144
'Zerg Spore Colony': 145
'Unused Zerg Bldg': 146
'Unused Zerg Building1': 146
'Zerg Sunken Colony': 147
'Zerg Overmind (With Shell)': 148
'Zerg Overmind': 149
'Zerg Extractor': 150
'Mature Chrysalis': 151
'Mature Crysalis': 151
'Zerg Cerebrate': 152
'Zerg Cerebrate Daggoth': 153
'Unused Zerg Building2': 154
'Protoss Nexus': 155
'Protoss Robotics Facility': 156
'Protoss Pylon': 157
'Protoss Assimilator': 158
'Protoss Unused type 1': 158
'Unused Protoss Building1': 159
'Protoss Observatory': 160
'Protoss Gateway': 161
'Protoss Unused type 2': 162
'Unused Protoss Building2': 162
'Protoss Photon Cannon': 163
'Protoss Citadel of Adun': 164
'Protoss Cybernetics Core': 165
'Protoss Templar Archives': 166
'Protoss Forge': 167
'Protoss Stargate': 168
'Stasis Cell/Prison': 169
'Protoss Fleet Beacon': 170
'Protoss Arbiter Tribunal': 171
'Protoss Robotics Support Bay': 172
'Protoss Shield Battery': 173
'Khaydarin Crystal Formation': 174
'Protoss Temple': 175
"Xel'Naga Temple": 176
'Mineral Field (Type 1)': 177
'Mineral Field (Type 2)': 178
'Mineral Field (Type 3)': 179
'Cave': 180
'Cave (Unused)': 180
'Cave-in': 181
'Cave-in (Unused)': 181
'Cantina': 182
'Cantina (Unused)': 182
'Mining Platform': 183
'Mining Platform (Unused)': 183
'Independent Command Center': 184
'Independent Command Center (Unused)': 184
'Independent Starport': 185
'Independent Starport (Unused)': 185
'Jump Gate': 186
'Independent Jump Gate (Unused)': 186
'Ruins (Unused)': 187
'Kyadarin Crystal Formation': 188
'Khaydarin Crystal Formation (Unused)': 188
'Vespene Geyser': 189
'Warp Gate': 190
'Psi Disrupter': 191
'Zerg Marker': 192
'Terran Marker': 193
'Protoss Marker': 194
'Zerg Beacon': 195
'Terran Beacon': 196
'Protoss Beacon': 197
'Zerg Flag Beacon': 198
'Terran Flag Beacon': 199
'Protoss Flag Beacon': 200
'Power Generator': 201
'Overmind Cocoon': 202
'Dark Swarm (Unit)': 203
'Floor Missile Trap': 204
'Floor Hatch (Unused)': 205
'Floor Hatch (UNUSED)': 205
'Left Upper Level Door': 206
'Right Upper Level Door': 207
'Left Pit Door': 208
'Right Pit Door': 209
'Floor Gun Trap': 210
'Left Wall Missile Trap': 211
'Left Wall Flame Trap': 212
'Right Wall Missile Trap': 213
'Right Wall Flame Trap': 214
'Start Location': 215
'Flag': 216
'Young Chrysalis': 217
'Psi Emitter': 218
'Data Disc': 219
'Khaydarin Crystal': 220
'Mineral Chunk (Type 1)': 221
'Mineral Cluster Type 1': 221
'Mineral Chunk (Type 2)': 222
'Mineral Cluster Type 2': 222
'Vespene Orb (Protoss Type 1)': 223
'Protoss Vespene Gas Orb Type 1': 223
'Vespene Orb (Protoss Type 2)': 224
'Protoss Vespene Gas Orb Type 2': 224
'Vespene Sac (Zerg Type 1)': 225
'Zerg Vespene Gas Sac Type 1': 225
'Vespene Sac (Zerg Type 2)': 226
'Zerg Vespene Gas Sac Type 2': 226
'Vespene Tank (Terran Type 1)': 227
'Terran Vespene Gas Tank Type 1': 227
'Vespene Tank (Terran Type 2)': 228
'Terran Vespene Gas Tank Type 2': 228

# Weapons
'Gauss Rifle (Marine)': 229
'Gauss Rifle (Jim Raynor)': 230
'C-10 Canister Rifle (Ghost)': 231
'C-10 Canister Rifle (Sarah Kerrigan)': 232
'Fragmentation Grenade (Vulture)': 233
'Fragmentation Grenade (Jim Raynor)': 234
'Twin Autocannons (Goliath)': 235
'Hellfire Missile Pack (Goliath)': 236
'Twin Autocannons (Alan Schezar)': 237
'Hellfire Missile Pack (Alan Schezar)': 238
'Arclite Cannon (Siege Tank)': 239
'Arclite Cannon (Edmund Duke)': 240
'Fusion Cutter': 241
'Fusion Cutter (Harvest)': 242
'Gemini Missiles (Wraith)': 243
'Burst Lasers (Wraith)': 244
'Gemini Missiles (Tom Kazansky)': 245
'Burst Lasers (Tom Kazansky)': 246
'ATS Laser Battery (Battlecruiser)': 247
'ATA Laser Battery (Battlecruiser)': 248
'ATS Laser Battery (Norad II)': 249
'ATA Laser Battery (Norad II)': 250
'ATS Laser Battery (Hyperion)': 251
'ATA Laser Battery (Hyperion)': 252
'Flame Thrower (Firebat)': 253
'Flame Thrower (Gui Montag)': 254
'Arclite Shock Cannon (Siege Tank)': 255
'Arclite Shock Cannon (Edmund Duke)': 256
'Longbolt Missile': 257
'Nuclear Strike (Weapon)': 258
'EMP Shockwave (Weapon)': 259
'Claws (Zergling)': 260
'Claws (Devouring One)': 261
'Claws (Infested Kerrigan)': 262
'Needle Spines (Hydralisk)': 263
'Needle Spines (Hunter Killer)': 264
'Kaiser Blades (Ultralisk)': 265
'Kaiser Blades (Torrasque)': 266
'Toxic Spores': 267
'Spines': 268
'Acid Spray (Unused 1)': 269
'Acid Spray (Unused 2)': 270
'Acid Spore (Guardian)': 271
'Acid Spore (Kukulza)': 272
'Glave Wurm (Mutalisk)': 273
'Glave Wurm (Kukulza)': 274
'Venom (Defiler)': 275
'Venom (Unclean One)': 276
'Suicide (Infested Terran)': 277
'Seeker Spores': 278
'Subterranean Tentacle': 279
'Suicide (Scourge)': 280
'Particle Beam': 281
'Psi Blades (Zealot)': 282
'Psi Blades (Fenix)': 283
'Warp Blades (Dark Templar Hero)': 284
'Warp Blades (Zeratul)': 285
'Phase Disruptor (Dragoon)': 286
'Phase Disruptor (Fenix)': 287
'Psi Assault (High Templar)': 288
'Psi Assault (Tassadar)': 289
'Psionic Shockwave (Archon)': 290
'Psionic Shockwave (Tassadar/Zeratul)': 291
'Unused72': 292
'Dual Photon Blasters (Scout)': 293
'Anti-matter Missiles (Scout)': 294
'Dual Photon Blasters (Mojo)': 295
'Anti-matter Missiles (Mojo)': 296
'Phase Disruptor Cannon (Arbiter)': 297
'Phase Disruptor Cannon (Danimoth)': 298
'Pulse Cannon': 299
'STS Photon Cannon': 300
'STA Photon Cannon': 301
'Scarab (Weapon)': 302
'Missiles': 303
'Laser Battery': 304
'Tormentor Missiles': 305
'Bombs': 306
'Raider Gun': 307
'Flechette Grenade': 308
'Twin Autocannons': 309
'Hellfire Missile Pack': 310
'Flame Thrower': 311
'Undefined Weapon Name': 312

# Spells
'Stim Packs (Tech)': 313
'Lockdown (Weapon)': 314
'EMP Shockwave (Tech)': 315
'Spider Mines (Weapon)': 316
'Scanner Sweep (Tech)': 317
'Tank Siege Mode': 318
'Defensive Matrix (Tech)': 319
'Irradiate (Tech)': 320
'Yamato Gun (Weapon)': 321
'Cloaking Field': 322
'Personnel Cloaking': 323
'Research Stim Pack Tech': 324
'Research Lockdown': 325
'Research EMP Shockwave': 326
'Research Spider Mines': 327
'Research Siege Tech': 328
'Research Defensive Matrix': 329
'Research Irradiate': 330
'Research Yamato Gun': 331
'Research Cloaking Field': 332
'Research Personnel Cloaking': 333
'Use Stim Packs': 334
'Lockdown (Cast)': 335
'Use Spider Mines': 336
'Scanner Sweep (Cast)': 337
'Siege Mode (Cast)': 338
'Tank Mode (Cast)': 339
'Activate Defensive Matrix': 340
'Activate EMP Shockwave': 341
'Irradiate (Cast)': 342
'Yamato Gun (Cast)': 343
'Cloak (Cast)': 344
'Decloak (Cast)': 345
'Stim Packs:': 346
'Stim Packs: Research at Academy': 346
'Lockdown:': 347
'Lockdown: Research at Covert Ops': 347
'Spider Mines:': 348
'Spider Mines: Research at Machine Shop': 348
'Siege Mode:': 349
'Siege Mode: Research at Machine Shop': 349
'Defensive Matrix:': 350
'Defensive Matrix: Research at Science Facility': 350
'EMP Shockwave:': 351
'EMP Shockwave: Research at Science Facility': 351
'Irradiate:': 352
'Irradiate: Research at Science Facility': 352
'Yamato Gun:': 353
'Yamato Gun: Research at Physics La': 353
'Cloaking Field:': 354
'Cloaking Field: Research at Control Tower': 354
'Personnel Cloaking:': 355
'Personnel Cloaking: Research at Covert Ops': 355
'Burrowing': 356
'Infestation': 357
'Spawn Broodling (Tech)': 358
'Dark Swarm (Tech)': 359
'Parasite (Tech)': 360
'Plague (Tech)': 361
'Consume (Tech)': 362
'Ensnare (Tech)': 363
'Evolve Burrow': 364
'Evolve Infestation': 365
'Evolve Spawn Broodling': 366
'Evolve Dark Swarm': 367
'Evolve Parasite': 368
'Evolve Plague': 369
'Evolve Ensnare': 370
'Evolve Consume': 371
'Burrow (Cast)': 372
'Unburrow (Cast)': 373
'Infest Terran Command Center': 374
'Spawn Broodling (Cast)': 375
'Dark Swarm (Cast)': 376
'Parasite (Cast)': 377
'Plague (Cast)': 378
'Consume (Defiler)': 379
'Consume (Infested Kerrigan)': 380
'Ensnare (Cast)': 381
'Burrow:': 382
'Burrow: Evolve at Hatchery': 382
'Infest:': 383
"Infest: Evolve at Queen's Nest": 383
'Spawn Broodlings:': 384
"Spawn Broodlings: Evolve at Queen's Nest": 384
'Dark Swarm:': 385
'Dark Swarm: Evolve at Defiler Mound': 385
'Parasite:': 386
"Parasite: Evolve at Queen's Nest": 386
'Plague:': 387
'Plague: Evolve at Defiler Mound': 387
'Consume:': 388
'Consume: Evolve at Defiler Mound': 388
'Ensnare:': 389
"Ensnare: Evolve at Queen's Nest": 389
'Psionic Storm (Unused)': 390
'Hallucination (Unused)': 391
'Recall (Unused)': 392
'Stasis Field (Unused)': 393
'Archon Warp (Unused)': 394
'Develop Psionic Storm': 395
'Develop Hallucination': 396
'Develop Recall': 397
'Develop Stasis Field': 398
'Develop Archon Warp': 399
'Psionic Storm (Cast)': 400
'Hallucination (Cast)': 401
'Recall (Cast)': 402
'Stasis Field (Cast)': 403
'Archon Warp (Cast)': 404
'Psionic Storm:': 405
'Psionic Storm: Develop at Templar Archives': 405
'Hallucination:': 406
'Hallucination: Develop at Templar Archives': 406
'Recall:': 407
'Recall: Develop at Arbiter Tribunal': 407
'Stasis Field:': 408
'Stasis Field: Develop at Arbiter Tribunal': 408
'Archon Warp: (Templar Archives)': 409
'Archon Warp: Research at Templar Archives': 409
'Archon Warp: (High Templar)': 410
'Archon Warp: Select 2 or more Templars': 410

# Upgrades
'Terran Infantry Armor': 411
'Terran Vehicle Plating': 412
'Terran Ship Plating': 413
'Zerg Carapace': 414
'Zerg Flyer Carapace': 415
'Protoss Armor': 416
'Protoss Plating': 417
'Terran Infantry Weapons': 418
'Terran Vehicle Weapons': 419
'Terran Ship Weapons': 420
'Zerg Melee Attacks': 421
'Zerg Missile Attacks': 422
'Zerg Flyer Attacks': 423
'Protoss Ground Weapons': 424
'Protoss Air Weapons': 425
'Protoss Plasma Shields': 426
'U-238 Shells': 427
'Ion Thrusters': 428
'Burst Lasers': 429
'Titan Reactor': 430
'Ocular Implants': 431
'Moebius Reactor': 432
'Apollo Reactor': 433
'Colossus Reactor': 434
'Ventral Sacs': 435
'Antennae': 436
'Pneumatized Carapace': 437
'Metabolic Boost': 438
'Adrenal Glands': 439
'Muscular Augments': 440
'Grooved Spines': 441
'Gamete Meiosis': 442
'Metasynaptic Node': 443
'Singularity Charge': 444
'Leg Enhancements': 445
'Scarab Damage': 446
'Reaver Capacity': 447
'Gravitic Drive': 448
'Sensor Array': 449
'Gravitic Boosters': 450
'Khaydarin Amulet': 451
'Apial Sensors': 452
'Gravitic Thrusters': 453
'Carrier Capacity': 454
'Khaydarin Core': 455
'Upgrade Infantry Armor': 456
'Upgrade Vehicle Plating': 457
'Upgrade Ship Plating': 458
'Evolve Carapace': 459
'Evolve Flyer Carapace': 460
'Upgrade Ground Armor': 461
'Upgrade Air Armor': 462
'Upgrade Infantry Weapons': 463
'Upgrade Vehicle Weapons': 464
'Upgrade Ship Weapons': 465
'Upgrade Melee Attacks': 466
'Upgrade Missile Attacks': 467
'Upgrade Flyer Attacks': 468
'Upgrade Ground Weapons': 469
'Upgrade Air Weapons': 470
'Upgrade Plasma Shields': 471
'Research U-238 Shells': 472
'Research Ion Thrusters': 473
'Research Burst Lasers': 474
'Research Titan Reactor': 475
'Research Ocular Implants': 476
'Research Moebius Reactor': 477
'Research Apollo Reactor': 478
'Research Colossus Reactor': 479
'Evolve Ventral Sacs': 480
'Evolve Antennae': 481
'Evolve Pneumatized Carapace': 482
'Evolve Metabolic Boost': 483
'Evolve Adrenal Glands': 484
'Evolve Muscular Augments': 485
'Evolve Grooved Spines': 486
'Evolve Gamete Meiosis': 487
'Evolve Metasynaptic Node': 488
'Develop Singularity Charge': 489
'Develop Leg Enhancements': 490
'Upgrade Scarab Damage': 491
'Increase Reaver Capacity': 492
'Develop Gravitic Drive': 493
'Develop Sensor Array': 494
'Develop Gravitic Booster': 495
'Develop Khaydarin Amulet': 496
'Develop Apial Sensors': 497
'Develop Gravitic Thrusters': 498
'Increase Carrier Capacity': 499
'Develop Khaydarin Core': 500
'Infantry Armor L1 Require:': 501
'Infantry Armor L2 Require:': 502
'Infantry Armor L3 Require:': 503
'Infantry Weapons L1 Require:': 504
'Infantry Weapons L2 Require:': 505
'Infantry Weapons L3 Require:': 506
'Vehicle Weapons L1 Require:': 507
'Vehicle Weapons L2 Require:': 508
'Vehicle Weapons L3 Require:': 509
'Vehicle Plating L1 Requires:': 510
'Vehicle Plating L2 Requires:': 511
'Vehicle Plating L3 Requires:': 512
'Ship Weapons L1 Require:': 513
'Ship Weapons L2 Require:': 514
'Ship Weapons L3 Require:': 515
'Ship Plating L1 Requires:': 516
'Ship Plating L2 Requires:': 517
'Ship Plating L3 Requires:': 518
'Melee Attacks L1 Require:': 519
'Melee Attacks L2 Require:': 520
'Melee Attacks L3 Require:': 521
'Missile Attacks L1 Require:': 522
'Missile Attacks L2 Require:': 523
'Missile Attacks L3 Require:': 524
'Carapace L1 Requires:': 525
'Carapace L2 Requires:': 526
'Carapace L3 Requires:': 527
'Flyer Attacks L1 Require:': 528
'Flyer Attacks L2 Require:': 529
'Flyer Attacks L3 Require:': 530
'Flyer Carapace L1 Requires:': 531
'Flyer Carapace L2 Requires:': 532
'Flyer Carapace L3 Requires:': 533
'Adrenal Glands Require:': 534
'Ground Weapons L1 Require:': 535
'Ground Weapons L2 Require:': 536
'Ground Weapons L3 Require:': 537
'Air Weapons L1 Require:': 538
'Air Weapons L2 Require:': 539
'Air Weapons L3 Require:': 540
'Ground Armor L1 Requires:': 541
'Ground Armor L2 Requires:': 542
'Ground Armor L3 Requires:': 543
'Air Armor L1 Requires:': 544
'Air Armor L2 Requires:': 545
'Air Armor L3 Requires:': 546
'Shields L1 Require:': 547
'Shields L2 Require:': 548
'Shields L3 Require:': 549
'Recruit (Unused)': 550
'Private (Marine Unused)': 551
'Private (SCV Unused)': 552
'Corporal (Unused)': 553
'Specialist (Unused)': 554
'Sergeant (Unused)': 555
'First Sergeant (Goliath Unused)': 556
'Master Sergeant (Unused)': 557
'Warrant Officer (Unused)': 558
'Captain (Unused)': 559
'Major (Unused)': 560
'Lt Commander (Unused)': 561
'First Sergeant (Gui Montag Unused)': 562
'Sergeant Major (Unused)': 563
'Colonel (Unused)': 564
'Commodore (Unused)': 565
'Marshall (Unused)': 566
'Lieutenant (Unused)': 567
'General (Unused)': 568
'Captain Raynor (Unused)': 569
'General Duke (Unused)': 570
'Admiral (Unused)': 571
'Tassadar (Unused)': 572
'Interceptors (Unused)': 573
'ESC': 574
'Morph to Zerglings': 575
'Morph to Hydralisk': 576
'Morph to Ultralisk': 577
'Morph to Drone': 578
'Morph to Overlord': 579
'Morph to Mutalisk': 580
'Guardian Aspect (Cast)': 581
'Morph to Queen': 582
'Morph to Defiler': 583
'Morph to Scourge': 584
'Train Infested Terran': 585
'Train Marine': 586
'Train Ghost': 587
'Train Firebat': 588
'Build Vulture': 589
'Build Goliath': 590
'Build Siege Tank': 591
'Build SCV': 592
'Build Wraith': 593
'Build Science Vessel': 594
'Build Dropship': 595
'Build Battlecruiser': 596
'Arm Nuclear Silo': 597
'Build Observer': 598
'Build Probe': 599
'Warp in Zealot': 600
'Warp in Dragoon': 601
'Warp in High Templar': 602
'Build Shuttle': 603
'Warp in Scout': 604
'Warp in Arbiter': 605
'Warp in Carrier': 606
'Build Interceptor': 607
'Build Reaver': 608
'Build Scara': 609
'Hire Merc Biker': 610
'Hire Merc Gunship': 611
'Hire Raider': 612
'Mutate into Hatchery': 613
'Mutate into Creep Colony': 614
'Mutate into Extractor': 615
'Mutate into Spawning Pool': 616
'Mutate into Evolution Chamber': 617
'Mutate into Hydralisk Den': 618
'Mutate into Nydus Canal': 619
'Mutate into Spire': 620
"Mutate into Queen's Nest": 621
'Mutate into Ultralisk Cavern': 622
'Mutate into Defiler Mound': 623
'Mutate into Lair': 624
'Mutate into Hive': 625
'Mutate into Greater Spire': 626
'Mutate into Spore Colony': 627
'Mutate into Sunken Colony': 628
'Place Nydus Canal Exit': 629
'Warp in Nexus': 630
'Warp in Pylon': 631
'Warp in Assimilator': 632
'Warp in Gateway': 633
'Warp in Forge': 634
'Warp in Photon Cannon': 635
'Warp in Cybernetics Core': 636
'Warp in Shield Battery': 637
'Warp in Robotics Facility': 638
'Warp in Observatory': 639
'Warp in Citadel of Adun': 640
'Warp in Templar Archives': 641
'Warp in Stargate': 642
'Warp in Fleet Beacon': 643
'Warp in Arbiter Tribunal': 644
'Warp in Robotics Support Bay': 645
'Build Command Center': 646
'Build Supply Depot': 647
'Build Refinery': 648
'Build Barracks': 649
'Build Engineering Bay': 650
'Build Missile Turret': 651
'Build Academy': 652
'Build Bunker': 653
'Build Factory': 654
'Build Starport': 655
'Build Science Facility': 656
'Build Armory': 657
'Build Comsat Station': 658
'Build Nuclear Silo': 659
'Build Control Tower': 660
'Build Covert Ops': 661
'Build Physics La': 662
'Build Machine Shop': 663
'Move': 664
'Stop (Cast)': 665
'Attack (Cast)': 666
'Patrol (Cast)': 667
'Hold Position (Cast)': 668
'Way Points': 669
'Land': 670
'Liftoff': 671
'Set Rally Point': 672
'Recharge Shields (Cast)': 673
'Select Larva': 674
'Gather': 675
'Return Cargo': 676
'Repair (Cast)': 677
'Build Structure': 678
'Build Advanced Structure': 679
'Basic Mutation': 680
'Advanced Mutation': 681
'Advanced Morph': 682
'Load': 683
'Unload All': 684
'Nuclear Strike (Cast)': 685
'Place COP': 686
'ESC - Cancel (Unknown)': 687
'ESC - Cancel (Normal)': 688
'ESC - Cancel Construction': 689
'ESC - Cancel Unit Training': 690
'ESC - Cancel Upgrade': 691
'ESC - Cancel Research': 692
'ESC - Cancel Last': 693
'ESC - Cancel Addon': 694
'ESC - Cancel Morph': 695
'ESC - Cancel Mutation (Build)': 696
'ESC - Cancel Infestation': 697
'ESC - Cancel Mutation (Lair)': 698
'ESC - Cancel Nuclear Strike': 699
'ESC - Halt Construction': 700
'Ghost Requires:': 701
'Firebat Requires:': 702
'Goliath Requires:': 703
'Siege Tank Requires:': 704
'Science Vessel Requires:': 705
'Dropship Requires:': 706
'Battlecruiser Requires:': 707
'Comsat Station Requires:': 708
'Nuclear Silo Requires:': 709
'Barracks Requires:': 710
'Academy Requires:': 711
'Factory Requires:': 712
'Starport Requires:': 713
'Science Facility Requires:': 714
'Engineering Bay Requires:': 715
'Armory Requires:': 716
'Missile Turret Requires:': 717
'Bunker Requires:': 718
'Dragoon Requires:': 719
'Templar Requires:': 720
'Arbiter Requires:': 721
'Carrier Requires:': 722
'Reaver Requires:': 723
'Observer Requires:': 724
'Gateway Requires:': 725
'Forge Requires:': 726
'Photon Cannon Requires:': 727
'Shield Battery Requires:': 728
'Cybernetics Core Requires:': 729
'Robotics Facility Requires:': 730
'Stargate Requires:': 731
'Citadel of Adun Requires:': 732
'Observatory Requires:': 733
'Robotics Support Bay Requires:': 734
'Fleet Beacon Requires:': 735
'Templar Archives Require:': 736
'Arbiter Tribunal Requires:': 737
'Zerglings Require:': 738
'Hydralisk Requires:': 739
'Ultralisk Requires:': 740
'Mutalisk Requires:': 741
'Guardian Aspect Requires:': 742
'Queen Requires:': 743
'Defiler Requires:': 744
'Scourge Require:': 745
'Lair Requires:': 746
'Hive Requires:': 747
'Nydus Canal Requires:': 748
'Hydralisk Den Requires:': 749
'Spire Requires:': 750
'Greater Spire Requires:': 751
"Queen's Nest Requires:": 752
'Evolution Chamber Requires:': 753
'Ultralisk Cavern Requires:': 754
'Defiler Mound Requires:': 755
'Spawning Pool Requires:': 756
'Spawning Pool Requires: Hatchery': 756
'Spore Colony Requires:': 757
'Spore Colony Requires: Evolution Chamber': 757
'Sunken Colony Requires:': 758
'Sunken Colony Requires: Spawning Pool': 758
'Carrier Attack:': 759
'Carrier Attack: Build Interceptors': 759
'Reaver Attack:': 760
'Reaver Attack: Build Scarabs': 760
'Nuclear Strike Requires:': 761
'Nuclear Strike Requires: Armed Nuclear Silo': 761
'Not Implemented': 762
'mk': 763
'Kills:': 764
'Evolving (1)': 765
'Upgrading (1)': 766
'Upgrading (2)': 767
'Evolving (2)': 768
'Researching': 769
'Developing': 770
'Morphing (1)': 771
'Building (1)': 772
'Opening Warp Gate': 773
'Morphing (2)': 774
'Building (2)': 775
'Building (3)': 776
'Damage:': 777
'Armor:': 778
'Shields:': 779
'Mining Delay:': 780
'Production': 781
'Unit Ptr:': 782
'Current Order:': 783
'Next Order:': 784
'% Complete': 785
'Order:': 786
'Mutating (1)': 787
'Adding On': 788
'Opening Warp Rift (1)': 789
'Summoning': 790
'Interceptors (Count)': 791
'Scarabs': 792
'Nukes': 793
'Spider Mines (Count)': 794
'Next Level:': 795
'Minerals:': 796
'Vespene Gas:': 797
'Depleted': 798
'Mutating (2)': 799
'Under Construction': 800
'Opening Warp Rift (2)': 801
'Cancel Morph (%s)': 802
'Cancel Construction (%s)': 803
'Cancel Warp (%s)': 804
'Cancel Upgrade': 805
'Cancel Research': 806
'Cancel Morph': 807
'Unload Unit (%s)': 808
'Click: Select Unit': 809
'Show Terrain in Minimap (Tab)': 810
'Hide Terrain in Minimap (Tab)': 811
'Diplomacy': 812
'Messaging': 813
'Game Menu (F10)': 814
'Control Provided:': 815
'Supplies Provided:': 816
'Psi Provided:': 817
'Total Control:': 818
'Total Supplies:': 819
'Total Psi:': 820
'Control Used:': 821
'Supplies Used:': 822
'Psi Used:': 823
'Control Max:': 824
'Supplies Max:': 825
'Psi Max:': 826
'Parasite Detected': 827
'Disabled (1)': 828
'Disabled (2)': 829
'Unpowered': 830
'Detector': 831
'Hallucination (Status)': 832
'Units (1)': 833
'Units (2)': 834
'Resources': 835
'Kills': 836
'Score': 837
'Units to go (1)': 838
'Units to go (2)': 839
'Resources to go': 840
'Kills to go': 841
'Score to go': 842
"Nowhere to return to...can't return.": 843
'Too many underlings...create more Overlords.': 844
'Not enough supplies...build more Supply Depots.': 845
'Not enough psi...build more Pylons.': 846
'Underling limit exceeded.': 847
'Supply limit exceeded.': 848
'Psi limit exceeded.': 849
'Not enough minerals...mine more minerals.': 850
'Not enough Vespene gases....harvest more gas.': 851
"You can't build next to minerals or geysers.": 852
'An undetected unit is in the way.': 853
"You can't build off the map.": 854
"You can't build near the edge of the map.": 855
"You can't build there.": 856
'You must explore there first.': 857
'You must currently be able to see the location.': 858
'Could not build there find a Vespene Geyser to build on.': 859
'You must build on the Creep.': 860
'You must build near a Pylon.': 861
"Couldn't reach the building site.": 862
"You can't land there.": 863
'Not enough energy. (1)': 864
'Not enough energy. (2)': 865
'Not enough energy. (3)': 866
'Nothing to harvest. Find a Mine or a Vespene Geyser.': 867
'Nothing to harvest. Find a Mine or build a Refinery at a Vespene Geyser.': 868
'Nothing to harvest. Find a Mine or build an Assimilator at a Vespene Geyser.': 869
'Must target severely damaged Terran Command Center.': 870
"Unit's waypoint list is full.": 871
'Unable to add order.': 872
'Running low on orders your last order was not processed.': 873
'Not enough life remaining.': 874
'Vespene Geyser depleted.': 875
'Invalid target. (1)': 876
'Unable to target structure. (1)': 877
'Must target units.': 878
'Unable to attack target.': 879
'Invalid target. (2)': 880
'Must target mechanical units.': 881
'Invalid target. (3)': 882
'Must target damaged mechanical units or damaged complete buildings.': 883
'Must target Terran units.': 884
'Invalid target. (4)': 885
'Must target non-robotic ground units.': 886
'Must target ground.': 887
'Target out of range.': 888
'Target is too close.': 889
'Can only pick up your own transportable units.': 890
'Not enough room for unit.': 891
'Must gather from a Mineral Field or Vespene Geyser.': 892
'Morph an Extractor there first.': 893
'Build a Refinery there first.': 894
'Build an Assimilator there first.': 895
'Must gather gases from your own geyser.': 896
'Invalid target. (5)': 897
'Invalid target. (6)': 898
'Invalid target. (7)': 899
"Units in stasis can't be targeted.": 900
'Must target non-hovering ground units.': 901
'Must target passable terrain.': 902

# Commands
'Die': 903
'Fizzle': 904
'Stop (Order)': 905
'Guard': 906
'Player Guard': 907
'Turret Guard': 908
'Bunker Guard': 909
'Ignore': 910
'Carrier Ignore': 911
'Carrier Stop': 912
'Reaver Stop': 913
'Attack (Order)': 914
'Attack Unit': 915
'Attack Fixed Range': 916
'Move Attack Unit': 917
'Attack Tile': 918
'Hover': 919
'Attack Move': 920
'Atk Move EP': 921
'Harass Move': 922
'AI Patrol': 923
'Tower': 924
'Vulture Mine': 925
'Carrier Attack': 926
'Carrier Attack Move': 927
'Stay In Range': 928
'Turret Attack': 929
'Nothing': 930
'Drone Start Build': 931
'Drone Build': 932
'Drone Attack Unit': 933
'Infest Mine': 934
'Build': 935
'Build Protoss': 936
'Pylon Build': 937
'Construct Building': 938
'Repair (Order)': 939
'Place Add-On': 940
'Build Add-On': 941
'Train': 942
'Zerg Birth': 943
'Morph': 944
'Zerg Building Morph': 945
'Build Self': 946
'Zerg Build Self': 947
'Enter Nydus Canal': 948
'Protoss Build Self': 949
'Follow': 950
'Carrier': 951
'Carrier Fight': 952
'Reaver': 953
'Reaver Attack': 954
'Reaver Fight': 955
'Reaver Hold': 956
'Train Fighter': 957
'Strafe Unit': 958
'Scarab (Order)': 959
'Return': 960
'Drone Land': 961
'Building Land': 962
'Building Lift Off': 963
'Drone Lift Off': 964
'Lift Off': 965
'Reasearch Tech': 966
'Upgrade': 967
'Larva': 968
'Spawning Larva': 969
'Harvest': 970
'Harvest Gas': 971
'Return Gas': 972
'Harvest Minerals': 973
'Return Minerals': 974
'Enter Transport (Order)': 975
'Pick Up': 976
'Powerup': 977
'Siege Mode (Order)': 978
'Tank Mode (Order)': 979
'Watch Target': 980
'Initing Creep Growth': 981
'Stopping Creep Growth': 982
'Spread Creep': 983
'Guardian Aspect (Order)': 984
'Warping Archon': 985
'Completing Archon Summon': 986
'Hold Position (Order)': 987
'Cloak (Order)': 988
'Decloak (Order)': 989
'Unload': 990
'Move Unload': 991
'Fire Yamato Gun': 992
'Magna Pulse': 993
'Burrow (Order)': 994
'Burrowed': 995
'Unburrow (Order)': 996
'Cast Parasite': 997
'Summon Broodlings': 998
'EMP Shockwave (Order)': 999
'Lockdown (Order)': 1000
'Nuke Wait': 1001
'Nuke Train': 1002
'Nuke Launch': 1003
'Nuke Paint': 1004
'Nuke Unit': 1005
'Nuke Ground': 1006
'Nuke Track': 1007
'Initializing Arbiter': 1008
'Cloaking nearby units': 1009
'Place Mine': 1010
'Right Click Action': 1011
'Left Click Action': 1012
'Sap Unit': 1013
'Sap Location': 1014
'Teleport': 1015
'Teleport to Location': 1016
'Place Scanner': 1017
'Scanner': 1018
'Defensive Matrix (Order)': 1019
'Reset Collision (1)': 1020
'Reset Collision (2)': 1021
'Patrol (Order)': 1022
'Computer AI': 1023
'Guard Post': 1024
'Rescue Passive': 1025
'Neutral': 1026
'Computer Return': 1027
'Initing Psi Provider': 1028
'Self Destructing': 1029
'Decaying creep': 1030
'Recharge Shields (Order)': 1031
'Shield Battery': 1032
'Rally Point': 1033
'CTF COP Init': 1034
'CTF COP': 1035
'Critter': 1036
'Hidden Gun': 1037
'Open Door': 1038
'Close Door': 1039
'Hide Trap': 1040
'Reveal Trap': 1041
'Enable Doodad': 1042
'Disable Doodad': 1043
'Warp In': 1044
'Hide and Suicide': 1045
'Fatal': 1046

# AI Scripts
'Nuclear launch detected.': 1047
'Terran Custom Level': 1048
'Terran Campaign Easy': 1049
'Terran Campaign Medium': 1050
'Terran Campaign Difficult': 1051
'Terran Campaign Area Town': 1052
'Terran 3 - Zerg Town': 1053
'Terran 5 - Terran Main Town': 1054
'Terran 5 - Terran Harvest Town': 1055
'Terran 6 - Air Attack Zerg': 1056
'Terran 6 - Ground Attack Zerg': 1057
'Terran 6 - Zerg Support Town': 1058
'Terran 7 - Bottom Zerg Town': 1059
'Terran 7 - Right Zerg Town': 1060
'Terran 7 - Middle Zerg Town': 1061
'Terran 8 - Confederate Town': 1062
'Terran 9 - Light Attack': 1063
'Terran 9 - Heavy Attack': 1064
'Terran 10 - Confederate Towns': 1065
'Terran 11 - Zerg Town': 1066
'Terran 11 - Lower Protoss Town': 1067
'Terran 11 - Upper Protoss Town': 1068
'Terran 12 - Nuke Town': 1069
'Terran 12 - Phoenix Town': 1070
'Terran 12 - Tank Town': 1071
'Protoss Custom Level': 1072
'Protoss Campaign Easy': 1073
'Protoss Campaign Medium': 1074
'Protoss Campaign Difficult': 1075
'Protoss Campaign Area Town': 1076
'Protoss 1 - Zerg Town': 1077
'Protoss 2 - Zerg Town': 1078
'Protoss 3 - Unused': 1079
'Protoss 3 - Air Zerg Town': 1080
'Protoss 3 - Ground Zerg Town': 1081
'Protoss 4 - Zerg Town': 1082
'Protoss 4 - Zerg Town (unused?)': 1083
'Protoss 5 - Zerg Town Island': 1084
'Protoss 5 - Zerg Town Base': 1085
'Protoss 6 - incomplete': 1086
'Protoss 7 - Left Protoss Town': 1087
'Protoss 7 - Right Protoss Town': 1088
'Protoss 7 - Shrine Protoss': 1089
'Protoss 8 - Left Protoss Town': 1090
'Protoss 8 - Right Protoss Town': 1091
'Protoss 8 - Protoss Defenders': 1092
'Protoss 9 - Ground Zerg': 1093
'Protoss 9 - Air Zerg': 1094
'Protoss 9 - Spell Zerg': 1095
'Protoss 10 - Mini-Towns': 1096
'Protoss 10 - Mini-Town Master': 1097
'Protoss 10 - Overmind Defenders': 1098
'Zerg Custom Level': 1099
'Zerg Campaign Easy': 1100
'Zerg Campaign Medium': 1101
'Zerg Campaign Difficult': 1102
'Zerg Campaign Area Town': 1103
'Zerg 1 - Terran Town': 1104
'Zerg 2 - Protoss Town': 1105
'Zerg 3 - Terran Town': 1106
'Zerg 4 - Right Terran Town': 1107
'Zerg 4 - Lower Terran Town': 1108
'Zerg 5 - incomplete': 1109
'Zerg 6 - Protoss Town': 1110
'Zerg 7 - Ground Town': 1111
'Zerg 7 - Air Town': 1112
'Zerg 7 - Support Town': 1113
'Zerg 8 - Scout Town': 1114
'Zerg 8 - Templar Town': 1115
'Zerg 9 - Teal Protoss': 1116
'Zerg 9 - Left Yellow Protoss': 1117
'Zerg 9 - Right Yellow Protoss': 1118
'Zerg 9 - Left Orange Protoss': 1119
'Zerg 9 - Right Orange Protoss': 1120
'Zerg 10 - Left Teal (Attack)': 1121
'Zerg 10 - Right Teal (Support)': 1122
'Zerg 10 - Left Yellow (Support)': 1123
'Zerg 10 - Right Yellow (Attack)': 1124
'Zerg 10 - Red Protoss': 1125
'Set a Default Staging Area': 1126
'Send All Units on Strategic Suicide Missions': 1127
'Send All Units on Random Suicide Missions': 1128
'Set Player to Enemy': 1129
'Set Player to Ally': 1130
'Move Dark Templars to Region': 1131
'Switch Computer Player to Rescue Passive': 1132
'Enter Closest Bunker': 1133
'Value This Area Higher': 1134
'Clear Previous Combat Data': 1135
'Debug Script 1 (general)': 1136
'Debug Script 2 (general)': 1137
'Debug Script 3 (general)': 1138
'Debug Script 4 (general)': 1139
'Debug Script 5 (general)': 1140
'Debug Script 1 (location)': 1141
'Debug Script 2 (location)': 1142
'Debug Script 3 (location)': 1143
'Debug Script 4 (location)': 1144
'Debug Script 5 (location)': 1145

# Doodads
'Structure': 1146
'Structure Wall': 1147
'Cliff (Badlands)': 1148
'High Dirt (Badlands)': 1149
'Grass (Badlands)': 1150
'High Grass (Badlands)': 1151
'Dirt (Badlands)': 1152
'Rocky Ground (Badlands)': 1153
'Asphalt': 1154
'Water (Badlands)': 1155
'Coastal Cliff': 1156
'Jungle': 1157
'High Jungle': 1158
'Ruins (Jungle)': 1159
'High Ruins': 1160
'Temple Wall': 1161
'High Temple Wall': 1162
'Dark Platform': 1163
'High Plating': 1164
'Plating (Space)': 1165
'Platform': 1166
'Platform Wall': 1167
'Low Platform': 1168
'Low Platform Wall': 1169
'Rusty Pit Wall': 1170
'Rusty Pit': 1171
'Solar Array': 1172
'Dirt (Ashworld)': 1173
'High Dirt (Ashworld)': 1174
'Shale': 1175
'Cliff (Ashworld)': 1176
'Floor': 1177
'Wall': 1178
'Substructure': 1179
'Substructure Wall': 1180
'Plating (Installation)': 1181
'Bridges (1)': 1182
'Bridges (2)': 1183
'Elevated Catwalk Ramps': 1184
'Bridges (3)': 1185
'Tar': 1186
'Tar Cliff': 1187
'Dirt (Desert)': 1188
'Dried Mud': 1189
'Sand Dunes': 1190
'Rocky Ground (Desert)': 1191
'Crags': 1192
'Sandy Sunken Pit': 1193
'Compound': 1194
'High Dirt (Desert)': 1195
'High Sand Dunes': 1196
'High Crags': 1197
'High Sandy Sunken Pit': 1198
'High Compound': 1199
'Water (Ice World)': 1200
'Snow': 1201
'Moguls': 1202
'Dirt (Ice World)': 1203
'Rocky Snow': 1204
'Grass (Ice World)': 1205
'Ice': 1206
'Outpost': 1207
'High Snow': 1208
'High Dirt (Ice World)': 1209
'High Grass (Ice World)': 1210
'High Ice': 1211
'High Outpost': 1212
'Water (Twilight)': 1213
'Dirt (Twilight)': 1214
'Mud': 1215
'Crushed Rock': 1216
'Crevices': 1217
'Flagstones': 1218
'Sunken Ground': 1219
'Basilica': 1220
'High Dirt (Twilight)': 1221
'High Crushed Rock': 1222
'High Flagstones': 1223
'High Sunken Ground': 1224
'High Basilica': 1225
'Terran Campaign Insane': 1226
'Protoss Campaign Insane': 1227
'Zerg Campaign Insane': 1228
'Terran 1 - Electronic Distribution': 1229
'Terran 2 - Electronic Distribution': 1230
'Terran 3 - Electronic Distribution': 1231
'Terran 1 - Shareware': 1232
'Terran 2 - Shareware': 1233
'Terran 3 - Shareware': 1234
'Terran 4 - Shareware': 1235
'Terran 5 - Shareware': 1236
'Halo Rockets': 1237
'Corrosive Acid': 1238
'Subterranean Spines': 1239
'Neutron Flare': 1240
'Mind Control (Weapon)': 1241
'Healing': 1242
'Restoration (Tech)': 1243
'Optical Flare (Tech)': 1244
'Research Restoration': 1245
'Research Optical Flare': 1246
'Heal': 1247
'Restoration (Cast)': 1248
'Optical Flare (Cast)': 1249
'Restoration:': 1250
'Restoration: Research at Academy': 1250
'Optical Flare:': 1251
'Optical Flare: Research at Academy': 1251
'Lurker Aspect': 1252
'Evolve Lurker Aspect': 1253
'Lurker Aspect: (Hydralisk Den)': 1254
'Lurker Aspect: Requires Lair': 1254
'Disruption Web (Tech)': 1255
'Mind Control (Tech)': 1256
'Dark Archon Meld (Tech)': 1257
'Feedback (Tech)': 1258
'Maelstrom (Tech)': 1259
'Develop Disruption We': 1260
'Develop Mind Control': 1261
'Develop Feedback': 1262
'Develop Maelstrom': 1263
'Dark Archon Meld (Cast)': 1264
'Disruption Web (Cast)': 1265
'Mind Control (Cast)': 1266
'Feedback (Cast)': 1267
'Maelstrom (Cast)': 1268
'Disruption Web:': 1269
'Disruption Web: Develop at Fleet Beacon': 1269
'Mind Control:': 1270
'Mind Control: Research at Templar Archives': 1270
'Dark Archon Meld:': 1271
'Dark Archon Meld: Research at Templar Archives': 1271
'Dark Archon Warp:': 1272
'Dark Archon Warp: Select 2 or more Dark Templars': 1272
'Feedback:': 1273
'Feedback: No requirement': 1273
'Maelstrom:': 1274
'Maelstrom: Develop at Templar Archives': 1274
'Caduceus Reactor': 1275
'Charon Booster': 1276
'Anabolic Synthesis': 1277
'Chitinous Plating': 1278
'Argus Jewel': 1279
'Argus Talisman': 1280
'Research Caduceus Reactor': 1281
'Research Charon Booster': 1282
'Evolve Anabolic Synthesis': 1283
'Evolve Chitinous Plating': 1284
'Develop Argus Jewel': 1285
'Develop Argus Talisman': 1286
'Research Charon Booster:': 1287
'Research Charon Booster: Requires Armory': 1287
'Devourer Aspect': 1288
'Morph to Lurker': 1289
'Train Medic': 1290
'Build Valkyrie': 1291
'Warp in Corsair': 1292
'Warp in Dark Templar': 1293
'Medic Requires:': 1294
'Medic Requires: Academy': 1294
'Valkyrie Requires:': 1295
'Valkyrie Requires: Attached Control Tower Armory': 1295
'Dark Templar Requires:': 1296
'Dark Templar Requires: Templar Archives': 1296
'Devourer Aspect Requires:': 1297
'Devourer Aspect Requires: Greater Spire': 1297
'Lurker Aspect: (Hydralisk)': 1298
'Lurker Aspect: Evolve at Hydralisk Den': 1298
'Blind': 1299
'Acid Spores': 1300
'per rocket': 1301
'Recruit (Rank)': 1302
'Private (Marine Rank)': 1303
'Private (SCV Rank)': 1304
'1st Lieutenant (Rank)': 1305
'Corporal (Rank)': 1306
'Specialist (Rank)': 1307
'Sergeant (Rank)': 1308
'First Sergeant (Goliath Rank)': 1309
'Master Sergeant (Rank)': 1310
'Warrant Officer (Rank)': 1311
'Captain (Rank)': 1312
'Major (Rank)': 1313
'First Sergeant (Gui Montag Rank)': 1314
'Sergeant Major (Rank)': 1315
'Colonel (Rank)': 1316
'Commodore (Rank)': 1317
'Lt Commander (Rank)': 1318
'Marshall (Rank)': 1319
'Lieutenant (Rank)': 1320
'General (Rank)': 1321
'Captain Raynor (Rank)': 1322
'General Duke (Rank)': 1323
'Admiral (Rank)': 1324
'Must target injured non-mechanical ground units': 1325
'Invalid target. (8)': 1326
'Must target enemy units': 1327
'Must target non-mechanical units.': 1328
'Unable to target structure. (2)': 1329
'Must target units with energy.': 1330
'Medic': 1331
'Medic Heal': 1332
'Restoration (Order)': 1333
'Cast Disruption We': 1334
'Mind Control (Order)': 1335
'Warping Dark Archon': 1336
'Cast Feedback': 1337
'Cast Optical Flare': 1338
'Cast Shockwave': 1339
'Heal Move': 1340
'Medic Hold Position': 1341
'Junk Yard Dog': 1342
'Terran Expansion Custom Level': 1343
'Protoss Expansion Custom Level': 1344
'Zerg Expansion Custom Level': 1345
'Brood Wars Protoss 1 - Town A': 1346
'Brood Wars Protoss 1 - Town ': 1347
'Brood Wars Protoss 1 - Town C': 1348
'Brood Wars Protoss 1 - Town D': 1349
'Brood Wars Protoss 1 - Town E': 1350
'Brood Wars Protoss 1 - Town F': 1351
'Brood Wars Protoss 2 - Town A': 1352
'Brood Wars Protoss 2 - Town ': 1353
'Brood Wars Protoss 2 - Town C': 1354
'Brood Wars Protoss 2 - Town D': 1355
'Brood Wars Protoss 2 - Town E': 1356
'Brood Wars Protoss 2 - Town F': 1357
'Brood Wars Protoss 3 - Town A': 1358
'Brood Wars Protoss 3 - Town ': 1359
'Brood Wars Protoss 3 - Town C': 1360
'Brood Wars Protoss 3 - Town D': 1361
'Brood Wars Protoss 3 - Town E': 1362
'Brood Wars Protoss 3 - Town F': 1363
'Brood Wars Protoss 4 - Town A': 1364
'Brood Wars Protoss 4 - Town ': 1365
'Brood Wars Protoss 4 - Town C': 1366
'Brood Wars Protoss 4 - Town D': 1367
'Brood Wars Protoss 4 - Town E': 1368
'Brood Wars Protoss 4 - Town F': 1369
'Brood Wars Protoss 5 - Town A': 1370
'Brood Wars Protoss 5 - Town ': 1371
'Brood Wars Protoss 5 - Town C': 1372
'Brood Wars Protoss 5 - Town D': 1373
'Brood Wars Protoss 5 - Town E': 1374
'Brood Wars Protoss 5 - Town F': 1375
'Brood Wars Protoss 6 - Town A': 1376
'Brood Wars Protoss 6 - Town ': 1377
'Brood Wars Protoss 6 - Town C': 1378
'Brood Wars Protoss 6 - Town D': 1379
'Brood Wars Protoss 6 - Town E': 1380
'Brood Wars Protoss 6 - Town F': 1381
'Brood Wars Protoss 7 - Town A': 1382
'Brood Wars Protoss 7 - Town ': 1383
'Brood Wars Protoss 7 - Town C': 1384
'Brood Wars Protoss 7 - Town D': 1385
'Brood Wars Protoss 7 - Town E': 1386
'Brood Wars Protoss 7 - Town F': 1387
'Brood Wars Protoss 8 - Town A': 1388
'Brood Wars Protoss 8 - Town ': 1389
'Brood Wars Protoss 8 - Town C': 1390
'Brood Wars Protoss 8 - Town D': 1391
'Brood Wars Protoss 8 - Town E': 1392
'Brood Wars Protoss 8 - Town F': 1393
'Brood Wars Terran 1 - Town A': 1394
'Brood Wars Terran 1 - Town ': 1395
'Brood Wars Terran 1 - Town C': 1396
'Brood Wars Terran 1 - Town D': 1397
'Brood Wars Terran 1 - Town E': 1398
'Brood Wars Terran 1 - Town F': 1399
'Brood Wars Terran 2 - Town A': 1400
'Brood Wars Terran 2 - Town ': 1401
'Brood Wars Terran 2 - Town C': 1402
'Brood Wars Terran 2 - Town D': 1403
'Brood Wars Terran 2 - Town E': 1404
'Brood Wars Terran 2 - Town F': 1405
'Brood Wars Terran 3 - Town A': 1406
'Brood Wars Terran 3 - Town ': 1407
'Brood Wars Terran 3 - Town C': 1408
'Brood Wars Terran 3 - Town D': 1409
'Brood Wars Terran 3 - Town E': 1410
'Brood Wars Terran 3 - Town F': 1411
'Brood Wars Terran 4 - Town A': 1412
'Brood Wars Terran 4 - Town ': 1413
'Brood Wars Terran 4 - Town C': 1414
'Brood Wars Terran 4 - Town D': 1415
'Brood Wars Terran 4 - Town E': 1416
'Brood Wars Terran 4 - Town F': 1417
'Brood Wars Terran 5 - Town A': 1418
'Brood Wars Terran 5 - Town ': 1419
'Brood Wars Terran 5 - Town C': 1420
'Brood Wars Terran 5 - Town D': 1421
'Brood Wars Terran 5 - Town E': 1422
'Brood Wars Terran 5 - Town F': 1423
'Brood Wars Terran 6 - Town A': 1424
'Brood Wars Terran 6 - Town ': 1425
'Brood Wars Terran 6 - Town C': 1426
'Brood Wars Terran 6 - Town D': 1427
'Brood Wars Terran 6 - Town E': 1428
'Brood Wars Terran 6 - Town F': 1429
'Brood Wars Terran 7 - Town A': 1430
'Brood Wars Terran 7 - Town ': 1431
'Brood Wars Terran 7 - Town C': 1432
'Brood Wars Terran 7 - Town D': 1433
'Brood Wars Terran 7 - Town E': 1434
'Brood Wars Terran 7 - Town F': 1435
'Brood Wars Terran 8 - Town A': 1436
'Brood Wars Terran 8 - Town ': 1437
'Brood Wars Terran 8 - Town C': 1438
'Brood Wars Terran 8 - Town D': 1439
'Brood Wars Terran 8 - Town E': 1440
'Brood Wars Terran 8 - Town F': 1441
'Brood Wars Zerg 1 - Town A': 1442
'Brood Wars Zerg 1 - Town ': 1443
'Brood Wars Zerg 1 - Town C': 1444
'Brood Wars Zerg 1 - Town D': 1445
'Brood Wars Zerg 1 - Town E': 1446
'Brood Wars Zerg 1 - Town F': 1447
'Brood Wars Zerg 2 - Town A': 1448
'Brood Wars Zerg 2 - Town ': 1449
'Brood Wars Zerg 2 - Town C': 1450
'Brood Wars Zerg 2 - Town D': 1451
'Brood Wars Zerg 2 - Town E': 1452
'Brood Wars Zerg 2 - Town F': 1453
'Brood Wars Zerg 3 - Town A': 1454
'Brood Wars Zerg 3 - Town ': 1455
'Brood Wars Zerg 3 - Town C': 1456
'Brood Wars Zerg 3 - Town D': 1457
'Brood Wars Zerg 3 - Town E': 1458
'Brood Wars Zerg 3 - Town F': 1459
'Brood Wars Zerg 4 - Town A': 1460
'Brood Wars Zerg 4 - Town ': 1461
'Brood Wars Zerg 4 - Town C': 1462
'Brood Wars Zerg 4 - Town D': 1463
'Brood Wars Zerg 4 - Town E': 1464
'Brood Wars Zerg 4 - Town F': 1465
'Brood Wars Zerg 5 - Town A': 1466
'Brood Wars Zerg 5 - Town ': 1467
'Brood Wars Zerg 5 - Town C': 1468
'Brood Wars Zerg 5 - Town D': 1469
'Brood Wars Zerg 5 - Town E': 1470
'Brood Wars Zerg 5 - Town F': 1471
'Brood Wars Zerg 6 - Town A': 1472
'Brood Wars Zerg 6 - Town ': 1473
'Brood Wars Zerg 6 - Town C': 1474
'Brood Wars Zerg 6 - Town D': 1475
'Brood Wars Zerg 6 - Town E': 1476
'Brood Wars Zerg 6 - Town F': 1477
'Brood Wars Zerg 7 - Town A': 1478
'Brood Wars Zerg 7 - Town ': 1479
'Brood Wars Zerg 7 - Town C': 1480
'Brood Wars Zerg 7 - Town D': 1481
'Brood Wars Zerg 7 - Town E': 1482
'Brood Wars Zerg 7 - Town F': 1483
'Brood Wars Zerg 8 - Town A': 1484
'Brood Wars Zerg 8 - Town ': 1485
'Brood Wars Zerg 8 - Town C': 1486
'Brood Wars Zerg 8 - Town D': 1487
'Brood Wars Zerg 8 - Town E': 1488
'Brood Wars Zerg 8 - Town F': 1489
'Brood Wars Zerg 9 - Town A': 1490
'Brood Wars Zerg 9 - Town ': 1491
'Brood Wars Zerg 9 - Town C': 1492
'Brood Wars Zerg 9 - Town D': 1493
'Brood Wars Zerg 9 - Town E': 1494
'Brood Wars Zerg 9 - Town F': 1495
'Brood Wars Zerg 10 - Town A': 1496
'Brood Wars Zerg 10 - Town ': 1497
'Brood Wars Zerg 10 - Town C': 1498
'Brood Wars Zerg 10 - Town D': 1499
'Brood Wars Zerg 10 - Town E': 1500
'Brood Wars Zerg 10 - Town F': 1501
'Expansion Zerg Campaign Easy': 1502
'Expansion Zerg Campaign Medium': 1503
'Expansion Zerg Campaign Difficult': 1504
'Expansion Zerg Campaign Area Town': 1505
'Expansion Protoss Campaign Easy': 1506
'Expansion Protoss Campaign Medium': 1507
'Expansion Protoss Campaign Difficult': 1508
'Expansion Protoss Campaign Area Town': 1509
'Expansion Terran Campaign Easy': 1510
'Expansion Terran Campaign Medium': 1511
'Expansion Terran Campaign Difficult': 1512
'Expansion Terran Campaign Area Town': 1513
'Expansion Terran Campaign Insane': 1514
'Expansion Protoss Campaign Insane': 1515
'Expansion Zerg Campaign Insane': 1516
'Set Generic Command Target': 1517
'Make These Units Patrol': 1518
'Enter Transport (AIScript)': 1519
'Exit Transport': 1520
'Turn ON Shared Vision for Player 1': 1521
'Turn ON Shared Vision for Player 2': 1522
'Turn ON Shared Vision for Player 3': 1523
'Turn ON Shared Vision for Player 4': 1524
'Turn ON Shared Vision for Player 5': 1525
'Turn ON Shared Vision for Player 6': 1526
'Turn ON Shared Vision for Player 7': 1527
'Turn ON Shared Vision for Player 8': 1528
'Turn OFF Shared Vision for Player 1': 1529
'Turn OFF Shared Vision for Player 2': 1530
'Turn OFF Shared Vision for Player 3': 1531
'Turn OFF Shared Vision for Player 4': 1532
'Turn OFF Shared Vision for Player 5': 1533
'Turn OFF Shared Vision for Player 6': 1534
'Turn OFF Shared Vision for Player 7': 1535
'Turn OFF Shared Vision for Player 8': 1536
'AI Nuke Here': 1537
'AI Harass Here': 1538
'Set Unit Order To: Junk Yard Dog': 1539
'View Players': 1540
'Speed Up': 1541
'Play': 1542
'Pause': 1543
'Slow Down': 1544
'Replay Progress': 1545
'Paused': 1546
'Unlimited': 1547
```

  


