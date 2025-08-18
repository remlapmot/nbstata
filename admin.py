uv init
uv venv
uv add jupyter nbdev numpy
source .venv/bin/activate
nbdev_install_hooks
uv pip install -e '.[dev]'
jupyter notebook nbs/04_core_utils.ipynb
nbdev_prepare
python -m nbstata.install --sys-prefix
