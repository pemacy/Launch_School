require 'spreadsheet'

# book = Spreadsheet::Workbook.new
# sheet1 = book.create_worksheet name: "First_Worksheet"
# sheet1.row(0).concat %w{Name Country Acknowlegement}
my_path = Dir.pwd
# book.write my_path + '/excel-file.xls'

file = my_path + '/pricing.xls'
book2 = Spreadsheet.open(file)
sheet2 = book2.worksheet 0
sheet2.row(1)[12] = 'red'
r = sheet2.row(1)
p r[12]
book2.write my_path + '/pricing.xls'
