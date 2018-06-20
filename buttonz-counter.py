import argparse
from operator import itemgetter
from file_handler import FileHandler
from website_searcher import WebsiteParser


# here is where we start
def main():
    # parsing arguments passed when calling script
    parser = argparse.ArgumentParser(description="Choosing input and output file with addresses")
    parser.add_argument('websites_file', help="type input file", type=str)
    parser.add_argument('counted_websites', help="type output file", type=str)

    arg = parser.parse_args()

    # initialization of a file
    file_handler = FileHandler(arg.counted_websites)
    # get list of websites
    websites = file_handler.read_file(arg.websites_file)

    website = WebsiteParser()
    websites_info = website.manage_websites(websites)

    # sort list of websites by value of tag_num
    websites_info = sorted(websites_info, key=itemgetter('tag_num'), reverse=True)

    file_handler.make_output_file(websites_info)


if __name__ == '__main__':
    main()
