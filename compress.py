chars = ["a", "a", "b", "b", "c", "c", "c"]
# output = 6 ["a", "2", "b", "2", "c", "3]
chars = [
"a","b","b","b","b","b","b","b","b","b","b","b","b"
]

# output = ["a","b","12"]


def compress(chars):
	result = []
	for char in chars:
		if char in result:
			result[-1] += 1
		else:
			result.extend([char, 1])
	return [str(i) for i in result]

def compress_v2(chars):
	count = 1
	index = 0
	while index < len(chars):
		if index != len(chars) - 1 and chars[index] == chars[index + 1]:
			chars.pop(index)
			count += 1

		else:
			if count > 1:
				chars.insert(index + 1, str(count))
				index += 2
			else:
				index += 1
			count = 1
	return chars
chars = [
"a","b","b","b","b","b","b","b","b","b","b","b","b"
]
def compress_v3(chars):
    count = 1
    chars.append(True)

    while True:
        current = chars.pop(0)
        if current is True:
            break

        if current == chars[0]:
            count += 1

        else:
            if count > 1:
                 chars.extend([
                        current,
                        *[i for i in str(count)]
                    ])
            else:
                chars.append(current)
            count = 1
    return chars
print(compress_v3(chars))
