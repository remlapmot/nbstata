uv init
uv venv .venvpy314 --python 3.14
source .venvpy314/bin/activate
uv add --active jupyter nbdev numpy
nbdev_install_hooks
uv pip install -e '.[dev]'
jupyter notebook nbs/09_magics.ipynb
nbdev_prepare
python -m nbstata.install --sys-prefix
