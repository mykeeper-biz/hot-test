# hot-instinet
 
## Python Technical Assessment 
 
### INTRODUCTION 
 
This exercise is designed to allow candidates to demonstrate their coding abilities on a simplified use-case. It should take no longer than 1-2 hours to produce a minimal solution. Candidates will be asked to discuss their solution during the technical interview and consider how it could be extended to accommodate other usecases. 
 
The DevOps & Engineering group often leverages open source software and tooling. To ensure close integration with Instinet’s ecosystem it is often necessary to extend and enhance the functionality of this software. This typically involves leveraging HTTP / RESTful APIs.  
 
This assessment asks candidates to write a small application which utilises two third-party APIs to retrieve and cross-reference data. Information about these APIs is provided on the next page. Candidates are encouraged to demonstrate how they would typically structure their projects, e.g. dependency management via pip. 
 
Solutions should be packaged up into a compressed file, along with any supporting documentation, and returned at least 24 hours prior to the technical interview. 
 
Sometimes the Nomura / Instinet e-mail server will quarantine e-mails that have attachments containing executable code. To avoid this issue, the submitted ZIP file should not contain any compiled code. Alternatively candidates can use third-party file hosting facilities (e.g. Dropbox, OneDrive) to provide their solution. 
 
 
### INSTRUCTIONS 
 
The API Reference (next page) provides details on how to retrieve public holidays and historic weather data. 
 
#### Exercise One: 
What was the highest / lowest temperature on a specific bank holiday? 
 
Candidates should write a small application to retrieve the highest / lowest temperature recorded on a specific holiday: “What was the highest temperature in Liverpool on Good Friday in 2019?” 
 
###### Application Arguments 
 **Location** 
 – The name of a **UK** city that the weather data should be retrieved for Example argument “Liverpool”
  
 **Bank Holiday** 
 – The name of the bank holiday to look-up Example argument: “Good Friday”
  
 **Year**
– The year that the bank holiday took place (relevant for holidays with non-fixed dates)  Example Argument: 2019 
 
##### Exercise Two: 
Which year had the hottest bank holiday? 
 
Candidates should write a small application to identify which year recorded the highest temperature for a specific holiday: “Which year recorded the highest temperature Good Friday in Liverpool?” 
 
###### Application Arguments 
**Location**
 – The name of a UK city that the weather data should be retrieved for Example argument “Liverpool”
  
**Bank Holiday**
 – The name of the bank holiday to look-up Example argument: “Good Friday”   

 
 
 
 
 
 
## API Reference 
 
 
### BANK HOLIDAY API 
 
The UK Government provides a list of historic bank holidays via their gov.uk portal: 
 
https://www.gov.uk/bank-holidays.json 
 
 
 
### WEATHER API 
 
The Metaweather API provides temperature information from specific dates / locations: 
 
https://www.metaweather.com/api/location/<woeid>/<yyyy>/<mm>/<dd>/ 
 
Location parameters are encoded in “Where on Earth IDentifier” (WOEID) format. Metaweather provide a WOEID lookup API: 
 
https://www.metaweather.com/api/location/search/?query=<city> 
 
For example, the following API call looks-up the WOEID for Liverpool: 
 
https://www.metaweather.com/api/location/search/?query=Liverpool 
 
This returns the WOEID 26734 which can be used to look-up the weather in Liverpool for Christmas 2019 with the following API call: 
 
https://www.metaweather.com/api/location/26734/2019/12/25/  
 
This returns weather information in two-hour increments. For example, the min/max temperature recorded at 23:28:47 was 4.295 / 6.465. 