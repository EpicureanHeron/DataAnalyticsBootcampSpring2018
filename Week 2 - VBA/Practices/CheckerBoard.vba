Sub CreateBoard()

    For i = 1 To 8
        For j = 1 To 8
            If i Mod 2 = 0 Then
                If j Mod 2 = 0 Then
                    Cells(i, j).Interior.ColorIndex = 3
                Else
                    Cells(i, j).Interior.ColorIndex = 1
                End If
            Else
                If j Mod 2 = 0 Then
                    Cells(i, j).Interior.ColorIndex = 1
                Else
                    Cells(i, j).Interior.ColorIndex = 3
                End If
            End If
            Cells(i, j).ColumnWidth = 10
            Cells(i, j).RowHeight = 50
        Next j
    Next i

End Sub
