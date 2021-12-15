import networkx as nx
import numpy as np

SIZE = 100

cavern = np.genfromtxt("./input.txt", delimiter=SIZE * (1,)).astype(int)

POS = [(-1, 0), (0, 1), (1, 0), (-1, 0)]


def get_short_path(cavern):
    G = nx.DiGraph()

    for r in range(cavern.shape[0]):
        for c in range(cavern.shape[0]):
            G.add_node((r, c), node_weight=cavern[r, c])

            for pos in POS:
                rr, cc = pos
                if 0 <= r + rr < cavern.shape[0] and 0 <= c + cc < cavern.shape[0]:
                    G.add_edge(
                        (r, c),
                        (r + rr, c + cc),
                        weight=cavern[r, c] + cavern[r + rr, c + cc],
                    )

    return sum(
        [
            G.nodes[n]["node_weight"]
            for n in nx.dijkstra_path(
                G,
                (0, 0),
                (cavern.shape[0] - 1, cavern.shape[0] - 1),
                weight="weight",
            )
            if n != (0, 0)
        ]
    )


print(get_short_path(cavern))


full_cavern = np.zeros((5 * SIZE, 5 * SIZE))

for i in range(5):
    for j in range(5):
        tmp_cavern = cavern + (i + j)
        tmp_cavern[tmp_cavern >= 10] = tmp_cavern[tmp_cavern >= 10] - 9

        full_cavern[i * SIZE : i * SIZE + SIZE, j * SIZE : j * SIZE + SIZE] = tmp_cavern

print(get_short_path(full_cavern))
