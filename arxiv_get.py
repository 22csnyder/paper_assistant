"""arxiv_get.py"""

import arxiv 
import os, re, requests, time
import requests


def arxiv_id2url(arxiv_id):
    return f"https://arxiv.org/abs/{arxiv_id}"


test_id = '2403.06634'
test_url=arxiv_id2url(test_id)
from guess_metadata import get_metadata,llm_infer_filename
guess_filename=llm_infer_filename(test_url)


from dotenv import load_dotenv
load_dotenv()
BOX= os.getenv("BOX")
PAPERS = os.path.join(BOX,"PAPERS, BOX")
assert os.path.exists(PAPERS)


paper = next(arxiv.Client().results(arxiv.Search(id_list=[test_id])))
# Download the PDF to the PWD with a default filename.
# paper.download_pdf()
# Download the PDF to the PWD with a custom filename.
# paper.download_pdf(filename="downloaded-paper.pdf")




# Download the PDF to a specified directory with a custom filename.
paper.download_pdf(dirpath=PAPERS, filename=guess_filename)