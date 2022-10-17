#!/usr/bin/python3
"""
    Place class file for object creation
    and manipulation in HBnB console.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Place class implementation

        Attributes:
        name - string representing the name of the place
        city_id - string representing the city_id
        user_id - string representing the user_id
        description - string containing the description of the place
        number_rooms - int representing the number of rooms in the place
        number_bathrooms - int representing the number of bathrooms in the place
        max_guest - int representing the maximum guest capacity in the place
        price_by_night - int representing the price established for the place
        latitude - float representing the geographical latitude of the place
        longitude - float representing the geographical longitude of the place
        amenity_ids - list of amenities related to the place
    """
    name = ""
    city_id = ""  # empty string but it will be City.id
    user_id = ""  # empty string but it will be User.id
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # empty list but will have Amenity.id
