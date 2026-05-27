import os
import time

class Tools:
    
    @staticmethod
    def Clear_console():
        os.system('cls')
    
    @staticmethod
    def Pause(seconds):
        time.sleep(seconds)