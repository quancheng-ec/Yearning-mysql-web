<p align="center">
        <img width="300" src="logo.png">
</p>

# Yearning SQL审核平台

![](https://img.shields.io/badge/build-release-brightgreen.svg)  
![](https://img.shields.io/badge/version-v1.3.5-brightgreen.svg)  
![](https://img.shields.io/badge/vue.js-2.5.13-brightgreen.svg) 
![](https://img.shields.io/badge/iview-3.1.0-brightgreen.svg?style=flat-square) 
![](https://img.shields.io/badge/python-3.6-brightgreen.svg)
![](https://img.shields.io/badge/Django-2.0.1-brightgreen.svg)

##### 企业级MYSQL web端 SQL审核平台。增加支持ssh登录mysql数据库

## Website 官网

[www.yearning.io](http://yearning.io)

## Quancheng-ec Adaption
1. 给 api 和 spa 分别作了两个 docker 文件可以 docker 化部署
2. 调整了下用户创建模型，对 ldap 更友好一些
3. 调整了配置从环境变更获取的逻辑
4. 调整了 spa 的 api base domain，去掉了:8000 这个，要做一层前端转发，如果本地测试可以调整下`webpage/src/lib/utils.js`里面的设置


## Feature 功能

- 数据库字典自动生成
- SQL查询
    - 查询工单 
    - 导出
    - 自动补全，智能提示 
    - 查询语句审计
- SQL可视化自动生成
    - 索引语句自动生成
    - DDL语句自动生成
- SQL审核
    - 流程化工单
    - SQL语句检测与执行
    - SQL回滚
    - 历史审核记录
- 推送
    - E-mail工单推送
    - 钉钉webhook机器人工单推送
- 其他
    - todoList
    - LDAP登陆  
    - 动态配置 
- 用户权限及管理
    - 拼图式权限划分(共12项独立权限,可随意组合)
    - 组合式权限组
    - 支持限制邮箱后缀名的有限注册功能

## Environment 环境

- Python 3.6

- Vue.js 2.5

- Django 2.0

## Install 安装及使用日志

详细安装步骤请访问[www.yearning.io](http://yearning.io)获得帮助

增加了ssh登录数据库，需要修改下面2个文件，需要有公钥可以登录远程服务器，详细见安装步骤文档

```
src/libs/call_inception.py
src/libs/con_database.py
```

[安装步骤](安装步骤.md)

[使用及安装文档](http://guide.yearning.io)

## Support 支持Yearning

如果Yearning能够帮助到你，请支持下Yearning吧，让Yearning能够持续改善并更新

[捐赠](https://github.com/cookieY/Yearning)

## About 联系方式

   QQ群:103674679

   E-mail: im@supermancookie.com

## Snapshot 效果展示

- Login



![login](img/login.jpeg)


- Dashboard

![](img/dash.png)

- 审核

![](img/order.png)

- SQL语法高亮及自动补全

![](img/lighit.png)

- 查询

![](img/query.png)

- 细粒度的权限分配
  ![](img/PER.png)

- 我的工单
  ![](img/myorder.png)


## License

- AGPL v3

任何二次开发及二次开源项目请严格遵守相应开源许可

2018 © Cookie


