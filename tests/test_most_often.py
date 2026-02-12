from lib.most_often import MostOften

"""
Given a list you initially return the same list
"""

def test_given_list_returns_same_list():
    word_list = MostOften([1,2,3])
    assert word_list.starting_list == [1,2,3]

