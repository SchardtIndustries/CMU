def findDuplicateStudentsSet(students):
    seen = set()
    duplicates = set()
    for student in students:
        if student in seen:
            duplicates.add(student)
        else:
            seen.add(student)
    return list(duplicates)

def test_findDuplicateStudentsSet():
    print("Testing findDuplicateStudentsSet()...", end='')
    assert(findDuplicateStudentsSet(["Alice", "Bob", "Charlie"]) == [])
    assert(findDuplicateStudentsSet(["Alice", "Bob", "Alice"]) == ["Alice"])
    assert(sorted(findDuplicateStudentsSet(["Alice", "Bob", "Charlie", "Bob", "Charlie", "Alice"])) ==
           sorted(["Alice", "Bob", "Charlie"]))
    assert(findDuplicateStudentsSet([]) == [])
    assert(findDuplicateStudentsSet(["apple", "Apple", "apple"]) == ["apple"])
    assert(sorted(findDuplicateStudentsSet(["101", "102", "101", "103"])) ==sorted(["101"]))
    assert(sorted(findDuplicateStudentsSet(["a", "b", "a", "c"])) == sorted(["a"]))
    assert(sorted(findDuplicateStudentsSet([("id", 1), ("id", 2), ("id", 1)])) == sorted([("id", 1)]))
    assert(set(findDuplicateStudentsSet(["1", "2", "3", "2", "1"])) == {"1", "2"})
    assert(set(findDuplicateStudentsSet([1, "1", 2, "2", 1])) == {1})
    assert(set(findDuplicateStudentsSet(["x"] * 1000 + ["y"] * 999)) == {"x", "y"})
    assert(set(findDuplicateStudentsSet(["z"] * 50)) == {"z"})
    assert(set(findDuplicateStudentsSet([(i, i*2) for i in range(50)] + [(25, 50), (40, 80)])) == {(25, 50), (40, 80)})

    print('Passed!')

test_findDuplicateStudentsSet()
