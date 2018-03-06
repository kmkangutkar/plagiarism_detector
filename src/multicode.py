import sys
import preproc
import itertools
import counter
from greedy_tiling import *

#arguments: list of filenames and their contents to compare
#function: returns html string of results of code comparisons
def multicode(reader):
#reader - [fname, contents]
	preproc_data = []
	result = []
	flag = 0
	x = len(reader)
	for i in range(x):
		data = preproc.preprocess(reader[i])
		preproc_data.append(data)
	
	combinations = list(itertools.combinations(preproc_data, 2))
	for combo in combinations:
		result.append(preproc.check(combo))
	sim_result = ""
	for i in range(len(result)):
		if result[i] == True:
			flag = 1
			sim_result += "</br><b>Suspicious programs:</b> <i>%s %s</i>" %(combinations[i][0][3], combinations[i][1][3])
			tok1 = preproc.replace_tokens(combinations[i][0][0]) 
			tok2 = preproc.replace_tokens(combinations[i][1][0])
			p1, p2 = greedy_string_tiling(tok1, tok2)
			sim_result += "</br><b>%d%s</b> of %s found similar to %s" %(p1, "%", combinations[i][0][3], combinations[i][1][3])
			sim_result += "</br><b>%d%s</b> of %s found similar to %s</br>" %(p2, "%", combinations[i][1][3], combinations[i][0][3])
	
	if flag == 0:
		sim_result +=  "</br>Nothing suspicious found..."
	sim_result += "</p>"
	return sim_result
				

