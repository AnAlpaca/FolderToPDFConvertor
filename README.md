# FolderToPDFConvertor
AUTHOR: CALVIN VAN WIERINGEN
DATE: 2020/09/03
LANGUAGE: PYTHON
DEPENDANCIES: OS, DOCX2PDF, TKINTER, SHUTIL, SUBPROCESS

DESCRIPTION:
This script will allow the user to select a folder with a dialog box. 
The folder will then be cloned into the same location with "_PDFClone" added to the name. 
The script then searches the folder and all sub folders for .doc and .docx files and converts them to PDF. 
After which the .doc and .docx files are deleted. 
This is useful for exporting folders to pdf when sending files to clients in business.

HOW TO LAUNCH:
1. Copy the repo to any folder you wish.
2. Open dist folder and scroll to PDFCLone.exe
3. You can run from here or
4. Create shortcut of PDFClone.exe and place in a more useful location.

KNOWN BUGS:
If file not selected the current location of the file will be used - exit the program when this happens and delete the unwanted cloned folder.

