# this gotchas file contains a number of observations, which should be taken into account

1) The holiday list from the API seems to only bo back to 2015, we would need some other lookup API to go further back.
2) The holiday list has future dates, which should be ommited for processing
3) There are 3 divisions in the holidays list, each showing different selection of bank holidays
   england-and-wales, scotland,northern-ireland. We need to add a parameter to select the valid division first
4) When requesting data for a Location which isn't recorded in the Weather API we get no woeid. In such cases we will 
   return a message, or change the location box to RED    
5) There is no future data in the database, so we need to reject any request for a future date or return a message
