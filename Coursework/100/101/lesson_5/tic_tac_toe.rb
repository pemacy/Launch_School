require 'pry'

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
VALID_SELECTIONS = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
WINNING_COMBINATIONS =  [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]

# =========== BOARD LAYOUT =============
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

# =========== RESETS THE BOARD ARRAY =============
def board_reset(board)
  (0..8).to_a.each { |num| board[num] = INITIAL_MARKER }
end

# =========== USER INPUT (ALSO UPDATES THE BOARD)=============
def verify_selection(user_input)
  VALID_SELECTIONS.include?(user_input)
end

def user_input!(board)
  if board_full?(board)
    false
  elsif someone_win?(board)
    false
  else
    loop do
      print "Enter square location: "
      user_input = gets.chomp.downcase
      if verify_selection(user_input) &&
         board[VALID_SELECTIONS.index(user_input)] == INITIAL_MARKER
        return board[VALID_SELECTIONS.index(user_input)] = PLAYER_MARKER
      else
        puts "Invalid entry, try again"
      end
    end
  end
end

# =========== COMPUTER INPUT (ALSO UPDATES THE BOARD)=============
def computer_input!(board)
  defend = ai_defence_move(board)
  attack = ai_offensive_move(board)
  if board_full?(board)
    false
  elsif someone_win?(board)
    false
  else
    loop do
      if attack
        board[attack] = COMPUTER_MARKER
        break
      elsif defend
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

# =========== AI DEFENCE Methods =============
def threat_row_for_ai(board)
  defend_spaces = {}
  WINNING_COMBINATIONS.each { |threat| defend_spaces[threat] = 0 }
  WINNING_COMBINATIONS.each do |threat|
    threat.each do |is_x|
      defend_spaces[threat] += 1 if board[is_x] == PLAYER_MARKER
      if board[is_x] == COMPUTER_MARKER
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
      k.each do |threat|
        defence_move = threat if board[threat] == INITIAL_MARKER
      end
    end
  end
  defence_move
end

# =========== AI OFFENCE Methods =============
def offensive_row_for_ai(board)
  offensive_play = {}
  WINNING_COMBINATIONS.each { |offense| offensive_play[offense] = 0 }
  WINNING_COMBINATIONS.each do |offense|
    offense.each do |is_x|
      offensive_play[offense] += 1 if board[is_x] == COMPUTER_MARKER
      if board[is_x] == PLAYER_MARKER
        offensive_play[offense] = 0
        break
      end
    end
  end
  offensive_play
end

def ai_offensive_move(board)
  offense_move = false
  offense_spaces = offensive_row_for_ai(board)
  offense_spaces.each do |k, v|
    if v == 2
      k.each do |threat|
        offense_move = threat if board[threat] == INITIAL_MARKER
      end
    end
  end
  offense_move
end

# =========== CHECKS FOR A TIE =============
def board_full?(board)
  false
  true unless board.include?(INITIAL_MARKER)
end

# =========== CHECK FOR WINNER =============
def someone_win?(board)
  !!detect_winner(board)
end

def detect_winner(board)
  WINNING_COMBINATIONS.each do |sq|
    if board.values_at(*sq).count(PLAYER_MARKER) == 3
      return'Player'
    elsif board.values_at(*sq).count(COMPUTER_MARKER) == 3
      return 'Computer'
    end
  end
  nil
end

# =========== UPDATE THE SCORE =============
def update_score(score, board)
  if detect_winner(board) == 'Player'
    score[0] += 1
  else
    score[1] += 1
  end
end

# =========== INITIALIZING LOOP =============
loop do
  board = []
  score = [0,0]     # USER SCORE score[0], COMPUTER SCORE score[1]
  board_reset(board)
  puts "Game to 5!  Press 1 to go first, or 2 to go second:"
  order = gets.chomp.to_i
  play = true

  # =========== MAIN GAME LOOP =============
  while play
    if order == 1
      display_board(board)
      puts "You #{score[0]} ... Computer #{score[1]}"
      user_input!(board)
      computer_input!(board)
    else
      computer_input!(board)
      display_board(board)
      puts "You #{score[0]} ... Computer #{score[1]}"
      user_input!(board)
    end

    if someone_win?(board)
      display_board(board)
      update_score(score, board)
      puts "#{detect_winner(board)} Wins!"
      board_reset(board)
      sleep(2)
    end
    if score.count(5) > 0
      puts ""
      puts "Player #{score[0]} ... Computer #{score[1]}"
      play = false
    elsif board_full?(board)
      display_board(board)
      board_reset(board)
      puts "Cat's Game"
      sleep(2)
    end
  end

  print "Would you like to play again?:  "
  play_again = gets.chomp.downcase
  break unless play_again.start_with?('y')
end

puts "Thanks for playing!  Good-bye."
