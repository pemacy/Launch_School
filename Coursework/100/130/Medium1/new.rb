require 'spreadsheet'
require 'minitest/autorun'

puts $LOADED_FEATURES.select{|e| e[/minitest.rb/] == 'minitest.rb' }

dir = Dir.pwd

p dir.class

book = Spreadsheet.open('test.xls')


class CompareFiles
  def process
    @d = Dir.pwd
    @files = Dir.entries(@d)
    @txt = @files.select { |f| f.end_with?('.txt')}
    @file = File.open(@txt.first, "r")
    @lines = @file.readlines.each_with_index do |line, num|
      puts "#{num}: #{line}" if num < 10
    end
    nil
  end
end

analyzer = CompareFiles.new
p analyzer.process

def block_test(&block)
  p block.object_id
end

block_test

def meth(&block)
  p block.class
end

meth{|n|}
meth{|n, k|}
meth{|n, k, l|}
