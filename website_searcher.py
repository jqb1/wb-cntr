from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


class WebsiteParser:
    def __init__(self, websites):
        self.websites = websites
        self.manage_websites(websites)

    def manage_websites(self, websites):
        for website in websites:
            self.get_html(website)

    def get_html(self, website):
        # checking the link structure
        m = re.match(r"http.:", website)
        if not m:
            website = "http://%s/" % website
        # get html code of the website
        html = urlopen(website)

        self.soup_read(html)

        # print(html.read().decode('utf-8'))

    def soup_read(self, html):
        soup = BeautifulSoup(html.read(), "html.parser")

        #count only in body
        print(soup.body)
        print(len(soup.find_all('button')))

        regex = re.compile('submit|reset|button')
        print(len(soup.find_all('input', {'type': regex})))

        regex2 = re.compile('(?i).*btn.*|(?i).*button.*')
        print(len(soup.find_all('form', {'class': regex2})))

