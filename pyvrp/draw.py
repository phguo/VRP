from matplotlib import pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def _get_edges_from_route(route):
    assert len(route) >= 2
    edges = []
    for i, n in enumerate(route):
        if i >= 1:
            edges.append((route[i - 1], route[i]))
    return edges


def draw_vrp(pos, routes, save_file=False, file_name=None):
    fig, ax = plt.subplots()
    ax.scatter([pos[n][0] for n in pos.keys()], [pos[n][1] for n in pos.keys()])
    for route in routes:
        verts = [pos[n] for n in route]
        path = Path(verts)
        patch = patches.PathPatch(path, facecolor='none', lw=1, zorder=0)
        ax.add_patch(patch)

    if save_file:
        file_name = file if file_name is not None else f"{len(pos.keys())}_nodes_{len(routes)}_routes"
        plt.savefig(f"{file_name}.pdf", bbox_inches='tight', transparent=True, pad_inches=0.1)

    plt.show()


if __name__ == '__main__':
    pos = {1: (0, 0), 2: (1, 1), 3: (2, 3)}
    routes = [[1, 2, 3, 1]]
    draw_vrp(pos, routes, save_file=True)
