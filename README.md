# wongnaicafeanalysis
### This project is for education purpose only
This project is created to study about how to scrap the data via the website and visualize to get insight about top cafe in bangkok via python

Note: this project is my first project that use python so some of the function can be developed further For example you can use pandas library instead of the list manage function(list_edit_func.py)

# Require Library
1.beautifulsoup4 4.11.1

2.selenium 4.7.2

# How to scrap 
you can scrap by running the data_scraping.py file and execute the scrap_gen_data function however you can choose the desired page by modify the 
The main python file consist of 4 main file which are

in order to start the scrap you will need the url of the desire page that you want to scrap and then you can use the data_scraping function in data_scraping_func.py file to start the scraping process
###### 1. data_scraping_func.py 
This python code store the function that mainly about scraping the data via bs4 and selenium. You can modify the selector in data_scraping(url) function to choose what text do you want select.
###### 2. manage_csv.py
Due to this project was created when I start to learn about python in that time I do not realise the pandas library. So I created the function that manage the csv file. However, you can neglect this file and use the pandas library instead.
###### 3. list_edit_func.py
This python code was created to write and read a list and dict to a text file
###### 4. data_scraping.py 
The data_scraping.py is the trigger file that will trigger the function in data_scraping_func.py and read the stored data via the manage_csv.py and list_edit_func.py
