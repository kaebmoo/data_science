if WScript.Arguments.Count < 3 Then
    WScript.Echo "Please specify the source and the destination files. Usage: ExcelToCsv <xls/xlsx source file> <csv destination file> <worksheet number (starts at 1)>"
    Wscript.Quit
End If

csv_format = 6

Set objFSO = CreateObject("Scripting.FileSystemObject")

src_file = objFSO.GetAbsolutePathName(Wscript.Arguments.Item(0))
dest_file = objFSO.GetAbsolutePathName(WScript.Arguments.Item(1))
worksheet_number = CInt(WScript.Arguments.Item(2))

Dim oExcel
Set oExcel = CreateObject("Excel.Application")

Dim oBook
Set oBook = oExcel.Workbooks.Open(src_file)
oBook.Worksheets(worksheet_number).Activate

oBook.SaveAs dest_file, csv_format

oBook.Close False
oExcel.Quit

' https://stackoverflow.com/questions/28766133/faster-way-to-read-excel-files-to-pandas-dataframe
' # create a list with sheet numbers you want to process
' sheets = map(str,range(1,6))

' # convert each sheet to csv and then read it using read_csv
' df={}
' from subprocess import call
' excel='C:\\Users\\rsignell\\OTT_Data_All_stations.xlsx'
' for sheet in sheets:
'    csv = 'C:\\Users\\rsignell\\test' + sheet + '.csv' 
'    call(['cscript.exe', 'C:\\Users\\rsignell\\ExcelToCsv.vbs', excel, csv, sheet])
'    df[sheet]=pd.read_csv(csv)