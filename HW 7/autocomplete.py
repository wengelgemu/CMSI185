'''
autocomplete.py
Name: Wengel Gemu  
Collaborators:
Date: October 24th, 2019
Description: Use sorting and binary search algorithms to provide autocomplete for a given query.
Copyright Matthew Drabick and Kevin Wayne, 2014.
'''



##### Classes #####


class Term():
    def __init__(self, query, weight):
        # initializing query and weight attributes
        
        if weight < 0:
            raise Exception('weights cannot be negative')

        ### TODO: YOUR CODE HERE ###
        self.query = query
        self.weight = weight

    # overrides basic operators so we can compare terms alphabetically
    def __eq__(self, other):
        return self.query.lower() == other.query.lower()

    def __lt__(self, other):
        return self.query.lower() < other.query.lower()

    # MEANT TO BE > ?
    def __gt__(self, other):
        return self.query.lower() > other.query.lower()

    # allows us to print the object so it's human-readable
    def __str__(self):
        return str(self.weight) + ' ' + self.query


class Autocomplete():
    def __init__(self, terms):
        self.terms = terms
        self.terms.sort() # sort terms alphabetically

    def all_matches(self, prefix):
        matches = self.terms[:]

        # binary search to find all queries starting w/ given prefix
        first_match_index = binary_search_for_first_index(matches, prefix)
        last_match_index = binary_search_for_last_index(matches, prefix)
        matches = matches[first_match_index : last_match_index + 1]

        # sort matching terms in descending order by weight
        matches.sort(key=get_weight, reverse=True)
        return matches

    def number_of_matches(self, prefix):
        ### TODO: YOUR CODE HERE ###
        x = 0
        for i in matches[prefix]:
            x+=1
        print("there are: " + str(x) + "matches")
        print(matches[0:top_k])
        print('hello')




#### Helper functions #####

def binary_search_helper(terms, left, right, prefix):
    """
    Finds the index of a term where the query starts with the given prefix.
    """

    ### TODO: YOUR CODE HERE ###

    if right < left:
        return -1

    mid = (left + right) // 2
    check = terms[mid]

    if prefix.lower() > check.query.lower():
        return binary_search_helper(terms, mid+1, right, prefix)
    elif prefix.lower() < check.query[:len(prefix)].lower():
        return binary_search_helper(terms, left, mid-1, prefix)
    elif check.query.lower().startswith(prefix.lower()):
        return mid
    


# if prefix > terms[mid],query:
#         return binary_search_helper(terms, mid+1, right, prefix)
#     elif prefix < terms[mid]:
#         return binary_search_helper(terms, left, mid-1, prefix)
#     elif prefix == [terms[mid]]:
#         return mid
#     else:
#         return -1


# def binary_search_helper(terms, left, right, prefix):

#     """
#     Finds the index of a term where the query starts with the given prefix.
#     """

#     ### TODO: YOUR CODE HERE ###
#     mid = (left + right) // 2
#     prefix_length = len(prefix)
#     middle_value = terms[mid]

#     # TEST CASES
#     print(middle_value[:prefix_length])
#     print(terms[right])
#     print(terms[mid])
#     print(terms[left])
    

#     if middle_value[:prefix_length] < prefix:
#         return binary_search_helper(terms, mid+1, right, prefix)
#     elif middle_value[:prefix_length] > prefix:
#         return binary_search_helper(terms, left, mid-1, prefix)
#     elif middle_value[:prefix_length] == prefix:
#         return binary_search_helper(terms, middle, prefix)
#     else:
#         return -1



def binary_search_for_first_index(terms, prefix):
    """
    Many Terms may start with the given prefix. First, find one match. Then
    work backwards through the sorted terms to find the first matching Term.
    """
    # first, find the index of a match
    match_index = binary_search_helper(terms, 0, len(terms) - 1, prefix)

    # check for edge cases
    if match_index == -1:
        return match_index

    # if a match is found check previous terms until reach FIRST match
    while terms[match_index].query[:len(prefix)].lower() == prefix.lower():
        match_index -= 1

    return match_index + 1

def binary_search_for_last_index(terms, prefix):
    """
    Many Terms may start with the given prefix. First, find one match. Then
    search through the following sorted terms to find the last matching Term.
    """
    # first, find the index of a match
    match_index = binary_search_helper(terms, 0, len(terms) - 1, prefix)

    # check for edge cases
    if match_index == -1 or match_index == len(terms) - 1:
        return match_index

    # if a match is found check next terms until reach LAST match
    while terms[match_index].query[:len(prefix)].lower() == prefix.lower():
        match_index += 1

    return match_index - 1


def get_weight(term):
    return term.weight

def process_file(filename):
    terms = []
    file = open(filename)
    file.readline()
    for line in file.readlines():
        weight, query = line.strip().split('\t')
        term = Term(query, int(weight))
        terms.append(term)
    return terms



##### Main part of script #####


filename = input('Please enter a filename, either wiktionary or cities: ')
top_k = eval(input('Please enter the number of results to display: '))
prefix = input('Please enter the prefix of your search query: ')

terms = process_file(filename+'.txt')  # either 'wiktionary' or 'cities'
autocomplete = Autocomplete(terms)
for result in autocomplete.all_matches(prefix)[:top_k]:
    print(result)
