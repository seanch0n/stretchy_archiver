# stretchy_archiver

stretchy_archiver is a way of storing PDF files in elasticsearch. This gives you the crazy search abilities of elasticsearch, across all your PDFs.

A while back working in objective-c I realized that "everything lives on the internet forever" is not actually true. Seriously, go try and do anything in objective-c and you'll find answers on how to do it in swift.
Since then, I have been saving PDFs of most web pages I go to that I find useful. Interesting blog posts, tech write ups, etc.
However, searching all of these for something I'm looking for is a pain. 

With this system, all the text of the document is stored in elasticsearch, easily searchable. No more digging through PDFs attempting to find the one I'm looking for, or keeping notes on what content is in which PDF.

To use it, start elasticsearch. I'm using a docker container, you do whatever you want.

Then, simply point the script at your instance, then your pdf file, and *go*
```
python3 uploader my_pdf.pdf
```
