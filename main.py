from rcon.source import rcon
import asyncio

class Match():
    """Если ипользовать наследование от класса Client - методы не работают. 
    Отдельные методы для каждой команды делать не стал - подумал, что громоздко."""

    MAPS = { # В бд?
        "Anubis": "de_anubis", 
        "Inferno": "de_inferno",
        "Overpass": "de_overpass",
        "Mirage": "de_mirage",
        "Ancient": "de_ancient", 
        "Nuke": "de_nuke", 
        "Vertigo": "de_vertigo", 
        "ShortDust": 'de_shortdust',
        "ShortNuke": "de_shortnuke"
    }

    def __init__(self, host:str, port:int, passwd:str):
        self.status = True
        self.host = host
        self.port = port
        self.passwd = passwd
          
    async def command(self, command):
        """ Execute any command."""
        try:
            res = await rcon( 
                command=command, 
                host=self.host, 
                port=self.port, 
                passwd=self.passwd
                )
        except OSError:
            print("Не удалось подключиться к серверу!")
            raise RuntimeError

        if "Unknown command" in res: # Данная ситуация не вызывает ошибки, поэтому так.
            raise KeyError 
        print(res)# tests

    async def change_map(self, map_name):
        map_code = None
        try:
            map_code = Match.MAPS[map_name]
        except KeyError:
            print("Такой карты нет!") # тесты
            raise KeyError
        try:
            res = await rcon( 
                command=f"map {map_code}", 
                host=self.host, 
                port=self.port, 
                passwd=self.passwd
                )
        except OSError:
            print("Не удалось подключиться к серверу!")
            raise RuntimeError
            
        print(res)
            

"""
Команды:
exit
host_map
game_type 0; game_mode 2;
restart
bot_add ct easy
status
"""
#serv1 = Match(host="89.108.70.130", port=27015, passwd="changeme") Мой личный сервак
serv1 = Match(host="91.238.230.110", port=27015, passwd="dharma7452210") # Сервак Артура

async def main():
    task1 = asyncio.create_task(serv1.command('status'))
    await task1
    
asyncio.run(main())


# Сервер Артура steam://connect/91.238.230.110 