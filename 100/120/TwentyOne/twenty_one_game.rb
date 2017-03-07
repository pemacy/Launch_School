class Game
  attr_reader :human, :computer, :deck

  def initialize
    @human = Player.new
    @computer = Player.new(:dealer)
    @deck = Deck.new
    @game_over = false
  end

  def play
    welcome
    deal_cards
    puts display_all_hands
    player_hit
    player_bust? ? display_winner : computer_hit
    clear
    puts display_winner
    puts ""
    display_all_hands
    goodbye
  end

  def deal_cards
    2.times do
      human.cards << deck.deck.pop
      computer.cards << deck.deck.pop
    end
  end

  def display_winner
    @game_over = true
    puts ""
    return "Player Bust! You Lost." if player_bust?
    return "Dealer Bust! You Won!" if computer_bust?
    if human.hand_amount > computer.hand_amount
      "You Won!"
    else
      "Dealer Won!"
    end
  end

  def player_bust?
    human.hand_amount > 21
  end

  def computer_bust?
    computer.hand_amount > 21
  end

  def hit?
    puts ""
    puts "Hit or Stand? (h/s)"
    answer = gets.chomp.downcase
    answer.start_with?('h') ? true : false
  end

  def player_hit
    loop do
      break unless hit?
      human.cards << deck.deck.pop
      system "clear"
      display_all_hands
      return if human.hand_amount > 21
    end
  end

  def display_all_hands
    puts "===== Human Hand: #{human.hand_amount} ====="
    display_cards(human)
    puts ""
    puts "===== Dealer Hand#{": #{computer.hand_amount}" if @game_over} ====="
    display_cards(computer)
  end

  def clear
    system "clear"
  end

  def display_cards(player)
    if player.type == :player
      puts player.cards
    else
      hidden = [player.cards[0]]
      (player.cards.size - 1).times { hidden << "Hidden Card" }
      puts hidden unless @game_over
      puts player.cards if @game_over
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

  def welcome
    clear
    puts "Welcome to 21 Blackjack."
  end

  def goodbye
    puts ""
    puts "Thank you for playing, good bye."
  end
end

class Player
  attr_accessor :cards, :score, :hand_amount, :type

  def initialize(type = :player)
    self.type = type
    self.cards = []
    self.score = 0
    self.hand_amount = 0
  end

  def hand_amount
    cards.inject(0) { |sum, card| sum += Deck::TOTAL_VALUES[card] }
  end
end

class Deck
  SUITES = %w(Hearts Spades Diamonds Clubs)
  CARDS = %w(2 3 4 5 6 7 8 9 10 Jack Queen King Ace)
  VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
  TOTAL_VALUES = SUITES.map.with_object(hsh = Hash.new) do |s, hsh|
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

Game.new.play
