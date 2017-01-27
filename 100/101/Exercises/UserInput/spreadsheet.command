#!/usr/bin/env ruby
require 'spreadsheet'

puts "Running"

book = Spreadsheet::Workbook.new
sheet = book.create_worksheet
5.times {|j| 5.times {|i| sheet[j,i] = (i+1)*10**j}}
book.write 'out.xls'

puts "ran"
