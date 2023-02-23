class Guesser
  def initialize(min, max)
    @random_number = Random.new.rand(min..max)
    @counter = Math.log2(max - min).to_i + 1
    @guess = nil
    @all_guesses = {}
    @min = min
    @max = max
  end

  def play
    clear_screen
    welcome
    loop do
      break if won?
      display_status
      decrement_counter
      break if counter_zero?
      new_guess
    end
    goodbye
  end

  def welcome
    puts "Welcome to Number Guesser 2.0"
    new_guess
  end

  def goodbye
    clear_screen
    if won?
      puts "#{@all_guesses}"
      puts "\nYou win! The number was #{@random_number}"
    else
      puts "You lose, the number was #{@random_number}"
    end
    puts "Goodbye!"
  end

  def decrement_counter
    @counter -= 1
  end

  def counter_zero?
    @counter == 0
  end

  def new_guess
    loop do
      print "Enter a number between #{@min} and #{@max}:  "
      @guess = gets.chomp
      if valid?
        @guess = @guess.to_i
        break
      else
        puts "Invalid entry, try again"
      end
    end
  end

  def valid?
    return false if @guess.to_i.to_s != @guess
    (@min..@max).include?(@guess.to_i)
  end

  def won?
    if @guess == @random_number
      @all_guesses[@guess] = :nailed_it
      true
    else
      false
    end
  end

  def display_status
    clear_screen
    case @guess <=> @random_number
    when 1
      @all_guesses[@guess] = :high
      puts "#{@all_guesses}\nToo High"
    when -1
      @all_guesses[@guess] = :low
      puts "#{@all_guesses}\nToo Low"
    end
    puts "\nYou have #{@counter} guesses left"
  end

  def clear_screen
    system 'clear'
  end
end


Guesser.new(50,1500).play
