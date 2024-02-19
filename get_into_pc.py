import requests
from bs4 import BeautifulSoup

async def searsh_resolts_name_git_into_pc(app_name):
    apps_list = []    
    # apps_list.clear()

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://getintopc.com/?s={app_name}', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')

        if soup.find('div', {'class':'posts clear-block'}).find_all('h2', {'class':'title'}) == None:
            # await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
            pass


        else :

            a = soup.find('div', {'class':'posts clear-block'}).find_all('h2', {'class':'title'})

            for i in a :
                a = i.find('a')['title']
                app_name_split = a.split()
                if app_name_split[0] == 'Permanent' and app_name_split[1] == 'Link:':
                    app_name_split.remove('Permanent')
                    app_name_split.remove('Link:')
                else:
                    pass
                app_name = " ".join(app_name_split)
                apps_list.append(app_name)
            
        
            return apps_list
        
            
    except:
        # await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )

        # bot.send_message ( user_id, "يوجد مشكله جرب مره ثانيه لاحقا او تواصل مع فريق الدعم مرفق لهم  searsh_resolts_git_into_pc_ERROR" )
        pass

async def searsh_resolts_links_git_into_pc(app_name):

    links_list = []
    # links_list.clear()
    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://getintopc.com/?s={app_name}', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')

        if soup.find('div', {'class':'posts clear-block'}).find_all('h2', {'class':'title'}) == None:
            #bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
            pass

        else :

            a = soup.find('div', {'class':'posts clear-block'}).find_all('h2', {'class':'title'})

            for i in a :
                a = i.find('a')['href']
                links_list.append(a)
            
            return links_list
        
    except:
        pass