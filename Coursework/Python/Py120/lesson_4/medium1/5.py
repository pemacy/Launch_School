'''
How could you change the light_status method name below so that the method
name is clearer and less repetitive?
'''

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def status(self):
        return (f'I have a brightness level of {brightness} '
                f'and a color of {color}')

my_light = Light(50, 'Red')
print(my_light.status())
