import ply.lex as lex
import sys
import numpy as np
from math import sqrt as sqrt
import re

def count_incr(d, t):
	d[t] += 1	

#class Counts -> all attribute counts of a code
class Counts():
	keywords_list = ['AUTO', 'DOUBLE', 'INT', 'STRUCT', 'BREAK', 'ELSE', 'LONG', 'SWITCH', 'CASE', 'ENUM', 'REGISTER', 'TYPEDEF', 'CHAR', 'EXTERN', 'RETURN', 'UNION', 'CONST', 'FLOAT', 'SHORT', 'UNSIGNED', 'CONTINUE', "LOOP", "SIGNED", "VOID", "DEFAULT", "GOTO", "SIZEOF", "VOLATILE", "DO", "IF", "STATIC", "BEFOREFUN"]
	operators_list = ["PLUS", "MINUS", "DIVIDE", "MULTIPLY", "MODULO", "EQUAL_ASG", "EQUALS", "LT", "GT", "LTE", "GTE", "NOT_EQUAL"]
	symbols_list = ["SEMICOLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LSQUARE", "RSQUARE", "DOUBLE_Q", "SINGLE_Q", "COMMA", "AMPERSAND", "HASH", "PERCENT"]
	keywords_count = {}
	operators_count = {}
	symbols_count = {}
	identifiers_count = {}
	functions_count = {}
	def __init__(self):
		self.keywords_count = dict((x, 0) for x in self.keywords_list)
		self.operators_count = dict((x, 0) for x in self.operators_list)
		self.symbols_count = dict((x, 0) for x in self.symbols_list)
		self.identifiers_count = {}
		self.functions_count = {}


#arguments: object of class Count
#function: tokenizes input code and updates token count in Count object			
def lex_counter(c):
	tokens = ["ID", "NUMBER", 'COMMENT', "LIBRARY", "STRING", "FUNCALL", "FUNDEF"] + c.keywords_list + c.operators_list + c.symbols_list 
	#ignore blank spaces
	t_ignore = ' \t'

	#comments /*...*/ and //...	
	t_COMMENT  = r'/\s*\*.*\*/|//.*'
		#t.lexer.skip(1)
	#operators
	def t_PLUS(t):
		 r'\+'
		 
		 count_incr(c.operators_count, t.type)
		 return t
	def t_MINUS(t):
		r'\-'
		
		count_incr(c.operators_count, t.type)
		return t
	def t_MULTIPLY(t):
		r'\*'
		
		count_incr(c.operators_count, t.type)
		return t
	def t_DIVIDE(t):
		r'///'	
		count_incr(c.operators_count, t.type)
		return t
	def t_MODULO(t):
		r'\%'
		count_incr(c.operators_count, t.type)
		return t
	def t_EQUALS(t):
		r'=='
		count_incr(c.operators_count, t.type)
		return t
	def t_EQUAL_ASG(t):
		r'=' 
		count_incr(c.operators_count, t.type)
		return t
	def t_NOT_EQUAL(t):
		r'!='
		count_incr(c.operators_count, t.type)
		return t
	def t_LTE(t):
		r'<='
		count_incr(c.operators_count, t.type)
		return t
	def t_GTE(t):
		r'>='
		count_incr(c.operators_count, t.type)
		return t
	def t_LT(t):
		r'<'
		count_incr(c.operators_count, t.type)
		return t
	def t_GT(t):
		r'>'
		count_incr(c.operators_count, t.type)
		return t
	def t_LOOP(t):
		r'for|while'
		count_incr(c.keywords_count, t.type)
		return t
	def t_BEFOREFUN(t):
		r'if|switch|return'
		t.type = t.value.upper()
		count_incr(c.keywords_count, t.type)
		return t
	#function definition
	def t_FUNDEF(t):
		r'\w+\s(\w+)\s*\(.*\)'
		x = re.match(r'(\w+) +(\w+) *\(.*\)', t.value)
		func_name = x.group(2)
		if func_name in c.functions_count:
			c.functions_count[func_name] += 1
		else:
			c.functions_count[func_name] = 1
		return t
	#function call
	def t_FUNCALL(t):
		r'(\w+)\(.*\)'
		x = re.match(r'(\w+)\(.*\)', t.value)
		func_name = x.group(1)
		if func_name in c.functions_count:
			c.functions_count[func_name] += 1
		else:
			c.functions_count[func_name] = 1
		return t
	#string
	def t_STRING(t):
		r'\".*\"'
		t.lexer.skip(1)
		return t
	#library
	def t_LIBRARY(t):
		r'\#include.*\.h>'
		t.lexer.skip(1)
		return t
	#symbols
	def t_SEMICOLON(t):
		r';'
		count_incr(c.symbols_count, t.type)
		return t
	def t_LPAREN(t):
		r'\('
		count_incr(c.symbols_count, t.type)
		return t
	def t_RPAREN(t):
		r'\)'
		count_incr(c.symbols_count, t.type)
		return t
	def t_LBRACE(t):
		r'{' #blockstart
		count_incr(c.symbols_count, t.type)
		return t
	def t_RBRACE(t):
		r'}' #blockend
		count_incr(c.symbols_count, t.type)
		return t
	def t_LSQUARE(t):
		r'\['
		count_incr(c.symbols_count, t.type)
		return t
	def t_RSQUARE(t):
		r'\]'
		count_incr(c.symbols_count, t.type)
		return t
	def t_DOUBLE_Q(t):
		r'\"'
		count_incr(c.symbols_count, t.type)
		return t
	def t_SINGLE_Q(t):
		r'\''
		count_incr(c.symbols_count, t.type)
		return t
	def t_AMPERSAND(t):
		r'&'
		count_incr(c.symbols_count, t.type)
		return t
	def t_HASH(t):
		r'\#'
		
		count_incr(c.symbols_count, t.type)
		return t
	def t_PERCENT(t):
		r'%'
		count_incr(c.symbols_count, t.type)
		return t
	def t_NUMBER(t):
		r'\d+'
		t.value = int(t.value)
		return t
	def t_ID(t):
		r'\w+'
		if t.value.upper() in c.keywords_count:
			t.type = t.value.upper()
			count_incr(c.keywords_count, t.type)
			return t
		else:
			t.type = 'ID'
			if t.value in c.identifiers_count:
				count_incr(c.identifiers_count, t.value)
			else:
				c.identifiers_count[t.value] = 1
		return t
	def t_newline(t):
		r'\n+'
		t.lexer.lineno += len(t.value)
	def t_error(t):
		t.lexer.skip(1)
	return lex.lex()


