#!/usr/bin/env python3.5
import sys
class A():
	def __init__(self, l: list):
		self.listing = l

j = A(["a", "b", "c", "d"])
k = A(["e", "f", "g", "k"])
t = [element.listing for element in [j, k]]
flat_list = []
for sublist in t:
    for item in sublist:
        flat_list.append(item)
#print(flat_list)

# TODO
# funnel_cake -F spotify_urls.txt -O example_output (read from file)
# funnel_cake -L "url1,url2,url3" -O example_output (read from comma separated list)
# cat spotify_urls.txt | funnel_cake (read from STDIN)

def read_from_file(path: str):
	return [line.strip() for line in open(path).readlines()]
def read_from_comma_list(comma_list: str):
	return comma_list.split(",")

# converting a list of lists into a set
def l_of_l_to_set(lst: list):
	return set(tuple(element) for element in lst)

# converting a set into a list
def set_to_lst(st: set):
	return [element for sublist in st for element in sublist]
file_list = read_from_file("example.txt")
comma_list = read_from_comma_list("url1,url2")
file_list_list = [A([*file_list]).listing for element in file_list]


stdin_content = [A([element.strip()]) for element in sys.stdin]
print(stdin_content)
