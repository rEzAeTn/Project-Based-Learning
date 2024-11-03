from abc import ABC, abstractmethod
from pathlib import Path

from src.nlp.text_processor import (ConvertCase, RemoveDigit, RemovePunkt,
                                    RemoveSpace, StripAccent, TextPipeline)






class SearchEngine:                  # Union[str, path]  ---> # from typing import Union
    def __init__(self, documents_path: str, stop_words: list = None):

        # Crawl Data
        self.data = self.crwl(documents_path)

        # Load Text PreProcess
        self.pipe = TextPipeline(ConvertCase, StripAccent(), RemoveDigit(), RemovePunkt(), RemoveSpace())

        # Load Stop Words
        if stop_words == None:
            stop_words = open('data/stop_words.txt').read().split('\n')
        self.stop_words = stop_words
        stop_words = list(map(self.pipe.transform, stop_words))


        # Index Data
        self.index = self.index_data()



    # Crawling
    def crwl(self, documents_path):
        # data = {keys=file_name, value=file.read}
        data = {}

        for doc_path in list(Path(documents_path).iterdir()):
            if doc_path.suffix != '.txt':
                continue

            with open(doc_path) as f:
                doc_name = doc_path.stem.replace('_', ' ').title()
                # data[key] = value
                data[doc_name] = f.read()

        return data



    # Indexing
    def index_data(self, ):
        index = {}

        for doc_name, doc_content in self.data.items():
            for word in  doc_content.split():
                word = self.pipe.transform(word)

                # Empty Words
                if not word:
                    continue

                # Ignore(remove) Stop Words
                if word in self.stop_words:
                    continue

                # Add to index
                if word in index:
                    index[word].add(doc_name)
                else:
                    index[word] = {doc_name}

            return index





if __name__ == '__main__':
    searcher = SearchEngine(documents_path='data/documents', )
