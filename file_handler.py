import csv


class FileHandler:
    def __init__(self, output_filename):
        self.output_filename = output_filename

    def read_file(self, filename):
        websites = []
        try:
            with open(filename) as f:
                reader = csv.reader(f)
                for line in reader:
                    # get first column of every line (web address)
                    websites.append(line[0])

        except IOError:
            raise IOError('An Error occurred wile trying to open a file. Did you pass correct name?')

        return websites

    def make_output_file(self, websites_info):

        output_file = self.output_filename
        for website in websites_info:
            print("Address:%s" % website['address'], "Number of tags: %s" % website['tag_num'])
        try:
            # fieldnames = sorted(list(set(k for d in websites_info for k in d)))
            fieldnames = ['address', 'tag_num']

            with open(output_file, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(websites_info)
        except IOError:
            raise IOError('An Error occurred wile trying to write to a file.')
