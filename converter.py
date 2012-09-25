#!/usr/bin/env python
# encoding: utf-8
import subprocess
import os
import sys
import djangosettings
from nome.models import *

# constants
TEXTILE_DOCUMENT_FILEPATH = "doc.textile"
MARKDOWN_DOCUMENT_FILEPATH = "doc.markdown"
PANDOC_COMMAND = "pandoc"

# avoiding encoding issues
reload(sys)
sys.setdefaultencoding( "utf-8" )

def touch_file(content):
    file = open(TEXTILE_DOCUMENT_FILEPATH, 'w')
    file.write(content)
    file.close()

def read_file():
    file = open(MARKDOWN_DOCUMENT_FILEPATH, 'r')
    new_summary = file.read()
    file.close()
    return new_summary

def delete_file(file):
    os.remove(file)

def erase_temp_files():
    delete_file(TEXTILE_DOCUMENT_FILEPATH)
    delete_file(MARKDOWN_DOCUMENT_FILEPATH)

# Convert all kb articles to markdown
for article in KbArticles.objects.all():
    
    # write article summary in textile in temp file
    touch_file(article.summary)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_summary = read_file()

    # write article content in textile in temp file
    touch_file(article.content)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result
    new_content = read_file()

    # update database
    article.content = new_content
    article.summary = new_summary
    article.save()
    print "updated article ", article.id
    
# erase temp files
# erase_temp_files()
    
# Convert all wiki pages to markdown
for wikipage in WikiContents.objects.all():
    
    # write wikipage text in textile in temp file
    touch_file(wikipage.text)
    # run pandoc to convert to markdown
    subprocess.call([PANDOC_COMMAND, TEXTILE_DOCUMENT_FILEPATH, "-o", MARKDOWN_DOCUMENT_FILEPATH])
    # read converted result from markdown file
    new_text = read_file()
    
    # update database
    wikipage.text = new_text
    wikipage.save()
    print "updated wikipage ", wikipage.id

# erase temp files
erase_temp_files()