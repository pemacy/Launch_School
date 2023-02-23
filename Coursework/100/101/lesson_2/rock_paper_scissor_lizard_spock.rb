# rock_paper_scissor_lizard_spock.rb

# user makes a choice
# computer makes a choice

# scissors cuts paper,
# paper covers rock,
# rock crushes lizard,
# lizard poisons spock,
# spock smashes scissors,
# scissors decapitates lizard,
# lizard eats paper,
# paper disproves spock,
# spock vaporizes rock,
# rock crushes scissors

# the winner is displayed

VALID_CHOICES = %w(rock paper scissors lizard spock)

SHORT_CHOICES = {
  'r' => 'rock',
  'p' => 'paper',
  'sc' => 'scissors',
  'l' => 'lizard',
  'sp' => 'spock'
}

WIN_COMBO = {
  'rock' => %w(scissors lizard),
  'paper' => %w(rock spock),
  'scissors' => %w(paper lizard),
  'lizard' => %w(spock paper),
  'spock' => %w(scissors rock)
}

def prompt(message)
  Kernel.puts("=> #{message}")
end

def display_rules
  <<-RULES
  ====Rules====

      scissors cuts paper,
      paper covers rock,
      rock crushes lizard,
      lizard poisons spock,
      spock smashes scissors,
      scissors decapitates lizard,
      lizard eats paper,
      paper disproves spock,
      spock vaporizes rock,
      rock crushes scissors

      =============
  RULES
end

def player_choice
  loop do
    prompt("Choose one: #{VALID_CHOICES.join(', ')}")
    choice = Kernel.gets().chomp()

    if VALID_CHOICES.include?(choice)
      return choice
    elsif VALID_CHOICES.include?(SHORT_CHOICES[choice])
      return SHORT_CHOICES[choice]
    else
      prompt("Invalid choice")
    end
  end
end

def reset
  prompt("Would you like to play again? (Y)")
  play_again = Kernel.gets().chomp()
  if play_again.downcase.start_with?('y')
    prompt(display_rules)
    { player: 0, computer: 0 }
  else
    false
  end
end

def display_score(choice, computer_choice, score, winner)
  prompt("You chose: #{choice}, computer chose #{computer_choice}")
  prompt(winner)
  prompt("You: #{score[:player]}, Computer: #{score[:computer]}")
end

score = { player: 0, computer: 0 }
prompt(display_rules)

loop do
  choice = player_choice
  computer_choice = VALID_CHOICES.sample

  if WIN_COMBO[choice].include?(computer_choice)
    score[:player] += 1
    winner = "You Win!"
  elsif WIN_COMBO[computer_choice].include?(choice)
    score[:computer] += 1
    winner = "Computer Won!"
  else
    winner = "It's a tie!"
  end

  display_score(choice, computer_choice, score, winner)

  if score[:player] == 5 || score[:computer] == 5
    score = reset
    break unless score
  end
end
