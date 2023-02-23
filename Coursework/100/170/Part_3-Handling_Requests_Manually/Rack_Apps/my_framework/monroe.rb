# monroe.rb

class Monroe
  def erb(filename, local = {})
    b = binding
    message = local[:message]
    path = File.expand_path("../my_framework/views/#{filename}.erb")
    p path
    content = File.read(path)
    ERB.new(content).result(b)
  end

  def response(status, headers, body = '')
    body = yield if block_given?
    [status, headers, [body]]
  end
end
