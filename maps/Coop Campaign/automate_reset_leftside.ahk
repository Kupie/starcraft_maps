#Requires AutoHotkey v2.0

CoordMode "Mouse", "Screen"
SendMode "Event"

running := false

F6:: {
	global running
	running := !running
	if running
		SetTimer DoLoop, 75
	else
		SetTimer DoLoop, 0
}

DoLoop() {
	global running
	if !running
		return
	; RClick unit/left box
	Click 351, 116, "Right"
	Sleep 75
	; Click reset
	Click 541, 249
	; Click down arrow on left box
	Sleep 75
	Click 559, 803
	Sleep 0
}