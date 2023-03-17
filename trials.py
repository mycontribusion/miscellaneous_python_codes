from pathlib import Path
import PyPDF2
import shutil
import pyarabic.araby
myfolder= Path('try files')

for pickedfile in myfolder.iterdir():
    print(pickedfile)
    try:
        pdfFileObj=open(pickedfile, 'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        pageObj=pdfReader.getPage(0)
        filecontent=pageObj.extractText()
        name= filecontent[:60]
        filename=name.split()
        editedname= []
        for alphabet in filename:
            if alphabet !='\n':
                editedname.append(alphabet)

        delimiter = ' '
        usablename=(delimiter.join(editedname))



        print(usablename)
        shutil.move(pickedfile, f'forcedto/{usablename}.pdf')
    except:
        pass











