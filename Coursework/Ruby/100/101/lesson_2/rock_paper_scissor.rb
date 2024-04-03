# rock_paper_scissor.rb

# user makes a choice
# computer makes a choice
# the winner is displayed

def prompt(message)
  puts "=> #{message}"
end

def computer_selection
  rand(3) + 1
end

def user_input(message)
  loop do
    prompt(message)
    input = gets.chomp
    if input =~ /^[1-3]$/
      return input
    else
      prompt("Invalid input, try again")
    end
  end
end

def convert_selection(selection)
  case selection
  when 1
    "Rock"
  when 2
    "Paper"
  when 3
    "Scissors"
  end
end

def winner(user, computer)
  prompt("You selected #{convert_selection(user)}")
  prompt("Computer selected #{convert_selection(computer)}")

  return "It's a tie!" if (user - computer).zero?

  case user
  when 1
    case computer
    when 2
      "Paper beats Rock, Computer Wins"
    when 3
      "Rock beats Scissors, You Win!"
    end
  when 2
    case computer
    when 1
      "Paper beats Rock, You Win!"
    when 3
      "Scissors beats Paper, Computer Wins"
    end
  when 3
    case computer
    when 1
      "Rock beats Scissors, Computer Wins"
    when 2
      "Scissors beats Paper, You Win!"
    end
  end
end

prompt("Welcome to the Rock Paper Scissor Game!")

loop do
  display_choices = <<-SELECTION
    Select from the following choices:
    1) Rock
    2) Paper
    3) Scissors
  SELECTION

  user_selection = user_input(display_choices)

  prompt(winner(user_selection.to_i, computer_selection()))

  prompt("Would you like to play again? (Y)")
  play_again = gets.chomp
  break unless play_again.downcase.start_with?('y')
end
