# rock_paper_scissor.rb

# user makes a choice
# computer makes a choice
# the winner is displayed

VALID_CHOICES = %w(rock paper scissors)

WIN_COMBO = {
  'rock' => 'scissors',
  'scissors' => 'paper',
  'paper' => 'rock'
}

def prompt(message)
  Kernel.puts("=> #{message}")
end

def display_results(player, computer)
  if WIN_COMBO[player] == computer
    prompt("You won!")
  elsif WIN_COMBO[computer] == player
    prompt("Computer won")
  else
    prompt("Tie Game!")
  end
end

loop do
  choice = ''
  loop do
    prompt("Choose one: #{VALID_CHOICES.join(', ')}")
    choice = Kernel.gets().chomp()

    if VALID_CHOICES.include?(choice)
      break
    else
      prompt("Invalid choice")
    end
  end

  computer_choice = VALID_CHOICES.sample

  prompt("You chose: #{choice}, computer chose #{computer_choice}")
  display_results(choice, computer_choice)

  prompt("Would you like to play again? (Y)")
  play_again = Kernel.gets().chomp()
  break unless play_again.downcase.start_with?('y')
end
