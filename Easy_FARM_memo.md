# Easy FARM

## 0. やりたいこと

1. Udemy講座の簡略化
2. MongoDBのローカル化
3. 会社環境で再実行

## 1. 導入

以下のUdemy講座を元にしている

[FastAPI + React によるフルスタック Web開発](https://www.udemy.com/course/farm-stack-react-fastapi/)

## 2. Easy FARM

Udemy講座のものからセキュリティなどの面倒くさいものを省略したアプリを作成したい。

それとMongoDBはローカルのものに変更する

TODO: 会社の想定したい環境で作成する。

## 2.1. 環境構築

Udemy講座のものを流用。ただしMongoDBはローカル版を利用

mongodb-windows-x86_64-6.0.3-signed.msi

## 2.2. やったコマンドなど

動作確認
uvicorn main:app –-reload

### もっとも簡単なFastAPI

~~~python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to Fast API!!!"
~~~

コマンドラインで以下を実行

uvicorn main:app –-reload