import os
import PyPDF2
delete_list = ["sir james knowles", "knowles", "james knowles", "the legends of king arthur and his knights",
               "samuel e. lowe", "samuel edward lowe", "samuel lowe", "lowe ", "in the court of king arthur",
               "[illustration]", ]


def gutenberg(fin, fout, delete):
    infile = open(fin)
    outfile = open(fout, "w+")
    begin = False
    for line in infile:
        a = line.lower()
        if not begin and not a.startswith("*** start of this project gutenberg ebook"):
            continue
        elif a.startswith("*** start of this project gutenberg ebook"):
            begin = True
            continue
        if a.startswith("*** end of this project gutenberg ebook"):
            break
        for word in delete:
            a = a.replace(word, " ")
        outfile.write(a)
    infile.close()
    outfile.close()


def pdfreader(fin, fout):
    infile = open(fin, 'rb')
    reader = PyPDF2.PdfFileReader(infile)
    outfile = open(fout, "w+")
    print(reader.numPages)
    for page in range(1, reader.numPages):
        x = reader.getPage(page)
        text = x.extractText()
        for line in text:
            a = line.lower()
            outfile.write(a)
    infile.close()
    outfile.close()


if __name__ == "__main__":
    gutenberg("lowe.txt", "loweclean.txt", delete_list)
    gutenberg("knowles.txt", "knowlesclean.txt", delete_list)
