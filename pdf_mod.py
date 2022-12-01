import PyPDF2
import sys
import os

inputs = os.listdir()[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        if pdf.endswith(".pdf"):
            merger.append(pdf)
            print(merger)
    merger.write('super.pdf')


if __name__ == "__main__":
    pdf_combiner(inputs)


