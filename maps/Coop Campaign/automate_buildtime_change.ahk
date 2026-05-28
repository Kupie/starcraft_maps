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
	; Click unit/left box
	Click 444, 117
	Sleep 75
	; Click text box and paste
	Click 1564, 425
	Sleep 75
	Send "^v"
	; Click down arrow on left box
	Sleep 75
	Click 559, 803
	Sleep 0
}