from subprocess import call

file = "D:\\DW\\ลูกหนี้คงเหลือ\\non2021\\202101 nondw.xlsx"
csv = "D:\\DW\\ลูกหนี้คงเหลือ\\non2021\\202101 nondw.csv"
sheet = "1"
call(['cscript.exe', 'C:\\Users\\CAT\\Documents\\GitHub\\bot_nt\\ExcelToCsv.vbs', file, csv, sheet])
