import itertools
import imagedet
from PIL import Image

#arguments: list of image name stored in base folder -> /tmp to compare
#function: calculates % of similarity between the images
def multiimage(image_names):
	res = []
	preprocessed_data =[]
	base = "/tmp/"
	result = []
	x = len(image_names)
	for i in range(x):
		image = Image.open(base + image_names[i])
		res = imagedet.dhash(image)
		preprocessed_data.append([res, image_names[i]])
	combinations = list(itertools.combinations(preprocessed_data, 2))
	
	sim_result = ""
	for combo in combinations:
		i = 0
		f1 = combo[0]
		f2 = combo[1]
		length1 = len(f1[0])
		length2 = len(f2[0])
		minimum = min(length1, length2)
		count = 0
		for i in xrange(minimum):
			for j in xrange(2):
				if(f1[0][i][j] == f2[0][i][j]):
					count = count + 1

		p1 = ((count * 100)/ (minimum * 2))
		if(p1 > 50):
			sim_result += "</br><b>%d%s</b> of %s found similar to %s</br>" %(p1, "%", combo[0][1], combo[1][1])
		else:
			sim_result += "</br>No plagiarism detected in <i>%s and %s</i></br>" %(combo[0][1], combo[1][1])
	return sim_result
