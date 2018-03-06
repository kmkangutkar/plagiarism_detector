from counter import *
from greedy_tiling import *

KEY_THRESHOLD = 0.5
OP_THRESHOLD = 0.7
SYM_THRESHOLD = 0.8
ID_THRESHOLD = 0.7

#arguments: list of filename and its content [filename, contents]
#function: returns preprocessed data --> list of [tokens_sequence, frquencies_dictionary(keywords, operators, symbols, identifiers), norm_dictionary(keywords, operators, symbols, identifiers), filename]
def preprocess(inp):
	doc = Counts()
	attr_counter = lex_counter(doc)
	fname = inp[0]
	data = inp[1]	
	attr_counter.input(data)	

	tokens_seq = []
	while(True):
		tok = attr_counter.token()
		if not tok:
			break
		else:
			tokens_seq.append(tok.type)
	keyword_freq = doc.keywords_count.values()
	key_norm = vector_norm(keyword_freq)
	op_freq = doc.operators_count.values()
	op_norm = vector_norm(op_freq)
	sym_freq = doc.symbols_count.values()
	sym_norm = vector_norm(sym_freq)
	id_freq = doc.identifiers_count.values()
	id_norm = vector_norm(id_freq)
	
	freq_l = {"key": keyword_freq, "op": op_freq, "sym": sym_freq, "id": id_freq}
	norm_l = {"key":key_norm, "op":op_norm, "sym":sym_norm, "id":id_norm}
	return [tokens_seq, freq_l, norm_l, fname]
	
#arguments: tuple of size 2 - (code1 preprocessed_data, code2 preprocessed_data)
#function: calculates the similarity and returns True if above the similarity threshold else False
def check(combo):
	f1 = combo[0]
	f2 = combo[1]
	key_norm_sim = norm_similarity(f1[2]["key"], f2[2]["key"])
	key_cosine_sim = cosine_similarity(f1[1]["key"], f2[1]["key"], f1[2]["key"], f2[2]["key"])
	op_norm_sim = norm_similarity(f1[2]["op"], f2[2]["op"])
	op_cosine_sim = cosine_similarity(f1[1]["op"], f2[1]["op"], f1[2]["op"], f2[2]["op"])
	sym_norm_sim = norm_similarity(f1[2]["sym"], f2[2]["sym"])
	sym_cosine_sim = cosine_similarity(f1[1]["sym"], f2[1]["sym"], f1[2]["sym"], f2[2]["sym"])
	id_norm_sim = norm_similarity(f1[2]["id"], f2[2]["id"])
	id_cosine_sim = cosine_similarity(f1[1]["id"], f2[1]["id"], f1[2]["id"], f2[2]["id"])
	
	fin_k_sim = key_norm_sim * key_cosine_sim
	fin_o_sim = op_norm_sim * op_cosine_sim
	fin_s_sim = sym_norm_sim * sym_cosine_sim
	if (id_cosine_sim):
		fin_i_sim = id_norm_sim * id_cosine_sim
	else:
		fin_i_sim = id_norm_sim
		
	if fin_k_sim >= KEY_THRESHOLD:
		if fin_o_sim >= OP_THRESHOLD:
			if fin_i_sim >= ID_THRESHOLD:
				if fin_s_sim >= SYM_THRESHOLD:
					return True
	return False
