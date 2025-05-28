import pywinauto                                                                # bringing an .exe to the foreground
import time
import tkinter as tk                                                            # Tkinter's Tk class
import win32con                                                                 # justify right or left the GUI.
import win32gui                                                                 # bring apps to front foreground
from tkinter import messagebox
from win32gui import GetWindowText, GetForegroundWindow                         # check position of a window

main = tk.Tk()
main.geometry('10x10+5+5')                                                      # Set the geometry of the GUI (LxH+posX+posY)
main.title("Manual Test")                                                       # title might have to be main window, from the last statement; if __name__ == "__main__":

sample_pos_arr = [2,5,10,15,24]
pos_len = len(sample_pos_arr)                                                   # 5 samples

failed_samps_040 = [str(i) for i in sample_pos_arr]
print(f'Sample positions 015: {", " . join(failed_samps_040)} failed.\n')

def console():                                                                  # place python console in foreground and 1/4 screen
    py_title = 'C:\Program Files\Python311\python.exe'                          # the title of the console
    py_app = pywinauto.Application().connect(title=py_title)                    # connect to the app with the title
    py_win = py_app[py_title]                                                   # assign the app to a variable
    py_win.set_focus()                                                          # set the focus to the excel file to the foreground
    print('Python is in the foreground now.')
    time.sleep(1)                                                               # pause to allow to come to foreground

    full_py = win32gui.GetForegroundWindow()                                    # grab the window in the foreground
    py_rect = win32gui.GetWindowRect(full_py)                                   # assign window rectangle coordinates to an array
    a = py_rect[0]                                                              # a=upper left corner positon of the Kinesis window in the X coordinates of the screen
    b = py_rect[1]                                                              # b=upper left corner positon of the Kinesis window in the Y coordinates of the screen
    c = py_rect[2] - a                                                          # c is the length of the kinesis window, should be half the length of the screen 1920/2=960
    d = py_rect[3] - b                                                          # d is the height of the kinesis window, should be the entire height of the screen 1080
    if b != 600:                                                                  # if b is not equal to 0 (Y in the 0 location)
        win32gui.SetWindowPos(full_py, win32con.HWND_TOP, 0, 600, 960, 600, 0)  # set to upper left hand corner (0,600) 1/4 screen (960x600)
        print('Python Console is now 1/4 screen.')                              # X,Y,L,H. X&Y are top left corner position. L&W of the GUI window
        time.sleep(1)
    else:                                                                   
        print('Python is already 1/4 screen.')

