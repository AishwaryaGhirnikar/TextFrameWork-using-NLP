import re
import unicodedata
from Text_Fw.interfaces.preprocessing_interface import preprocessing_interface
import spacy
from Text_Fw.preprocessing.CONTRACTION_MAP import CONTRACTION_MAP

nlp = spacy.load("en_core_web_sm")

class spacy_preprocessing(preprocessing_interface):

    def __init__(self, text):
        self.__text = text
        self.__result = None

    def tokenization(self, parameter_dictionary):
        my_tokens = []
        for words in nlp(self.__text):
            my_tokens.append(words)
        return my_tokens

    def stemming(self, parameter_dictionary):
        pass

    def lemmatization(self, parameter_dictionary):
        my_lem = []
        for words in nlp(self.__text):
            my_lem.append([words.text, words.lemma_])
        return my_lem

    def NER(self, parameter_dictionary):
        doc = nlp(self.__text)
        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)

    def POS(self, parameter_dictionary):
        my_POS = []
        for words in nlp(self.__text):
            my_POS.append([words.text, words.pos_])
        return my_POS

    def remove_stopwords(self, parameter_dictionary):
        my_rem_stop = []
        for words in nlp(self.__text):
            if words.is_stop == False:
                my_rem_stop.append(words.text)
        return my_rem_stop

    def remove_emails(self, parameter_dictionary):
        my_rem_emails = re.sub("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", "", self.__text)
        return my_rem_emails

    def remove_html_tags(self, parameter_dictionary):
        html_tags = re.compile('<.*?[^>]+>')
        my_rem_html = re.sub(html_tags, '', self.__text)
        return my_rem_html

    def remove_numbers(self, parameter_dictionary):
        my_rem_num = re.sub('[0-9]+', '', self.__text)
        return my_rem_num

    def remove_punctuations(self, parameter_dictionary):
        punc_marks = re.compile('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]')
        my_rem_punc = re.sub(punc_marks, '', self.__text)
        return my_rem_punc

    def remove_unicode(self, parameter_dictionary):
        my_rem_unicode = unicodedata.normalize('NFKD', self.__text).encode('ascii', 'ignore').decode("utf-8", 'ignore')
        return my_rem_unicode

    def remove_specialcharacters(self, parameter_dictionary):
        my_rem_splchr = re.sub('[^a-zA-Z0-9 \n\.]', '', self.__text)
        return my_rem_splchr

    def remove_hash_tags(self, parameter_dictionary):
        my_rem_hashtag = re.sub("(#+[a-zA-Z0-9(_)]{1,})", '', self.__text)
        return my_rem_hashtag

    def expand_contractions(self, parameter_dictionary, contraction_mapping=CONTRACTION_MAP):
        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                          flags=re.IGNORECASE | re.DOTALL)

        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match) \
                if contraction_mapping.get(match) \
                else contraction_mapping.get(match.lower())
            expanded_contraction = first_char + expanded_contraction[1:]
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, self.__text)
        expanded_text = re.sub("'", "", expanded_text)
        return expanded_text


if __name__ == "__main__":
    sp = spacy_preprocessing("   This project is based on spacy Processing. It includes 14 methods."
                             "\n numbers = 0123456789,"
                             "\n punctuations = .,:;!?"
                             "\n html tags = <html><title>Insert title here</title></html>"
                             "\n spl chars = @#$#@,"
                             "\n mail id1 = myemail@gmail.com" " mail id2 = myyahoo@gmail.com,"
                             "\n hashtags = #my name is #aishu"
                             "\n contractions = ain't, i'll've, mustn't've, aren't, I'd, I'd've, she'll, so's, mayn't, where've")

    print(sp.tokenization({}))
    print("\n", sp.stemming({}))
    print("\n", sp.lemmatization({}))
    print("\n", sp.NER({}))
    print("\n", sp.POS({}))
    print("\n", sp.remove_stopwords({}))
    print("\n", sp.remove_emails({}))
    print("\n", sp.remove_html_tags({}))
    print("\n", sp.remove_numbers({}))
    print("\n", sp.remove_punctuations({}))
    print("\n", sp.remove_unicode({}))
    print("\n", sp.remove_specialcharacters({}))
    print("\n", sp.remove_hash_tags({}))
    print("\n", sp.expand_contractions({}))