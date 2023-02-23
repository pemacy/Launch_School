require "sinatra"
require "sinatra/reloader" if development?
# require 'tilt/erubis'

before do
  toc = File.expand_path('../data/toc.txt', __FILE__)
  @contents = File.readlines(toc)
end

helpers do
  def in_paragraphs(text)
    text.split("\n\n").map.with_index do |line, paragraph|
      "<p id=#{paragraph}>#{line}</p>"
    end
  end

  def search_word(str)
    @contents.select { |item| item.downcase.include?(str.downcase)}
  end

  def adv_search(str)
    stored_search = stored_paragraph = Hash.new({})
    @contents.each_with_index do |content, idx|
      chapter_file = File.expand_path("../data/chp#{idx + 1}.txt", __FILE__)
      chapter = in_paragraphs(File.read(chapter_file))
      stored_search[content] = chapter.each_with_index.with_object({}) do |(item,i), hsh|
        hsh[i] = item if item.downcase.include?(str.downcase)
      end
    end
    stored_search
  end

  def highlight_terms(sentence, query)
    sentence.gsub(/(#{query})/,'<strong>\1</strong>')
  end
end

get "/" do
  @title = "The Adventures of Sherlock Holmes"
  erb :home
end

get "/chapter/:num" do |num|
  chapter_file = File.expand_path("../data/chp#{num}.txt", __FILE__)

  @title = "Chapter #{num}"
  @chapter = in_paragraphs(File.read(chapter_file)).join

  erb :chapter
end

get "/search" do
  @query = params['query'] || ""
  @results = @query.empty? ? [] : search_word(@query)
  p "THESE ARE THE RESULTS: ", @results
  erb :search
end

get "/advanced_search" do
  @query = params['query'] || ""
  @results = @query.empty? ? [] : adv_search(@query)
  # p "----- IN THE HASH: ", @results
  erb :advanced_search
end

not_found do
  redirect '/'
end
