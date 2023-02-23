# frozen_string_literal: true

# You want to have a small script delivering motivational quotes, but with the
# following code you run into a very common error message: no implicit
# conversion of nil into String (TypeError). What is the problem and how can
# you fix it?

def get_quote(person)
  if person == 'Yoda'
    'Do. Or do not. There is no try.'
  end

  if person == 'Confucius'
    'I hear and I forget. I see and I remember. I do and I understand.'
  end

  if person == 'Einstein'
    'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
  end
end

puts 'Confucius says:'
puts '"' + get_quote('Confucius') + '"'

# => an if statement returns nil, and since the last if statement is false, it will return nil
# to return the proper conditional, either group all the conditions in one conditional
# using elsif and else, or use 'return' keyword inside each if conditional
