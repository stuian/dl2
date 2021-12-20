# 创建并激活 python3.8的环境
conda create -y --force -n ag python=3.8 pip
conda activate ag
# 安装autogluon
pip install "mxnet<2.0.0"
pip install autogluon