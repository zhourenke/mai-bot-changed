# mai-bot（改）使用指南

注意：本 Bot 用到了闭源项目 LLOneBot，此软件会修改您的 QQNT 且无法保证安全性，若您有更好的开源反向 WebSocket 工具，可以使用您自己的工具代替 LLOneBot。

即便本 Bot 是在原项目上经过修改完善的，但同样建议您至少拥有一定的编程基础之后再尝试使用本工具。

## Step 1. 安装 Python

请下载 Python 3.8 以保证正常运行本工具。

推荐使用 Anaconda 或 Miniconda 以保证在正常运行本工具的同时不干扰您自己的 Python。

配置 Conda 的详细步骤，请参考 [Conda Documentation](https://docs.conda.io/en/latest/)。

## Step 2. 配置环境

建议使用 Git 对此项目进行版本管理。
当然您也可以直接在本界面下载代码的压缩包进行运行。

在运行本工具之前，您需要从 [这里](https://www.diving-fish.com/maibot/static.zip) 下载图片资源并解压到项目主目录的 `src` 文件夹中。

在此之后，您需要打开控制台，并切换到该项目所在的目录。

之后，输入
```
pip install -r requirements.txt
```
安装工具所需依赖。

如果不能正常安装依赖，您可能需要使用
```
python --version
```
来检查您是否正确安装 Python 3.8

至此，本工具已经全部配置完成。

## Step 3. 运行 mai-bot（改）

在控制台中输入
```
python bot.py
```
运行项目。如果输出如下所示的内容，代表运行成功：
```
06-07 11:18:15 [SUCCESS] nonebot | NoneBot is initializing...
06-07 11:18:15 [INFO] nonebot | Current Env: prod
06-07 11:18:15 [SUCCESS] nonebot | Succeeded to import "public"
06-07 11:18:19 [SUCCESS] nonebot | Succeeded to import "maimaidx"
06-07 11:18:19 [SUCCESS] nonebot | Running NoneBot...
06-07 11:18:19 [INFO] uvicorn | Started server process [114514]
06-07 11:18:19 [INFO] uvicorn | Waiting for application startup.
06-07 11:18:19 [INFO] uvicorn | Application startup complete.
06-07 11:18:19 [INFO] uvicorn | Uvicorn running on http://127.0.0.1:10219 (Press CTRL+C to quit)
```
运行成功后请勿关闭此窗口，后续需要与 LLOneBot 连接。

## Step 4. 连接 LLOneBot

参考 [LLOneBot Documentation](https://llonebot.github.io/zh-CN/guide/getting-started) 完成 LLOneBot 的安装。

安装完成后打开 QQNT 的设置界面，在侧栏中即可找到 LLOneBot。

关闭所有默认开启的选项，仅打开 `启用反向 WebSocket 服务`，添加新的监听地址：
```
ws://127.0.0.1:10219/onebot/v11/ws
```
然后点击下放的保存按钮。

至此，您就可以和对应的 QQ 号聊天并使用 mai-bot（改）的所有功能了。

## 使用说明

您可以向对应的 QQ 号发送
```
## 帮助
```
获取本 Bot 的全部功能。

## FAQ

我已经按照格式要求注册了账号并正确输入了查询 Best 40 和 Best 50 的命令，但是 Bot 提示 `未找到此玩家，请确保此玩家的用户名和查分器中的用户名相同。` 这要怎么解决？
> 您需要在 [这里](https://www.diving-fish.com/) 导入自己的舞萌 DX 成绩，导入方式参考 [舞萌 DX 查分器使用指南](https://www.diving-fish.com/maimaidx/prober_guide)。

为什么有的定数查歌消息发不出来？
> 我的设置了 Bot 输出的最大乐曲条数为 300 条，消息可能会超过 QQ 的单条消息长度上限，此时您可以在代码中手动修改这个值，以确保不会出现发不出来的情况。