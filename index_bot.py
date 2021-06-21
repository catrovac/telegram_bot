from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
import telethon
import time
import requests
import bs4
import os
from selenium import webdriver
import selenium
#import pprint
# import popen
from setting import api, api_hash
from sql import content
from sql import vallet
from sql import headers

while True:
    name = content[0][0]
    api = content[0][1]
    api_hash = content[0][2]
    client = telethon.TelegramClient(name, api, api_hash)
    y = content.pop(0)
    content.append(y)


    async def main():
        count = 0
        await client.start()
        me = await client.get_me()
        user = me.username
        print(user)
        dialog = await client.get_dialogs()
        bot = []
        for name in dialog:
            name.to_dict()
            if 'click bot' in name.name.lower():
                bot.append(name.name)

        for bot_name in bot:
            try:
                while True:
                    await client.send_message(bot_name, '/visit')
                    time.sleep(2)
                    messages = await client.get_messages(bot_name, limit=1)
                    text_button = messages[0].reply_markup.rows[0].buttons[0].text
                    rec_url = messages[0].reply_markup.rows[0].buttons[0].url
                    rec = messages[0].reply_markup.rows[1].buttons[1].data
                    rec_id = messages[0].id
                    if rec_url:
                        if text_button:
                            s = requests.session()
                            result = s.get(rec_url, allow_redirects=True,headers=headers).text
                            time.sleep(2)
                            soup = bs4.BeautifulSoup(result, 'lxml')
                            data = soup.find('title')
                            datax = ''.join(data)
                            print(datax)
                            # print(soup)
                            # times = await client.get_messages(bot_name, limit=1)
                            # print(times)
                            s.cookies.keys()
                            s.cookies.clear()
                            if 'just' in datax.lower():
                                print(bot_name)
                                print(f'на страничке {rec_url} есть капча, открываю браузер по умолчанию')
                                os.system(f"start \"\" {rec_url}")
                                time.sleep(6)
                                msg2 = await client.get_messages(bot_name, limit=1)
                                msg2x = msg2[0].message
                                if 'Please stay on the site for at' in str(msg2x):
                                    time.sleep(16)
                                else:
                                    time.sleep(68)
                                # print(msg2x)
                                os.system("TASKKILL /F /IM chrome.exe")
                                os.system(("TASKKILL /F /IM software_reporter_tool.exe"))
                            else:
                                print(bot_name)
                                firefox = webdriver.Firefox()
                                firefox.get(rec_url)
                                time.sleep(5)
                                msg2 = await client.get_messages(bot_name, limit=1)
                                msg2x = msg2[0].message
                                if 'Please stay on the site for at' in str(msg2x):
                                    time.sleep(16)
                                else:
                                    time.sleep(68)
                                firefox.close()
                                firefox.quit()
            except ConnectionError as connect:
                print(connect)
            except AttributeError as atribute:
                print(atribute)
                await client.send_message(bot_name, '/balance')
                time.sleep(1)
                ball = await client.get_messages(bot_name, limit=1)
                ballx = ball[0].message
                qx = bot_name.split(" ")[0]
                print(qx)
                q = str(ballx)
                x = q.replace('Available balance:', '').split()[0]#
                print(x, bot_name)
                if float(x) > float(0.00022) and bot_name != 'DOGE Click Bot' and bot_name != 'BTC Click Bot':
                    await client.send_message(bot_name, 'Withdraw')
                    time.sleep(1)
                    vals = vallet[qx]
                    await client.send_message(bot_name, vals)
                    time.sleep(1)
                    await client.send_message(bot_name, 'Max amount')
                    time.sleep(1)
                    await client.send_message(bot_name, 'confirm')
                elif bot_name == 'DOGE Click Bot' and float(2.1) < float(x):
                    await client.send_message(bot_name, 'Withdraw')
                    time.sleep(1)
                    zxbot = list(bot_name.split())
                    await client.send_message(bot_name, vallet[qx])
                    time.sleep(1)
                    await client.send_message(bot_name, 'Max amount')
                    time.sleep(1)
                    await client.send_message(bot_name, 'confirm')
                elif bot_name == 'BTC Click Bot' and float(0.000050) < float(x):
                    # await client.send_message(bot_name, 'withraw')
                    time.sleep(1)
                    x_bot = list(bot_name.split())[0]
                    print(x_bot)
                    await client.send_message(bot_name, 'Withdraw')
                    time.sleep(1)
                    await client.send_message(bot_name, vallet[qx])
                    time.sleep(1)
                    await client.send_message(bot_name, 'Max amount')
                    time.sleep(1)
                    await client.send_message(bot_name, 'confirm')
            except TypeError as type_error:
                print(type_error)
                await client.send_message(bot_name, '/Balance')
            except TimeoutError as timeout:
                print(timeout)
            except requests.exceptions.TooManyRedirects as redirect:
                # from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                resp = await client(GetBotCallbackAnswerRequest(bot_name, rec_id, data=rec))
                resp
                print(redirect)
            except selenium.common.exceptions.TimeoutException as timeexcept:
                print(timeexcept)
            except NameError as name:
                print(name)
            except ValueError as val:
                print(val)
        time.sleep(20)


    with client:
        client.loop.run_until_complete(main())
