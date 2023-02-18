# wechat-ChatGPT

## 使用方式

 - 方式一：虚拟终端接入ChatGPT，使用wechat.py。填入API_KEY后，直接运行即可（这种方式较不稳定，会被微信警告）
 - 方式二：RPA的方式，使用chatgpt-rpa.py。填入API_KEY后，直接将脚本复制到RPA程序即可（很稳定）

# 配合视频，姿势更正确噢

  - 【微信接入ChatGPT最稳定的方式，被抓你来找我 ｜ 用ChatGPT做表格直接生成Excel文件-哔哩哔哩】 https://b23.tv/668Ukt4

  **如果您觉得有用，记得给我一键三连~**

## 核心方法介绍

  1. text_reply(msg)
  自动回复，封装好的装饰器，当接收到的消息是Text，即文字消息

  2. chatgpt(question)
  调用chatgpt接口问答，支持联系上下文

  3. generate_excel(table_str)
  能够在ChatGPT聊天过程中直接生成Excel文件进行发送

## 方式一环境要求

  环境要求：python3
  
  相关库：itchat,openai,xlwt。使用pip install即可
  
  api_key:根据视频指示进入OpenAI官网生成，对应填写到脚本的 openai.api_key 中即可
  
  运行：直接运行脚本，会自动弹出二维码，扫码进行登录就可以自动回复了
  
## 方式二环境要求

  直接在RPA程序中安装openai的库即可

## 注意事项

  1. 由于最近微信的限制，方式一模拟登录的方式有可能会被检测到，微信会进行警告，如果追求稳妥可以看土土视频的第二种方式
  2. 由于最近微信的限制，新注册的用户无法通过方式一登录，只支持老用户(2017之前注册的)
  3. **强烈推荐大家先看土土的视频一步步跟着操作，超简单的喔～**

