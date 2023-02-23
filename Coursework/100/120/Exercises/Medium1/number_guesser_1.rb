class GuessLogic
  def initialize(guess)
    @guess = guess
  end


end

class PingGame
  MAX_GUESSES = 7

  def play
    @number = rand(101)
    counter = MAX_GUESSES
    loop do
      guess = GuessLogic.new(get_guess(counter))
      @compare_guess = does_guess_match?(guess)
      print_status
      break if @guess_status == :won
      counter -= 1
      break if counter == 0
    end

    goodbye
  end

  private

  def goodbye
    if @guess_status == :won
      puts "Goodbye"
    else
      puts "You are out of guesses. You lose."
    end
  end

  def print_status
    case @compare_guess
    when -1 then puts "Guess too #{@guess_status = :low}"
    when 0 then puts "You #{@guess_status = :won}!"
    when 1 then puts "Guess too #{@guess_status = :high}"
    end
  end

  def test_guess_between_valid_range(guess)
    return false if guess.to_i.to_s != guess
    (1..100).include?(guess.to_i)
  end

  def get_guess(counter)
    puts "You have #{counter} guesses remaining"
    print "Enter a number between 1 and 100: "
    guess = gets.chomp
    loop do
      break if test_guess_between_valid_range(guess)
      print "Invalid guess, enter a number between 1 and 100: "
      guess = gets.chomp
    end
    guess.to_i
  end

  def does_guess_match?(guess)
    guess <=> @number
  end
end

game = PingGame.new
game.play
