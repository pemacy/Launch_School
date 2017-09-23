require 'socket'

server = TCPServer.open('localhost', 3000)

loop do
	client = server.accept

	request_line = client.gets
	next if !request_line || request_line =~ /favicon/

	# Response Header
	client.puts 'HTTP/1.0 200 OK'
	client.puts 'Content-Type: text/html'
	client.puts

	# Response Body
	queries = request_line.split('?').last
	statements = queries.split('&')
	parameters = statements.each_with_object({}) do |statement, hsh|
		parameter, value = statement.split('=')
		hsh[parameter] = value.to_i
	end

	client.puts "<html>\n<body>\n<h1>Hello</h1></body></html>"
	client.puts "rolls: #{parameters['rolls']}, sides: #{parameters['sides']}"

	if parameters['rolls'] && parameters['sides']
		parameters['rolls'].times do |n|
			client.print "<h3>Roll #{n+1}:  #{rand(parameters['sides']) + 1}</h3>"
		end
	end

	puts request_line
	client.puts $_
	
	client.puts "</body></html>"

	client.close
end
