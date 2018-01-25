Sub GetVolume()

    Dim total As Double
    Dim currentrow As Long
    Dim tickerrow As Long
    Dim LastRow As Double

    For Each ws In Worksheets
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

            currentrow = 2
            total = 0
            tickerrow = 2

        For i = 0 To LastRow

            ' add to total
            total = total + ws.Cells(currentrow, 7).Value

            ' if the ticker changes
            If ws.Cells(currentrow, 1).Value <> ws.Cells(currentrow + 1, 1).Value Then
                ' fill in the ticker name
                ws.Cells(tickerrow, 9).Value = ws.Cells(currentrow, 1).Value
                ' fill in the ticker total
                ws.Cells(tickerrow, 10).Value = total
                ' increment the tickerrow
                tickerrow = tickerrow + 1
                ' reset the total
                total = 0
            End If
            ' increment the row
            currentrow = currentrow + 1
        Next i
    Next
End Sub
