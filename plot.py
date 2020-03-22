import matplotlib.pyplot as plt


def mark_by_z(ax, solution, zval, color):
    x = []
    y = []
    z = []
    for c in solution:
        if c[2] == zval:
            x.append(c[0])
            y.append(c[1])
            z.append(c[2])
    ax.scatter(x, y, zs=z, zdir='z', c=color, s=100.0)


def plot_solution(solution):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x = [c[0] for c in solution]
    y = [c[1] for c in solution]
    z = [c[2] for c in solution]
    ax.plot(x, y, zs=z, zdir='z')
    mark_by_z(ax, solution, 0, 'red')
    mark_by_z(ax, solution, 1, 'green')
    mark_by_z(ax, solution, 2, 'blue')
    mark_by_z(ax, solution, 3, 'black')

    # Make legend, set axes limits and labels
    ax.legend()
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_zlim(min(z), max(z))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.view_init(elev=35., azim=-15)

    plt.show()


if __name__ == '__main__':
    s = [(0, 0, 0), (2, 0, 0), (2, 3, 0), (-1, 3, 0), (-1, 0, 0), (-1, 0, 1), (2, 0, 1), (2, 0, 2), (-1, 0, 2), (-1, 1, 2), (-1, 1, 1), (0, 1, 1), (0, 1, 0), (0, 2, 0), (1, 2, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1), (-1, 2, 1), (-1, 3, 1), (2, 3, 1), (2, 1, 1), (2, 1, 3), (2, 0, 3), (-1, 0, 3), (-1, 1, 3), (1, 1, 3), (1, 1, 2), (0, 1, 2), (0, 2, 2), (-1, 2, 2), (-1, 3, 2), (1, 3, 2), (1, 2, 2), (2, 2, 2), (2, 3, 2), (2, 3, 3), (-1, 3, 3), (-1, 2, 3), (2, 2, 3)]
    plot_solution(s)
