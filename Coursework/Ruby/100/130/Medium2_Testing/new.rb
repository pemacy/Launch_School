# def print_all(*args, **keyword_arguments)
#   puts keyword_arguments
#   p args
# end
#
# def mixed_signature(some: 'option', **rest)
#   puts some
#   puts rest
# end
#
# print_all 1, 2, 3, 4, example: 'double splat (**)', arbitrary: 'keyword arguments'
# # {:example=>"double splat (**)", :arbitrary=>"keyword arguments"}
#
# mixed_signature another: 'option'
# # option
# # {:another=>"option"}

def metho(**keys, *args, &block)
  p args
  p keys
  yield(2)
end

metho(a: 1, B: 2, C: 3, 'foo', 'bar'){|n| p n}
