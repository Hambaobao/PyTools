from pathlib import Path


def save_per_line(filepath, data_list):
    ''' Save list of strings into a file, one string per line. 
        
        Parameters
        -----------------------------------------
        filepath: str
            the path to save the file, eg. "./workspace/file.txt".
        data_list: list
            list of strings, where strings are to be written into 
            file at file_path one per line.
    '''

    with Path(filepath).open("w") as f:
        f.writelines([f"{line}\n" for line in data_list])


def read_per_line(filepath):
    ''' read text from file form of list of string,
        each element of list is a string object.

        Parameters
        ------------------------------
        filepath: str
            the path of file that one will read from.
    '''
    with open(filepath) as f:
        lines = f.readlines()
        lines = [l.strip('\n') for l in lines]

    return lines


def write_text2file(path: str, text: int):
    ''' write string to file
    
        Parameters
        -------------------------
        path: str
            the path to save the file, eg. "./workspace/file.txt".
        text: str
            the content will be write to file.
    '''
    file = Path(path)
    file.parent.mkdir(exist_ok=True, parents=True)
    file.write_text(text)
