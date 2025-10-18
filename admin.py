uv venv --python 3.14
uv init
source .venv/bin/activate
uv add jupyterlab nbdev numpy
nbdev_install_hooks
uv pip install -e .
jupyter notebook nbs/09_magics.ipynb
nbdev_prepare
python -m nbstata.install --sys-prefix
