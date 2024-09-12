from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By # Util that helps to select elements with XPath
import csv # CSV library that helps us save our result

options = Options() 
options.add_argument("--headless") # Run selenium under headless mode
 
driver = webdriver.Chrome(options=options) # Initialize the driver instance

filecsv = open('FBREF.csv', 'w', encoding='utf8') # Creates a CSV file called "FBREF" 
csv_columns = ['Rank', 'Squard', 'MP', 'W','D', 'L', 'GF', 'GA','GD','Pts','Pts/MP', 'xG', 'xGA', 'xGD','xGD/90'] # Columns for the data imported
writer = csv.DictWriter(filecsv, fieldnames = csv_columns)
writer.writeheader()

driver.get("https://fbref.com/en/comps/9/2018-2019/2018-2019-Premier-League-Stats") 
# products = driver.find_elements(By.XPATH, '//*[@id="results2018-201991_overall"]')
products = driver.find_elements(By.XPATH, '//*[@id="results2018-201991_overall"]/tbody/tr')

number = 0

for product in products:

    number += 1 # this line is used to spot errors

    #product.find_element(By.XPATH, where "make edits"). "make edits"
    rank = product.find_element(By.XPATH, ".//th").text # the output of this is rank 
    squard = product.find_element(By.XPATH, ".//a").text # supposed to find the team names
    mp = product.find_element(By.XPATH, ".//td[@data-stat='games']").text # the outpiut of this is man city
    w = product.find_element(By.XPATH, ".//td[@data-stat='wins']").text
    d = product.find_element(By.XPATH, ".//td[@data-stat='ties']").text
    l = product.find_element(By.XPATH, ".//td[@data-stat='losses']").text
    gf = product.find_element(By.XPATH, ".//td[@data-stat='goals_for']").text
    ga = product.find_element(By.XPATH, ".//td[@data-stat='goals_against']").text 
    gd = product.find_element(By.XPATH, ".//td[@data-stat='goal_diff']").text
    pts = product.find_element(By.XPATH, ".//td[@data-stat='points']").text
    pts_per_match = product.find_element(By.XPATH, ".//td[@data-stat='points_avg']").text
    xg = product.find_element(By.XPATH, ".//td[@data-stat='xg_for']").text
    xga = product.find_element(By.XPATH, ".//td[@data-stat='xg_against']").text
    xgd = product.find_element(By.XPATH, ".//td[@data-stat='xg_diff']").text
    xgd_per_90 = product.find_element(By.XPATH, ".//td[@data-stat='xg_diff_per90']").text

    writer.writerow({'Rank': rank, 'Squard': squard, 'MP': mp, 'W': w, 'D': d, 'L': l, 'GF': gf, 'GA': ga, 'GD': gd, 'Pts': pts, 'Pts/MP': pts_per_match, 'xG': xg, 'xGA': xga, 'xGD': xgd, 'xGD/90': xgd_per_90}) #csv_column in quotes, the product on the other side
 
print("The number of product is", number) # this line is used to spot errors

filecsv.close()
driver.close()


# //*[@id="results2018-201991_overall"]/tbody/tr[1] #the XPATH for 1 column in the table
