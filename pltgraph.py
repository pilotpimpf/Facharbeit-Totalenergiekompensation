import matplotlib.pyplot as plt
import numpy as np

#%matplotlib qt

def plt_data(x, y, description = None, grid = True, borders = None, zerotime = False):
    # plt.style.use('./vscode_dark.mplstyle')
    if not description == None: fig = plt.figure(num=description["title"],figsize=(8,4), dpi=400)
    else: fig = plt.figure(figsize=(6,4), dpi=400)

    if not type(y) == tuple:y = (y,)

    if zerotime: x = [t-x[borders[0]] for t in x]

    for i in y:
        if borders: plt.plot(x[borders[0]:borders[1]], i[borders[0]:borders[1]])
        else: plt.plot(x, i)
    
    if not description == None:
        plt.xlabel(description["xLable"])
        plt.ylabel(description["yLable"])
        plt.title(description["title"])
        if not description.get("ylims")  == None: plt.ylim(description["ylims"][0], description["ylims"][1])
    # plt.ticklabel_format(style="plain")
    #fig.patch.set_facecolor('xkcd:white')

    plt.grid(grid)
    plt.show()


def plot_multiple_scales(x, Y , description = False, grid= True):
    fig, ax = plt.subplots(figsize=(8,4))


    colors = ['#8dd3c7', '#feffb3', '#BFBBD9', '#fa8174', '#81b1d2', '#fdb462', '#b3de69', '#bc82bd', '#ccebc4', '#ffed6f']

    # Twin the x-axis twice to make independent y-axes.
    axes = [ax]

    for n in range(len(Y)-1):
        axes.append(ax.twinx())

    # Make some space on the right side for the extra y-axis.
    fig.subplots_adjust(right=0.75)


    for axe in axes[2:]:
        # Move the last y-axis spine over to the right by 20% of the width of the axes
        axe.spines['right'].set_position(('axes', 1.2))

        # To make the border of the right-most axis visible, we need to turn the frame
        # on. This hides the other plots, however, so we need to turn its fill off.
        axe.set_frame_on(True)
        axe.patch.set_visible(False)

    # And finally we get to plot things...

    if description:
        for ax,y, color, lable in zip(axes,Y, colors[:len(Y)], description["Y"]):
            ax.plot(x,y, color=color)
            ax.set_ylabel(lable, color=color)
            ax.tick_params(axis='y', colors=color)
        axes[0].set_xlabel(description["xLable"])
    else:
        for ax,y, color in zip(axes,Y, colors[:len(Y)]):
            ax.plot(x,y, color=color)
            ax.tick_params(axis='y', colors=color)
    axes[0].grid(axis="both")
    # plt.grid(grid)
    plt.show()


def smoothListGaussian(list,degree=5):
    list =[list[0]]*(degree-1) + list + [list[-1]]*degree
    window=degree*2-1  
    weight=np.array([1.0]*window)  
    weightGauss=[]  
    for i in range(window):  
        i=i-degree+1  
        frac=i/float(window)  
        gauss=1/(np.exp((4*(frac))**2))  
        weightGauss.append(gauss)  
    weight=np.array(weightGauss)*weight  
    smoothed=[0.0]*(len(list)-window)  
    for i in range(len(smoothed)):  
        smoothed[i]=sum(np.array(list[i:i+window])*weight)/sum(weight)  
    return smoothed
