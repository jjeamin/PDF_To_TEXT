# -*- coding: utf-8 -*-
import os
import re
from tqdm import tqdm
from tkinter.filedialog import askopenfilename
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter,resolve1
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter

def page_count(pdf_path):
    file = open(pdf_path, 'rb')
    parser = PDFParser(file)
    document = PDFDocument(parser)

    # This will give you the count of pages
    print(document.get_dest)
    print(resolve1(document.catalog['Pages'])['Count'])

def clean_text_file(path):
    f = open(path,"rb")
    line_list = []

    while True:
        line = f.readline()
        line_list.append(line)
        if not line: break

    #empty remove
    result = b" ".join(line_list).split()
    txt = b" ".join(result)

    #ASCII remove
    pattern = re.compile(b"[\x80-\xff]")
    clean_txt = re.sub(pattern,b"",txt)

    #sentense
    #clean_txt = txt.split(b". ")

    f.close()

    return clean_txt.decode('utf-8')

def translation(text):
    translator= Translator(to_lang="ko")

    for i in text:
        translation = translator.translate(str(i,'utf-8'))
        print(translation)

    #return trans_text

def isExistFile(file_path):
    file_name = file_path.split('/')[-1]

    for i in os.listdir("."):
        if file_name == i:
            return True

    return False

def pdf2txt():
    #input
    password=''
    pagenos=set()
    maxpages=0

    # output
    imagewriter = None
    rotation = 0
    codec = 'UTF-8'
    pageno = 1
    scale = 1
    caching = True
    showpageno = True
    laparams = LAParams()

    #input file
    input_file = askopenfilename()
    infp = open(input_file,"rb")

    #output file
    output_file = input_file[:-4] + '_trans.txt'

    #
    if isExistFile(output_file):
        infp.close()
        return output_file

    outfp = open(output_file,"w",encoding='UTF8')

    #page total num
    parser = PDFParser(infp)
    document = PDFDocument(parser)
    page_total_num = resolve1(document.catalog['Pages'])['Count']

    #
    rsrcmgr = PDFResourceManager(caching=caching)

    # pdf -> text converter
    device = TextConverter(rsrcmgr,
                           outfp,
                           codec=codec,
                           laparams=laparams,
                           imagewriter=imagewriter)

    # pdf -> text interpreter
    interpreter = PDFPageInterpreter(rsrcmgr,device)

    #pdf -> text start
    with tqdm(total=page_total_num) as pbar:
        for page in PDFPage.get_pages(infp,
                                      pagenos,
                                      maxpages,
                                      password=password,
                                      caching=caching,
                                      check_extractable=True):

            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)

            pbar.update(1)

    print('success')

    outfp.close()
    infp.close()

    return output_file

path = pdf2txt()
clean_text = clean_text_file(path)
print(clean_text)
