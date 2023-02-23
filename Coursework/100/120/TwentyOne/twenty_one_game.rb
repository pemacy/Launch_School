module Hand
  def display_cards(game_over = false)
    if type == :player
      puts cards
    else
      hidden = [cards.first]
      (cards.size - 1).times { hidden << "Hidden Card" }
      puts hidden unless game_over
      puts cards if game_over
    end
  end

  def hand_amount
    num_aces = 0
    sum = 0
    cards.each { |c, _| num_aces += 1 if c.split.first == 'Ace' }
    cards.each { |card| sum += Deck::TOTAL_VALUES[card] }
    num_aces.times { |_| hand -= 10 if hand > 21 }
    sum
  end

  def bust?
    hand_amount > 21
  end
end

class Player
  include Hand

  attr_accessor :cards, :score, :type, :name

  def initialize(type = :player)
    self.type = type
    self.name = ''
    reset
  end

  def player_hit?
    puts ""
    puts "Hit or Stand? (h/s)"
    answer = gets.chomp.downcase
    answer.start_with?('h')
  end

  def reset
    self.cards = []
    self.score = 0
  end
end

class Deck
  SUITES = %w(Hearts Spades Diamonds Clubs)
  CARDS = %w(2 3 4 5 6 7 8 9 10 Jack Queen King Ace)
  VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
  TOTAL_VALUES = SUITES.each_with_object(hsh = Hash.new) do |s, hsh|
    CARDS.each_with_index do |c, i|
      hsh["#{c} of #{s}"] = VALUES[i]
    end
  end

  attr_accessor :deck

  def initialize
    reset
  end

  def reset
    @deck = new_deck.shuffle
  end

  def new_deck
    deck = []
    SUITES.map { |s| CARDS.each { |c| deck << "#{c} of #{s}" } }
    deck
  end

  def card_value(card)
    TOTAL_VALUES[card]
  end
end

class Game
  attr_reader :human, :computer, :deck

  def initialize
    @human = Player.new
    @computer = Player.new(:dealer)
    @deck = Deck.new
    reset
  end

  def play
    welcome
    loop do
      deal_cards
      display_all_hands
      player_hit
      human.bust? ? display_winner : computer_hit
      puts display_winner
      puts ""
      display_all_hands
      break unless play_again?
      reset
    end
    goodbye
  end

  def reset
    clear
    deck.reset
    human.reset
    computer.reset
    @game_over = false
  end

  def play_again?
    puts ""
    puts "Would you like to play again?"
    gets.chomp.downcase.start_with?('y')
  end

  def deal_cards
    2.times do
      human.cards << deck.deck.pop
      computer.cards << deck.deck.pop
    end
  end

  def player_hit
    loop do
      break unless human.player_hit?
      human.cards << deck.deck.pop
      system "clear"
      display_all_hands
      return if human.bust?
    end
  end

  def computer_hit
    loop do
      break if computer.hand_amount > 17
      computer.cards << deck.deck.pop
      clear
      display_all_hands
      sleep 1
    end
  end

  def hit
    if type == :player
      player_hit
    else
      computer_hit
    end
  end

  def display_winner
    @game_over = true
    clear
    return "Player Bust! You Lost." if human.bust?
    return "Dealer Bust! You Won!" if computer.bust?
    if human.hand_amount > computer.hand_amount
      "You Won!"
    else
      "Dealer Won!"
    end
  end

  def display_all_hands
    puts "===== #{human.name}'s' Hand: #{human.hand_amount} ====="
    human.display_cards
    puts ""
    puts "===== Dealer Hand#{": #{computer.hand_amount}" if @game_over} ====="
    computer.display_cards(@game_over)
  end

  def clear
    system "clear"
  end

  def welcome
    clear
    puts "Welcome to 21 Blackjack."
    loop do
      puts "What's your name?"
      human.name = gets.chomp.capitalize
      break unless human.name.empty?
      puts "Sorry, must enter a value"
    end
    clear
  end

  def goodbye
    clear
    puts "Thank you for playing, good bye."
  end
end

Game.new.play
