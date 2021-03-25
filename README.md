# FlaskをDockerで起動するサンプル

## Docker関連

#### 起動方法
`$ docker-compose up -d --build`

#### 停止
`$ docker-compose down`

## DB(Sqlite3)初期化

コンテナ内にssh  
`$ docker-compose exec web_flask bash`

appフォルダへ移動  
`$ cd app`

pythonコマンド起動  
`$ python`

DB初期化
```
$ from models.database import init_db
$ init_db()
```
これでmodels/task.dbが作成されます。

## DB(Sqlite3)データ投入方法

コンテナ内にssh  
`$ docker-compose exec web_flask bash`

appフォルダへ移動  
`$ cd app`

pythonコマンド起動  
`$ python`

データ投入
```
>>> from models.database import db_session
>>> from models.models import TaskContent
>>> t1 = TaskContent("タスク1","説明1")
>>> db_session.commit()
```

## DB(Sqlite3)データ確認方法

コンテナ内にssh  
`$ docker-compose exec web_flask bash`

appフォルダへ移動しsqlite3コマンド起動  
```
$ cd app/models
$ sqlite3 task.db
sqlite> select * from tasks;
1|タスク1|説明1|0|2021-03-25 14:46:00.429922
```
