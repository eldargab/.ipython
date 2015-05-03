# Configuration file for ipython-notebook.

c = get_config()

#------------------------------------------------------------------------------
# InlineBackend configuration
#------------------------------------------------------------------------------

# An object to store configuration of the inline backend.

# The figure format to enable (deprecated use `figure_formats` instead)
# c.InlineBackend.figure_format = u''

# A set of figure formats to enable: 'png',  'retina', 'jpeg', 'svg', 'pdf'.
c.InlineBackend.figure_formats = set(['svg'])

# Extra kwargs to be passed to fig.canvas.print_figure.
#
# Logical examples include: bbox_inches, quality (for jpeg figures), etc.
# c.InlineBackend.print_figure_kwargs = {'bbox_inches': 'tight'}

# Close all figures at the end of each cell.
#
# When True, ensures that each cell starts with no active figures, but it also
# means that one must keep track of references in order to edit or redraw
# figures in subsequent cells. This mode is ideal for the notebook, where
# residual plots from other cells might be surprising.
#
# When False, one must call figure() to create new figures. This means that
# gcf() and getfigs() can reference figures created in other cells, and the
# active figure can continue to be edited with pylab/pyplot methods that
# reference the current active figure. This mode facilitates iterative editing
# of figures, and behaves most consistently with other matplotlib backends, but
# figure barriers between cells must be explicit.
# c.InlineBackend.close_figures = True

# Subset of matplotlib rcParams that should be different for the inline backend.
# c.InlineBackend.rc = {'font.size': 10, 'figure.figsize': (6.0, 4.0), 'figure.facecolor': (1, 1, 1, 0), 'savefig.dpi': 72, 'figure.subplot.bottom': 0.125, 'figure.edgecolor': (1, 1, 1, 0)}