def move_kinesis(next_samp_pos):
    samp_pos = int(next_samp_pos)
    print("Sample Position #", samp_pos)
    start_posX = float(132.8)                                                           # starting position of X
    relat_posX = float(20.325)                                                          # increment this distance
    start_posY = float(24.6)                                                            # starting position of Y
    relat_posY = float(29.325)                                                          # increment this distance
    if samp_pos == 1:
        x_startpos = start_posX                                                         # 132.8
        y_startpos = start_posY                                                         # 24.6
    elif samp_pos == 2:
        x_startpos = (start_posX - relat_posX)                                          # 132.8 - 20.235 = 112.565
        y_startpos = start_posY                                                         # 24.6
    elif samp_pos == 3:
        x_startpos = (start_posX - relat_posX - relat_posX)                             # 112.565 - 20.235 = 92.33                  
        y_startpos = start_posY                                                         # 24.6                     
    elif samp_pos == 4:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX)                # 92.33 - 20.235 = 72.095            
        y_startpos = start_posY                                                         # 24.6                     
    elif samp_pos == 5:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX - relat_posX)   # 72.095 - 20.235 = 51.86                
        y_startpos = start_posY                                                         # 24.6        
        
    elif samp_pos == 6:
        x_startpos = start_posX                                                         # 132.8                    
        y_startpos = (start_posY + relat_posY)                                          # 24.6 + 29.325 = 53.925                      
    elif samp_pos == 7:
        x_startpos = (start_posX - relat_posX)                                          # 112.565                      
        y_startpos = (start_posY + relat_posY)                                          # 53.925
    elif samp_pos == 8:
        x_startpos = (start_posX - relat_posX - relat_posX)                             # 92.33                         
        y_startpos = (start_posY + relat_posY)                                          # 53.925                      
    elif samp_pos == 9:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX)                # 72.095                         
        y_startpos = (start_posY + relat_posY)                                          # 53.925                      
    elif samp_pos == 10:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX - relat_posX)   # 51.86                        
        y_startpos = (start_posY + relat_posY)                                          # 53.925                      

    elif samp_pos == 11:
        x_startpos = start_posX                                                         # 132.8                    
        y_startpos = (start_posY + relat_posY + relat_posY)                             # 53.925 + 29.325 = 83.16                        
    elif samp_pos == 12:
        x_startpos = (start_posX - relat_posX)                                          # 112.565                      
        y_startpos = (start_posY + relat_posY + relat_posY)                             # 83.16
    elif samp_pos == 13:
        x_startpos = (start_posX - relat_posX - relat_posX)                             # 92.33                         
        y_startpos = (start_posY + relat_posY + relat_posY)                             # 83.16                       
    elif samp_pos == 14:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX)                # 72.095                         
        y_startpos = (start_posY + relat_posY + relat_posY)                             # 83.16                          
    elif samp_pos == 15:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX - relat_posX)   # 51.86                        
        y_startpos = (start_posY + relat_posY + relat_posY)                             # 83.16       

    elif samp_pos == 16:
        x_startpos = start_posX                                                         # 132.8                    
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY)                # 83.16 + 29.325 = 112.485                      
    elif samp_pos == 17:
        x_startpos = (start_posX - relat_posX)                                          # 112.565                      
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY)                # 112.485          
    elif samp_pos == 18:
        x_startpos = (start_posX - relat_posX - relat_posX)                             # 92.33                         
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY)                # 112.485                      
    elif samp_pos == 19:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX)                # 72.095                         
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY)                # 112.485                        
    elif samp_pos == 20:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX - relat_posX)   # 51.86                        
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY)                # 112.485     

    elif samp_pos == 21:
        x_startpos = start_posX                                                         # 132.8                    
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY + relat_posY)   # 112.485 + 29.325 = 141.81                     
    elif samp_pos == 22:
        x_startpos = (start_posX - relat_posX)                                          # 112.565                      
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY + relat_posY)   # 141.81                    
    elif samp_pos == 23:
        x_startpos = (start_posX - relat_posX - relat_posX)                             # 92.33                         
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY + relat_posY)   # 141.81                      
    elif samp_pos == 24:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX)                # 72.095                       
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY + relat_posY)   # 141.81                         
    else:
        x_startpos = (start_posX - relat_posX - relat_posX - relat_posX - relat_posX)   # 51.86                     
        y_startpos = (start_posY + relat_posY + relat_posY + relat_posY + relat_posY)   # 141.81      

    x_startpos = format(x_startpos, '.3f')                                              # limit to 3 decimal points
    y_startpos = format(y_startpos, '.3f')                                              # limit to 3 decimal points
    print("X Position:   ", x_startpos, "\nY Position:   ", y_startpos)

console()

for s in range(0,pos_len):
    next_samp = sample_pos_arr[s]
    print("Next sample is: ", next_samp)
    print("Position length: ", pos_len)
    print("s: ", s)

    if (s+1) == pos_len:                                                    # if the loop # is equal to than position length, ask the operator to click OK to move to the next sample
        msg_box_endmanual = tk.messagebox.askquestion('End of Manual Test', 'End of test. Click OK to close the console.', icon='info', type='okcancel')
        if msg_box_endmanual == 'ok':
            print("End manual test.")
            exit()   
        else:
            print("Cancel was selected")
            exit()                                                      # Exit out of this class. Go back to Main Window GUI.
    elif s==0:                                                          # On first sample move to start position
        move_kinesis(next_samp)
    else:                                                               # if the loop is less than than position length, ask the operator to click OK to move to the next sample
        move_kinesis(next_samp)
        msg_box_next = tk.messagebox.askquestion('Next Sample', 'Click OK when ready for Kinesis to move to the next sample locaiton.', icon='info', type='okcancel')
        if msg_box_next == 'ok':
            print("Ok was selected, move Kinesis to the next position.")
        else:
            print("Cancel was selected, quit the loop.")
            exit()
main.mainloop()