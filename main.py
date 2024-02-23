from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message
from bs4 import BeautifulSoup
import requests
import asyncio
import os
from flask_app import keep_alive
from buttons_generator import button_generater_func
from short_link import short_link_opration
from get_into_pc import searsh_resolts_name_git_into_pc, searsh_resolts_links_git_into_pc
from freesoftwarefiles import searsh_resolts_name_free_soft_ware, searsh_resolts_links_free_soft_ware
from allpcworld import searsh_resolts_name_allpcworld, searsh_resolts_links_allpcworld
from buttons_replay import buttoms_replay, pages, how_to_skip_ads
from texte_for_bot import skip_ads, suggestions, how_it_works, the_bots, the_user_helper, welcomeing_text
from data import write, read

# تجهيز قاعده البيانات لاضافع ال id 
db_path = 'db.json'
if os.path.exists(db_path):
    pass
else:
    write(db_path, [])
data = read(db_path)

bot_token="6626941096:AAERjvdFJsOV7y3p3mng0cH8geFe6x1Y9Fs"
#معلومات و التعريف عن البوت
bot_pyrogram = Client(
    name='Bot',
    api_hash="db93b5d1b9cc15b7b8512a7082a99692",
    api_id=29817603,
    bot_token=bot_token
)

# #الحصول على جميع id الن\مستخدمين في القناه
# ch = "RANDOMS_CH" 
# with bot_pyrogram as client:
#     # الحصول على معرفات المستخدمين في القناة
#     users = client.get_chat_members(ch)

#     # طباعة معرفات المستخدمين
#     for user in users:
#         user_id = user.user.id

#         if user_id not in data and user_id != 6104541947 and user_id != 6626941096:
#             data.append(user_id)
#             write(db_path, data)
#         else:
#             pass

#تحتوي على مذا بحث المستخدم
servers_search_name_dic = {
    'server_one_search_name':[],
    'server_two_search_name':[],
    'server_three_search_name':[]
    }

#تحتوي على نتائج البحت
servers_dic = {
    'server_one':[],
    'server_two':[],
    'server_three':[]
    }

#لمعرفه اي سيرفر اختار العميل
nummber_of_the_server = []


#########################################################
#########################################################

