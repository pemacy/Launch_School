require 'sinatra'
require 'sinatra/reloader'
require 'tilt/erubis'

configure do
	set :info_msg, {}
	set :signed_in_status, false
end

def root
	File.expand_path('..', __FILE__)
end

def file_path(file)
	root + '/data/' +  file
end

def data_path
	root + '/data'
end

def files_array
	Dir.glob(file_path('*')).map { |file| File.basename(file) }
end

def contents_whole(file)
	File.read(file_path(file))
end

def contents_by_line(file)
	File.readlines(file_path(file))
end

def is_file?(file)
	files_array.include? file
end

get '/' do
	if settings.signed_in_status
		@files = files_array
		settings.info_msg[:msg] = 'Made it!'
		erb :home, layout: :layout
	else
		settings.info_msg[:msg] = 'Please sign in'
		redirect '/sign_in'
	end
end

get '/sign_in' do
	@user = settings.info_msg.delete :user
	@pw = settings.info_msg.delete :pw
	erb :sign_in
end

post '/sign_in' do
	user = params[:username]
	pw = params[:password]
	if user == 'admin' && pw == 'secret'
		settings.info_msg[:msg] = 'Welcome'
		response.status = 302
		settings.signed_in_status = true
		redirect '/'
	else
		settings.info_msg[:msg] = 'Invalid Credentials'
		settings.info_msg[:user] = user
		settings.info_msg[:pw] = pw
		redirect '/sign_in'
	end
end

post '/signout' do
	settings.signed_in_status = false
	settings.info_msg[:msg] = 'You have been signed out'
	redirect '/sign_in'
end

get '/new' do
	@value = settings.info_msg.delete(:value)
	erb :new
end

post '/new' do
	if params[:new_doc].empty?
		settings.info_msg[:msg] = 'A name is required'
		redirect '/new'
	elsif File.extname(params[:new_doc]).empty?
		settings.info_msg[:value] = params[:new_doc]
		settings.info_msg[:msg] = 'Name must have an extensinon on it'
		redirect '/new'
	else
		File.new(File.join(data_path, params[:new_doc]), 'w')
		settings.info_msg[:msg] = "'#{params[:new_doc]}' has been created"
		redirect '/'
	end
end

get '/:file' do
	@file = params[:file]
	if is_file?(@file)
		@contents = contents_by_line(@file)
		erb :show_file, layout: :layout
	else
		settings.info_msg[:msg] = "'#{@file}' does not exist."
		redirect '/'
	end
end

get '/:file/edit' do
	@file = params[:file]
	@content = contents_whole(@file)
	erb :edit, layout: :layout
end

post '/:file/edit' do
	File.open(File.join(data_path, params[:file]), 'w') { |f| f.puts params[:new_content] }
	settings.info_msg[:msg] = "'#{params[:file]}' has been updated"
	redirect "/"
end

post '/:file/delete' do
	File.delete(File.join(data_path, params[:file]))
	settings.info_msg[:msg] = "'#{params[:file]}' has been deleted"
	redirect '/'
end	

get '/*' do
	redirect '/'
end
