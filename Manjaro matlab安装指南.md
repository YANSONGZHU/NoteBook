# Manjaro matlab安装指南

从matlab官网下载Linux安装压缩包

使用unzip解压压缩包文件

通过AUR安装libselinux和libsepol

运行安装脚本：

```bash
$ ./install
```

在安装过程中：

创建指向以下位置中的MATLAB脚本的符号链接 :/usr/local/bin/ 提示无权限

运行以下命令：

```bash
$ cd /usr/local/
$ sudo chmod 777 bin
```

