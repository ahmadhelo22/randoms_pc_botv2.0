import requests
from bs4 import BeautifulSoup

def searsh_resolts_name_free_soft_ware(app_name):
    apps_list = []    

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://filecr.com/search/?q={app_name}&primary=ms-windows', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')

        a = soup.find('section', {'class':'products'}).find_all('div', {'class':'card_info__LY5ob'})

        if a == None:
            pass

        else:
            for i in a :
                a = i.find('a').next_element
                premium = i.find('span')
                if premium == None :
                    apps_list.append(a)

            return apps_list

        # if soup.find('div', id = 'content').find_all('h2') == None:
        #     # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
            
        #     pass


        # else:

        #     a = soup.find('div', id = 'content').find_all('h2')

        #     for i in a :
        #         app_name_ = i.find('a').next_element
        #         apps_list.append(app_name_)

        #     return apps_list
    except Exception as e:
        # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
        print(e)

        pass

# searsh_resolts_name_free_soft_ware('add')

def searsh_resolts_links_free_soft_ware(app_name):
    apps_links = []    

    try:

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(f'https://filecr.com/search/?q={app_name}&primary=ms-windows', headers=headers)
        src = result.content
        soup = BeautifulSoup(src, 'xml')

        
        a = soup.find('section', {'class':'products'}).find_all('div', {'class':'card_info__LY5ob'})

        if a == None:
            pass
        
        else:
            for i in a :
                a = i.find('a')['href']
                premium = i.find('span')
                if premium == None :
                    b = f'https://filecr.com/{a}'
                    apps_links.append(b)

            return apps_links

        # if soup.find('div', id = 'content').find_all('h2') == None:
        #     pass

        # else:

        #     a = soup.find('div', id = 'content').find_all('h2')

        #     for i in a :
        #         app_name_ = i.find('a')['href']
        #         apps_links.append(app_name_)

        #     return apps_links
    except:
        # bot.send_message ( user_id, "البرنامج غير موجود تاكد من الاسم او اعد المحاوله لاحقا" )
        pass


