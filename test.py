import docx

# Load the Word file
doc = docx.Document('file.docx')

# Print the text from each paragraph in the file
for para in doc.paragraphs:
    print(para)
