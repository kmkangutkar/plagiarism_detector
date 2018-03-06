#arguments: list of tokens of 2 docs 
#function: finds the common substring patches in the list
def greedy_string_tiling(doc_tokens1, doc_tokens2):
	tokens_matched1 = [[x, False] for x in doc_tokens1]
	tokens_matched2 = [[x, False] for x in doc_tokens2] 
	MIN_MATCH = 2
	tiles = []
	t1 = ''
	f = open('match.txt', 'w')
	while(True):
		max_match = MIN_MATCH
		matches = []
		for i in range(len(tokens_matched1)):
			for j in range(len(tokens_matched2)):
				k = 0
				#f.write('\n')
				while (i + k < len(tokens_matched1) and j + k < len(tokens_matched2)) and tokens_matched1[i + k][0] == tokens_matched2[j + k][0] \
				and not tokens_matched1[i + k][1] and not tokens_matched2[j + k][1]:
				#	t1 = tokens_matched1[i + k][0] + ' '
				#	f.write(t1)
					k += 1
				if k == max_match:
					matches.append((i, j, k))
				elif k > max_match:
					matches = [(i, j, k)]
					max_match = k
		for x in matches:
			for k in range(max_match):
				tokens_matched1[x[0] + k][1] = True
				tokens_matched2[x[1] + k][1] = True
				t1 += (tokens_matched1[x[0] + k][0] + ' ')
			t1 += '\n'
			tiles.append(x)
		f.write(t1)
		if max_match <= MIN_MATCH:
			break
	f.close()
	return perc_sim(tokens_matched1,tokens_matched2)
	
#arguments: 2 lists of tokens_matched
#function: calculates the percentage similarity based on the matched tokens
def perc_sim(tokens_matched1, tokens_matched2):
	a_sim = 0
	b_sim = 0
	for x in tokens_matched1:
		if x[1] == True:
			a_sim += 1
	for x in tokens_matched2:
		if x[1] == True:
			b_sim += 1
	return float(a_sim)/len(tokens_matched1) * 100, float(b_sim)/len(tokens_matched2) * 100 
			

