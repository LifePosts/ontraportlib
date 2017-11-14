# -*- coding: utf-8 -*-

"""
    ontraportlib.models.address
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 11/14/2017
"""
import  ontraportlib.models.base_model

class Address(ontraportlib.models.base_model.BaseModel):

    """Implementation of the 'Address' model.

    TODO: type model description here.

    Attributes:
        address (string): TODO: type description here.
        city (string): TODO: type description here.
        country (string): TODO: type description here.
        state (string): TODO: type description here.
        zip (string): TODO: type description here.
        address_2 (string): TODO: type description here.

    """

    def __init__(self, 
                 address = None,
                 city = None,
                 country = None,
                 state = None,
                 zip = None,
                 address_2 = None):
        """Constructor for the Address class"""
        
        # Initialize members of the class
        self.address = address
        self.city = city
        self.country = country
        self.state = state
        self.zip = zip
        self.address_2 = address_2

        # Create a mapping from Model property names to API property names
        self.names = {
            "address" : "address",
            "city" : "city",
            "country" : "country",
            "state" : "state",
            "zip" : "zip",
            "address_2" : "address2",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            address = dictionary.get("address")
            city = dictionary.get("city")
            country = dictionary.get("country")
            state = dictionary.get("state")
            zip = dictionary.get("zip")
            address_2 = dictionary.get("address2")
            # Return an object of this model
            return cls(address,
                       city,
                       country,
                       state,
                       zip,
                       address_2)