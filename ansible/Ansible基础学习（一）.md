### Ansible基础学习 Inventory文件（一）

---

#### Inventory 文件

Ansible 默认从/etc/ansible/hosts Inventory文件中读取远程主机信息。

> [webservers]
> 192.168.1.102
> 192.168.1.103
> one.example.com
> two.example.com
>
> [dbservers]
> database01
> database02

中括号内的是组名称，一台主机可以属于多个组。一台属于多个组的主机会读取多个组的变量文件，这样可能会有冲突。

如果SSH不是使用默认端口，可以在主机后面指定ssh端口。

> server.example.com:2222

如果使用静态IP，希望hosts文件中使用别名或者通过通道连接。

> server  ansible_ssh_port=5555  ansible_ssh_host=192.168.1.104

如果有很多主机名称类似

>  www[01:50].example.com
>  db-[a:f].example.com

可以指定每个主机的连接类型和用户。

> webserver.example.com ansible_connection=ssh  ansible_ssh_user=root
> localhost     ansible_connection=local

##### 主机变量

> [atlanta]
> host1    http_port=80   maxRequestsPerChild=809
> host2    http_port=303  maxRequestsPerChild=900

##### 组变量

> [atlanta]
> host1
> host2
>
> [atlanta:vars]
> ntp_server=ntp.atlanta.example.com
> proxy=proxy.atlanta.example.com

##### 组的组以及组变量

> [atlanta]
> host1
> host2
>
> [raleigh]
> host2
> host3
>
> [southeast:children]
> atlanta
> raleigh
>
> [southeast:vars]
> some_server=foo.southeast.example.com
> halon_system_timeout=30

##### 分离主机和组变量

Ansible中更好的实践并不是把变量保存到Inventory文件，而是使用YAML格式保存到和Inventory文件单独的文件中。

假设Inventory文件路径为/etc/ansible/hosts,其中一个主机名为'foosball'，属于'raleigh'和'webserver'两个组，
那么以下位置的YAML文件对foosball主机有效。

> /etc/ansible/group_vars/raleigh
> /etc/ansible/group_vars/webservers
> /etc/ansible/host_vars/foosball

raleigh文件内容类似：

> ntp_server: acme.example.com
> database_server: storage.example.org

你可以创建和组名相同的目录，ansible会读取该目录中所有的YAML文件。

> /etc/ansible/group_vars/raleigh/db_settings
> /etc/ansible/group_var/raleigh/cluster_settings

**group_vars和host_vars目录可以在playbook目录下或者Inventory目录下，如果两者都有，playbook目录下的会覆盖Inventory目录下的**
