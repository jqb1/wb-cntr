class FileHandler:
    def __init__(self, filename, output_filename):
        self.output_filename = output_filename

        self.read_file(filename)

    def read_file(self, filename):
        try:
            with open(filename) as f:
                for line in f:
                    print(line)
        except IOError:
            raise IOError('An Error occurred wile trying to open a file. Did you pass correct name?')