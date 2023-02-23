class Board
  WINNING_COMBO = %w(123 456 789 147 258 369 159 357)

  attr_accessor :board

  def initialize
    reset
  end

  def reset
    self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
  end

  def grid
    cell = 0
    puts " ___ ___ ___"
    3.times do
      puts "|   |   |   |"
      puts "| #{board[cell]} | #{board[cell + 1]} | #{board[cell + 2]} |"
      puts "|___|___|___|"
      cell += 3
    end
  end

  def winner?(player)
    return if player.moves.size < 3
    combos = player.moves.combination(3).to_a.map{|m| m.join}
    player.win = true if !(combos & WINNING_COMBO).empty?
  end

  def update_board(player)
    player.moves.each{|a| @board[(a.to_i)-1] = player.marker}
  end
end
