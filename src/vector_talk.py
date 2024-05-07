ANKI_ROBOT_SERIAL = '00702f96'

async def talk(text: str = "") -> None: 
    import anki_vector as av
    with av.Robot() as robot:
        print(f"Say '{text}'...")
        robot.behavior.say_text(text)