# CPU version
git clone https://github.com/pytorch/pytorch.git

git submodule update --init
### needs PATH/LD_LIBRARY_PATH of python3, cuda, cudnn, openmpi, nccl, cmake
### may need gcc > v4.8
python3 setup.py install



# GPU version
git clone https://github.com/pytorch/pytorch.git

git submodule update --init

### needs recent CMAKE
export CUDNN_INCLUDE_DIR=/opt/libs/cudnn/7.1/cuda9/include

export CUDNN_LIB_DIR=/opt/libs/cudnn/7.1/cuda9/lib64

export C_INCLUDE_PATH=$INCLUDE:/opt/libs/cudnn/7.1/cuda9/include

python3 setup.py install

