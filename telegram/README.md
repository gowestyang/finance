## Environment Setup

conda create -n telegram-py38 python=3.8

conda activate telegram-py38

pip install ipykernel aiogram requests

---- remove conda env ----

conda deactivate

conda env remove -n telegram-py38
