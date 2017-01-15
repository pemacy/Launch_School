require 'pry'

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
VALID_SELECTIONS = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
WINNING_COMBINATIONS = ['012', '345', '678', '036', '147', '258', '048', '246']

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

def user_input(board)
  loop do
    print "Enter location: "
    user_input = gets.chomp.downcase
    if verify_selection(user_input) &&
       board[VALID_SELECTIONS.index(user_input)] == INITIAL_MARKER
      return board[VALID_SELECTIONS.index(user_input)] = PLAYER_MARKER
    else
      puts "Invalid entry, try again"
    end
  end
end

def computer_input(board, score)
  defend = ai_defence_move(board)
  if board_full?(board)
    false
  elsif winner?(board, score)
    false
  else
    loop do
      if defend
        board[defend] = COMPUTER_MARKER
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

def verify_selection(user_input)
  VALID_SELECTIONS.include?(user_input)
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

def board_full?(board)
  full_board = false
  full_board = true unless board.include?(INITIAL_MARKER)
  full_board
end

def board_reset(board)
  (0..8).to_a.each { |num| board[num] = INITIAL_MARKER }
end

def score_reset(score)
  score[0] = 0
  score[1] = 0
end

def winner?(board, score)
  winner = false
  which_marker = ''
  WINNING_COMBINATIONS.each do |combo|
    which_marker = board[combo[0].to_i]
    square2 = board[combo[1].to_i]
    square3 = board[combo[2].to_i]
    if which_marker == square2 && square2 == square3
      winner = which_marker
    end
  end
  display_winner(winner, score)
end

def display_winner(winner, score)
  if winner == PLAYER_MARKER
    p "You Won!"
    score[0] += 1
  elsif winner == COMPUTER_MARKER
    p "Computer Won!"
    score[1] += 1
  else
    false
  end
end

def play_again?(board, score)
  print "Would you like to play again?:  "
  play_again = gets.chomp.downcase
  if play_again.start_with?('y')
    board_reset(board)
    score_reset(score)
    display_board(board)
    puts "Game to 5! You go first"
    return true
  else
    return false
  end
end

# =========== AI Methods =============
def threat_row_for_ai(board)
  defend_spaces = {}
  WINNING_COMBINATIONS.each { |threat| defend_spaces[threat] = 0 }
  WINNING_COMBINATIONS.each do |threat|
    threat.chars.each do |is_x|
      defend_spaces[threat] += 1 if board[is_x.to_i] == PLAYER_MARKER
      if board[is_x.to_i] == COMPUTER_MARKER
        defend_spaces[threat] = 0
        break
      end
    end
  end
  defend_spaces
end

def ai_defence_move(board)
  defence_move = false
  defend_spaces = threat_row_for_ai(board)
  defend_spaces.each do |k, v|
    if v == 2
      k.chars.each do |threat|
        defence_move = threat.to_i if board[threat.to_i] == INITIAL_MARKER
      end
    end
  end
  defence_move
end

# =========== INITIAL GAME SETUP =============
board = []
score = [0,0]
board_reset(board)
display_board(board)
puts "Game to 5!  You go first"
play_again = true

while play_again
  puts "You #{score[0]} ... Computer #{score[1]}"
  user_input(board)
  computer_input(board, score)

  display_board(board)

  winner = winner?(board, score)

  if winner
    winner
    if score[0] == 5 || score[1] == 5
      play_again = play_again?(board, score)
    else
      board_reset(board)
      display_board(board)
    end
  elsif board_full?(board)
    display_board(board)
    board_reset(board)
    puts "Cat's Game"
  end
end

puts "Thanks for playing!  Good-bye."
