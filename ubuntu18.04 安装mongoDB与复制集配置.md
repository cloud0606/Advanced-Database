# mongoDB使用

## 实验环境

- 虚拟机：ubuntu18.04 
- mongoDB 4.0
- python3.6

## 操作过程

- 安装

```bash
# 导入公钥
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
# 添加apt源
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list

# apt-get 下载 
sudo apt-get update
sudo apt-get install -y mongodb-org

# 关闭自动更新
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections

# 服务启动关闭
sudo service mongod stop

# 日志文件
/var/log/mongodb/mongod.log
```

- 数据库连接

  后台mongod启动后使用mongo shell进行连接,连接遵循以下url格式

  > ### Connection String:
  >
  > `mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]`
  >
  > - **mongodb://** 这是固定的格式，必须要指定。
  > - **username:password@** 可选项，如果设置，在连接数据库服务器之后，驱动都会尝试登陆这个数据库
  > - **host1** 必须的指定至少一个host, host1 是这个URI唯一要填写的。它指定了要连接服务器的地址。如果要连接复制集，请指定多个主机地址。
  > - **portX** 可选的指定端口，如果不填，默认为27017
  > - **/database** 如果指定username:password@，连接并验证登陆指定数据库。若不指定，默认打开admin数据库。
  > - **?options** 是连接选项。如果不使用/database，则前面需要加上/。所有连接选项都是键值对name=value，键值对之间通过&或;（分号）隔开

```bash
# 方法1 MongoDB shell
# 实例
# 此时连接本地默认端口27017
mongo 
# 指定端口
mongo --port 28015
# 连接远程端口
mongo "mongodb://mongodb0.example.com:27017"
# 带认证的连接
mongo "mongodb://alice@mongodb0.examples.com:27017/?authSource=admin"
# 开启TLS/SSL 
mongo "mongodb://mongodb0.example.com.local:27017,mongodb1.example.com.local:27017,mongodb2.example.com.local:27017/?replicaSet=replA&ssl=true"

# 方法2 通过其他编程接口

```

- 基本操作

```bash
# 显示当前数据库
db
# 显示所有数据库
show dbs
# 切换数据库,数据库不存在则创建数据库
use <database>
# 删除数据库
db.dropDatabase()
# 删除集合
db.collection.drop()
# 删除站点
db.site.drop()
```

- 增删查改

```bash
# 插入
db.inventory.insertMany([
   // MongoDB adds the _id field with an ObjectId if _id is not present
   { item: "journal", qty: 25, status: "A",
       size: { h: 14, w: 21, uom: "cm" }, tags: [ "blank", "red" ] },
   { item: "notebook", qty: 50, status: "A",
       size: { h: 8.5, w: 11, uom: "in" }, tags: [ "red", "blank" ] },
   { item: "paper", qty: 100, status: "D",
       size: { h: 8.5, w: 11, uom: "in" }, tags: [ "red", "blank", "plain" ] },
   { item: "planner", qty: 75, status: "D",
       size: { h: 22.85, w: 30, uom: "cm" }, tags: [ "blank", "red" ] },
   { item: "postcard", qty: 45, status: "A",
       size: { h: 10, w: 15.25, uom: "cm" }, tags: [ "blue" ] }
]);
db.collection.insertOne() 

# 查询
db.inventory.find( { status: "D" } )
db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )
db.inventory.find( { "size.uom": "in" } )
db.inventory.find( { tags: "red" } )
```

- python操作

```bash
# 安装pymongo模块 
pip install pymongo -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

# 配置mongoDB允许远程连接
sudo vim  /etc/mongod.conf
bind_ip 设置为0.0.0.0
systemctl restart mongod 
#sudo ufw allow 27017
```

## 知识点

- 数据类型
- 数据库创建的基本操作（创建数据库、集合）
- 增删查改
- 用户管理
- 索引的使用
- 数据导入导出
- 主从复制（读写分离）
- 复制集
  - 只有一个主节点（接受写操作，记录到oplog中），然后复制到从节点
  - 读请求默认指向主节点

  [演示视频](https://weibo.com/tv/v/Hv2qgj4IZ?fid=1034:4373974055069394)

```bash
# 配置文件
sudo vim /etc/mongod.conf

replication:
  replSetName:
sudo systemctl enable mongod
sudo systemctl restart  mongod

# 连接mongod
sudo mongo

# 查看复制集状态
rs.status()

# 在任一节点上执行复制集初始化命令
rs.initiate( {
  _id : "rs0",
  members: [
      { _id: 0, host: "192.168.56.102:27017" },
      { _id: 1, host: "192.168.56.104:27017" },
      { _id: 2, host: "192.168.56.105:27017" }
  ]
})

# 删除数据库
db.dropDatabase();

# 测试数据同步功能
# 主节点
use test
db.test.insertOne({"name": "kenny"})

# 从节点查询
use test
rs.slaveOk()
db.test.find()

# 测试主节点选举功能
# 强制关闭主节点上的MongoDB服务，然后重新登入mongo shell
use admin
db.shutdownServer()
rs.isMaster()

# 查看端口
ps -ef | grep mongo
netstate  -tlnp

# 修改主机标识
cat /etc/machine-id
```

## 参考

[install-mongodb-on-ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)