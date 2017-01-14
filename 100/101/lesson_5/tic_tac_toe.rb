require 'pry'

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'

def display_board(board)
  system 'clear'
  puts ""
  puts "     1     2     3"
  puts ""
  puts "        |     |"
  puts "A    #{board[0]}  |  #{board[1]}  |  #{board[2]}  "
  puts "        |     |"
  puts "   -----+-----+-----"
  puts "        |     |"
  puts "B    #{board[3]}  |  #{board[4]}  |  #{board[5]}  "
  puts "        |     |"
  puts "   -----+-----+-----"
  puts "        |     |"
  puts "C    #{board[6]}  |  #{board[7]}  |  #{board[8]}  "
  puts "        |     |"
  puts ""
end

def user_input(valid_selections, board)
  loop do
    print "Enter location: "
    user_input = gets.chomp.downcase
    if verify_selection(user_input, valid_selections) && board[valid_selections.index(user_input)] == INITIAL_MARKER
      return board[valid_selections.index(user_input)] = PLAYER_MARKER
    else
      puts "Invalid entry, try again"
    end
  end
end

def computer_input(board, winning_combinations)
  p board
  defend_spaces = threat_spaces_for_ai(winning_combinations, board)

  unless board_full?(board)
    loop do
      if defence_for_ai(defend_spaces)
        board[defence_for_ai(defend_spaces)] = COMPUTER_MARKER
        break
      else
        computer_input = rand(0..8)
        if board[computer_input] == INITIAL_MARKER
          board[computer_input] = COMPUTER_MARKER
          break
        end
      end
    end
  end
end

def verify_selection(user_input, valid_selections)
  valid_selections.include?(user_input)
end

def user_selection(board)
  user_selections = []
  board.each_with_index do |spot, i|
    user_selections << i.to_s if spot == PLAYER_MARKER
  end
  user_selections
end

def computer_selection(board)
  computer_selections = []
  board.each_with_index do |spot, i|
    computer_selections << i.to_s if spot == COMPUTER_MARKER
  end
  computer_selections
end

def check_winner(board, winning_combinations)
  user_selections = user_selection(board)
  computer_selections = computer_selection(board)
  if user_win?(user_selections, winning_combinations)
    'You Won!'
  elsif computer_win?(computer_selections, winning_combinations)
    'Computer Won!'
  elsif board_full?(board)
    'Tie Game!'
  else
    false
  end
end

def user_win?(user_selections, winning_combinations)
  win = false
  winning_combinations.each do |el|
    win = true if (el.chars & user_selections).size == 3
  end
  win
end

def computer_win?(computer_selections, winning_combinations)
  win = false
  winning_combinations.each do |el|
    win = true if (el.chars & computer_selections).size == 3
  end
  win
end

def board_full?(board)
  full_board = false
  full_board = true unless board.include?(INITIAL_MARKER)
  full_board
end

def update_board(user_input, computer_input, valid_selections)
  user_spot = valid_selections.index(user_input)
  board[user_spot] = PLAYER_MARKER
  board[computer_input] = COMPUTER_MARKER
end

def board_reset
  (0..8).to_a.each_with_object([]) { |_, arr| arr << INITIAL_MARKER }
end

# =========== AI Methods =============
def threat_spaces_for_ai (winning_combinations, board)
  p board
  defend_spaces = {}
  winning_combinations.each {|el| defend_spaces[el] = []}
  winning_combinations.each do |threat|
    threat_group = false
    threat.chars.each do |is_X|
      if board[is_X.to_i] == 'O'
        defend_spaces[threat] = []
        break
      elsif board[is_X.to_i] == 'X'
        threat_group = true
      end
      if threat_group == true && board[is_X.to_i] == ' '
        defend_spaces[threat] << is_X.to_i

      end
    end
  end
  defend_spaces
end

def defence_for_ai(defend_spaces)
  should_ai_defend = false
  defend_spaces.each do | _ , v |
    if v.size == 1
      should_ai_defend = v[0]

    end
  end
  should_ai_defend
end


board = board_reset
valid_selections = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
winning_combinations = ['012', '345', '678', '036', '147', '258', '048', '246']
display_board(board)

loop do
  user_input(valid_selections, board)
  computer_input(board, winning_combinations)


  if check_winner(board, winning_combinations)
    display_board(board)
    puts check_winner(board, winning_combinations)
    print "Would you like to play again?:  "
    play_again = gets.chomp.downcase
    if play_again.start_with?('y')
      board = board_reset
      display_board(board)
    else
      break
    end
  else
    display_board(board)
    puts threat_spaces_for_ai(winning_combinations, board)
  end
end
