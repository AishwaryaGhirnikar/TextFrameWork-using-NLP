from abc import ABC, abstractmethod


class preprocessing_interface(ABC):
    '''
    this class is an interface for processing libraries
    '''

    @abstractmethod
    def tokenization(self, parameter_dictionary):
        pass

    @abstractmethod
    def stemming(self, parameter_dictionary):
        pass

    @abstractmethod
    def lemmatization(self, parameter_dictionary):
        pass

    @abstractmethod
    def NER(self, parameter_dictionary):
        pass

    @abstractmethod
    def POS(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_stopwords(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_emails(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_html_tags(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_numbers(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_punctuations(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_unicode(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_hash_tags(self, parameter_dictionary):
        pass

    @abstractmethod
    def remove_specialcharacters(self, parameter_dictionary):
        pass

    @abstractmethod
    def expand_contractions(self, parameter_dictionary):
        pass
