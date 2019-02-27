# web-wallpaper-on-win10-forUSTC

-----

## 这是什么

这个项目包含了将网页设为windows壁纸的python３脚本，以及为USTC定制的网页壁纸
桌面预览：（图片较大加载很慢）

![cmd-markdown-logo](https://github.com/fyr233/web-wallpaper-on-win10-forUSTC/blob/master/img/wallpaper.bmp)

## 配置环境

要想运行它，您需要有以下库或程序：

> * win32gui
> * win32api
> * wkhtmltoimage

安装方法：

### 1.win32gui与win32api

首先，在命令行运行：
```python
pip install win32gui
pip install win32api
```
如果您能运行import win32gui和import win32api，那恭喜您可以跳过这一部分

如果报错：
```python
No module named 'win32gui'
```
看看这里：https://stackoverflow.com/questions/20113456/installing-win32gui-python-module

### 2.wkhtmltoimage

下载地址：https://wkhtmltopdf.org/downloads.html

## 运行

直接运行main.py即可，如果不希望出现黑框框，可以在命令行运行　pythonw main.py

## 扩展

若要自定义桌面壁纸，将webpage文件夹中的网页替换为你的网页，其中html文件的文件名为index.html
