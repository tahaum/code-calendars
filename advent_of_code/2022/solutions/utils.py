def read_text_file_standard(path: str): 
    with open(path, 'r') as f:
        data = f.read().splitlines()
    return data