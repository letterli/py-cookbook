### Ansible简介以及安装配置

----

#### 简介

Ansible是用python编写的一个IT自动化工具。它能配置系统、部署软件、编排更复杂的IT任务等。
Ansible特点简洁、不需要在每个节点上安装组件。

#### 工作方式

Ansible工具不使用守护进程。Ansible 1.3之后版本使用原生OpenSSH连接远程主机。Ansible 1.2前，使用
python paramiko模块连接远程主机。

Ansible默认假设你使用ssh秘钥进行验证，如果你想通过输入密码进行验证，可以用选项 -ask-pass。要使用sudo功能，
需要密码时可以用 -ask-sudo-pass。

+--------------------------+                           +------------------------------------------+
|安装了Ansible的Linux/Unix  |             SSH            |  文件服务器1           本地或远程数据中心    |
| 工作站                    | <------------------------> |  数据库服务器          的Unix/Linux服务器  |
|                          |                            |  代理服务器                               |
+--------------------------+             模块           +------------------------------------------+
         管理端

1.管理端安装Ansible。
2.文件服务器到代理服务器，使用管理端Ansible来自动管理所有服务器。
3.SSH 本地/远程服务器之间设置SSH秘钥。

#### 安装

##### CentOS 安装ansible

> yum install ansible

#####  使用pip安装ansible

> pip install ansible

#####  Ubuntu 安装ansible

> apt-get install software-properties-common
> apt-add-repository ppa:ansible/ansible
> apt-get update
> apt-get install ansible

#### 配置SSH秘钥

> ssh-keygen -t rsa  生成  ~/.ssh/id_rsa.pub
> ssh-copy-id -i id_rsa.pub root@slaveserver



