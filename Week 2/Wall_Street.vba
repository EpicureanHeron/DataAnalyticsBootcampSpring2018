Sub GetVolume()

    Dim total As Double
    Dim currentrow As Long
    Dim tickerrow As Long
    Dim LastRow As Double
    Dim YearOpen As Double
    Dim YearClose As Double
    Dim PercentChange As Double
    Dim PercentMax As Double
    Dim PercentMin As Double
    Dim MaxVolume As Double
    Dim MaxPercentTicker As String
    Dim MinPercentTicker As String
    Dim MaxTicker As String

    For Each ws In Worksheets
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

            currentrow = 2
            total = 0
            tickerrow = 2
            MaxVolume = 0
            MaxPercentTicker = 0
            MinPercentTicker = 0
            MaxVolume = 0
            PercentMax = 0
            PercentMin = 0
        ' get the year's opening price
        YearOpen = ws.Cells(currentrow, 3).Value

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
                ' get year's closing volume
                YearClose = ws.Cells(currentrow, 6).Value
                ' calculate % change
                If YearOpen = 0 Then
                    PercentChange = (YearClose - YearOpen) / 1
                Else
                    PercentChange = (YearClose - YearOpen) / YearOpen
                End If
                ' calculate the difference
                Change = YearClose - YearOpen
                ' fill in the % change
                ws.Cells(tickerrow - 1, 11).Value = PercentChange
                ' fill in change
                ws.Cells(tickerrow - 1, 12).Value = Change
                ' get next ticker's year open
                YearOpen = ws.Cells(currentrow + 1, 3).Value
            End If
            ' increment the row
            currentrow = currentrow + 1
        Next i

        For j = 2 To LastRow
            If ws.Cells(j, 11).Value > PercentMax Then
                PercentMax = ws.Cells(j, 11).Value
                MaxPercentTicker = ws.Cells(j, 9).Value
            ElseIf ws.Cells(j, 11).Value < PercentMin Then
                PercentMin = ws.Cells(j, 11).Value
                MinPercentTicker = ws.Cells(j, 9).Value
            ElseIf ws.Cells(j, 10).Value > MaxVolume Then
                MaxVolume = ws.Cells(j, 10).Value
                MaxTicker = ws.Cells(j, 9).Value
            End If
        Next j

        ws.Cells(2, 15).Value = MaxPercentTicker
        ws.Cells(2, 16).Value = PercentMax
        ws.Cells(3, 15).Value = MinPercentTicker
        ws.Cells(3, 16).Value = PercentMin
        ws.Cells(4, 15).Value = MaxTicker
        ws.Cells(4, 16).Value = MaxVolume

    Next
End Sub
