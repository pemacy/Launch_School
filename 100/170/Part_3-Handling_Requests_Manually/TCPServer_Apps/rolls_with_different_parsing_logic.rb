require 'socket'

server = TCPServer.new("localhost", 3003)

def parse_request(input, client)
  params = Hash.new(0)  # params = {rolls => num, sides => num}
  parse = input.scan(/\?[\w=&]+/).first.scan(/\w+/)
  2.times { |i| params[parse[i*2]] = parse[i*2+1].to_i}

  params['rolls'].times do
    client.puts rand(params['sides']) + 1
  end
end

loop do
  client = server.accept

  request_line = client.gets
  puts request_line

  client.puts request_line

  parse_request(request_line, client)if request_line.include?('?')
  
  client.close
end
