def read_file(file_name):
    with open(file_name) as testfile:
        return list(map(lambda line_str: line_str.strip(), testfile.readlines()))
