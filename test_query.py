import Query

## Defining test cases for the functions

def test_get_ans1():
    res=Query.get_ans1()
    assert res == 365

def test_get_ans2():
    res=Query.get_ans2()
    assert res == 2

def test_get_ans4():
    res=Query.get_ans4()
    assert res == 'EMBRAER'
def test_get_ans5():
    res=Query.get_ans5()
    assert res == 'New York => Chicago'