#arguments: list of frequencies of tokens
#function: calculates the norm of frequency_vector
def vector_norm(frequency_vector):
	return sqrt(sum(map((lambda x: x ** 2), frequency_vector)))	

#arguments: two frequency_vector norms
#function: calculates the norm similarity
def norm_similarity(norm1, norm2):
	try:
 		x = (min(norm1, norm2) / max(norm1, norm2))
	except ZeroDivisionError:
		x = 0
	return x

#arguments: 2 frequency_vetors and their norms
#function: calculates the cosine similarity of the vectors
def cosine_similarity(freq1, freq2, norm1, norm2):
	if len(freq1) == len(freq2):
		dot = np.dot(freq1, freq2)
		#print "dot" , dot
		#sum(map(operator.mul, freq1, freq2))
		try:
			x = dot / (norm1 * norm2)
		except ZeroDivisionError:
			x = 0
		return x
	else:
		return None
		
#arguments: list of tokens
#function: merges group of tokens into a common token and return new list of tokens
def replace_tokens(toks):
	strn = " ".join(toks)
	strn = re.sub(r"(ID PLUS (PLUS|(EQUAL_ASG NUMBER)))", "INCR", strn)
	strn = re.sub(r"(ID MINUS (MINUS|(EQUAL_ASG NUMBER)))", "DECR", strn)
	strn = re.sub(r"(ID EQUAL_ASG (NUMBER|ID))", "ASSIGN", strn)
	strn = re.sub(r"(IF LPAREN (ID|NUMBER) (.*?) (ID|NUMBER) RPAREN)", r'IF \3', strn)
	strn = re.sub(r"(ID|NUMBER) (.*?) (ID|NUMBER)", r'\2', strn)
	return strn.split(" ")
