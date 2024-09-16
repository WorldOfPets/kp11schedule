Sub ПоискНакладок()
    Dim objShell As Object
    Dim PythonExe As String, PythonScript As String, filePath As String
    Dim wb As Excel.Workbook
    Dim xlApp As Excel.Application
    
    Set wb = ThisWorkbook
    Set xlApp = New Excel.Application
    Set objShell = VBA.CreateObject("Wscript.Shell")

    PythonExe = """C:\Users\Evgen\AppData\Local\Programs\Python\Python311\python.exe"""
    PythonScript = "C:\Users\Evgen\Work\programs\kp11dev\mainCheckNacladka.py"
    filePath = ThisWorkbook.Path & "\" & ThisWorkbook.Name

    ThisWorkbook.Save
    objShell.Run PythonExe & " " & PythonScript & " " & filePath
    Application.OnTime Now + TimeValue("00:00:05"), "ReOpen"
    ThisWorkbook.Close (False)
    
End Sub

Sub ПоискКабинета()
    Dim objShell As Object
    Dim PythonExe As String, PythonScript As String, filePath As String
    Dim wb As Excel.Workbook
    Dim xlApp As Excel.Application
    Dim row As Long
    row = ActiveCell.row
    
    Set wb = ThisWorkbook
    Set xlApp = New Excel.Application
    Set objShell = VBA.CreateObject("Wscript.Shell")

    PythonExe = """C:\Users\Evgen\AppData\Local\Programs\Python\Python311\python.exe"""
    PythonScript = "C:\Users\Evgen\Work\programs\kp11dev\mainFindCabinet.py"
    filePath = ThisWorkbook.Path & "\" & ThisWorkbook.Name
    
    ThisWorkbook.Save
    objShell.Run PythonExe & " " & PythonScript & " " & filePath & " " & row
    Application.OnTime Now + TimeValue("00:00:05"), "ReOpen"
    ThisWorkbook.Close (False)
    
End Sub

Sub ПоискОшибок()
    Dim objShell As Object
    Dim PythonExe As String, PythonScript As String, filePath As String
    
    Set objShell = VBA.CreateObject("Wscript.Shell")

    PythonExe = """C:\Python312\python.exe"""
    PythonScript = "C:\Users\Admin\Desktop\testPYVBA\checkError.py"
    filePath = ThisWorkbook.Path & "\" & ThisWorkbook.Name
    
    ThisWorkbook.Save
    objShell.Run "cmd /K " & PythonExe & " " & PythonScript & " " & filePath
    Application.OnTime Now + TimeValue("00:00:07"), "ReOpen"
    ThisWorkbook.Close (False)
    
End Sub

Private Sub ReOpen()
    Application.Workbooks.Open (ThisWorkbook.FullName)
End Sub

