from my_belavia_parser_lz import Parser_Belavia
import time
import datetime
import csv
import os
import pandas as pd
from selenium.webdriver.chrome.options import Options

def log(func):
    log_data = {"Function": [func], "Time": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "User": [os.environ.get('USERNAME')]}
    df = pd.DataFrame(log_data)
    df.to_csv('logging.csv', index=False, mode="a", sep=";", header=not os.path.isfile('logging.csv'), encoding="utf-8-sig")

def main():
    parser = Parser_Belavia('https://belavia.by/booking/#/results/11357256459')
    time.sleep(5)
    parser.accept_cookie()

    belavia_one_road = 'belavia_one_road.csv'
    belavia_two_road = 'belavia_two_road.csv'

    try:
        for step in range((datetime.date(2027, 1, 1) - datetime.date(2026, 10, 28)).days):
            for ticket in parser.get_info():
                if len(ticket) < 5:
                    continue

                if len(ticket) < 20:
                     row_info = parser.one_road(ticket)
                     target_file = belavia_one_road
                     func_name_one_road = 'one_road_ticket'
                else:
                     row_info = parser.two_roads(ticket)
                     target_file = belavia_two_road
                     func_name_one_road = 'two_road_ticket'

                file_exists = os.path.exists(target_file)
                with open(target_file, mode='a', newline='', encoding='utf-8-sig') as file:
                    writer = csv.DictWriter(file, fieldnames=row_info.keys(), delimiter=',')
                    
                    if not file_exists:
                        writer.writeheader() 
                        
                    writer.writerow(row_info)

                log(func_name_one_road)
                     
            time.sleep(1)
            parser.click_next_day()
            time.sleep(3)

    except Exception as e:
        print(f'Вы получили ошибку:{e}')

    finally:
        print('Благодарю за использование. Работа закончена!')

if __name__ == "__main__":
    main()