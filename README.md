``` —————————————————————— 软件打包命令 ——————————————————————

pyinstaller NjtechAutologin.py -w --clean -i UI\resource\njtech-icon\NJtech02.ico --log-level WARN --hidden-import PyQt5.sip --noconfirm -F

pyinstaller autologin.py -w --clean -i UI\resource\njtech-icon\autologin.ico --log-level WARN --noconfirm

--specpath Build

pyi-makespec -w xxx.py

pyinstaller -D xxx.spec

pyside2-uic login.ui -o login.py

pyside2-rcc resource.qrc -o resource.py


```



# **【南工大上网认证 项目开发日志】**  

[🔗CSDN项目地址][CSDN_URL]  



## **项目开发命名规范：**  

- > 1.用户软件压缩包名：大驼峰中划线  
    2.打包的主程序名称：大驼峰命名  
    3.打包的子程序名称：全小写命名  

- > 1.项目编译文件夹：build  
    2.源码运行产生库：config  
    3.软件发布文件夹：dist  
    4.源码依赖工具库：lib  
    5.软件前端界面UI：ui

- > 1.类名：大驼峰  
    2.函数：小驼峰  
    3.变量：全小写中划线  
    4.控件：建议用大驼峰后缀  



## **源码运行问题日志**  
  
- > 用户登录文件的读写 ✔



## **软件发布测试日志**

- > 软件执行路径问题，读写找不到文件 ✔  
    pyinstaller打包：--specpath dir 打包无图标 ❓



## **项目开发日记**

- 21.10.3晚  
  软件打包遇到无图标问题，以为PS处理了icon图片产生的问题，下载图标制作软件误装全家！
- 21.10.4早  
  全家桶弹窗，C盘大清理。无法访问外网，已忘上次处理方法，仍未知问题所在，干脆回滚系统，重装驱动。冥思苦想，删除上网认证cookies，问题解决！





[CSDN_URL]:https://blog.csdn.net/Alpherkin/article/details/115599094
