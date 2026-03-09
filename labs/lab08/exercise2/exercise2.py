# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    unique_names = set()
    
    f1 = open(file1, 'r')
    for line in f1:
        name = line.strip()
        if name != "":
            unique_names.add(name)
    f1.close()

    f2 = open(file2, 'r')
    for line in f2:
        name = line.strip()
        if name != "":
            unique_names.add(name)
    f2.close()

    sorted_names = sorted(unique_names)

    out = open(output_file, 'w')
    for name in sorted_names:
        out.write(name + "\n")
    out.close()

    return len(sorted_names)

result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
