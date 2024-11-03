from abc import ABC, abstractmethod
from unidecode import unidecode
import string


class TextProcessor(ABC):

    @abstractmethod
    def transform(self, text):
        pass


class ConvertCase(TextProcessor):
    def __init__(self, conversion='lower'):
        self.conversion = conversion

    def transform(self, text):
        if self.conversion == 'lower':
            return text.lower()
        elif self.conversion == 'upper':
            return text.upper()
        elif self.conversion == 'title':
            return text.title()



class RemoveDigit(TextProcessor):

    def transform(self, text):
        return ''.join(filter(lambda char: not char.isdigit(), text))



# import string
class RemovePunkt(TextProcessor):

    def transform(self, text):
        return ''.join(filter(lambda char: char not in string.punctuation, text))



class RemoveSpace(TextProcessor):

    def transform(self, text):
        return ' '.join(text.split())



# from unidecode import unidecode

class StripAccent(TextProcessor):

    def transform(self, text):
        return unidecode(text)



class TextPipeline(TextProcessor):
    def __init__(self, *args):
        self.transformers = args

    def transform(self, text):
        for tf in self.transformers:
            text = tf.transform(text)

        return text

    def __repr__(self):
        transformers = '\n '.join([f'Step_{i+1}: {tf.__class__.__name__}' for i, tf in enumerate(self.transformers)])  # enumerate('iterable') --> (0, i)
        return f'Pipeline:\n {transformers}'

