from revChatGPT.V1 import Chatbot
config={
  "email": "Xccj3Btc@proton.me",
  "password": "Xccj3Btc6p6dfR6e"
}
chatbot = Chatbot(config)
result = chatbot.ask("在吗")
print(result)
prev_text = ""

for data in result:

    # 从回答数据中提取ChatGPT的回答，并去除前面已经输出过的文本部分
    message = data["message"][len(prev_text) :]

    # 输出ChatGPT的回答
    print(message, end="", flush=True)

    # 更新prev_text变量
    prev_text = data["message"]