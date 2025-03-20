import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Update this with the name of your Jupyter notebook
notebook_filename = 'weather.ipynb'
output_filename = 'output_notebook.ipynb'

with open(notebook_filename) as f:
    notebook = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

ep.preprocess(notebook, {'metadata': {'path': './'}})

with open(output_filename, 'w') as f:
    nbformat.write(notebook, f)
