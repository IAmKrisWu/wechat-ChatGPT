# wechat-ChatGPT

## 核心方法

  1. text_reply(msg)
  自动回复，封装好的装饰器，当接收到的消息是Text，即文字消息

  2. chatgpt(question)
  调用chatgpt接口问答，支持联系上下文

  3. generate_excel(table_str)
  能够在ChatGPT聊天过程中直接生成Excel文件进行发送

## 使用方式

  环境要求：python3
  相关库：itchat,openai,xlwt。使用pip install即可
  api_key:根据视频指示进入OpenAI官网生成，对应填写到脚本的 openai.api_key 中即可
  运行：直接运行脚本，会自动弹出二维码，扫码进行登录就可以自动回复了

## 注意事项

  1. 由于最近微信的限制，这种模拟登录的方式有可能会被检测到，微信会进行警告，如果追求稳妥可以看土土视频的第二种方式
  2. 由于最近微信的限制，新注册的用户无法通过itchat登录，此种方式只支持老用户(2017之前注册的)

# 配合视频，姿势更正确噢

【微信接入ChatGPT最稳定的方式，被抓你来找我 ｜ 用ChatGPT做表格直接生成Excel文件-哔哩哔哩】 https://b23.tv/668Ukt4
如果您觉得有用，记得给我一键三连~
