import CSP_6_03_Writing_to_files as HW
def test_write_file():
    HW.writeFile([12, 93, 9, "Lebron", "James"], "file.txt")
    assert open("file.txt","r").read() == "12\n93\n9\nLebron\nJames"


def test_sort_names():
    assert open("source.txt", "w").write("1\n12\n7\n92\n52\n16\n601\n6")
    HW.sortNames("source.txt","target.txt")
    assert open("target.txt", "r").read() == "1\n12\n16\n52\n6\n601\n7\n92"



def test_high_score():
    assert HW.highScore(10) == 88

