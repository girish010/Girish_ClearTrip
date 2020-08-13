# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:40:25 2020

@author: Girish_Rathode
"""
user_avatar_text = "XPATH,//li[@class='menuItem listMenuContainer userAccountMenuContainer']//span[text()='$value']"
round_trip_radio_button = "ID,RoundTrip"
from_text_field = "NAME,origin"
destination_text_field = "NAME,destination"

from_date = "ID,FromDate"
return_date = "ID,ReturnDate"

calendar_date_selector = "XPATH,//table[@class='calendar']//td[@data-year='$value1' and @data-month='$value2']" \
                         "/a[text()='$value3']"

search_flights_button = "ID,SearchBtn"

