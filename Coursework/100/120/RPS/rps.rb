class RPSGame
  attr_accessor :human, :computer

  def initialize
    @human = Player.new
    @computer = Player.new(:computer)
  end

  def play
    welcome
    loop do
      human.choose
      computer.choose
      puts "Player chose #{human.choice}, Computer chose #{computer.choice}"
      Rules.new(human.choice, computer.choice).winner
      puts "Play again?"
      break unless gets.chomp.downcase.include?('y')
    end
    goodbye
  end

  def welcome
    puts "Welcome to Rock, Paper, Scissors"
  end

  def goodbye
    puts "Thanks for playing. Goodbye!"
  end
end

class Player
  CHOICES = %w(rock paper scissors)
  SHORT_CHOICES = { 'r' => 'rock', 'p' => 'paper', 's' => 'scissors' }

  attr_accessor :choice

  def initialize(player_type = :human)
    @player_type = player_type
  end

  def choose
    if human?
      human_choose
    else
      CHOICES.sample
    end
  end

  def human_choose
    puts "Choose: r - Rock, p - Paper, s - Scissors"
    loop do
      choice = gets.chomp.downcase
      if CHOICES.include?(choice)
        return choice
      elsif SHORT_CHOICES.include?(choice)
        choice = SHORT_CHOICES[choice]
        return choice
      else
        puts "#{choice} is not a valid input, please try again."
      end
    end
  end

  def human?
    @player_type == :human
  end
end

class Rules
  WIN_COMBO = { 'rock' => 'scissors', 'scissors' => 'paper', 'paper' => 'rock' }

  def initialize(player, computer)
    @player = player
    @computer = computer
  end

  def winner
    if WIN_COMBO[@player] == @computer
      puts 'Player wins'
    elsif WIN_COMBO[@computer] == @player
      puts 'Computer wins'
    else
      puts 'Tie Game'
    end
  end
end

RPSGame.new.play
