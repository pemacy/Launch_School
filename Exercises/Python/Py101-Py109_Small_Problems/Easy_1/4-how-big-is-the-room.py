'''
Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
'''

SQ_METER_TO_SQ_FEET = 10.7639

print('Find area of room, all units in meters')
length = float(input('Enter length of room: '))
width = float(input('Enter width of room: '))

area_meters = length * width
area_feet = area_meters * SQ_METER_TO_SQ_FEET

print(f'Area in meters: {area_meters:.3f} sq-meters')
print(f'Area in feet: {area_feet:.3f} sq-ft')
