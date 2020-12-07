def read_file(filename:str):
    with open(filename) as f:
        return [line.rstrip() for line in f]