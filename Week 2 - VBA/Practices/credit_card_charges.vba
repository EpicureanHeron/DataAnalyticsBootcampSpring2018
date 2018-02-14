Sub SummarizeCards()
    Dim total As Double
    Dim currentrow As Integer
    Dim cardrow As Integer

    currentrow = 2
    total = 0
    cardrow = 2

    For i = 0 To 100
        ' add to total
        total = total + Cells(currentrow, 3).Value
        
        ' if card changes next interation
        If Cells(currentrow, 1).Value <> Cells(currentrow + 1, 1).Value Then
            ' let me know the card changes
            MsgBox ("Card has changed from " + Cells(currentrow, 1).Value + " to " + Cells(currentrow + 1, 1).Value)
            ' fill in the card name
            Cells(cardrow, 7).Value = Cells(currentrow, 1).Value
            ' fill in the card total
            Cells(cardrow, 8).Value = total
            ' increment the cardrow
            cardrow = cardrow + 1
            ' reset the total
            total = 0
        End If
        ' increment the row
        currentrow = currentrow + 1
    Next i

End Sub
