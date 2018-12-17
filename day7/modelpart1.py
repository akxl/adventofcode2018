from networkx import DiGraph, lexicographical_topological_sort as lt_sort

if __name__ == "__main__":
    input = open("input.txt", "r")
    print(''.join(lt_sort(DiGraph((line.split()[1], line.split()[-3]) for line in input))))