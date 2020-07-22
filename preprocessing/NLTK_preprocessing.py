import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import unicodedata
from Text_Fw.preprocessing.CONTRACTION_MAP import CONTRACTION_MAP
from Text_Fw.interfaces.preprocessing_interface import preprocessing_interface

class NLTK_preprocessing(preprocessing_interface):

    def __init__(self, text):
        self.__text = text
        self.__result = None

    def tokenization(self, parameter_dictionary):
        token_type = parameter_dictionary.get("token_type", "word")
        if token_type == "word":
            res = word_tokenize(self.__text)
        else:
            res = sent_tokenize(self.__text)
        self.__result = res
        return self.__result

    def stemming(self, parameter_dictionary):
        stemmer = PorterStemmer()
        my_stem = []
        for w in word_tokenize(self.__text):
            stem = stemmer.stem(w)
            my_stem.append(stem)
        return my_stem

    def lemmatization(self, parameter_dictionary):
        lemmatizer = WordNetLemmatizer()
        my_lem = []
        for w in word_tokenize(self.__text):
            lem = lemmatizer.lemmatize(w)
            my_lem.append(lem)
        return my_lem

    def NER(self, parameter_dictionary):
        #for w in str(word_tokenize(self.__text)):
        pos_tag = nltk.pos_tag(word_tokenize(self.__text))
        my_NER = nltk.ne_chunk(pos_tag, binary=True)
        return my_NER

    def POS(self, parameter_dictionary):
        my_POS = nltk.pos_tag(word_tokenize(self.__text))
        return my_POS

    def remove_stopwords(self, parameter_dictionary):
        stop_words = set(stopwords.words('english'))
        my_rem_stop = []
        for w in word_tokenize(self.__text):
            if not w in stop_words:
                my_rem_stop.append(w)
        my_rem_stop = " ".join(my_rem_stop)
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
    nk = NLTK_preprocessing("   #This project is based on NLTK Processing. It includes 14 methods."
                            "\n #numbers = 0123456789"
                            "\n #punctuations = .,:;!?"
                            "\n #html tags = <html><title>Insert title here</title></html>"
                            "\n #spl chars = @#$#@,"
                            "\n #mail id1 = myemail@gmail.com" " mail id2 = myyahoo@gmail.com"
                            "\n #hashtags = #my name is #aishu"
                            "\n #contractions = ain't, i'll've, mustn't've, aren't, I'd, I'd've, she'll, so's, mayn't, where've" )

    print(nk.tokenization({"token_type": "word"}))
    print("\n", nk.stemming({}))
    print("\n", nk.lemmatization({}))
    print("\n", nk.NER({}))
    print("\n", nk.POS({}))
    print("\n", nk.remove_stopwords({}))
    print("\n", nk.remove_emails({}))
    print("\n", nk.remove_html_tags({}))
    print("\n", nk.remove_numbers({}))
    print("\n", nk.remove_punctuations({}))
    print("\n", nk.remove_unicode({}))
    print("\n", nk.remove_specialcharacters({}))
    print("\n", nk.remove_hash_tags({}))
    print("\n", nk.expand_contractions({}))