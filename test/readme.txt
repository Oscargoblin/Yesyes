第一步，在其中創建一個項目文件夾和一個venv文件夾：
> mkdir myproject
> cd myproject
> py -3 -m venv venv

激活環境
>venv\Scripts\activate

要運行應用程序，請使用flask命令
flask --app hello run


要啟用調試模式，使用該--debug選項。
flask --app run --debug run

要在虛擬機venv使用python
> python
> from run import User
> User.query.all() 

要退出
> exit()

安裝 flask-wtf 表單library
> pip install -U Flask-WTF

123123123