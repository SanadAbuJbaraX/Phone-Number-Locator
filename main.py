from phonenumbers import geocoder,carrier   
import phonenumbers
from opencage.geocoder import OpenCageGeocode
import folium
class PhoneNumber:
    def __init__(self,number,region=None,lang="en"):
        self.lang = lang
        self.phoneNumber = phonenumbers.parse(number=number,region=region)
        self.geocoder = OpenCageGeocode('2cc45f148bf245618ef3c042a6aeb003')
    def parse_data(self):
        self.country = geocoder.description_for_valid_number(self.phoneNumber,self.lang)
        self.service = carrier.name_for_number(self.phoneNumber,self.lang)
        self.location =  [self.geocoder.geocode(str(self.country))[0]['geometry']['lat'],self.geocoder.geocode(str(self.country))[0]['geometry']['lng']]
    def Map(self):
        self.map = folium.Map(location=self.location,zoom_start=11)
        folium.Marker(location=self.location,popup=self.country).add_to(self.map)
        self.map.save("location.html")
        self.map.show_in_browser()

number = PhoneNumber(input('Enter Phone Number: '))
number.parse_data()
print(number.location,number.service,number.country)
number.Map()
