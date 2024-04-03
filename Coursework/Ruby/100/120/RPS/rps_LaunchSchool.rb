class RPSGame
  attr_accessor :human, :computer

  def initialize
    @human = Human.new
    @computer = Computer.new
  end

  def play
    welcome
    loop do
      human.choose
      computer.choose
      display_moves
      winner
      puts "Play again?"
      break unless gets.chomp.downcase.include?('y')
    end
    goodbye
  end

  def display_moves
    puts "#{human.name} chose #{human.move.value},
    Computer chose #{computer.move.value}"
  end

  def winner
    if human.move.value == computer.move.value
      puts "It's a tie!"
    elsif human.move > computer.move
      puts "#{human.name} wins!"
    else
      puts "Computer wins"
    end
  end

  def welcome
    puts "Welcome to Rock, Paper, Scissors"
  end

  def goodbye
    puts "Thanks for playing. Goodbye!"
  end
end

class Move
  VALUES = %w(rock paper scissors)
  SHORT_CHOICES = { 'r' => 'rock',
                    'p' => 'paper',
                    's' => 'scissors' }

  attr_accessor :value

  def initialize(value)
    @value = value
  end

  def rock?; @value == 'rock'; end
  def paper?; @value == 'paper'; end
  def scissors?; @value == 'scissors'; end

  def >(other_move)
    (rock? && other_move.scissors?) ||
      (paper? && other_move.rock?) ||
      (scissors? && other_move.paper?)
  end
end

class Player
  attr_accessor :move, :name

  def initialize
    set_name
  end
end

class Human < Player
  def set_name
    n = ""
    loop do
      puts "What's your name?"
      n = gets.chomp
      break if /^[a-z]+\s{1}?[a-z]*$/i =~ n
      puts "That is not a valid entry"
    end
    self.name = n
  end

  def choose
    choice = nil
    loop do
      puts "Choose: r - rock, p - paper, s - scissors"
      choice = gets.chomp
      choice =  Move::SHORT_CHOICES[choice] if
                Move::SHORT_CHOICES.include?(choice)
      break if Move::VALUES.include?(choice)
      puts 'Invalid value, try again'
    end
    self.move = Move.new(choice)
  end
end

class Computer < Player
  def set_name
    self.name = %w(R2D2 Hal Chappie).sample
  end

  def choose
    self.move = Move.new(Move::VALUES.sample)
  end
end

RPSGame.new.play
