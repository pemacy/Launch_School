module Screen
  module Widgets

    module MacOS
      DEFAULT_RESOLUTION = [1024, 768]
    end
  end
end

# Alternative syntax

module Screen::Widgets::MacOS::Button
  def self.inspect_nesting
    puts Module.nesting.inspect
    puts Screen::Widgets::MacOS::DEFAULT_RESOLUTION
  end
end

p Screen::Widgets::MacOS::Button.inspect_nesting
# => [Screen::Widgets::MacOS::Button]
