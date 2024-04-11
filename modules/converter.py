from PyPDF2 import PdfWriter, PdfReader


# This function splits pdf into pages, naming each with their respect student id
def split_pdf(filepath):
    
    inputpdf = PdfReader(open(filepath, "rb"))

    # Dividing Pages
    for number in range(1,len(inputpdf.pages)):
        # Choosing a page
        page = inputpdf.pages[number]
        
        # Writing new pdf
        output = PdfWriter()
        output.add_page(page)
        
        # Search for id
        page_content = page.extract_text().split("\n")
        id = page_content[6].split(' ')[1]
        
        # Saving
        with open(f"files\\save\\id{id}.pdf", "wb") as outputStream:
            output.write(outputStream)

