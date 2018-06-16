from urllib.request import urlopen
import re


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
        print(html.read().decode('utf-8'))
