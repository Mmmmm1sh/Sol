
from highrise import BaseBot, Position
from highrise.models import SessionMetadata, User
from highrise import __main__
from webserver import keep_alive

keep_alive()

from asyncio import run as arun
import random

class Bot(BaseBot):
    greetings = [ "❤️🥰شو هطله الحلوه",
                 "❤️🥰توها نورت ي هلا وسهلا",

                 
        # ... (ترحيبات أخرى هنا)
    ]
    
    dances = [ "emote-tired", "emoji-thumbsup", "emoji-angry", "dance-macarena",
            "emote-hello","dance-weird", "emote-superpose", "idle-lookup", "idle-hero", "emote-wings",
            "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes", "emote-theatrical",
            "emote-teleporting", "emote-slap", "emote-ropepull", "emote-think", "emote-hot",
            "dance-shoppingcart", "emote-greedy", "emote-frustrated", "emote-float", "emote-baseball",
            "emote-yes", "idle_singing", "idle-floorsleeping", "idle-enthusiastic", "emote-confused",
            "emoji-celebrate", "emote-no", "emote-swordfight", "emote-BUMMED", "emote-shy", "dance-tiktok2", "emote-model",
            "emote-charging", "emote-snake", "dance-russian", "emote-sad", "emote-lust", "emoji-cursing",
            "emoji-flex", "emoji-gagging", "dance-tiktok8", "dance-blackpink", "dance-pennywise",
            "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
            "emote-maniac", "emote-energyball", "emote-frog", "emote-cute", "dance-tiktok9", "dance-tiktok10",
            "emote-pose7", "emote-pose8","idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5",
            "emote-cutey", "emote-Relaxing", "emote-model", "emote-cursty", "emote-Rest", "emote-zero gavity" , "emote-LEVITATE" , "emote-FAINT" , "idle-Attentive" , "emote-NAUGHTY" , "dance-PROPOSING", "dance-FALL" ,"idle-Rest" , "emote-Confusion","dance-SAY SO DANCE"
        # ... (أنواع الرقصات هنا)
    ]

    message_count = {}

    def check_level(self, user_id):
        level = self.message_count.get(user_id, 0) // 10
        return level

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("hey2004")
        self.highrise.tg.create_task(self.highrise.teleport(
            session_metadata.user_id, Position(19. , 0, 11.19, "FrontRight")))

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")
    
    async def on_user_join(self, user: User) -> None:
        greeting = random.choice(self.greetings)
        await self.highrise.chat(f"{greeting}، {user.username}!")
        
        # تشغيل رقصة عند دخول المستخدم
        try:
            emote_id = random.choice(self.dances)
            await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
            print(f"Error: {e}")

    async def on_chat(self, user: User, message: str) -> None:
        if user.id not in self.message_count:
            self.message_count[user.id] = 0
        # ... (باقي الأوامر هنا)
        elif "1" in message:
            try:
                emote_id = random.choice(self.dances)
                await self.highrise.send_emote(emote_id, user.id)
            except Exception as e:
                print(f"Error: {e}")
              
        
    
        if "طيرني" in message:
            try:
                await self.highrise.send_emote('emote-float', user.id)
            except Exception as e:
                print(f"Error: {e}")          
        elif "طلعني" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(1, 7,1))
            except Exception as e:
                print(f"Error: {e}")
        
        elif "نزلني" in message:
            try:
                await self.highrise.teleport(f"{user.id}", Position(1, 0,1))
            except Exception as e:
                print(f"Error: {e}")
        
        elif "طولي" in message:
            try:
                height_cm = random.randint(110, 199)
                await self.highrise.chat(f"{user.username} طولك {height_cm} سنتيمتر!")
            except Exception as e:
                print(f"Error: {e}")
        elif "وزني" in message:
            try:
                weight_kg = random.randint(35, 150)
                await self.highrise.chat(f"{user.username} وزنك {weight_kg} كيلوجرام!")
            except Exception as e:
                print(f"Error: {e}") 


  
    async def on_channel(self, sender_id: str, message: str, tags: set[str]) -> None:
        pass
    
    
    async def run(self, room_id, token) -> None:
        while True:
            try:
                await __main__.main(self, room_id, token)
            except Exception as e:
                print(f"Error: {e}")
                continue

keep_alive()
if __name__ == "__main__":
    room_id = "66aa54f73d7044f1ecb94d4a"
    token = "4ff6166a9684df47ac283559777a2b298d9cabddc603d6368c949d0a77228bfb"
    arun(Bot().run(room_id, token))
