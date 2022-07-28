#!/usr/bin/env python3

import PyPDF2
from elasticsearch import Elasticsearch
import json


def parse_pdf(filename: str) -> str:
    '''parse the pdf into a dict of its meta data and contents to be sent to elastic
    return json data of the dict'''
    read_pdf = PyPDF2.PdfFileReader(filename, strict=False)
    pdf_meta = read_pdf.getDocumentInfo()
    num = read_pdf.getNumPages()
    all_pages = {}
    all_pages["meta"] = {}
    for meta, value in pdf_meta.items():
        # add meta data for the pages
        all_pages["meta"][meta] = value
    
    # add text from the pages
    for page in range(num):
        data = read_pdf.getPage(page)
        page_text = data.extractText()
        all_pages[page] = page_text

    try:
        json_data = json.dumps(all_pages)
    except json.JSONDecodeError as e:
        raise(e)
    
    return json_data

def upload_to_es(es: Any, json_data: str, filename: str) -> Any:
    '''upload the pdf data to elastic. data goes under "data", the filename
    associated with the file goes under "filename"'''
    body_doc = {"data": json_data, "filename": filename}
    # get the current number of documents in the index so we know our ID
    es.indices.refresh('pdf')
    index_ID = es.cat.count('pdf', params={'format':'json'})[0]['count'] + 1
    result = es.index(index='pdf', doc_type="_doc", id = index_ID, body=body_doc)

    return result

def main():
    # connect to the docker elasticsearch instance
    es = Elasticsearch(hosts = [{"host":"localhost", "port":"9200"}])

    filename = "filename.pdf"
    json_data = parse_pdf(filename)

    print(upload_to_es(es, json_data))

if __name__ == "__main__":
    main()