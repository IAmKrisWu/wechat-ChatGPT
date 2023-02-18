# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块
import os
import openai


def chatgpt(question):

    openai.api_key = "填入你的API_KEY

    prompt = "\nHuman: " + question
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = question,
            temperature=0.9,
            max_tokens=2000,
            frequency_penalty=0,
            presence_penalty=0,
            stop=[" Human:"," AI:"]
        )
        
        result = response["choices"][0]["text"].strip()

        return result
    except Exception as exc:
        print(exc)
