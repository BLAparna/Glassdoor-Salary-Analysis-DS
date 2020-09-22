## Glassdoor-Salary-Analysis-DS
**This is salary analysis of glassdoor job data exclusively in Us for Data Scientists. This project has been done by closely follwing @ken jee my favorite DS on youtube .
Couple of items to note:

Requirements and Issues and Basecode:

  #I didnt have headquarters and Competitors data (i am not sure why because i am fetching the data from India). 
  #I have choosen US as location since in India i couldn't find salary estimate.
  #Glassdoor scraper is written based on Selenium and pandas ...this code has been provided by Omer sakariya and further modified by Kenjee. Later minor changes are done but (the changes are not huge ...like we were not able to fetch salary for some)
  
  Environment :
    Used Spyder IDE
    Pip install selenium
    Pip install pandas    
    
    you can find the glassdoor scraper and the whole project by following Kenjee video@https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t
    a) Data Collection
    
        Used the glassdoor scraper and fetched 1000 rows . Almost took 46 mins to 1hr approximately
    b) Data Cleaning
        
        Data is cleaned based on
                    #1.Create a state column and sort by state
                    #2.remove rows where salary estimate is -1
                    #3.drop headquarters and competitors column
                    #4.find essential data scientist skills(Python, Rstudio, sas, spark, aws, tableau, powerbi, sql, excel) from job title 
                    #5.remove rating from company and create a column
                    #6 dropped headquarters and competitors as i found no data 
                    #7 generated separated columns for min salary and max salary
     c) 
                    
                    
