# pymonitor

使用 python 实现的检测网站连通性的小工具，每隔一定的时间访问一次任务网站并显示访问细节。

## 运行方法

```bash
pip install -r requirements.txt
python main.py
```
根据实际情况修改配置文件`config.yml`

## 样例配置


```yml
# config.yml
log:
  config_path: logging.ini # 日志配置
monitor:
  tasks:
    - name: github # 任务名
      url: www.github.com # 访问 www.github.com
      interval: 10 # 每隔 10s 访问一次
    - name: google
      url: www.google.com
      interval: 15 # 每隔 15s 访问一次
```

## 运行结果

```
2018-03-10 19:41:54 main.py[line:43] [DEBUG] 加载日志配置完成 logging.ini
2018-03-10 19:41:54 main.py[line:23] [DEBUG] 任务个数 3
2018-03-10 19:41:54 main.py[line:28] [DEBUG] 开始任务 <Monitor(github, started)> {'name': 'github', 'url': 'www.github.com', 'interval': 10}
2018-03-10 19:41:54 main.py[line:28] [DEBUG] 开始任务 <Monitor(api, started)> {'name': 'api', 'url': 'api.github.com', 'interval': 15}
2018-03-10 19:41:54 main.py[line:28] [DEBUG] 开始任务 <Monitor(google, started)> {'name': 'google', 'url': 'www.google.com', 'interval': 15}
2018-03-10 19:41:54 Monitor.py[line:65] [DEBUG] pid:3392 github 进程加载日志配置完成 logging.ini
2018-03-10 19:41:54 Monitor.py[line:65] [DEBUG] pid:16832 api 进程加载日志配置完成 logging.ini
2018-03-10 19:41:54 Monitor.py[line:65] [DEBUG] pid:10088 google 进程加载日志配置完成 logging.ini
2018-03-10 19:42:03 Monitor.py[line:71] [DEBUG] pid:3392 github 正在监测 www.github.com
2018-03-10 19:42:04 Monitor.py[line:73] [DEBUG] pid:3392 github 监测完成
2018-03-10 19:42:04 Monitor.py[line:85] [INFO] URL:	http://www.github.com/
2018-03-10 19:42:04 Monitor.py[line:86] [INFO] Http Code:	301
2018-03-10 19:42:04 Monitor.py[line:87] [INFO] DNS lookup time:	235.0 ms
2018-03-10 19:42:04 Monitor.py[line:88] [INFO] Create conn time:	579.0 ms
2018-03-10 19:42:04 Monitor.py[line:89] [INFO] Ready conn time:	579.0 ms
2018-03-10 19:42:04 Monitor.py[line:90] [INFO] Tran Star time:	1016.0 ms
2018-03-10 19:42:04 Monitor.py[line:91] [INFO] Tran Over time:	1016.0 ms
2018-03-10 19:42:04 Monitor.py[line:92] [INFO] Download size:	0 bytes/s
2018-03-10 19:42:04 Monitor.py[line:93] [INFO] HTTP header size:	88 byte
2018-03-10 19:42:04 Monitor.py[line:94] [INFO] Avg download speed:	0.0 bytes/s
2018-03-10 19:42:04 Monitor.py[line:71] [DEBUG] pid:16832 api 正在监测 api.github.com
2018-03-10 19:42:07 Monitor.py[line:71] [DEBUG] pid:10088 google 正在监测 www.google.com
2018-03-10 19:42:12 Monitor.py[line:53] [INFO] api Failed to connect to api.github.com port 80: Timed out
2018-03-10 19:42:12 Monitor.py[line:73] [DEBUG] pid:16832 api 监测完成
......
```
