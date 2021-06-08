### Ansible基础学习（二）

---

#### 模式

Ansible中的模式定义了需要管理的主机。模式主要用在Ad-hoc命令中，基本格式如下：

> ansible  <pattern_goes_here> -m <module_name> -a <arguments>
>
> example: ansible webservers -m service -a "name=httpd state=restarted"

模式一般指一些组 all和*都指Inventory文件中的所有主机。模式也可以通过名称指定一个主机或一些主机：

> one.example.com
> one.example.com:two.example.com
> 192.168.1.*

模式中还可以使用简单的布尔运算。

> webservers:dbservers      webservers或dbservers中的主机
> webservers:!phoenix       属于webservers但不属于phoenix组的主机
> webservers:&staging       同时属于两个组的主机

只选择组中某些主机

> webservers[0]
> webservers[0:25]

模式中用正则表达式.

> ~(web|db).*\.example\.com

#### Ad-hoc命令

Ad-hoc命令是指快速运行，不需要保存下来的ansible命令。

##### 1.Shell

> ansible webservers -m shell -a "hostname"

##### 2.文件传输

> ansible webservers -m copy -a "src=/path/filename  dest=/path/filename"
>
> 创建目录
> ansible webservers -m file -a "dest=/path/filename mode=755 owner=wwwroot group=wwwroot state=directory"
> 删除目录
> ansible webservers -m file -a "dest=/path/filename state=absent"
> 创建文件
> ansible webservers -m file -a "dest=/path/filename owner=wwwroot group=wwwroot"
>

##### 3.管理软件包

> 确认一个软件包已安装但不更新
> ansible webservers -m yum -a "name=git state=present"
>
> 确认软件包安装指定版本
> ansible webservers -m yum -a "namge=git-1.9 state=present"
>
> 删除软件包
> ansible webservers -m yum -a "name=git state=absent"

##### 4.用户和组

> 添加用户
> ansible webservers -m user -a "name=wwwroot password=xxxxx"
>
> 删除用户
> ansible webservers -m user -a "name=wwwroot state=absent remove=yes"

##### 5.从源码部署

> ansible webservers -m git -a "repo=git://reposity.git dest=/path/code version=branch tag head"

##### 6.管理服务

> 确保所有主机启动httpd服务
> ansible webservers -m service -a "name=httpd state=started"
>
> 重启某个服务
> ansible webservers -m service -a "name=httpd state=restarted"
>
> 确认服务已停止
> ansible webservers -m service -a "name=httpd state=absent"

##### 7.限时后台操作

> 可以把耗时很长的操作放到后台，以后再检查他们的状态。
> ansible all -B 3600 -P 0 -a "/usr/bin/long_running_operation --do-stuff"
>
> 使用轮询
> ansible all -B 1800 -P 60 -a "/usr/bin/long_running_operation --do-stuff"
>

##### 8.获取Facts

Facts是指从系统中获得的一些信息或者变量。


