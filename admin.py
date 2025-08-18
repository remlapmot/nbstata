uv init
uv venv
uv add jupyter nbdev numpy
source .venv/bin/activate
nbdev_install_hooks
uv pip install -e '.[dev]'
jupyter notebook nbs/04_code_utils.ipynb
jupyter notebook nbs/09_magics.ipynb
jupyter notebook nbs/11_completions.ipynb
nbdev_prepare
python -m nbstata.install --sys-prefix
