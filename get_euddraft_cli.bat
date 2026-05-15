@echo off
:loop
for /f "delims=" %%a in ('powershell -command "Get-WmiObject Win32_Process -Filter 'name=\"euddraft.exe\"' | Select-Object -ExpandProperty CommandLine" 2^>nul') do (
	echo Found: %%a
	pause
	exit /b
)
goto loop