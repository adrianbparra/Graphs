
def earliest_ancestor(ancestors, starting_node):
    
    # ancestors = [(parent, child),(child)]
    # starting node = int
    # dfs
    # last child avilable

    # make ancestors into a dict

    # loop over items each parent, child set
    # make child = key , parents = set(values)
        # {1: {3}, 2: {3}}

    ancestors_dict = {}


    for ancestor in ancestors:
        if ancestor[1] in ancestors_dict:
            ancestors_dict[ancestor[1]].add(ancestor[0])
        else:
            ancestors_dict[ancestor[1]] = set()
            ancestors_dict[ancestor[1]].add(ancestor[0])
    
    print(ancestors_dict, end = "\n")
    # queue
    queue = []
    
    # parents
    parents = []
    
    # if node has parents
    if starting_node in ancestors_dict:

        # add node to queue
        queue.append(starting_node)

        # while the que has nodes
        while len(queue) > 0:
        
            # get the last node
            vertex = queue[-1]

            # print(vertex)
            # if node has perents
            if vertex in ancestors_dict:
                # remove current node
                queue.pop()
                # add parents to queue
                for ancs in ancestors_dict[vertex]:
                    # clears parents
                    parents = []
                    queue.append(ancs)
            # if no parents add to parents to check min later
            else:
                parents.append(queue.pop())
                
        # return min oldest parents
        return min(parents)

    # return -1 if no parents
    else:
        return -1




    return ancestors_dict

print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))