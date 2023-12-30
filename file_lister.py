import os

def get_file_list(app):
    subfolder_path = os.path.join(app.static_folder, 'subfolder')
    file_list = os.listdir(subfolder_path)
    return file_list
