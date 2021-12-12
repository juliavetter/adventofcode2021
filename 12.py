V = set()
E = set()
G = (V, E)

def adjacent_vertices(G: tuple, v: str) -> set:
    E = G[1]
    adj = set()
    for (a, b) in E:
        if a == v:
            adj.add(b)
        elif b == v:
            adj.add(a)
    return adj

def big(v: str) -> bool:
    return v.isupper()

with open("12.txt") as input:
    for line in input.readlines():
        u = line.split("-")[0].strip()
        v = line.split("-")[1].strip()
        V.add(u)
        V.add(v)
        E.add((u, v))

# part 1

def find_paths(G: tuple, cur: str, path: list, paths: list) -> list:
    path.append(cur)
    if cur == 'end':
        paths.append(path)
        return paths
    for v in adjacent_vertices(G, cur):
        if big(v) or v not in path:
            find_paths(G, v, path.copy(), paths)
    return paths

paths = find_paths(G, 'start', list(), list())
print(len(paths))

# part 2

# return true iff the path has visited a small cave twice already
def bonus_taken(path: list) -> bool:
    for v in path:
        if not big(v) and path.count(v) >= 2:
            return True
    return False

def find_paths2(G: tuple, cur: str, path: list, paths: list) -> list:
    path.append(cur)
    if cur == 'end':
        paths.append(path)
        return paths
    for v in adjacent_vertices(G, cur):
        if v == 'start':
            continue
        elif not bonus_taken(path):
            # then we could add any vertex
            find_paths2(G, v, path.copy(), paths)
        # otherwise we can only add a big vertex or a small cave not visited already
        elif big(v) or v not in path:
            find_paths2(G, v, path.copy(), paths)
    return paths

paths2 = find_paths2(G, 'start', list(), list())
print(len(paths2))