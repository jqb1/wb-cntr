import argparse
from file_handler import FileHandler
from website_searcher import WebsiteParser


# here is where we start
def main():
    # parsing arguments passed when calling script
    parser = argparse.ArgumentParser(description="Choosing input and output file with addresses")
    parser.add_argument('websites_file', help="type input file", type=str)
    parser.add_argument('counted_websites', help="type output file", type=str)

    arg = parser.parse_args()

    file_handler = FileHandler(arg.counted_websites)
    websites = file_handler.read_file(arg.websites_file)

    print(websites)

    WebsiteParser(websites)

main()
