## Environment Setup

conda create -n algo-oanda-demo-py38 python=3.8

conda activate algo-oanda-demo-py38

pip install -r requirements.txt

pip install git+https://github.com/happydasch/btoandav20

---- remove conda env ----

conda deactivate

conda env remove -n algo-oanda-demo-py38
