import pyautogui as pg
import time
print ("program in 5 seconds...")
time.sleep(10)

for i in range(100):
    pg.write("Sorry Mari Chimpanzee (empress)")
    time.sleep(0.5)
    pg.press("Enter")