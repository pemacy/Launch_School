# blackjack.rb

require 'pry'

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
BUST_VALUE = 21
DEALER_DO_NOT_EXCEED = 17

# ========== MAKES A DECK OF 52 CARDS AND SHUFFLES THEM ==========
def initialize_deck
  deck_array = []
  SUITS.each do |suit|
    CARDS.each_with_index do |card, i|
      deck_array << [card.to_s + ' of ' + suit, VALUES[i]]
    end
  end
  deck = {}
  deck_array.shuffle!
  deck_array.each { |card| deck[card[0]] = card[1] }
  deck
end

# ========== RETURNS AND REMOVES FIRST CARD FROM DECK ==========
def deal_card!(deck)
  card = deck.first
  deck.delete(card[0])
  card
end

def initial_deal(deck)
  [deal_card!(deck), deal_card!(deck)]
end

# ========= DISPLAY HANDS ==========
def show_cards(hand, all=true)
  cards = ""
  if all
    hand.each do |card|
      cards << "\n" + card[0]
    end
  else
    cards = "\n" + hand[0][0]
  end
  cards
end

def dealer_hidden_cards(hand)
  hidden_cards = ""
  hand.each_with_index do |_, i|
    break if i == hand.size - 1
    hidden_cards << "\nHidden Card"
  end
  hidden_cards
end

def display_player_and_dealer(player, dealer, all)
  puts  "\n-- Player hand: #{sum_cards_in_hand(player)} #{show_cards(player)}"
  puts  "\n-- Dealer hand: #{sum_cards_in_hand(dealer) if all}\
        #{show_cards(dealer, all)}\
        #{dealer_hidden_cards(dealer) unless all}"
end

def display_player(player)
  puts "\n-- Player hand: #{sum_cards_in_hand(player)} #{show_cards(player)}"
end

def display_dealer(dealer, all)
  puts  "\n-- Dealer hand: #{sum_cards_in_hand(dealer) if all}\
        #{show_cards(dealer, all)}\
        #{dealer_hidden_cards(dealer) unless all}"
end

def display_hand(player = nil, dealer = nil, all=false)
  if player && dealer
    display_player_and_dealer(player, dealer, all)
  elsif player
    display_player(player)
  elsif dealer
    display_dealer(dealer, all)
  end
end

# ========= SUM CARDS IN HAND =========
def sum_cards_in_hand(hand)
  sum = 0
  num_of_aces = 0
  hand.each { |card| num_of_aces += 1 if card[0][0..2] == 'Ace'}
  hand.each{ |card| sum += card[1]}
  num_of_aces.times do
    break if sum < 22
    sum -= 10
  end
  sum
end

# ========= HIT ==========
def add_card(deck, hand)
  hand << deal_card!(deck)
end

def player_hit(deck, hand, sum_of_hand)
  while sum_of_hand <= BUST_VALUE
    print "\nHit or Stand?: "
    break if gets.chomp.downcase != 'h'
    add_card(deck, hand)
    display_hand(hand)
    system 'clear'
    sum_of_hand = sum_cards_in_hand(hand)
  end
  if sum_of_hand > 21
    puts "\nPlayer BUST!" if sum_of_hand > BUST_VALUE
    sleep(2)
    return false
  end
  sum_of_hand
end

def dealer_hit(deck, hand, sum_of_hand)
  system 'clear'
  puts "\n--- Dealer's Turn ---"
  display_hand(nil, hand)
  while sum_of_hand < DEALER_DO_NOT_EXCEED
    add_card(deck, hand)
    sleep(1)
    display_hand(nil, hand)
    system 'clear'
    sum_of_hand = sum_cards_in_hand(hand)
    sleep(1)
  end
  if sum_of_hand > 21
    puts "\nDealer BUST!" if sum_of_hand > BUST_VALUE
    display_hand(nil, hand, true)
    sleep(2)
    return false
  end
  sum_of_hand
end

# ========== DISPLAY WINNER ==========
def show_winner(player, dealer, player_hand, dealer_hand, score)
  system 'clear'
  display_hand(player_hand, dealer_hand, true)
  puts player > dealer ? "\n You won this hand!" : "\nDealer won"
  player > dealer ? score[0] += 1 : score[1] += 1
end

# ========== EACH HAND LOOP ==========
def playing_a_hand(deck, player_hand, dealer_hand, score)
loop do
  display_hand(player_hand, dealer_hand, false)
  player_sum_of_hand = sum_cards_in_hand(player_hand)
  dealer_sum_of_hand = sum_cards_in_hand(dealer_hand)
  # ========== PLAYER HIT LOOP, EXITS IF BUST ==========
  player_turn = player_hit(deck, player_hand, player_sum_of_hand)
  unless player_turn
    score[1] += 1
    break
  end
  # ========== DEALER HIT LOOP, EXITS IF BUST ==========
  dealer_turn = dealer_hit(deck, dealer_hand, dealer_sum_of_hand, player_sum_of_hand) if player_turn
  unless dealer_turn
    score[0] += 1
    break
  end
  # ========== DETERMINE WINNER ==========
  show_winner(player_turn, dealer_turn, player_hand, dealer_hand, score)
  break
  end
end

# ========= PROGRAM LOOP ==========
loop do
  deck = initialize_deck
  score = [0,0]
  system 'clear'
  puts "Welcome to BlackJack, closest to #{BUST_VALUE} wins, but don't bust!"

  # ========== MAIN GAME LOOP, FIRST TO 5 WINS ==========
  while score.count(5) < 1
    puts ""
    puts "------ New Card Deal ------"
    puts "Player: #{score[0]}   .....   Dealer: #{score[1]}"
    player_hand = initial_deal(deck)
    dealer_hand = initial_deal(deck)

    # ========== EACH HAND LOOP ==========
    loop do
      display_hand(player_hand, dealer_hand, false)
      player_sum_of_hand = sum_cards_in_hand(player_hand)
      dealer_sum_of_hand = sum_cards_in_hand(dealer_hand)
      # ========== PLAYER HIT LOOP, EXITS IF BUST ==========
      player_turn = player_hit(deck, player_hand, player_sum_of_hand)
      unless player_turn
        score[1] += 1
        break
      end
      # ========== DEALER HIT LOOP, EXITS IF BUST ==========
      dealer_turn = dealer_hit(deck, dealer_hand, dealer_sum_of_hand, player_sum_of_hand) if player_turn
      unless dealer_turn
        score[0] += 1
        break
      end
      # ========== DETERMINE WINNER ==========
      show_winner(player_turn, dealer_turn, player_hand, dealer_hand, score)
      break
    end
  end
  puts "Final score: Player: #{score[0]}   .....   Dealer: #{score[1]}"
  puts "\nPlay again?:"
  break unless gets.chomp.downcase.start_with?('y')
end

puts ""
puts "Thanks for playing, good-bye!"
