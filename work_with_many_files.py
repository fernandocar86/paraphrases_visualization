from os import listdir
import re
import nltk
# Start. 

# This function returns the list of files in some extension
# from a selected folder
def find_files(path, extension):
    filenames = listdir(path)
    return [ filename for filename in filenames if filename.endswith( extension ) ]

# Count the whole group of paraphrases
def count_paraphrases(path):
   list_of_files = find_files(path, 'txt')
   list_of_paraphrases = []
   for file in list_of_files:
       paraphrases_from_file = paraphrase_finder(path, file)
       list_of_paraphrases = list_of_paraphrases + paraphrases_from_file
   count = len(list_of_paraphrases)
   return count

# return list of paraphrases    
def paraphrase_finder(path, file):
    entire_path = path + '/' + file
    pattern = r'\/<TRANS\+VAL=.*>\s\/<TRANS\+VAL=.*>'
    opened_file = open(entire_path, 'r', encoding='utf-8')
    string = opened_file.read()
    paraphrases_in_file = re.findall(pattern, string, flags=0)
    opened_file.close()
    return paraphrases_in_file

def paraphrases_tuples(file):
    sent_list = []
    opened_file = open(file, "r")
    read_file = opened_file.read() 
    normalized_sentences = re.sub(r'\n', '.\n', read_file, flags=0)
    sentences = nltk.sent_tokenize(normalized_sentences, language='spanish')
    for sent in sentences:
        sentences_tuples = []
        pattern1 = r'\/<ORIG\+VAL=(?P<original>.*?)>\s?'
        pattern2 = r'\/<TRANS\+VAL=(?P<paraphrase>.*?)>\s?'
        if re.search(pattern1, sent, flags=0):
            sent_original = re.sub(pattern2, '', sent, count=0, flags=0)
            sent_original = re.sub(pattern1, '\g<original>', sent_original, count=0, flags=0)
            sentences_tuples.append(sent_original)
            sent_paraphrased = re.sub(pattern1, '', sent, flags=0)
            paraphrases_cleaner(pattern2, sent_paraphrased, sentences_tuples)
        else:
            sentences_tuples.append(sent)
            sentences_tuples.append('')
        sent_list.append(sentences_tuples)
    opened_file.close()
    return sent_list

def paraphrases_cleaner(pattern2, sent, sentences_tuples):
    if re.search(pattern2, sent):
        sent_clean = re.sub(pattern2, '\g<paraphrase>', sent, count=1, flags=0)
        sent_clean = re.sub(pattern2, '', sent_clean, count=0, flags=0)
        sentences_tuples.append(sent_clean)
        sent_paraphrased = re.sub(pattern2, '', sent, count=1, flags=0)
        paraphrases_cleaner(pattern2, sent_paraphrased, sentences_tuples)

#def paraphrases_checker(file):
    

    
#def create_html(number):
#    name_for_file = 'paraphrase'+number
#    home = open('home.html', "w", encoding='utf-8')
#    home.write('<!DOCTYPE html> \n <html> \n <head> <title>Prode mundial</title> \n </head> \n <body> \n <h1>Resultados del prode mundial</h1> \n <p></p>\n')
#    home.write('<table>\n<tr>\n<th>Participante</th>\n<th>Puntaje</th>\n</tr>')
