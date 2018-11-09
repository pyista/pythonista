import argparse
import os
import PyPDF2

parser = argparse.ArgumentParser()
parser.add_argument('--paths', nargs='*', help='PDF paths')
args = parser.parse_args()
# print(args.paths)


def PDFmerge(pdfs, output):

    pdfMerger = []
    pdfWriter = PyPDF2.PdfFileWriter()

    for pdf in pdfs:
        pdfMerger.append(pdf)
    for file in pdfMerger:
        pdfFileobj = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileobj)
        for page in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(page)
            pdfWriter.addPage(pageObj)
    pdfOutput = open(output, 'wb')
    pdfWriter.write(pdfOutput)
    print('Merged Successfully')


if __name__ == "__main__":
    output = 'merged_pdf.pdf'
    PDFmerge(args.paths, output)
