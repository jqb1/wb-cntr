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



    # def make_output_filename(self,output_filename):
