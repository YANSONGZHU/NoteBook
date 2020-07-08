# Conda 使用指南

从官网下载MiniConda：https://docs.conda.io/en/latest/miniconda.html

通过bash安装

禁止bash默认启动conda

```bash
$ conda config --set auto_activate_base false
```

通过以下命令删除python环境

```bash
$ conda remove -n python --all
```

可以通过以下命令查看已有的环境列表

```bash
$ conda info -e
```

激活环境：

```bash
$ conda activate triqs
```

退出当前激活的环境：

```bash
$ conda deactivate
```

删除环境：

```bash
$ conda remove -n your_env_name --all
```

