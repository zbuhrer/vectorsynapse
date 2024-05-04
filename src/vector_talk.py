import anki_vector as av

ANKI_ROBOT_SERIAL = '00702f96'

async def talk(text: str = "") -> None: 
    with av.Robot(ANKI_ROBOT_SERIAL) as robot:
        print(f"Say '{text}'...")
        robot.behavior.say_text(text)