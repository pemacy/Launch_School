class GuessLogic
  attr_reader :random_number, :guess

  def initialize(num)
    @random_number = num
    @counter = PingGame::MAX_GUESSES
    @guess = []
    @status = Hash.new
    welcome
  end

  def welcome
    puts "Welcome to the number guess game!"
    new_guess
  end

  def valid?(input)
    return false if input.to_i.to_s != input
    (0..100).include?(input.to_i)
  end

  def new_guess
    loop do
      print "Enter a number between 1 and 100: "
      input = gets.chomp
      if valid?(input)
        @guess = input.to_i
        break
      else
        puts "Invalid, try again."
      end
    end
  end

  def counter_zero?
    @counter == 0
  end

  def counter_decrement
    @counter -= 1
  end

  def won?
    if guess == @random_number
      @status[guess] = :spot_on
      true
    else
      false
    end
  end

  def print_status
    case guess <=> @random_number
    when 1
      @status[guess] = :high
      puts "#{@status}\n\n#{guess} Too High"
    when -1
      @status[guess] = :low
      puts "#{@status}\n\n#{guess} Too Low"
    end
    puts "#{@counter} guesses left\n\n"
  end

  def goodbye
    puts "#{@status}\n\nThe number was #{random_number}\nYou guessed it in #{PingGame::MAX_GUESSES - @counter} guesses!" if won?
    puts "You lose, better luck next time!" unless won?
    puts "Goodbye"
  end
end

class PingGame
  MAX_GUESSES = 7

  def play
    clear_screen
    guess = GuessLogic.new(rand(101))
    loop do
      clear_screen
      guess.counter_decrement
      break if guess.counter_zero?
      break if guess.won?
      guess.print_status
      guess.new_guess
    end
    guess.goodbye
  end

  def clear_screen
    system "clear"
  end
end

game = PingGame.new
game.play
