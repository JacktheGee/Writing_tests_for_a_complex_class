from lib.most_often import MostOften

"""
Given a list you initially return the same list
"""

def test_given_list_returns_same_list():
    word_list = MostOften([1,2,3])
    assert word_list.starting_list == [1,2,3]

"""
Given a list, add a new item to the list,
which return the inital list + the new item
"""

def test_add_new_returns_list_plus_item():
    word_list = MostOften([1,2,3])
    word_list.add_new(5)

    assert word_list.starting_list == [1,2,3,5]

"""
Given a list with unique numbers
Function returns "no clear winner"
"""

def test_given_list_with_unique_num_returns_message():
    word_list = MostOften([1,2,3])
    assert word_list.get_most_often() == "no clear winner"