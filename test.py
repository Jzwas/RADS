import tkinter as tk   

def write_text():
    print("DETONATION STATUS: +")
    exec(open("tk.py").read())
    command=quit
    

    
    

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

text_disp= tk.Button(frame,
                   #exec(open("tk.py").read()),
                   text="DETONATE",
                    fg='green',
                   command=write_text
                   )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="EXIT",
                   fg="red",
                   command=quit)


exit_button.pack(side=tk.RIGHT)

parent.mainloop()

