from pathlib import Path


def save_per_line(filepath, data_list):
    ''' Save list of strings into a file, one string per line. 
        
        Parameters
        -----------------------------------------
        filepath: str
            the path to save the file, eg. "./workspace/file.txt"
        data_list: list
            list of strings, where strings are to be written into 
            file at file_path one per line
    '''

    with Path(filepath).open("w") as f:
        f.writelines([f"{line}\n" for line in data_list])