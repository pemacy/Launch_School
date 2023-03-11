# frozen_string_literal: true

# Create an object-oriented number guessing class for numbers in the range 1 to 100, with a limit of 7 guesses per game. The game should play like this:

# Note that a game object should start a new game with a new number to guess with each call to #play.

class GuessingGame
  MAX_GUESSES = 7

  def play
    reset_stats
    while guesses_available && @not_guessed
      display_stats
      enter_guess
      assess_guess
    end
  end

  def reset_stats
    @correct_number = (1..100).to_a.sample
    @guess_count = 0
    @not_guessed = true
    @numbers_guessed = []
  end

  def display_stats
    puts "You have #{MAX_GUESSES - @guess_count} guesses left"
    puts "Current guesses have been #{@numbers_guessed}" unless @numbers_guessed.empty?
  end

  def guesses_available
    @guess_count < MAX_GUESSES
  end

  def enter_guess
    puts 'Enter a number between 1 and 100:'
    @current_guess = gets.chomp.to_i
  end

  def assess_guess
    if valid_guess?
      too_low?
      too_high?
      correct_guess?
    else
      puts 'Invalid guess.'
    end
  end

  def valid_guess?
    (1..100).cover?(@current_guess)
  end

  def too_low?
    if @current_guess < @correct_number
      puts "The guess is too low"
      update_stats
    end
  end

  def too_high?
    if @current_guess > @correct_number
      puts "The guess is too high"
      update_stats
    end
  end

  def correct_guess?
    if @current_guess.eql? @correct_number
      puts "Correct Guess!"
      update_not_guessed
    end
  end

  def update_stats
    @guess_count += 1
    @numbers_guessed << @current_guess
  end

  def update_not_guessed
    @not_guessed = false
  end
end

game = GuessingGame.new
game.play

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

# game.play

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!
