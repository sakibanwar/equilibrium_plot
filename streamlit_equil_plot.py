import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.set_page_config(page_title="Equlibrium Plot", layout="wide")

# Set plot style
sns.set(style='ticks')
plt.rcParams['figure.dpi'] = 100

# Define the functions
def g(x, n, p):
    """Calculate the g function."""
    return (p * (1 - x)) / (x * (n - 1) - ((1 - x**p) * (1 - (1 - x**p)**(-1 + n))) / (x**(-1 + p)))

def h(x, n, p):
    """Calculate the h function."""
    return sum((1 - (1 - x**p)**(n - t)) * (1 - (1 - x**p)**(t - 1)) for t in range(2, n + 1))

def H(x, r, n, p):
    """Calculate the H function."""
    return (((r / n) * (g(x, n, p) * h(x, n, p) + 1)) - 1)

def plot_equilibrium(r, n, group_sizes, x_range=(-4, 4), x_points=90000):
    """
    Plot the equilibrium for given r, n, and a list of group sizes.

    Parameters:
    - r: The r value.
    - n: The n value.
    - group_sizes: List of group sizes (p values) to plot.
    - x_range: Tuple indicating the range of x values.
    - x_points: Number of points to generate in x_range.
    """
    x = np.linspace(x_range[0], x_range[1], x_points)
    fig, ax = plt.subplots()
    
    # Plot for each group size
    for p in group_sizes:
        ax.plot(x, H(x, r, n, p), linewidth=1.2, label=f'Group size {p}', linestyle='solid')

    plt.grid()
    plt.xlim([-1, 1.0])
    plt.ylim([-.5, 2.5])
    plt.axhline(y=0, color='k', linewidth=0.9)
    plt.axvline(x=0, color='k', linewidth=0.9)
    plt.title(f'Plot for \n(m=1, r={r}, n={n})', pad=20)
    
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(0.5)
    ax.xaxis.set_tick_params(width=0.5)
    ax.yaxis.set_tick_params(width=0.5)
    plt.xlabel(r'$\gamma$')
    plt.ylabel(r'$\Delta(\gamma)$')
    
    ax.legend(loc='upper right', shadow=False, fontsize='medium')
    st.pyplot(fig)

# Streamlit UI
st.title('Equilibrium Plot for Various Group Sizes')

r = st.sidebar.slider('r value', min_value=1, max_value=100, value=20)
n = st.sidebar.slider('No. of players', min_value=2, max_value=100, value=30)
group_sizes_str = st.sidebar.text_input('Enter group sizes (comma-separated)', '5, 10')
group_sizes = [int(x.strip()) for x in group_sizes_str.split(',') if x.strip()]

if group_sizes:
    plot_equilibrium(r, n, group_sizes)
else:
    st.warning('Please enter valid group sizes.')

