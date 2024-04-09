### 代码测试环境
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;用于测试"comtuscal"包；

--
### 操作步骤
> 1. 上传源码"./customcal"至LINUX环境（已安装DOCKER）  
>    例如"/tmp/customcal"
> 
> 2. 修改"Dockfile"中要使用的Python环境  
>    例如要使用"python:3.5-alpine"（取消"FROM python:3.5-alpine"前的"#"注释符, 并使用"#"注释其它"FROM"语句）
>    ```  
>    $ cd /tmp/customcal/_simpleTest
>    $ vi Dockerfile
>    FROM python:3.5-alpine   
>    # FROM python:3.12-alpine
>    ````
> 
> 4. 测试(LINUX上执行)  
>    ````
>    $ cd /tmp/customcal/_simpleTest
>    $ chmod +x testStart.sh
>    $ ./testStart.sh
>    ````
