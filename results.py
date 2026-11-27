string = ['not', 'sure', 1337, 'code']
result = []
for ele in string :
	if isinstance(ele, int):
		result.append(ele)
	else:
		result.append(str(ele))
print(f"Results: {result}")