from Text_Fw.preprocessing.NLTK_preprocessing import NLTK_preprocessing
from Text_Fw.preprocessing.spacy_preprocessing import spacy_preprocessing

LibraryBase = {
    "nltk":NLTK_preprocessing,
    "spacy":spacy_preprocessing
}