#اوامر المستخدم معرفه عدد المستخدمين
@bot_pyrogram.on_message(filters.command('users_num'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        users_count = len(data)
        await msg.reply(users_count)

# معرفه id المستخدمين اوامر المستخدم
@bot_pyrogram.on_message(filters.command('users_id'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        for i in data:
            await msg.reply(i)

#اوامر المستخدم معرفه معلومات حول مستخدم واحد فقط
@bot_pyrogram.on_message(filters.command('user'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        try:
            id = msg.text
            name = id.split(None, 1)[1]
            info = await bot.get_chat(int(name))
            await msg.reply(info)
        except:
            await msg.reply('اختر ال id الذي تود البحث عنه')

#اوامر المستخدم ارسال نص لكل مستخدمين البوت
@bot_pyrogram.on_message(filters.command('user_bc'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        try:
            id = msg.text
            text_to_send = id.split(None, 1)[1]
            for i in data:
                    await bot.send_message(i, text_to_send)
        except:
            await msg.reply("يوجد مشكله بارسال الرسائل لجميع المستخدمين او يجب ان تكتب الرساله التي تود ارسالها للمستخدمين")

# ارسال ملف يحتوي على الid الخاص بكل المستخدمين 
@bot_pyrogram.on_message(filters.command('users_file'))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        await bot.send_document(user_id, 'db.json')

# help, uh, user_help اوامر المستخدم
@bot_pyrogram.on_message(filters.command(['help', 'user_help', 'uh']))
async def on_owner_command(bot:Client, msg:Message):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    if user_id == 5497992601 :
        text = the_user_helper()
        await msg.reply(text)

#########################################################
#########################################################
#  بدايه البوت و الامر  'start'
@bot_pyrogram.on_message(filters.command('start'))
async def start(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    #حفظ id المستخدم فقط اذا ضغط ستارت start 
    if user_id not in data:
        data.append(user_id)
        write(db_path, data)
    
    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"

    req = requests.get(url)
    
    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        #الرد بالازرار
        buttoms = buttoms_replay()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        text = welcomeing_text()

        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, text, reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#صفحات مواقع التواصل الاجتماعي
@bot_pyrogram.on_message(filters.regex('صفحاتنا'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        #الرد بالازرار
        buttoms = pages()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, "تابعنا على وسائل التواصل الاجتماعي", reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#شرح كيف يعمل البوت
@bot_pyrogram.on_message(filters.regex('حول عمل البوت'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id


    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, how_it_works())

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#للتواصل معي بخصوص البوت
@bot_pyrogram.on_message(filters.regex('لاي اقتراحات'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, suggestions())

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#بوتاتنا
@bot_pyrogram.on_message(filters.regex('بوتاتنا'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        # ارسال الرساله 
        await bot.send_message(user_id, the_bots())

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#لتخطي الاعلانات
@bot_pyrogram.on_message(filters.regex('كيف تتخطا الاعلانات'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        #الرد بالازرار
        buttoms = how_to_skip_ads()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        #الرساله
        message = skip_ads()

        # ارسال الرساله 
        await bot.send_message(user_id, message, reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#ارسال مقطع اختصار الروابط windos
@bot_pyrogram.on_message(filters.regex('تخطي الاعلانات windows'))
async def skip_ad_windos(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        
        try:
            #رابط الفيديو
            vidio_dir = "http://res.cloudinary.com/dfcge5cyk/video/upload/c_limit,h_150/f_mp4,du_30/v1708668734/randoms/randoms_pc/hs5vmpnysosxp1wfa5zg.mp4"
            #ارسال الفيديو
            await bot.send_video(user_id, vidio_dir)
        except:
            text  = 'يوجد مشكله بارسال الفيديو'
            await bot.send_message(user_id, text)
    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		


#ارسال مقطع اختصار الروابط ios
@bot_pyrogram.on_message(filters.regex('تخطي الاعلانات لاجهزه ios'))
async def skip_ad_windos(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        try:
            #رابط الفيديو
            vidio_dir = "https://res.cloudinary.com/dfcge5cyk/video/upload/v1708685008/randoms/randoms_pc/yfnhfu9ifjnarrjrq4ql.mp4"
            #ارسال الفيديو
            await bot.send_video(user_id, vidio_dir)
        except:
            text  = 'يوجد مشكله بارسال الفيديو'
            await bot.send_message(user_id, text)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

#ارسال مقطع اختصار الروابط android
@bot_pyrogram.on_message(filters.regex('تخطي الاعلانات لاجهزه android'))
async def skip_ad_windos(bot:Client, msg:Message):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        try:
            #رابط الفيديو
            vidio_dir = "https://res.cloudinary.com/dfcge5cyk/video/upload/v1708690569/randoms/randoms_pc/yiexgixbr9zaaryaxhfp.mp4"
            #ارسال الفيديو
            await bot.send_video(user_id, vidio_dir)
        except:
            text  = 'يوجد مشكله بارسال الفيديو'
            await bot.send_message(user_id, text)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		


#للعوده للصفحه الرئيسيه للبوت
@bot_pyrogram.on_message(filters.regex('<<عوده'))
async def pages_(bot:Client, msg):
    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

        # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
        #الرد بالازرار
        buttoms = buttoms_replay()
        replay_markup = ReplyKeyboardMarkup(buttoms, one_time_keyboard= True, resize_keyboard=True)

        # ارسال الرساله الترحيبيه
        await bot.send_message(user_id, 'عدنا', reply_markup=replay_markup)

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		


#ارسال اسم البرنامج مع الفلم 
@bot_pyrogram.on_message(filters.command(['program', 'برنامج', 'p', 'P']))
async def movie_name(bot:Client, msg):

    #اليوسر ايد الخاص بالمرسل
    user_id = msg.from_user.id

    # يوزر القناة بدون @
    ch = "RANDOMS_CH" 
    # المستخدم من اجل التاكد من اشتراكه في البوت  id استخراج
    # توكن البوت - ورفعه مشرف بالقناه 
    token = bot_token
    url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ch}&user_id={user_id}"
    req =  requests.get(url)

    #اذا اليوسر مشترك بالقناه
    if user_id == ch or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:

        msg_for_bot = await bot.send_message ( user_id, "تتم المعالجه..." )

        #اسم البرنامج الذي ارسله المستخدم
        try:
            #استخلاص كلمه من رساله المستخدم p 
            name_row = msg.text
            name = name_row.split(None, 1)[1]

            #استخلاص رقم السيرفر و ارساله 
            num_of_the_server_split = name.split()
            num_of_the_server = num_of_the_server_split.pop()
            # bot.send_message(user_id, num_of_the_server)

            #استخلاص اسم البرنامج
            name_of_the_program_split = name_row.split()
            name_of_the_program_split.pop()
            name_of_the_program = " ".join(name_of_the_program_split).split(None, 1)[1]
            # bot.send_message(user_id, name_of_the_movie)

        except IndexError:
            await msg_for_bot.delete()
            await bot.send_message(user_id, 'اكتب اسم البرنامج مع رقم السيرفر')
            
        #ما العمليه التي ستتم عند اختياره لسيرفر معين 
            
        try:
            if num_of_the_server == "1":

                nummber_of_the_server.append('server one 1')

                app_name_split = name_of_the_program.split()
                app_name = '+'.join(app_name_split)

                #اضافه ما بحث عنه المستخدم
                servers_search_name_dic['server_one_search_name'].extend(app_name)

                a = await searsh_resolts_name_git_into_pc(app_name)
                #اضافه نتائج البحث

                try:
                    servers_dic['server_one'].extend(a)
                    await msg_for_bot.delete()
                    await button_generater_func(a, InlineKeyboardButton, InlineKeyboardMarkup, msg)
                except:
                    await msg_for_bot.delete()
                    await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )


            elif num_of_the_server == '2':
                nummber_of_the_server.append('server two 2')

                app_name_split = name_of_the_program.split()
                app_name = '+'.join(app_name_split)

                #اضافه ما بحث عنه المستخدم
                servers_search_name_dic['server_two_search_name'].extend(app_name)

                a = await searsh_resolts_name_free_soft_ware(app_name)

                try:
                    servers_dic['server_two'].extend(a)
                    await msg_for_bot.delete()
                    await button_generater_func(a, InlineKeyboardButton, InlineKeyboardMarkup, msg)
                except:
                    await msg_for_bot.delete()
                    await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )

            
            elif num_of_the_server == '3':
                nummber_of_the_server.append('server three 3')

                app_name_split = name_of_the_program.split()
                app_name = '+'.join(app_name_split)

                #اضافه ما بحث عنه المستخدم
                servers_search_name_dic['server_three_search_name'].extend(app_name)

                a = await searsh_resolts_name_allpcworld(app_name)

                try:
                    servers_dic['server_three'].extend(a)
                    await msg_for_bot.delete()
                    await button_generater_func(a, InlineKeyboardButton, InlineKeyboardMarkup, msg)
                except:
                    await msg_for_bot.delete()
                    await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )


            else:
                pass

        except UnboundLocalError:
            pass

    else:
        ch = "RANDOMS_CH" # يوزر القناة بدون @ 
        k = InlineKeyboardMarkup([[InlineKeyboardButton(f"RANDOMS_CH",url=f"t.me/{ch}")]])
        await msg.reply_text(f"""**عذرا عزيزي - {msg.from_user.first_name}  عليك الاشتراك في قناة**""",reply_markup=k,disable_web_page_preview=True)		

@bot_pyrogram.on_callback_query ( )
async def handle_button_click ( client:Client, query ) :
    # الحصول على النص المكتوب في الزر المضغوط
    new_sentences = query.data
    # query.message.reply_text ( new_sentences )

    if 'server one 1' in  nummber_of_the_server:
        nummber_of_the_server.clear()


        try:

            #اضافه + لكي يتعامل معها الفنكشن 
            app_name_split = servers_search_name_dic['server_one_search_name']
            app_name = ''.join(app_name_split)
            app_name_split.clear()

            #لسته لنكات البرامج
            links_of_apps = await searsh_resolts_links_git_into_pc(app_name)
            #لسته اسماء البرامح
            name_of_apps = servers_dic['server_one']

            #تبديل اسم البرنامج بالرابط
            index =  name_of_apps.index(new_sentences)
            adjacent_value =  links_of_apps[index]

            #اختصار الرابط
            short_link = short_link_opration(adjacent_value)

            #الرد بالرابط
            await query.message.reply_text ( short_link )

            #محي جميع السماء الافلام من الدكشنري ليبدا من جديد
            servers_dic['server_one'].clear()

        except:
            await query.message.reply_text ( 'تم محي البيانات المؤقته عاود بعد قليل بسبب الضغط...'  )

    elif 'server two 2' in  nummber_of_the_server:
        nummber_of_the_server.clear()

        try:

            #اضافه + لكي يتعامل معها الفنكشن 
            app_name_split = servers_search_name_dic['server_two_search_name']
            app_name = ''.join(app_name_split)
            app_name_split.clear()

            #لسته لنكات البرامج
            links_of_apps = searsh_resolts_links_free_soft_ware(app_name)
            #لسته اسماء البرامح
            name_of_apps = servers_dic['server_two']

            #تبديل اسم البرنامج بالرابط
            index =  name_of_apps.index(new_sentences)
            adjacent_value = links_of_apps[index]

            #اختصار الرابط
            short_link = short_link_opration(adjacent_value)

            #الرد بالرابط
            await query.message.reply_text ( short_link )

            #محي جميع السماء الافلام من الدكشنري ليبدا من جديد
            servers_dic['server_two'].clear()

        except:
            await query.message.reply_text ( 'تم محي البيانات المؤقته عاود بعد قليل بسبب الضغط...'  )

    elif 'server three 3' in  nummber_of_the_server:
        nummber_of_the_server.clear()

        try:

            #اضافه + لكي يتعامل معها الفنكشن 
            app_name_split = servers_search_name_dic['server_three_search_name']
            app_name = ''.join(app_name_split)
            app_name_split.clear()

            #لسته لنكات البرامج
            links_of_apps = searsh_resolts_links_allpcworld(app_name)
            #لسته اسماء البرامح
            name_of_apps = servers_dic['server_three']

            #تبديل اسم البرنامج بالرابط
            index = name_of_apps.index(new_sentences)
            adjacent_value = links_of_apps[index]

            #اختصار الرابط
            short_link = short_link_opration(adjacent_value)

            #الرد بالرابط
            await query.message.reply_text ( short_link )

            #محي جميع السماء الافلام من الدكشنري ليبدا من جديد
            servers_dic['server_three'].clear()

        except:
               await query.message.reply_text ( 'تم محي البيانات المؤقته عاود بعد قليل بسبب الضغط...' )
        
    else:
        await query.message.reply_text ( 'تم محي البيانات المؤقته عاود بعد قليل بسبب الضغط...'  )


if __name__ == "__main__":
    keep_alive()
    bot_pyrogram.run()

else:
    print("the bot is faile :(")
