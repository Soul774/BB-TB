$~e::
    WinGetPos, , , WinWidth, WinHeight, A
    Fov := 120

    ; Calculate the middle of the window
    MidX := WinWidth / 2
    MidY := WinHeight / 2

    ; Calculate the offsets based on FOV
    OffsetX := FOV / 2
    OffsetY := FOV / 2

    ; Calculate the square coordinates
    TopLeftX := MidX - OffsetX +20
    TopLeftY := MidY - OffsetY + 10
    BottomRightX := MidX + OffsetX - 20
    BottomRightY := MidY + OffsetY + 10
    ; 0x63DC89
    While GetKeyState("e", "P") {

        ;ToolTip, x, %TopLeftX%, %TopLeftY%, 1
        ;ToolTip, x, %BottomRightX%, %BottomRightY%, 2
        PixelSearch,,, TopLeftX, TopLeftY, BottomRightX, BottomRightY, 0x63DC89 ,15, Fast
        If (ErrorLevel = 0) {
            click
            Sleep 400
        }
        ;Tooltip, % A_Index,,,3
    }
    ;ToolTip,,,,3
    ;ToolTip,,,,1
    ;ToolTip,,,,2
Return

~f2::ExitApp

#IF