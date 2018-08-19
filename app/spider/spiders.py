import requests
from bs4 import BeautifulSoup


class Spider:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.status = -1
        self.response = None
        self.soup = None

    def get_response(self):
        try:
            self.response = requests.get(self.url)
            self.status = self.response.status_code
        except Exception as e:
            print(str(e))
        finally:
            print(self.status)
            if self.status != 200:
                return self.response.status_code
            return self.response

    def get_soup(self):
        self.get_response()
        if self.status != 200:
            return BeautifulSoup("<p>nothing</p>", "html.parser")
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        return self.soup

    def __repr__(self):
        return str(self.name) + " " + str(self.status)
