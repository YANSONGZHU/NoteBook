# TRIQS安装配置指南

使用TRIQS/CTHYB来计算DMFT

TRIQS主页：https://triqs.github.io/triqs/latest/

TRIQS/CTHYB主页：https://triqs.github.io/cthyb/latest/

TRIQS官方安装指南：https://triqs.github.io/triqs/latest/install.html

TRIQS/CTHYB官方安装指南：https://triqs.github.io/cthyb/latest/install.html



Ubuntu apt安装步骤：

```bash
sudo apt-get update && sudo apt-get install -y software-properties-common apt-transport-https curl
source /etc/lsb-release
curl -L https://users.flatironinstitute.org/~ccq/triqs/$DISTRIB_CODENAME/public.gpg | sudo apt-key add -
sudo add-apt-repository "deb https://users.flatironinstitute.org/~ccq/triqs/$DISTRIB_CODENAME/ /"
sudo apt-get update && sudo apt-get install -y triqs
sudo apt-get install -y triqs_cthyb
```

使用Pycharm编写Python代码

Pycharm下载主页：https://www.jetbrains.com/pycharm/download/#section=linux

使用Snap下载Pycharm：

```bash
sudo apt install snap
sudo snap install pycharm-community --classic
```



### 使用Conda安装TRIQS/CTHYB

```bash
$ conda install -c conda-forge triqs
$ conda install -c conda-forge triqs_cthyb
```