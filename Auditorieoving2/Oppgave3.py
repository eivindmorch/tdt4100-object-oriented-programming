# a)
def first_index (bucket_list, cats):
	for i, bucket in enumerate(bucket_list):
		if bucket >= cats:
			return i
		
		
print (first_index ([3, 1, 2, 7, 5, 3, 4, 10], 4))

# b)
def min_index (bucket_list, cats):
	bucket_num = 0
	bucket_size = max(bucket_list)
	for i in bucket_list:
		if i >= cats:
			if i < bucket_size:
				bucket_size = i
				bucket_index = bucket_num
		bucket_num += 1
	return bucket_index
print (min_index ([3, 1, 2, 7, 5, 3, 4, 10], 4))