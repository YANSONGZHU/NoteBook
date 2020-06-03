# Ubuntu KVM 虚拟机配置

### 确认您的硬件是否支持虚拟化

执行 `egrep` 命令以验证您的服务器的硬件是否支持虚拟化

```bash
$ egrep -c '(vmx|svm)' /proc/cpuinfo
```

输出结果大于 0，意味着硬件支持虚拟化

安装 `kvm-ok` 实用程序，该程序用于确定您的服务器是否能够运行硬件加速的 KVM 虚拟机

```bash
$ sudo apt install cpu-checker
```

运行 kvm-ok 命令确认输出结果

```bash
$ sudo kvm-ok
```

### 安装 KVM 及其依赖包

安装 KVM 及其依赖项

```bash
$ sudo apt update
$ sudo apt install qemu qemu-kvm libvirt-bin  bridge-utils  virt-manager
```

### 启动并启用 libvirtd 服务

我们在 Ubuntu 18.04 服务器上安装 qemu 和 libvirtd 软件包之后，它就会自动启动并启用 `libvirtd` 服务，如果 `libvirtd` 服务没有开启，则运行以下命令开启

```bash
$ sudo service libvirtd start
$ sudo update-rc.d libvirtd enable
```

确认 libvirtd 服务的状态

```bash
$ service libvirtd status
```

