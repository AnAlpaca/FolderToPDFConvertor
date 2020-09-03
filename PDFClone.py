import tkinter, tkinter.filedialog
import shutil, os
import docx2pdf
import subprocess
from docx2pdf import convert
from subprocess import call

print('test')
root = tkinter.Tk()
root.withdraw()
dirname = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory to clone')
absDirName = os.path.abspath(dirname)
absDirNameNew = absDirName + "_PDFclone"
print(absDirName)
print(absDirNameNew)
#os.chdir('dirname')
shutil.copytree(absDirName, absDirNameNew)




# The top argument for walk
topdir = absDirNameNew

# The extension to search for
exten_1 = '.docx'
exten_2 = '.doc'

# The main function
print("\nPDF Conversion In Progress\n")
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten_1):
            docx_path = os.path.join(dirpath, name)
            convert(docx_path)
        elif name.lower().endswith(exten_2):
            doc_path = os.path.join(dirpath, name)
            convert(doc_path)
print("\nPDF Conversion Done!\n")
print("\nRemoving Word Documents\n")
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten_1):
            docx_path = os.path.join(dirpath, name)
            os.unlink(docx_path)
        elif name.lower().endswith(exten_2):
            doc_path = os.path.join(dirpath, name)
            os.unlink(doc_path)
print("\nClone Successfull\n")