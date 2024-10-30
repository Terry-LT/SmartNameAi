import os
from message import print_alert_message,print_warning_message
from file import  supported_extensions, File, supported_image_extensions

class FilesInFolder:
    files_in_folder_exist_and_has_supported_files = False
    files_path = []
    def __init__(self, folder_path):
        if os.path.isdir(folder_path):
            files_name = os.listdir(folder_path)
            if files_name.__len__() > 0:
                supported_files = []
                for f in files_name:
                    if os.path.splitext(f)[1] in supported_extensions or os.path.splitext(f)[1] in supported_image_extensions:
                        supported_files.append(f)
                if supported_files.__len__() > 0:
                    for s in supported_files:
                        self.files_path.append(os.path.join(folder_path,s))
                    self.files_in_folder_exist_and_has_supported_files = True
                else:
                    print_warning_message("There is no supported files in this folder!")
            else:
                print_warning_message("The folder does not have files!")
        else:
            print_warning_message("The folder does not exist.")
            self.folder_exists_and_has_supported_files = False
    def rename(self):
        for f_path in self.files_path:
            file = File(file_path=f_path)
            file.rename()