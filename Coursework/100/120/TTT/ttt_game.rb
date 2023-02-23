require_relative 'board'
require_relative 'square'
require_relative 'player'

class TTTGame
  attr_accessor :human, :computer, :board, :squares

  def initialize
    self.board = Board.new
    self.human = Human.new
    self.computer = Computer.new
    self.squares = Square.new
  end

  def play
    welcome
    loop do
      pick_marker
      game_loop
      display_score
      puts "Play again?"
      break unless gets.chomp.downcase.include?('y')
      game_reset
      score_reset
    end
    goodbye
  end

  def game_loop
    loop do
      single_game
      display_end_of_round
      break if human.score == 5 || computer.score == 5
      game_reset
    end
  end

  def single_game
    loop do
      display_board
      display_score
      human_turn
      break if board.winner?(human) || squares.board_full?
      computer_turn
      break if board.winner?(computer) || squares.board_full?
    end
  end

  private

  def display_end_of_round
    display_board
    update_score
    p display_winner
    sleep 1
  end

  def game_reset
    board.reset
    human.reset
    computer.reset
    squares.reset
  end

  def score_reset
    human.score_reset
    computer.score_reset
  end

  def update_score
    human.add_point if human.win
    computer.add_point if computer.win
  end

  def display_score
    puts "#{"#{human.name} is #{human.marker}:".ljust(15)} #{human.score}"
    puts "#{"#{computer.name} is #{computer.marker}:".ljust(15)} #{computer.score}"
  end

  def human_turn
    human.mark(squares)
    squares.update_squares(human)
    board.update_board(human)
    display_board
  end

  def computer_turn
    computer.mark(squares, human, board)
    squares.update_squares(computer)
    board.update_board(computer)
  end

  def display_board
    clear
    board.grid
  end

  def clear
    system "clear"
  end

  def display_winner
    return "Human won!" if human.win
    return "Computer won!" if computer.win
    "Cat's Game!"
  end

  def welcome
    puts "Welcome to Tic Tac Toe!"
    puts "Enter your name:"
    name = gets.chomp.capitalize
    human.name = name
  end

  def pick_marker
    puts "Choose your marker X or O"
    new_marker = gets.chomp.upcase
    if new_marker != human.marker
      computer.marker = human.marker
      human.marker = new_marker
    end
  end
  def goodbye
    puts "Thanks for playing, goodbye!"
  end
end

game = TTTGame.new

game.play
