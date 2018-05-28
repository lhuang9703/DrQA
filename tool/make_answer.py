import json

def data_from_json(filename):
	with open(filename,'r') as f:
		data = json.load(f)
	return data

if __name__ == '__main__':
	file_a = '/home/jiaosd/drqa/results/phaseB_5b_01-20180524-5fb09399.json'
	data_a = data_from_json(file_a)

	file_b = '/home/jiaosd/drqa/data/BioASQ-trainingDataset6b.json'
	data_b = data_from_json(file_b)

	s_num = 0
	f_num = 0
	t_num = 0

	"""with open('right_result.txt','w') as f:
		for i in data_a:
			t_num += 1
			for j in range(len(data_b['questions'])):
				if data_b['questions'][j]['id'] == i:
					if data_b['questions'][j]['exact_answer'][0] in data_a[i] or data_a[i] in data_b['questions'][j]['exact_answer'][0]:
						s_num += 1
						f.write(('ID:'+i+':\n'+'FROM  '+'&&'.join(data_b['questions'][j]['exact_answer'])+'  TO  '+data_a[i]+'\n\n').encode('utf-8'))
				#data_b['questions'][j]['exact_answer'][0] = data_a[i]
				'''if data_b['questions'][j]['exact_answer'][0] in data_a[i]:
					s_num += 1
					print('\n')
					print(data_a[i]+'  hhh  '+data_b['questions'][j]['exact_answer'][0])
				else:
					f_num += 1
				#s_num += 1
				continue
			else:
				pass'''
	with open('wrong_result.txt','w') as f:
		for i in data_a:
			t_num += 1
			for j in range(len(data_b['questions'])):
				if data_b['questions'][j]['id'] == i:
					if data_b['questions'][j]['exact_answer'][0] not in data_a[i] and data_a[i] not in data_b['questions'][j]['exact_answer'][0]:
						f_num += 1
						f.write(('ID:'+i+':\n'+'FROM  '+'&&'.join(data_b['questions'][j]['exact_answer'])+'  TO  '+data_a[i]+'\n\n').encode('utf-8'))"""

	"""for i in data_a:
		t_num += 1
		for j in range(len(data_b['questions'])):
			if data_b['questions'][j]['id'] == i:
				ans = []
				ans.append(data_a[i])
				an = []
				an.append(ans)
				print(i)
				data_b['questions'][j]['exact_answer'] = an
				'''if data_b['questions'][j]['exact_answer'][0] in data_a[i]:
					s_num += 1
					print('\n')
					print(data_a[i]+'  hhh  '+data_b['questions'][j]['exact_answer'][0])
				else:
					f_num += 1'''
				s_num += 1
				continue
			else:
				pass"""
	for i in range(len(data_b['questions'])):
		for j in data_a:
			if data_b['questions'][i]['id'] == j:
				if data_b['questions'][i]['type'] == 'factoid':
					# data_b['questions'][i]['exact_answer'] = [[w] for w in data_a[j]]#(str(data_a[j]).lstrip('[').rstrip(']')).encode('utf-8')
					data_b['questions'][i]['exact_answer'] = [[[w][0][0]] for w in data_a[j]]
				else:
					# data_b['questions'][i]['exact_answer'] = [[w] for w in data_a[j]]
					data_b['questions'][i]['exact_answer'] = [[[w][0][0]] for w in data_a[j]]
				s_num += 1
		else:
			pass
	result = []
	for j in data_a:
		for i in range(len(data_b['questions'])):
			if data_b['questions'][i]['id'] == j:
				result.append(data_b['questions'][i])
	data_b['questions'] = result

	with open('/home/jiaosd/drqa/results/data01_5b_answer.json','w') as f:
		json.dump(data_b,f,indent = 2)

	print(s_num)
	print(f_num)
	print(t_num)
