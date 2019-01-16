from twitter.update import update_twitter
import tkinter as tk 
r = tk.Tk() 
r.title('Update Tweets') 
button = tk.Button(r, text='Updaate', width=25, command=lambda:update_twitter("nbc")) 
button.pack() 
r.mainloop() 