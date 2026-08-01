import os
import fitz  # type: ignore # PyMuPDF
from utils import clean_text


def read_pdfs(folder_path):
    """
    Read all PDF files in the folder.
    Returns a list where each page is stored separately.
    """

    documents = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):

            pdf_path = os.path.join(folder_path, filename)

            pdf = fitz.open(pdf_path)

            for page_number, page in enumerate(pdf, start=1):

                page_text = page.get_text()

                page_text = clean_text(page_text)

                if page_text.strip():

                    documents.append(
                        {
                            "filename": filename,
                            "page": page_number,
                            "text": page_text
                        }
                    )

            pdf.close()

    return documents