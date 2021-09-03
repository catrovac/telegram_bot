from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
import telethon
import time
import requests
import bs4
import os
from selenium import webdriver
import selenium
# import pprint
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
                    first_msg = messages[0].text

                    bot_servics = 'In order to use this bot, you must agree to our'
                    if bot_servics in str(first_msg):
                        url_1 = messages[0].reply_markup.rows[0].buttons[0].url
                        url_2 = messages[0].reply_markup.rows[0].buttons[1].url
                        button_igre_servise = messages[0].id
                        resp = messages[0].reply_markup.rows[1].buttons[0].data
                        result = requests.get(url_1, allow_redirects=True, headers=headers).text
                        os.system(f"start \"\" {url_1}")
                        time.sleep(5)
                        os.system("TASKKILL /F /IM chrome.exe")
                        os.system(("TASKKILL /F /IM software_reporter_tool.exe"))
                        result = requests.get(url_2, allow_redirects=True, headers=headers).text
                        os.system(f"start \"\" {url_2}")
                        time.sleep(5)
                        os.system("TASKKILL /F /IM chrome.exe")
                        os.system(("TASKKILL /F /IM software_reporter_tool.exe"))
                        time.sleep(3)
                        await client(GetBotCallbackAnswerRequest(bot_name, button_igre_servise, data=resp))
                        print('Ok')
                        await client.send_message(bot_name, '/Visit')
                    else:
                        text_button = messages[0].reply_markup.rows[0].buttons[0].text
                        rec_url = messages[0].reply_markup.rows[0].buttons[0].url
                        rec = messages[0].reply_markup.rows[1].buttons[1].data
                        rec_id = messages[0].id
                        with open('url.txt') as file:
                            url = file.read()
                        if rec_url:
                            if url == None or url != rec_url:
                                print(url)
                                if text_button:
                                    s = requests.session()
                                    # result = s.get(rec_url, allow_redirects=True, headers=headers)
                                    result = s.get(rec_url, allow_redirects=True, headers=headers).text
                                    time.sleep(2)
                                    soup = bs4.BeautifulSoup(result, 'lxml')
                                    title = soup.find('title').text
                                    print(title)
                                    if 'Just a moment...' in title:
                                        s.cookies.keys()
                                        s.cookies.clear()
                                        print(bot_name)
                                        print(f'на страничке {rec_url} есть капча, открываю браузер по умолчанию')
                                        os.system(f"start \"\" {rec_url}")
                                        time.sleep(1)
                                        msg2 = await client.get_messages(bot_name, limit=2)
                                        msg2x = msg2[0].message
                                        if 'Please stay on the site for at' in str(msg2x):
                                            time.sleep(12)
                                            os.system("TASKKILL /F /IM chrome.exe")
                                            os.system(("TASKKILL /F /IM software_reporter_tool.exe"))
                                        else:
                                            time.sleep(68)
                                            os.system("TASKKILL /F /IM chrome.exe")
                                            os.system(("TASKKILL /F /IM software_reporter_tool.exe"))
                                    else:
                                        firefox = webdriver.Firefox()
                                        firefox.get(rec_url)
                                        try:
                                            timer = firefox.find_element_by_class_name("timer").text
                                            print(timer)
                                            msg2 = await client.get_messages(bot_name, limit=2)
                                            msg2x = msg2[0].message
                                            time.sleep(1)
                                            if 'Please wait' in timer:
                                                t = str(timer).replace('Please wait', '')
                                                zx = t.replace(' seconds...', '')
                                                sleep = int(zx)
                                                print(sleep)
                                                time.sleep(sleep + 5)
                                                firefox.close()
                                                firefox.quit()
                                        except selenium.common.exceptions.WebDriverException as selen:
                                            print(selen)
                                            time.sleep(12)
                                            firefox.close()
                                            firefox.quit()
                                with open('url.txt', 'w') as file:
                                    file.write(rec_url)
                            else:
                                resp = await client(GetBotCallbackAnswerRequest(bot_name, rec_id, data=rec))
                                print(f"{rec_url} <- эта Ссылка уже была использована, пропускаем")
                                time.sleep(2)
            except ConnectionError as connect:
                print(connect)
                time.sleep(15)
            except AttributeError as atribute:
                print(atribute)
                await client.send_message(bot_name, '/balance')
                time.sleep(2)
                ball = await client.get_messages(bot_name, limit=1)
                ballx = ball[0].message
                qx = bot_name.split(" ")[0]
                print(qx)
                q = str(ballx)
                x = q.replace('Available balance:', '').split()[0]
                print(x, bot_name)
                try:
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
                except ValueError as val:
                    print(val)
                except ConnectionError as conn:
                    print(conn)
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
            except ConnectionError as conn:
                print(conn)
            except requests.exceptions.ConnectionError as con:
                print(con)
            except ValueError as val:
                print(val)
        time.sleep(10)


    with client:
        client.loop.run_until_complete(main())

