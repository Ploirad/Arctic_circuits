# Imports go at the top
from microbit import *

days_per_week = 7
hours_per_day = 24
hours_per_week = days_per_week * hours_per_day

seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour

candy = 100
friends = 7
candy_per_friend = candy//friends
rest_candy = candy%friends

display.scroll("Hours per week:")
display.scroll(hours_per_week)
display.scroll("Seconds per hour:")
display.scroll(seconds_per_hour)
display.scroll("Candies per friend:")
display.scroll(candy_per_friend)
display.scroll("Rest candies:")
display.scroll(rest_candy)