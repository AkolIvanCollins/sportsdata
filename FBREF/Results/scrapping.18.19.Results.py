from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By                                             # Util that helps to select elements with XPath
import csv                                                                              # CSV library that helps us save our result

options = Options() 
options.add_argument("--headless")                                                      # Run selenium under headless mode      # Home_team, away_team, home_goals_away_goals, results,season
 
driver = webdriver.Chrome(options=options)                                              # Initialize the driver instance

filecsv = open('FBREF.18.19.Results.csv', 'w', encoding='utf8')                         # Creates a CSV file called "FBREF"     #### [5] Change the file name for the results             ////
csv_columns = ['home_team', 'away_team', 'home_goals', 'away_goals','results',]         # Columns for the data imported         #### [3] Make changes to the headers for the csv files    ////
writer = csv.DictWriter(filecsv, fieldnames = csv_columns)
writer.writeheader()

driver.get("https://fbref.com/en/comps/9/2018-2019/schedule/2018-2019-Premier-League-Scores-and-Fixtures") #### [1] Change the link from where we are getting the data                  ////
products = driver.find_elements(By.XPATH, '//*[@id="sched_2018-2019_9_1"]/tbody/tr')                       #### [2] Change the XPATH to the table                                      ////

number = 0                                                                             # This is used to spot errors

for product in products:

    number += 1                                                                        # This line is used to spot errors

    #product.find_element(By.XPATH, where "make edits"). "make edits"
    home = product.find_element(By.XPATH, ".//td[@data-stat='home_team']").text        # The output of this is rank            #### [4] Change to the table to be added to the csv created. 
    away = product.find_element(By.XPATH, ".//td[@data-stat='away_team']").text        # Supposed to find the team names
    home_goals = product.find_element(By.XPATH, ".//td[@data-stat='score']").text 
    away_goals = product.find_element(By.XPATH, ".//td[@data-stat='score']").text
    results = product.find_element(By.XPATH, ".//td[@data-stat='score']").text


    writer.writerow({'home_team': home, 'away_team': away, 'home_goals': home_goals, 'away_goals': away_goals, 'results': results}) # csv_column in quotes, the product on the other side ////
 
print("The number of items  is", number)                                              # This line is used to spot errors

filecsv.close()
driver.close()


# //*[@id="results2018-201991_overall"]/tbody/tr[1] #the XPATH for 1 column in the table
