class Square
  attr_accessor :squares_available

  def initialize
    reset
  end

  def reset
    self.squares_available = %w(1 2 3 4 5 6 7 8 9)
  end

  def update_squares(player)
    self.squares_available = self.squares_available -
                        (player.moves & self.squares_available)
  end

  def board_full?
    squares_available.empty?
  end

  def two_empty(board, player)
    find_other_two_squares_for_a_win.each do |key, value|
      value.each do |s|
        first = board.board[s[0].to_i - 1]
        second = board.board[s[1].to_i - 1]
        if first == ' ' && second == ' ' && key == player.marker
          return s[0]
        end
      end
    end
    nil
  end

  def two_combo(board, player)
    find_other_two_squares_for_a_win.each do |_, value|
      value.each do |s|
        first = board.board[s[0].to_i - 1]
        second = board.board[s[1].to_i - 1]
        if first == player.marker && second == player.marker
          return s[0] + s[1]
        end
      end
    end
    nil
  end

  # def two_combo(board, player)
  #   two_combos = squares_available.map do |s|
  #     values = Board::WINNING_COMBO.map do |t|
  #       if t.include?(s)
  #         combo_squares = t.chars.map { |n| n if n != s }.compact
  #         doubles =
  #         if  board.board[combo_squares[0].to_i - 1] == player.marker &&
  #             board.board[combo_squares[1].to_i - 1] == player.marker
  #           combo_squares[0] + combo_squares[1]
  #         end
  #         doubles.chars.sort.join if doubles
  #       end
  #     end
  #     values.compact
  #   end
  #   p find_other_two_squares_for_a_win
  #   sleep 10
  #   two_combos.delete_if(&:empty?)
  # end

  private

  def find_possible_three_in_a_row
    winning_threes = Hash.new([])
    squares_available.map do |s|
      winning_threes[s] = Board::WINNING_COMBO.select do |t|
        t.include?(s)
      end
    end
    winning_threes
  end

  def find_other_two_squares_for_a_win
    other_two_squares = find_possible_three_in_a_row
    find_possible_three_in_a_row.each do |key,value|
      other_two_squares[key] = value.map { |s| s.delete(key)}
    end
    other_two_squares
  end
end
