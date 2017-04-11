class Pet
  attr_reader :species, :name

  def initialize(species, name)
    @species = species
    @name = name
  end

  def to_s
    "a #{species} named #{name}"
  end
end

class Owner
  attr_accessor :pets
  attr_reader :name
  def initialize(name)
    @name = name
    @pets = []
  end

  def add_pet(pet)
    pets << pet
  end

  def print_pets
    pets.each{ |pet| puts pet}
  end

  def number_of_pets
    pets.size
  end
end

class Shelter
  def initialize
    @owners = []
    @pets_that_need_adoption = []
  end

  def remove_pet_from_adoption_list(pet)
    @pets_that_need_adoption.delete(pet)
  end

  def add_pet_to_shelter(pet)
    @pets_that_need_adoption << pet
  end

  def adopt(owner, pet)
    owner.add_pet(pet)
    remove_pet_from_adoption_list(pet)
    @owners << owner unless @owners.include?(owner)
  end

  def print_adoptions
    @owners.each do |owner|
      puts "#{owner.name} has adopted the following pets:"
      owner.print_pets
      puts
    end
  end

  def print_adoptions_needed
    puts "The Animal shelter has #{@pets_that_need_adoption.size} unadopted pets"
    puts
  end

  def print_unadopted_pets
    puts "The Animal Shelter has the following unadopted pets:"
    @pets_that_need_adoption.each{ |pet| puts pet}
    puts
  end
end

butterscotch = Pet.new('cat', 'Butterscotch')
pudding      = Pet.new('cat', 'Pudding')
darwin       = Pet.new('bearded dragon', 'Darwin')
kennedy      = Pet.new('dog', 'Kennedy')
sweetie      = Pet.new('parakeet', 'Sweetie Pie')
molly        = Pet.new('dog', 'Molly')
chester      = Pet.new('fish', 'Chester')

phanson = Owner.new('P Hanson')
bholmes = Owner.new('B Holmes')

shelter = Shelter.new
shelter.add_pet_to_shelter(butterscotch)
shelter.add_pet_to_shelter(pudding)
shelter.add_pet_to_shelter(butterscotch)
shelter.add_pet_to_shelter(darwin)
shelter.add_pet_to_shelter(kennedy)
shelter.add_pet_to_shelter(sweetie)
shelter.add_pet_to_shelter(molly)
shelter.add_pet_to_shelter(chester)

shelter.print_adoptions_needed
shelter.print_unadopted_pets

shelter.adopt(phanson, butterscotch)
shelter.adopt(phanson, pudding)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)
shelter.print_adoptions
puts "#{phanson.name} has #{phanson.number_of_pets} adopted pets."
puts "#{bholmes.name} has #{bholmes.number_of_pets} adopted pets."
puts

shelter.print_adoptions_needed
shelter.print_unadopted_pets
