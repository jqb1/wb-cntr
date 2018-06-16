import argparse
from file_handler import FileHandler


# here is where we start
def main():
    # parsing arguments passed when calling script
    parser = argparse.ArgumentParser(description="Choosing input and output file with addresses")
    parser.add_argument('websites_file', help="type: -file filename if you want to pass your file", type=str)
    parser.add_argument('counted_websites', help="1-easy, other-hard , default - easy", type=int)

    arg = parser.parse_args()

    FileHandler(arg.websites_file, arg.counted_websites)


main()
