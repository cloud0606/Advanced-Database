# Docker下安装Mongodb

## 环境

- ubuntu-18.04.1-server-amd64

## 过程

- 如果没安装Docker，需提前安装

            # 更新源
            $ sudo apt-get update

            $ sudo apt-get install docker.io

- Docker安装成功后，进行Mongodb的配置

        # 拉取Mongodb镜像
        $ sudo docker pull mongo

        # 创建文件夹，以便后续将容器内文件映射到虚拟机内
        $ sudo mkdir /mysoft && cd /mysoft

        $ sudo mkdir mongodb && cd mongodb

        $ sudo mkdir configdb && sudo mkdir db

        # 创建容器，开放27017、28017两个端口，将容器内/data/configdb/和/data/db/映射到虚拟机内
        $ docker run -d -p 27017:27017 -p 28017:28017 -v /mysoft/mongodb/configdb:/data/configdb/ -v /mysoft/mongodb/db/:/data/db/ --name mongodb mongo

        # 如果有需要，可进入容器内进行Mongodb的配置
        $ docker exec -it  mongodb  mongo admin

        # 容器内的Mongodb的相关文件位于 /usr/bin 下，我们可在该文件夹下执行相关后续操作

        @ cd /usr/bin

        @ ./mongo

