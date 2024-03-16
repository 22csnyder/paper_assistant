"""guess_metadata.py"""

import os, re, requests, time
# from bs4 import BeautifulSoup
from lxml import html
import requests

import marvin

from typing import Dict,Literal
# def get_metadata(url:str)->Dict[Literal["title","date"],str]:
# def get_metadata(url:str)->Dict[str,str]:
@marvin.fn
def get_metadata(url:str)->dict:
    """Returns the title and date of a paper given its URL. 
    Format:
    {"title": "Title of the paper",
     "date": "Month Year"}
    Example:
    some_arxiv_url = "https://arxiv.org/abs/2102.00001"
    Returns:
    {"title": "A New Age for LLMs",
    "date": "March 2023"}
    """
    return requests.get(url).content

    # response = requests.get(url)
    # if response.status_code == 200:
    #     tree = html.fromstring(response.content)
    #     title = tree.xpath('//h1/text()')[0]
    #     date = tree.xpath('//div[@class="dateline"]/text()')[0]
    #     return {
    #         "title": title,
    #         "date": date
    #     }
    # else:
    #     return {
    #         "title": None,
    #         "date": None
    #     }
def test_get_metadata():
    from arxiv_get import arxiv_id2url
    test_id = '2403.06634'
    test_url=arxiv_id2url(test_id)

    # metadata=get_metadata(test_url)
    metadata=get_metadata(url_hf)
    print(metadata)

    assert metadata.keys() == {"title","date"}
    


def llm_infer_filename(url):
    """Returns the filename of a paper given its URL. """

    metadata=get_metadata(url)
    print(metadata)
    title=metadata['title']
    date=metadata['date']
    return f"{title} ({date}).pdf"

    

#from llmwksp/marvin.ipynb
@marvin.fn
def summarize_url(url: str) -> str:
    """
    Returns a summary of the contents of `url`.
    """
    # return the text found at the URL
    return requests.get(url).content 

# summarize_url('https://www.askmarvin.ai')
# import requests
# url_test = 'https://www.labcorp.com/tests/505271/cd4-cd8-ratio-profile'
# requests.get(url=url_test).content
    


url_hf="https://huggingface.co/papers/2403.06634"

arxiv_id="2403.08763"
url_arxiv="https://arxiv.org/abs/2403.08763"

def main():
    # sumdata = summarize_url(url_hf)
    # print(sumdata)


    mdata = get_metadata(url_hf)
    print(mdata)
    # print(get_metadata(url_hf))
    # print(summarize_url(url_hf))
    # print(get_metadata(url_test))

    return 0


if __name__ == "__main__":

    main()


