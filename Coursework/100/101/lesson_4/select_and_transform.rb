produce = {
  'apple' => 'Fruit',
  'carrot' => 'Vegetable',
  'pear' => 'Fruit',
  'broccoli' => 'Vegetable'
}

def select_fruit(produce)
  fruit = {}
  counter = 0
  produce_keys = produce.keys
  while counter < produce_keys.size
    if produce[produce_keys[counter]] == 'Fruit'
      fruit[produce_keys[counter]] = produce[produce_keys[counter]]
    end
    counter += 1
  end
  puts fruit
end

select_fruit(produce) # => {"apple"=>"Fruit", "pear"=>"Fruit"}
