import task1, task2, task3, task4, task5, task6, task7, task8, task9
def check(task, string, answer):
    assert task.Add(string) == answer
    
def test_tasks():
    check(task1, "", 0)
    check(task1, "1", 1)
    check(task1, "1,2", 3)

    check(task2, " 55,   3   ,   43 ,   56    , 0   , 0   , 1", 158)

    check(task3, "1\n2,3", 6)

    check(task4, "//;\n1;2", 3)

    check(task5, "//;\n-1;-2", -3)

    check(task6, "//;\n2;1001", 2)

    check(task7, "//[***]\n1***2", 3)

    check(task8, "//[*][%]\n1*2%3", 6)

    check(task9, "//[**][%][;;;;]\n1**2%3;;;;6", 12)
