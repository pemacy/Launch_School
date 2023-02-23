# cms_test.rb

ENV["RACK_ENV"] = 'test' 	# this variable is used by various parts of Sinatra
													# and Rack to know if the code is being tested and
													# in the case of Sinatra, to determine wheter it will 
													# start a web server or not (we don't want it to if we're
													# running tests)

# libraries used for testings
require 'minitest/autorun'
require 'rack/test'
require 'fileutils'

# Sinatra application
require_relative '../cms'

# class needs to subclass from Minitest::Test
class CMSTest < Minitest::Test
	# by mixing in Rack::Test::Methods, we gain access to a lot of useful test methods
	include Rack::Test::Methods 	

	# these methods expect a method called 'app' to exist and return an instance of
	# a Rack application when called
	def app
		Sinatra::Application
	end

	def setup
		FileUtils.mkdir_p(data_path)
	end

	def teardown
		FileUtils.rm_rf(data_path)
	end

	def create_file(name, contents='')
		File.open(File.join(data_path, name), 'w') do |file|
			file.write(contents)
		end
	end

	def sign_in
		post 'sign_in', username: 'admin', password: 'secret'
		get last_response['Location']
	end

	# General approach to testing:
	# 1. Make a request to your application using 'get', 'post', or other HTTP-method
	# 		named methods
	# 2. Access the response.  The response to your request will be accessible using
	# 		'last_response'.  This method will return an instance of Rack::MockResponse.
	# 		Instances of this class provide 'status', 'body', and '[]' methods for 
	# 		accessing their status code, body, and headers respectively.		
	# 3. Make assertions agains values in the response.  Use the standard assertions
	# 		found in Minitest.

	# methods should begin with 'test_'
	def test_index
		skip
		create_file 'changes.txt'
		create_file 'about.md'

		get '/'

		assert_equal 200, last_response.status	
		assert_includes last_response.body, 'changes.txt'
		assert_includes last_response.body, 'about.md'
	end

	def test_test_doc_link
		skip
		create_file 'test.txt', 'Sample test input'

		get '/test.txt'

		assert_equal 200, last_response.status
		assert_includes last_response.body, 'Sample test input'
	end

	def test_file_does_not_exist
		skip
		get '/non_existant.txt'

		assert_equal last_response.status, 302

		get last_response["Location"]
		
		assert_equal last_response.status, 200
		assert_includes last_response.body, "'non_existant.txt' does not exist."
	end

	def test_edit_page
		skip
		create_file 'test.txt'

		get '/test.txt/edit'

		assert_equal last_response.status, 200
		assert_includes last_response.body, 'Edit content of test.txt'
	end

	def test_updating_file
		skip
		settings.sign_in_status = true
		create_file 'test.txt'

		post '/test.txt/edit', new_content: "test suit: new content"

		assert_equal last_response.status, 302

		get last_response["Location"]

		assert_equal last_response.status, 200
		assert_includes last_response.body, "'test.txt' has been updated"

		get '/test.txt'

		assert_includes last_response.body, 'test suit: new content'
		settings.sign_in_status = false
	end

	def test_bad_username
		post '/sign_in', username: '', password: ''

		assert_equal last_response.status, 302
		
		get last_response['Location']

		assert_includes last_response.body, 'Invalid Credentials'
	end

	def test_correct_username_and_password
		sign_in
		assert_includes last_response.body, 'Welcome'
	end
	
	def test_signout
		sign_in

		post '/signout'
		get last_response['Location']
		assert_includes last_response.body, 'You have been signed out'
	end

end
