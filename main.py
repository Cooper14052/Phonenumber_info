import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = phonenumbers.parse('+')

valid = phonenumbers.is_valid_number(number)
carrier = carrier.name_for_number(number, 'ru')
region = geocoder.description_for_number(number, 'ru')

print(valid)
print(carrier)
print(region)
