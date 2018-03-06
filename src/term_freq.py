import nltk
import itertools
import math
import operator
from nltk.corpus import stopwords


#arguments: file contents
#function: removes stopwords from the file contents and returns word_sequence
def stop(data):
	stop = stopwords.words('english')
	sentence = data
	x = [i for i in sentence.lower().split() if i not in stop]
	return x
	
#arguments: term and document word sequence
#function: calculates the term frequency in the document
def termFrequency(term, document_seq):
	return document_seq.count(term) / float(len(document_seq))
     
#arguments: tuple of size 2 - (doc1 preprocessed_data, doc2 preprocessed_data)
#function: calculates similarity based on word sequence of doc, if above threshold returns True else False
def final(combo):
	d = combo[0][0]
	d1 = combo[1][0]
	res = 0
	result = 0
	result1 = 0
	s = 0
	s1 = 0
	my_sent = []
	for x in d:
		if x in d1:
			 res = res + (d[x] * d1[x])
			 my_sent.append(x);
	string = ' '.join(my_sent)	
	f = open('my.txt','w')
	f.write(string)
	f.close()	 
	for y in d:
		s += (d[y] * d[y])
		result = math.sqrt(s)
	for z in d1:
		s1 += (d1[z] * d1[z])
		result1 = math.sqrt(s1)
	try:
		cossim = res/(result * result1)
	except ZeroDivisionError:
		cossim = 0
	f_result =  cossim * 100
	if(f_result > 40):
		return True
	else:
		return False
		
#arguments: list of filenames and their contents
#function: returns preprocessed data -> [term_frequencies, word_seq, filename]
def preprocess(reader):
	filename = reader[0]
	doc = []
	d = {}
	doc.append(stop(reader[1]))
	sequence = list(itertools.chain.from_iterable(doc))
	for i in sequence:
		d[i] = termFrequency(i, sequence) 
	return [d, sequence, filename]
	


