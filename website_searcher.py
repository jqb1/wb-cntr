from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


class WebsiteParser:

    def manage_websites(self, websites):
        websites_info = []
        for website in websites:
            single_website_info = self.get_html(website)
            websites_info.append(single_website_info)
        return websites_info

    def get_html(self, website):
        website_data = {}

        if website == 'localhost':
            website = 'localhost:8000/localhost_template.html'

        # checking the link structure
        m = re.match(r"http.:", website)
        if not m:
            website = "http://%s" % website
        # get html code of the website
        html = urlopen(website)

        tag_num = self.soup_read(html)
        website_data['address'] = website
        website_data['tag_num'] = tag_num
        return website_data

        # print(html.read().decode('utf-8'))

    def soup_read(self, html):
        soup = BeautifulSoup(html.read(), "html.parser")

        # tag list

        tag_list = soup.body.find_all('button')

        regex = re.compile('submit|reset|button')
        tag_list2 = soup.body.find_all('input', {'type': regex})

        regex2 = re.compile('(?i).*btn.*|(?i).*button.*')
        tag_list3 = soup.body.find_all('', {'class': regex2})

        # all tags to one list, make it set in order to eliminate duplicates
        all_tags = set(tag_list + tag_list2 + tag_list3)

        # print(soup.body.find_all('', {'class': regex2}))
        all_button_num = len(all_tags)
        return all_button_num
