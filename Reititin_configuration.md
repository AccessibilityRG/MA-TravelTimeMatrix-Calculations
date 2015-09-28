# Calculation parameters
Calculations of 2015 MetropAccess-Travel Time Matrix are based on schedules of Monday 07.09.2015. 
 
2015 Travel Time Matrix will include travel times and distances based on two different times of the day:
1. Midday (optimized between 12:00-13:00) --> Comparable with 1st version of MetropAccess-Travel Time Matrix
2. Rush hour (optimized between 08:00-09:00) --> New for 2015 version of TTM!

Travel times by public transportation are optimized using 10 different departure times within the calculation hour using so called [Golomb ruler](https://en.wikipedia.org/wiki/Golomb_ruler).
The fastest route from these calculations are selected for the final travel time matrix.
Walking speed is set to 70 meters per minute (4.2 km/h).
 
**See detailed Reititin configuration files from here:**

- Midday (12:00-13:00):

    - [Public Transportation](Configuration/confMassaAjo2015_PT.json)
    - [Walk](Configuration/confMassaAjo2015_Walk.json)

- Rush hour (08:00-09:00):

    - [Public Transportation]()
    - [Walk]()
