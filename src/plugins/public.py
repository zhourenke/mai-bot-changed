from nonebot import on_command, on_notice
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, Event, Bot, MessageSegment
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
from src.libraries.image import *


@event_preprocessor
async def preprocessor(bot, event, state):
    if hasattr(event, 'message_type') and event.message_type == "private" and event.sub_type != "friend":
        raise IgnoredException("not reply group temp message")


help = on_command('## 帮助')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''可用命令：
## 今日舞萌
                                                                                                —— 查看今天的舞萌运势
                                
XXX mai XXX 什么
                                                                                                —— 在聊天中按照顺序包含“mai”和“什么”有惊喜哦
                                
## 随个 [dx/sd][绿/黄/红/紫/白]<难度>
                                                                                                —— 随机一首指定条件的乐曲，<难度> 中可带加号，不能带小数点
                                
## 查歌 <部分标题>
                                                                                                —— 查询曲名中包含 <部分标题> 的所有乐曲
                                
## [绿/黄/红/紫/白]<乐曲 ID>
                                                                                                —— 查询指定 <乐曲 ID> 的基本信息或对应谱色的详细谱面信息
                                
## 定数查歌 <定数>
## 定数查歌 <定数下限> <定数上限>
                                                                                                —— 查询指定定数或定数区间内的所有乐曲，<定数*> 中可带小数点，不能带加号
                                
## 分数线 <绿/黄/红/紫/白+乐曲 ID> <分数线>
                                                                                                —— 输入 “## 分数线 帮助” 以获得帮助

## b40 <用户名>
                                                                                                —— 查询在 https://www.diving-fish.com/ 注册的 <用户名> 的 Best 40 成绩图
                                                                                                
## b50 <用户名>
                                                                                                —— 查询在 https://www.diving-fish.com/ 注册的 <用户名> 的 Best 50 成绩图
                                                                                                                                                                                                
## 帮助
                                                                                                —— 显示此界面'''
    await help.send(Message([
        MessageSegment("image", {
            "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        })
    ]))



async def _group_poke(bot: Bot, event: Event) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


poke = on_notice(rule=_group_poke, priority=10, block=True)


@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if event.__getattribute__('group_id') is None:
        event.__delattr__('group_id')
    await poke.send(Message([
        MessageSegment("poke", {
            "qq": f"{event.sender_id}"
        })
    ]))
