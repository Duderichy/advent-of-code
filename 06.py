import fileinput
from collections import deque

def main():
    data = fileinput.input()
    deps = []
    for line in data:
        a, b = (text.replace('\n', '') for text in line.split(')'))
        deps.append((a, b))
    # print(deps)
    deps_map = gen_dep_map(deps)
    # print(deps_map)
    dep_count = count_deps(deps_map)
    print(dep_count)
    return dep_count

def gen_dep_map(deps_list):
    deps_map = {}
    for a, b in deps_list:
        if a not in deps_map:
            deps_map[a] = set()
        if b not in deps_map:
            deps_map[b] = set()
        deps_map[a].add(b)
    return deps_map

def count_deps(deps_map):
    queue = deque()
    queue.append(('COM', 1))
    total = 0
    while queue:
        cur, val = queue.pop()
        total += val - 1
        for dep in deps_map[cur]:
            queue.append((dep, val + 1))  
    return total

def find_shortest_path(deps_map, start, dest):
    pass

if __name__ == "__main__":
    print(main())