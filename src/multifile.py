import itertools
import operator
import greedy_tiling
import term_freq


#arguments: list of filenames and their contents to compare reader[[filename, contents]]
#function: returns html string of results of comparison of the input files
def multifile(reader):
	flag = 0
	preproc =[]
	result = []
	x = len(reader)
	for i in range(x):
		temp = term_freq.preprocess(reader[i])
		preproc.append(temp)
	combinations = list(itertools.combinations(preproc, 2))
	for combo in combinations:
		result.append(term_freq.final(combo))	
	sim_result = ""
	for i in range(len(result)):
		if result[i] == True:
			flag = 1
			sim_result +=  "</br><b>Suspicious programs:</b> <i>%s %s</i>" %(combinations[i][0][2], combinations[i][1][2])
			p1,p2 = greedy_tiling.greedy_string_tiling(combinations[i][0][1], combinations[i][1][1])
			sim_result += "</br>%d%s of %s found similar to %s" %(p1, "%", combinations[i][0][2], combinations[i][1][2])
			sim_result += "<br>%d%s of %s found similar to %s</br>" %(p2, "%", combinations[i][1][2], combinations[i][0][2])
	
	if flag == 0:
		sim_result += "</br>Nothing suspicious found..."
	return sim_result
	
