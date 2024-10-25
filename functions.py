from camel.loaders import Firecrawl
from camel.toolkits import FunctionTool

firecrawl = Firecrawl()

def load_url(url: str) -> str:
    """
    Load a URL and return the markdown content.
    :param url:
    :return: the markdown functions
    """
    response = firecrawl.scrape(url=url)
    return response["markdown"]

guess_tools = [FunctionTool(load_url), ]


