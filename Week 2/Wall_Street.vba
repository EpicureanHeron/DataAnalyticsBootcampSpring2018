Sub GetVolume()

    Dim total As Double
    Dim currentrow As Long
    Dim tickerrow As Long

    currentrow = 2
    total = 0
    tickerrow = 2

    For i = 0 To 70926
        ' add to total
        total = total + Cells(currentrow, 7).Value

        ' if the ticker changes
        If Cells(currentrow, 1).Value <> Cells(currentrow + 1, 1).Value Then
            ' fill in the ticker name
            Cells(tickerrow, 9).Value = Cells(currentrow, 1).Value
            ' fill in the ticker total
            Cells(tickerrow, 10).Value = total
            ' increment the tickerrow
            tickerrow = tickerrow + 1
            ' reset the total
            total = 0
        End If
        ' increment the row
        currentrow = currentrow + 1
    Next i

End Sub
