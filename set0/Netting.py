##################################
#   Khaja Anwar Ali Siddiqui
#   GS Coding Ninjas
#   SET 0
#   Q1
###################################


def getMin(settle_nodes):
    min_value = None
    min_node = None
    for node in settle_nodes:
        if not min_value or settle_nodes[node] < min_value:
            min_value = settle_nodes[node]
            min_node = node
    return min_node, min_value


def getMax(settle_nodes):
    max_value = None
    max_node = None
    for node in settle_nodes:
        if not max_value or settle_nodes[node] > max_value:
            max_value = settle_nodes[node]
            max_node = node
    return max_node, max_value


def recurse(settle_nodes, settled_txns):
    if len(settle_nodes) <= 1:
        return settled_txns
    else:
        max_node_value = getMax(settle_nodes)
        min_node_value = getMin(settle_nodes)
        if abs(max_node_value[1]) > abs(min_node_value[1]):
            settle_nodes.pop(min_node_value[0])
            settled_txns.append((min_node_value[0], max_node_value[0], -min_node_value[1]))
        else:
            settle_nodes.pop(max_node_value[0])
            settled_txns.append((min_node_value[0], max_node_value[0], -max_node_value[1]))
    return recurse(settle_nodes, settled_txns)

def main():
    all_txns = input("Give Txns")
    settle_nodes = {}
    finalized_txns = []

    for txn in all_txns:
        if txn[0] in settle_nodes:
            settle_nodes[txn[0]] -= txn[2]
        else:
            settle_nodes[txn[0]] = -txn[2]

        if txn[1] in settle_nodes:
            settle_nodes[txn[1]] += txn[2]
        else:
            settle_nodes[txn[1]] = +txn[2]
    recurse(settle_nodes, finalized_txns )
    print(finalized_txns)


main()
