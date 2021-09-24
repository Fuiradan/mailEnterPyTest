import pytest
import random

def test_str_one():
    str1 = "{} {}".format("Hello", "World!")
    str2 = "hello world!".title()
    assert str1 == str2

@pytest.mark.parametrize("string", ["123123", "6546456346", "5435345"])
def test_str_two(string):
        assert string.isdigit()

def test_str_three():
    data = "SomeStringWithSomeData"
    substr = "SomeSubStr"
    try:
        assert data.index(substr)
    except ValueError:
        pass

def test_list_one():
    data = [random.randint(-10, 10)] * 5
    minimal = min(data)
    data.sort()
    assert minimal == data[0]

def test_list_two():
    data = [1, 2, 3]
    copy_data = data.copy()
    assert data == copy_data

def test_list_three():
    list1 = [1, 2 , 4]
    list2 = [7, 4, 21, 5]
    assert (4 in list1) == (4 in list2)



    
