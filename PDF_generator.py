from reportlab.pdfgen import canvas

# Ask user for file name
pdf_file = input("Type file name + .pdf: ")

# Check to ensure '.pdf' was included in file type
index = pdf_file.find(".pdf")
if index != -1:
   print("Correct file name!")
   # Ask user for text to put in file
   text = input("Type what you want in the file: ")
   c = canvas.Canvas(pdf_file)
   c.drawString(100, 750, text)
   c.save()
else:
   print("Oops, did you forget to put .pdf file extension? Please try again ")
