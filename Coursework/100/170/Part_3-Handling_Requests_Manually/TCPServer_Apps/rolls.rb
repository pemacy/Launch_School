require 'socket'

server = TCPServer.new("localhost", 3003)

def parse_request(input)
  http_method, path_and_params, http = input.split(' ')
  path, params = path_and_params.split('?')
  params = params.split('&').each_with_object({}) do |param, hsh|
    key, value = param.split('=')
    hsh[key] = value.to_i
  end

  [http_method, path, params]
end

loop do
  client = server.accept

  request_line = client.gets
  puts request_line

  client.puts request_line

  if request_line.include?('?')
    http_method, path, params = parse_request(request_line)
    params['rolls'].times { client.puts rand(params['sides']) + 1 }
  end
  client.close
end
