import instructor
from openai import OpenAI
from assets.metadata import MayBeMetadata

class ExtractionHelper:
    def __init__(self, openai):
        self.instructor = instructor.patch(openai)

    
    def extract_metadata(self, text) -> MayBeMetadata: # type: ignore
        return self.instructor.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=MayBeMetadata,
            messages=[
                {"role": "user", "content": text},
            ],
        )  # type: ignore
    
