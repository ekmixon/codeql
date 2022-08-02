
def separate_headers(files):
    for file in files:
        lines = iter(file)
        try:
            header = next(lines) # Will raise StopIteration if lines is exhausted
        except StopIteration:
            #Empty file -- Just ignore
            continue
        body = list(lines)
        yield header, body
