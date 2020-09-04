# FolderToPDFConvertor
AUTHOR: CALVIN VAN WIERINGEN
DATE: 2020/09/03
LANGUAGE: PYTHON
DEPENDANCIES: OS, DOCX2PDF, TKINTER, SHUTIL, SUBPROCESS


This script will allow the user to select a folder with a dialog box. 
The folder will then be cloned into the same location with "_PDFClone" added to the name. 
The script then searches the folder and all sub folders for .doc and .docx files and converts them to PDF. 
After which the .doc and .docx files are deleted. 
This is useful for exporting folders to pdf when seing files to clients in business.

KNOWN BUGS:
If file not selected the current location of the file will be used - exit the program when this happens and delete the unwanted cloned folder.

