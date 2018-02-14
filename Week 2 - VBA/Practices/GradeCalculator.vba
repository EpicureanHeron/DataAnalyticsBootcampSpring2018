Sub GetGrade()
    Dim grade As Integer
    Dim pass As Integer
    Dim warning As Integer
    Dim fail As Integer

    ' grab grade score
    grade = Range("B2").Value

    ' check grade and set values
    If grade >= 90 Then
        Range("C2").Value = "Pass"
        Range("C2").Interior.ColorIndex = 4
        Range("D2").Value = "A"
    ElseIf grade >= 80 And grade < 90 Then
        Range("C2").Value = "Pass"
        Range("C2").Interior.ColorIndex = 4
        Range("D2").Value = "B"
    ElseIf grade >= 70 And grade < 80 Then
        Range("C2").Value = "Warning"
        Range("C2").Interior.ColorIndex = 6
        Range("D2").Value = "C"
    ElseIf grade < 70 Then
        Range("C2").Value = "Fail"
        Range("C2").Interior.ColorIndex = 3
        Range("D2").Value = "F"
    End If


End Sub
Sub ResetGrade()
    Dim previous_grade As Integer
    Dim previous_letter As String
    Dim previous_status As String

    ' grab previous results
    previous_grade = Range("B2").Value
    previous_status = Range("C2").Value
    previous_letter = Range("D2").Value

    ' set previous results
    Range("A12").EntireRow.Insert
    Range("A12").Value = previous_grade
    Range("B12").Value = previous_status
    Range("C12").Value = previous_letter

    ' reset cells to blank
    Range("B2").Value = ""
    Range("C2").Value = ""
    Range("D2").Value = ""
    Range("C2").Interior.ColorIndex = 0

    ' grab grade value
    grade = Range("A12").Value

    ' check grade results and set colors
    If grade >= 90 Then
        Range("B12").Interior.ColorIndex = 4
    ElseIf grade >= 80 And grade < 90 Then
        Range("B12").Interior.ColorIndex = 4
    ElseIf grade >= 70 And grade < 80 Then
        Range("B12").Interior.ColorIndex = 6
    ElseIf grade < 70 Then
        Range("B12").Interior.ColorIndex = 3
    End If

End Sub
