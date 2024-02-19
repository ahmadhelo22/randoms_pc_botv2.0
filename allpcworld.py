import requests
from bs4 import BeautifulSoup

async def searsh_resolts_name_allpcworld(app_name) -> list:

    apps_list = []    

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://allpcworld.com/?s={app_name}', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')

        if soup.find('div', {'class':'inner-wrapper'}).find('main', id = 'main').find('h1').next_element == 'Nothing Found':
            # await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
            # return None
            pass

        else:


            a = soup.find('div', {'class':'inner-wrapper'}).find('main', id = 'main').find_all('article')

            for i in a :
                c = i.find('a').next_element
                apps_list.append(c)

            return apps_list


    except:
        # await bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
        # return None
        pass




def searsh_resolts_links_allpcworld(app_name):
    apps_links = []    

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://allpcworld.com/?s={app_name}', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')


        if soup.find('div', {'class':'inner-wrapper'}).find('main', id = 'main').find('h1').next_element == 'Nothing Found':
            pass
        else:


            a = soup.find('div', {'class':'inner-wrapper'}).find('main', id = 'main').find_all('article')

            for i in a :
                c = i.find('a')['href']
                apps_links.append(c)
            
            return apps_links
                
    except:
        # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
        pass

