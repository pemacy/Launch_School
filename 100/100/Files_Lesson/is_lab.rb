# is_lab.rb

a = 'y'
while a == 'y' do
	puts "enter a word to see if lab is in it"
	inp = gets.chomp
	if /lab/ =~ inp
		puts "lab is in #{inp}, want to do it again?: "
		a = gets.chomp
	else
		puts "lab is not in #{inp}, want to play again?: "
		a = gets.chomp
	end
end
