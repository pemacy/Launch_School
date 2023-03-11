# frozen_string_literal: true

# In the previous exercise, you wrote a number guessing game that determines a secret number between 1 and 100, and gives the user 7 opportunities to guess the number.

# Update your solution to accept a low and high value when you create a GuessingGame object, and use those values to compute a secret number for the game. You should also change the number of guesses allowed so the user can always win if she uses a good strategy. You can compute the number of guesses with:

class GuessingGame
  def initialize(min, max)
    @min, @max = min, max
  end

  def play
    reset_stats
    while guesses_available && @not_guessed
      display_stats
      enter_guess
      assess_guess
    end
  end

  def reset_stats
    @correct_number = (@min..@max).to_a.sample
    @max_guesses = Math.log2(size_of_range).to_i + 1
    @guess_count = 0
    @not_guessed = true
    @numbers_guessed = []
  end

  def display_stats
    puts "You have #{@max_guesses - @guess_count} guesses left"
    puts "Current guesses have been #{@numbers_guessed}" unless @numbers_guessed.empty?
  end

  def guesses_available
    @guess_count < @max_guesses
  end

  def enter_guess
    puts "Enter a number between #{@min} and #{@max}:"
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
    (@min..@max).cover?(@current_guess)
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

  private

  def size_of_range
    @max - @min
  end
end


# Examples

game = GuessingGame.new(501, 1500)
game.play

# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 104
# Invalid guess. Enter a number between 501 and 1500: 1000
# Your guess is too low.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 1250
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 1375
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 80
# Invalid guess. Enter a number between 501 and 1500: 1312
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 1343
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 1359
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 1351
# Your guess is too high.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 1355
# That's the number!

# You won!

# game.play
# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 1000
# Your guess is too high.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 750
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 875
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 812
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 843
# Your guess is too high.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 820
# Your guess is too low.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 830
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 835
# Your guess is too low.

# You have 2 guesses remaining.
# Enter a number between 501 and 1500: 836
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 501 and 1500: 837
# Your guess is too low.

# You have no more guesses. You lost!
