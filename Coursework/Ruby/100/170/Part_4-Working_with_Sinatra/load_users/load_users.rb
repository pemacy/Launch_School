# load_users.rb

require 'sinatra'
require 'sinatra/reloader'
require 'yaml'
require 'psych'

configure do
  set :port, 3000
end

before do
  @users = Psych.load_file('public/users.yaml')
end

helpers do
  def count_interests
    @users.map { |k,v| @users[k][:interests]}.flatten.count
  end
end

get '/' do
  redirect '/users'
end

get '/users' do
  @title = 'Home'
  erb :home
end

get '/:user' do |user|
  p '=' * 45
  @current_user = @title = user.to_sym
  p @current_user
  erb :user_page
end
