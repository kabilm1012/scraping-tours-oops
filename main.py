from webscrape import Event
from database_handling import Database
from send_email import Email
import time

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL, HEADERS)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(database_path="database.db")
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                email = Email()
                email.send(extracted)
        time.sleep(2)