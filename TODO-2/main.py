import task1
def test_task1():
    assert task1.Add("") == 0
    assert task1.Add("1") == 1
    assert task1.Add("1,2") == 3
    assert task1.Add("1,   2  ") == 3
    assert task1.Add("  7  ,          901  ") == 908

##########################################################

import task2
def test_task2():
    assert task2.Add(" 55,   3   ,   43 ,   56    , 0   , 0   , 1") == 158

##########################################################

import task3
def test_task3():
    assert task3.Add("1\n2,3") == 6

##########################################################

import task4
def test_task4():
    assert task4.Add("//;\n1;2") == 3

##########################################################

import task5
def test_task5():
    assert task5.Add("//;\n-1;-2") == -3


##########################################################

import task6
def test_task6():
    assert task6.Add("//;\n2;1001") == 2


##########################################################

import task7
def test_task7():
    assert task7.Add("//[***]\n1***2") == 3


##########################################################

import task8
def test_task8():
    assert task8.Add("//[*][%]\n1*2%3") == 6


##########################################################

import task9
def test_task9():
    assert task9.Add("//[**][%][;;;;]\n1**2%3;;;;6") == 12