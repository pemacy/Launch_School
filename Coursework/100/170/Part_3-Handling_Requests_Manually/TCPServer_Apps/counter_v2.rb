# counter_v2.rb
# another go at the counter program to refresh the skills

require 'socket'

server = TCPServer.new 'localhost', 3001

loop do
	session = server.accept
	session.puts "HTTP/1.1/ 200 OK"
	session.puts "Content-Type: text/html"
	session.puts

	queries = session.gets.split('?')

	next unless queries.size > 1

	count = queries.last.split('=').last.to_i

	session.puts "<html><body>"

	session.puts "Count = #{count}"
	session.puts "<a href='/?count=#{count+1}'>Increment</a>"
	session.puts "<a href='/?count=#{count-1}'>Decrement</a>"

	session.puts "</body></html>"

	session.close
end


