from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyodbc
import random

x=0
while x<200:

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)

    url = "https://barkingmad.co.za/click-to-feed-2019-2/#"

    driver.get(url)

    js_code = """
    setInterval(function() { 
    document.getElementById("clicktofeedlink").click(); 
    }, 1000 / 1);
    """

    driver.execute_script(js_code)
   
    time.sleep(5)

    driver.quit()
    x+=1
    y= x*0.5
    q= x*10
    o = str(q)
    print(y,"R" + o)
    sql = 'DELETE DS_Rates INSERT INTO DS_Rates (Currency,Quantity,Rate, Date) VALUES ({}, {}, {}, GETDATE())'.format(x,y,q)
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Theebonewsql;'
                      'Database=SysproCompanyT;'
                      'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    time.sleep(random.randint(60, 120))
