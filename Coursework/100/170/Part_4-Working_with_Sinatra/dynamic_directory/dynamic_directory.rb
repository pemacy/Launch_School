require 'sinatra'
require 'sinatra/reloader'

get "/" do
  erb :home
end

get "/descending" do
  erb :reversed
end

get "/file/:num" do |num|
  @title = "File #{num}"
  file = "public/file" + num.to_s + ".txt"
  @contents = File.read(file)
  erb :file_viewer
end
