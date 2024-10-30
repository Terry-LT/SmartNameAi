from rich.prompt import Prompt
import tkinter
from tkinter.filedialog import askopenfilename, askdirectory
from  file import File
from folder import  FilesInFolder


def main():
    while True:
        rename_choice = Prompt.ask("Do you want to rename one file(+) or all files in the specific folder(-)? By default +:", choices=["+", "-"], default="+")
        if rename_choice == "+":
            #Renaming one file
            tkinter.Tk().withdraw()
            file_path = askopenfilename()
            file = File(file_path=file_path)
            file.rename()
        if rename_choice == "-":
            # Renaming all files in the specific folder
            tkinter.Tk().withdraw()
            folder_path = askdirectory()
            folder = FilesInFolder(folder_path=folder_path)
            folder.rename()

if __name__ == "__main__":
    main()