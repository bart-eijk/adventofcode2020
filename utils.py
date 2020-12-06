def read_file(filename:str):
    return [line.rstrip() for line in open(filename)]