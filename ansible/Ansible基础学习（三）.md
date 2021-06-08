### Ansible基础学习（三）

---

#### Playbooks

playbooks是ansible的配置、部署和编制语言。它描述了管理远程主机的策略和常见IT过程的步骤。
playbooks是和adhoc任务完全不同的使用ansible的方式，使用YAML格式表示，它看起来像是一种编程语言或者脚本。

```yaml
- hosts: webservers
  remote_user: root

  tasks:
  - name: ensure apache is at the latest version
    yum: pkg=httpd state=latest
  - name: write the apache config file
    template: src=/srv/httpd.j2 dest=/etc/httpd.conf

- hosts: databases
  remote_user: root

  tasks:
  - name: ensure postgresql is at the latest version
    yum: name=postgresql state=latest
  - name: ensure that postgresql is started
    service: name=postgresql state=running
```

一个play一般由4部分组成：

> * Target section: 定义将要执行play的远程主机组
> * Variable section: 定义play运行时需要使用的变量
> * Task section: 定义将要在远程主机上执行的任务列表
> * Handler section: 定义task执行完成以后需要调用的任务

example:

> - hosts: webservers       --- Target section
>
>   vars:
>       http_port: 80       --- Varible section
>       max_clients: 200
>       remote_user: root
>
>   tasks:
>       - name: ensure apache is at the latest version
>         yum:
>             pkg: httpd
>             state: latest
>
>       - name: write the apache config file
>         template:
>             src: /srv/httpd.j2
>             dest: /etc/httpd.conf
>         notify:
>             restart apache
>
>        - name: ensure apache is running
>          service:
>              name: httpd
>              state: started
>
>   handlers:
>       - name: restart apache
>         service:
>             name: httpd
>             state: restarted
>

