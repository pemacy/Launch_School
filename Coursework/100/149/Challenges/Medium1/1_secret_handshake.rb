require 'pry'

class SecretHandshake
  SHAKE = {1 => 'wink',
          10 => 'double blink',
          100 => 'close your eyes',
          1000 => 'jump'}

  def initialize(num)
    @num = num.to_i
  end

  def commands
    return [] if @num.zero?
    num = to_bin
    binary = (num.size < 5 ? num : num[1..-1])
    cmds = get_commands(binary).reverse.compact
    num.size < 5 ? cmds : cmds.reverse
  end

  def get_commands(n)
    # binding.pry
    return [SHAKE[n[0].to_i * 10 ** (n.size-1)]] if n.size <= 1
    [SHAKE[n[0].to_i * 10 ** (n.size-1)]] + get_commands(n[1..-1])
  end

  def to_bin
    exp = Math.log2(@num).to_i
    divmod_arr = [nil, @num]
    Decimal.new.convert(divmod_arr, exp).join
  end
end

class Decimal
  def convert(divmod_arr, exp)
    return [divmod_arr[1].divmod(2 ** exp)[0]] if exp == 0
    divmod_arr = divmod_arr[1].divmod(2 ** exp)
    [divmod_arr[0]] + convert(divmod_arr, exp -1)
  end
end

class Binary
  def initialize(num)
    @num = num.to_s
  end

  def convert
    @num.chars.reverse.each_with_index.reduce 0 do |dec, (bin, exp)|
      dec + bin.to_i * (2 ** exp)
    end
  end
end

p SecretHandshake.new(19).commands
