from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def render_scaling():
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    plt.show()


def render_non_scaling():
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_xlim(0,0.8)
    plt.show()

render_non_scaling()
