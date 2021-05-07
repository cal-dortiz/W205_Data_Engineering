<center> <h1> W205 Project 1 </h1></center>
<center> <h3> Dan Ortiz </h3></center>
<center> <h3>Thursday 4:00 PM </h3></center>
<center> <h3>T9/27/2020 </h3></center>

## Problem Statement

- You're a data scientist at Lyft Bay Wheels (https://www.lyft.com/bikes/bay-wheels), formerly known as Ford GoBike, the
  company running Bay Area Bikeshare. You are trying to increase ridership, and you want to offer deals through the mobile app to do so. 

- What are the 5 most popular trips that you would call "commuter trips"? 
  
- What are your recommendations for offers (justify based on your findings)?

## Findings and Recomendations

   - Top 5 Commuter Trips
      |Starting Station| Ending Station| Trips|
      |----------------|---------------|------|
      |Harry Bridges Plaza (Ferry Building)| 2nd and Townsend | 4141 |
      |Embarcadero at Sansome|Steuart at Market|4001|
      |San Francisco Caltrain (Townsend at 4th)|Harry Bridges Plaza (Ferry Building)|3877|
      |2nd at Townsend|Harry Bridges Plaza (Ferry Building)|3825|
      |Embarcadero at Folsom|San Francisco Caltrain (Townsend at 4th)|3773|
      
   - Interesting Findings
      - Lyft Bay Wheels most popular commuter routes connect patrons from one mode of transportation to another
      
      - There is directionality in the flow of commuters departing and arriving at stations
      
      - 8.45% of all trips originate or terminate at the 2nd and Townsend terminal. In addition, 8 of the most popular days coordinate with Giants Games at Oracle Park.
      
      - Most patrons traveling to and from Oracle Park live in:
      
         - Mission District
         
         - Greater Oakland Area
         
         - Greater San Rafael Area
 
   - Recommended Promotions
   
      - Push promotions from the Lyft App during the 9th inning to people in the geo-area of Oracle Park
      
      - Push promotions for Morning and Afternoon commuters for intermodal connecting
      
      - Offer a season pass for Giants season pass holders in the identified districts to increase ridership to and from the baseball games
      
   
   - Recommended Further Lines of Inquiry
   
      - Weekends tend to be more popular for bike rentals. Why is this?
      
      - Do bike commuters use our bikes to as a primary mode to commute to work or just to connect between modes of public transportation?
      
      - Are there opportunities to advertise on or partner with bay area public transportation to promote Lyft Bay Area Wheels?

      
## Project Structure

   - **Part 1** (supporting) Use the Big Query GUI to construct and run SQL Queries. Record Queries and Results in a markdown. 
   
   - **Part 2** (supporting) Use Big Query Command Line Interface to run queries. Record CLI queries and results in markdown.
   
   - **Part 3** Integrate query into a jupyter notebook and perform the main analysis.
   
   
## File Links

   - Part 1 and Part 2: [GUI and CLI Query Markdown Notebook](dortiz_project_1.ipynb)
   
   - Part 3: [Bike Share Analysis Notebook](dortiz_project_1_part_3.ipynb)
   


## Tools Used

   - Operating System : Ubuntu Linux
   
   - Tools:
      - **Python Jupyter Notebook** (Structured in Google AI Platform Notebook): Used as the primary interface to explore data and build visualizations
      
      - **Google Big Query**: Query tool for the Lyft Bay Area Bike data
      
      - **Python**: Base kernel for Jupyter notebook
      
      - **Pandas**: Primary package to build data frames and visualizations from queries
      
      - **Matplotlib**: Supplementary package to build visualizations from queries
   
   - Data Source:
      - Static Dataset
      
         - bigquery-public-data.san_francisco.bikeshare_trips
         
         - bigquery-public-data.san_francisco.bikeshare_status
         
         - bigquery-public-data.san_francisco.bikeshare_stations
         
      - Dynamic Dataset (Used for challenge Questions)
      
         - bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info
         
         - bigquery-public-data.san_francisco_bikeshare.bikeshare_regions
         
         - bigquery-public-data.san_francisco_bikeshare.bikeshare_trips)
         
      - San Francisco Rush Hour Data 
      
         - [sfgov.org](https://sfgov.org/scorecards/transportation/congestion)
         
      - Giants Baseball Game Reccords
      
         -[baseball-reference.com](https://www.baseball-reference.com)