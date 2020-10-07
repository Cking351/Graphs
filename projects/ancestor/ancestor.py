def earliest_ancestor(ancestors, starting_node, child=None):
    if child is None:
        child = {}

    if len(child) == 0:
        for a in ancestors:
            if a[1] in child:
                # look for the smallest value
                if child[a[1]] > a[0]:
                    child[a[1]] = a[0]
                else:
                    continue
            else:
                child[a[1]] = a[0]

    # if starting node is not a key
    if starting_node not in child:
        return -1
    if starting_node in child:
        if child[starting_node] not in child:
            return child[starting_node]
        else:
            return earliest_ancestor(ancestors, child[starting_node], child)



# Test samples
# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#         self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
#         self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
#         self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
