import json
from util.extraction import ExtractionHelper
import json


def extract_metadata():
    """
    Extracts metadata from the earnings data.

    Reads the earnings data from 'earnings/earnings.json' file,
    performs metadata extraction using the Extraction class,
    and prints the extracted metadata.

    Args:
        None

    Returns:
        None
    """
    with open('earnings/earnings.json') as file:
        data = json.load(file)
    extraction = ExtractionHelper()
    metadata = extraction.extract_metadata(",".join(data))
    print(metadata.result)

extract_metadata()

