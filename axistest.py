from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def render_scaling():
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot([0,1,2], [0,1,2], [0,1,2])


def render_non_scaling():
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_zmargin(0.05)
    ax.plot([0,1], [0,1], [0,1])
    #ax.set_xlim(0,1)
    #ax.set_ylim(0,1)
    print(ax.get_xbound())
    print(ax.get_ybound())
    print(ax.get_zbound())
    print(ax._xmargin)
    print(ax._ymargin)
    print(ax._zmargin)

render_scaling()
render_non_scaling()
plt.show()
