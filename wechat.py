#coding=utf8
import itchat
import openai
import time
import calendar
import xlwt

openai.api_key = "这里填入你的API_KEY"

# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    global last_result

    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        text = msg['Text']
        if str(text).__contains__('生成表格文件'):
            xlsname = generate_excel(last_result)
            itchat.send_file(xlsname,msg['FromUserName'])
            return u'文件已给您发送过去啦'
        else:
            # 回复给好友
            return u'%s' % (chatgpt(text))


def chatgpt(question):
    global text
    global turns
    global last_result
    
    prompt = text + "\nHuman: " + question

    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",#这里我们使用的是davinci-003的模型，准确度更高。
            prompt = prompt, # 你输入的问题
            temperature=0.9, #  控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
            max_tokens=2000, #这里限制的是回答的长度，你可以可以限制字数，如:写一个300字作文等。
            frequency_penalty=0, #  [控制字符的重复度] -2.0 ~ 2.0 之间的数字，正值会根据新 tokens 在文本中的现有频率对其进行惩罚，从而降低模型逐字重复同一行的可能性
            presence_penalty=0 # [控制主题的重复度] -2.0 ~ 2.0 之间的数字，正值会根据到目前为止是否出现在文本中来惩罚新 tokens，从而增加模型谈论新主题的可能性
        )
        
        result = response["choices"][0]["text"].strip()
        last_result = result
        turns += [question] + [result]#只有这样迭代才能连续提问理解上下文
        
        if len(turns)<=10:   #为了防止超过字数限制程序会爆掉，所以提交的话轮语境为10次。
            text = " ".join(turns)
        else:
            text = " ".join(turns[-10:])
        
        return result
    except Exception as exc: #捕获异常后打印出来
        print(exc)

def generate_excel(table_str):
    try:
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        xlsname = str(time_stamp) + '.xls'
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True)
        line_num = 0

        line_list = table_str.split('\n')
        for line in line_list:
            if str(line) == '':
                continue
            elif str(line).__contains__('-'):
                continue
            elif str(line).__contains__('|'):
                res = str(line).strip('|')
                # 分割行
                for i in range(len(res.split('|'))):
                    item = res.split('|')[i]

                    sheet.write(line_num, i, item)

                line_num += 1

        xls.save(xlsname)
        return xlsname
    except:
        raise

def man_girls_scale():
    # 获取好友列表
    friends = itchat.get_friends(update=True)[0:]
     
    # 初始化计数器，有男有女，当然，有些人是不填的
    male = female = other = 0
     
    # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
    # 1表示男性，2女性
    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
     
    # 总数算上，好计算比例啊～
    total = len(friends[1:])
     
    # 好了，打印结果
    print (u"男性好友：%.2f%%" % (float(male) / total * 100))
    print (u"女性好友：%.2f%%" % (float(female) / total * 100))
    print (u"其他：%.2f%%" % (float(other) / total * 100))


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
 
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    
    #man_girls_scale()
    text = "" #设置一个字符串变量
    turns = [] #设置一个列表变量，turn指对话时的话轮
    last_result = ""
    itchat.run()
