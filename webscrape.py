import requests
import selectorlib


class Event:
    def scrape(self, url, headers):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=headers)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value

