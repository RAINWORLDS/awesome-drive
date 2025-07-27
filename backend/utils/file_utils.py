import os

def get_file_list(directory="backend/static"):
    return [
        {"filename": f, "size": os.path.getsize(os.path.join(directory, f))}
        for f in os.listdir(directory)
    ]
