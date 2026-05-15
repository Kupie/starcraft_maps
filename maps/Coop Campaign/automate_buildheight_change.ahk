#Requires AutoHotkey v2.0

CoordMode "Mouse", "Screen"
SendMode "Event"

running := false

F6:: {
	global running
	running := !running
	if running
		SetTimer DoLoop, 0
	else
		SetTimer DoLoop, 0
}

DoLoop() {
	global running
	if !running
		return
	Click 420, 790
	Sleep 150
	Click 1052, 755
	Sleep 150
	Send "^v"
	Sleep 150
	Click 576, 810
	Sleep 150
}