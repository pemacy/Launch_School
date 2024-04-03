class Player
  attr_accessor :moves, :marker, :name, :win, :score

  def initialize(marker)
    self.moves = []
    self.win = false
    self.score = 0
    self.marker = marker
  end

  def reset
    self.moves = []
    self.win = false
  end

  def score_reset
    self.score = 0
  end

  def add_point
    self.score += 1
  end
end

class Human < Player
  def initialize(name = "Human")
    super('O')
    self.name = name
  end

  def mark(squares)
    loop do
      puts "Select a square"
      choice = gets.chomp
      if squares.squares_available.include?(choice)
        self.moves += [choice]
        self.moves.sort!
        break
      else
        puts "That square is not avaible"
      end
    end
  end
end

class Computer < Player
  def initialize
    super('X')
    self.name = ['R2D2', 'Chappie', 'Johnny5', 'HAL', 'Computer'].sample
  end

  def mark(squares, opponent, board)
    self.moves += [ai(squares, opponent, board)]
    self.moves.sort!
  end

  private

  def ai(squares, opponent, board)
    win = winning_move(squares, board)
    defend = defensive_move(squares, board, opponent)
    setup_win = go_for_two(squares, board)

    return win if win
    return defend if defend
    return setup_win if setup_win
    return "5" if middle_square_empty?(board)
    return corner_square(squares) if corner_square(squares)
    squares.squares_available.sample
  end

  def winning_move(squares, board)
    offence = squares.two_combo(board, self)
    if offence
      which_squares = Board::WINNING_COMBO.select do |el|
        el.include?(offence[0]) && el.include?(offence[1])
      end
      mark = which_squares[0].chars.delete_if{|d| offence.include?(d)}[0]
      squares.squares_available.include?(mark) ? mark : nil
    end
  end

  def defensive_move(squares, board, opponent)
    defence = squares.two_combo(board, opponent)
    if defence
      which_squares = Board::WINNING_COMBO.select do |el|
        el.include?(defence[0]) && el.include?(defence[1])
      end
      which_squares[0].chars.delete_if{|d| defence.include?(d)}[0]
    end
  end

  def go_for_two(squares, board)
    squares.two_empty(board, self)
  end

  def middle_square_empty?(board)
    board.board[4] == ' '
  end

  def corner_square(squares)
    (squares.squares_available & %w(1 3 7 9)).sample
  end
end
