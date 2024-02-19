import requests
from bs4 import BeautifulSoup


async def searsh_resolts_name_free_soft_ware(app_name):
    apps_list = []    

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://www.freesoftwarefiles.com/?s={app_name}&search=', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')


        if soup.find('div', id = 'content').find_all('h2') == None:
            # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
            
            pass


        else:

            a = soup.find('div', id = 'content').find_all('h2')

            for i in a :
                app_name_ = i.find('a').next_element
                apps_list.append(app_name_)

            return apps_list
    except:
        # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
        pass


def searsh_resolts_links_free_soft_ware(app_name):
    apps_links = []    

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://www.freesoftwarefiles.com/?s={app_name}&search=', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')


        if soup.find('div', id = 'content').find_all('h2') == None:
            pass

        else:

            a = soup.find('div', id = 'content').find_all('h2')

            for i in a :
                app_name_ = i.find('a')['href']
                apps_links.append(app_name_)

            return apps_links
    except:
        # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
        pass


