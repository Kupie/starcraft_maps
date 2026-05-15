; add_hyper_trigger.ahk
; Automates adding the hyper trigger to the currently focused SCMDraft map.
; 
; SETUP:
;   1. Copy the hyper trigger text to clipboard before running:
;      Trigger("All players"){Conditions:    Deaths("All players", "Cave", Exactly, 0);Actions:    Set Deaths("Current Player", "Cave", Set To, 1);    Wait(0);    Set Deaths("Current Player", "Cave", Set To, 0);    Wait(0);    Preserve Trigger();}
;   2. Make sure the SCMDraft map window is focused.
;   3. Press F5 to run the sequence for the current map.
;   4. Repeat for each map.
;
; Press Escape to abort mid-sequence.

#NoEnv
#SingleInstance Force
SetWorkingDir %A_ScriptDir%
SendMode Input

; Delay between keystrokes in ms - increase if SCMDraft misses inputs
KeyDelay := 80

; --- Hotkey: F5 runs the sequence on the focused map ---
F5::
	SetKeyDelay, %KeyDelay%

	; Open trigger editor
	Send ^+t
	Sleep, 500

	; Navigate player checkboxes - tab to first, check All Players
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Space}				; uncheck Player 1 (or whatever is default)
	Sleep, %KeyDelay%
	Send {Down}
	Sleep, %KeyDelay%
	Send {Space}				; navigate/check All Players
	Sleep, %KeyDelay%

	; Tab to conditions area
	Send {Tab}
	Sleep, %KeyDelay%

	; Move right x5 to reach the correct field
	Send {Right}
	Sleep, %KeyDelay%
	Send {Right}
	Sleep, %KeyDelay%
	Send {Right}
	Sleep, %KeyDelay%
	Send {Right}
	Sleep, %KeyDelay%
	Send {Right}
	Sleep, %KeyDelay%

	; Tab to text input, paste trigger text
	Send {Tab}
	Sleep, %KeyDelay%
	Send ^a
	Sleep, %KeyDelay%
	Send ^v
	Sleep, 200

	; Tab through remaining fields
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Space}
	Sleep, %KeyDelay%
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Space}
	Sleep, %KeyDelay%
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Tab}
	Sleep, %KeyDelay%
	Send {Space}
	Sleep, %KeyDelay%

	; Save
	Send ^s
	Sleep, 500

	; Close the map window (X button at 1903, 45)
	Click, 1903, 45
	Sleep, 300

	return

; --- Escape aborts ---
Escape::
	MsgBox, Aborted.
	return
