#PDF Should be into the same Directory as this code
#pip install pyttsx3

import pyttsx3 
import PyPDF2 
book = open('name.pdf','rb') 
pdf =PyPDF2.PdfFileReader(book) 
pages = pdfReader.numPages 
speaker = pyttsx3.init() 
for i in pages: 
  page = pdfReader.getPage(i) 
  text = page.extractText() 
  speaker.say(text) 
  speaker.runAndWait()
