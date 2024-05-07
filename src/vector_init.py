import json

from json import JSONEncoder, JSONDecoder
from pprint import PrettyPrinter

from anki_vector.robot import Robot as R, AsyncRobot as AR


class Synapse(R):
    def __init__(self,
                 serial,
                 name,
                 config: dict = {},
                 default_logging: bool = True,
                 behavior_activation_timeout: int = 10,
                 cache_animation_lists: bool = True,
                 enable_face_detection: bool = False,
                 estimate_facial_expression: bool = False,
                 enable_audio_feed: bool = False,
                 enable_custom_object_detection: bool = False,
                 enable_nav_map_feed: bool = False,
                 show_viewer: bool = False,
                 show_3d_viewer: bool = False,
                 ):
            super().__init__(serial=serial)
            self.serial = serial
            self.name = name
            self.config = config
            self.config = {}
            self.default_logging = default_logging
            self.behavior_activation_timeout = behavior_activation_timeout
            self.cache_animation_lists = cache_animation_lists
            self.enable_face_detection = enable_face_detection
            self.estimate_facial_expression = estimate_facial_expression
            self.enable_audio_feed = enable_audio_feed
            self.enable_custom_object_detection = enable_custom_object_detection
            self.enable_nav_map_feed = enable_nav_map_feed
            self.show_viewer = show_viewer
            self.show_3d_viewer = show_3d_viewer
            
            self.robot_data: dict = {}
            print(f"Current bot: {self.getcurrentbot()}")
            print(f"Settings JSON: \n {self.robot_data}")
        
    def getcurrentbot(self):
        def __init__(self):
            self.currentbot = Synapse.loadbot
            return self.currentbot

    def json_controller(self):
        def __init__(self):
            super().__init__()
            self.robot_settings = {}
            return self.robot_settings
        
    def loadbot(self, serial):
        def __init__(self, serial):
            self.serial = serial
        self.serial = serial
        try:
            with open("robots.json", "r") as f:
                self.robot_settings = json.load(f)
        except FileNotFoundError:
            print("No robots.json found. Creating file.")
            # create a new JSON file with the layout already programmed for an example. 
            example_robot = {"bots": [
                {"serial": '00000', 
                "name": 'Example Bot',
                "config": {},
                "default_logging": True,
                "behavior_activation_timeout": 10,
                "cache_animation_lists": True,
                "enable_face_detection": False,
                "estimate_facial_expression": False,
                "enable_audio_feed": False,
                "enable_custom_object_detection": False,
                "enable_nav_map_feed": False
                }
            ]}
            
            with open("robots.json", "w") as f:
                json.dump(example_robot, f)
            print("Created new robots.json file.")
            return
            
        except Exception as e:
                print(f"Error opening robots.json: {str(e)}")

        for bot in self.robot_settings["bots"]:
            if bot["serial"] == self.serial:
                self.robot_data = {
                    "serial": bot["serial"],
                    "name": bot["name"],
                    "ip": bot["ip"],
                    "config": bot["config"],
                    "default_logging": bot["default_logging"],
                    "behavior_activation_timeout": bot["behavior_activation_timeout"],
                    "cache_animation_lists": bot["cache_animation_lists"],
                    "enable_face_detection": bot["enable_face_detection"],
                    "estimate_facial_expression": bot["estimate_facial_expression"],
                    "enable_audio_feed": bot["enable_audio_feed"],
                    "enable_custom_object_detection": bot["enable_custom_object_detection"],
                    "enable_nav_map_feed": bot["enable_nav_map_feed"],
                    "show_viewer": bot["show_viewer"],
                    "show_3d_viewer": bot["show_3d_viewer"],
                    }
            else:
                print(f"Check robots.json for formatting issues.")
                pass
            return 

    def addbot(self,serial):
        def __init__(new_serial):
            serial = new_serial
            global current_robot_serial
            current_robot_serial   = serial
        try:
            Synapse.__init__(self, serial, self.name)
        except Exception as e:
            print(f"Error: {e}")

    def changebot(self, serial):
        def __init__(new_serial):
            serial = new_serial
            global current_robot_serial
            current_robot_serial  = serial
        try:
            Synapse.__init__(self, serial, self.name)
        except Exception as e:
            print(f"Error: {e}")
        pass

if __name__ == "__main__":
    botdata = Synapse.loadbot
    print(botdata)