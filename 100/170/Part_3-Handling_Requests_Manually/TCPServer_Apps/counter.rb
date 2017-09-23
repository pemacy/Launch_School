require 'socket'

server = TCPServer.new("localhost", 3003)

def parse_request(input)
  http_method, path_and_params, http = input.split(' ')
  path, params = path_and_params.split('?')
  params = (params || "").split('&').each_with_object({}) do |param, hsh|
    key, value = param.split('=')
    hsh[key] = value.to_i
  end

  [http_method, path, params]
end

num_refreshes = 0

loop do
  client = server.accept

  request_line = client.gets
  http_method, path, params = parse_request(request_line)

  puts request_line
  puts num_refreshes

  client.puts "HTTP/1.0 200 OK"
  client.puts "Content-Type: text/html"
  client.puts
  client.puts "<html>"
  client.puts "<body>"
  client.puts "<pre>"
  client.puts "Num Refreshes: #{num_refreshes}"
  client.puts request_line
  client.puts http_method
  client.puts path
  client.puts params
  number = params['number'].to_i
  client.puts "</pre>"
  client.puts "<h1>Counter Number: #{number}</h1>"
  client.puts "<h3><a href = 'http://localhost:3003/?number=#{number + 1}'>Count Up</a>"
  client.puts "<h3><a href = 'http://localhost:3003/?number=#{number - 1}'>Count Down</a>"
  client.puts "</body>"
  client.puts "</html>"

  client.close
  num_refreshes += 1
end
