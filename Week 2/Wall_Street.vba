Sub GetVolume()
    ' define variables
    Dim vol_range As Range
    Dim ticker_range As Range
    Dim volume(1 To 288) As Variant

    ' set variables
    Set vol_range = Range("G2:G70926")
    Set ticker_range = Range("I2:I290")

    ' fill array for total ticker volumes
    For i = 2 To ticker_range.Rows.Count - 2
        For j = 2 To vol_range.Rows.Count - 2
            If Cells(i, 9).Value = Cells(j, 1).Value Then
                volume(i) = volume(i) + Cells(j, 7).Value
            End If
        Next j
    Next i

    ' print volume totals
    For i = 2 To ticker_range.Rows.Count - 2
        Cells(i, 10).Value = volume(i)
    Next i
End Sub
