from Text_Fw.constant_enum import *

class Main():


    def preprocessing_text(self, text, lib_name, funcion_name, param_dict):
        classname = LibraryBase.get(lib_name,"nltk")
        class_ref = classname(text)
        result = getattr(class_ref,funcion_name)(param_dict)
        return result

if __name__ == "__main__":
    main = Main()
    param_dict= {"token type": "word"}
    print(main.preprocessing_text("my name is Donald Trump","nltk","tokenization",param_dict,))
    print(main.preprocessing_text("my name is Donald Trump","spacy", "tokenization", param_dict, ))


