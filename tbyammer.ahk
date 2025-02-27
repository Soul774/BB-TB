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

    ; 0x63DC89 ( COLOR )
    While GetKeyState("e", "P") {
        PixelSearch,,, TopLeftX, TopLeftY, BottomRightX, BottomRightY, 0x63DC89 ,15, Fast
        If (ErrorLevel = 0) {
            click
            Sleep 400
        }
    }

Return

~f2::ExitApp

#IF
