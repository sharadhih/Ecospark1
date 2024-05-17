import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")

def login_window():
    
    def login_event():
        if entry_1.get()=="ABC" and entry_2.get()=="123": #This is just a simple demo verification,                                            
            print("Password matched!")      
            root_login.destroy() #Destroy the login window after the verification
            new_window() #Make the new_window
        else: #If password doesn't match
            entry_1.configure(text_color="red")
            entry_2.configure(text_color="red")
            print("Wrong password/username!")
            
    #Define the login page window          
    root_login = customtkinter.CTk() 
    root_login.geometry(f"{500}x{500}")
    root_login.title("LOGIN PAGE")

    #Add some widgets for login page
    frame = customtkinter.CTkFrame(master=root_login,width=450, height=450, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_1 = customtkinter.CTkLabel(master=frame, width=400, height=60, corner_radius=10,
                                     fg_color=("gray70", "gray35"), text="Please Login! \nHint: Username=ABC, Pass=123")
    label_1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    entry_1 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, placeholder_text="Username")
    entry_1.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

    entry_2 = customtkinter.CTkEntry(master=frame, corner_radius=20, width=400, show="*", placeholder_text="Password")
    entry_2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button_login = customtkinter.CTkButton(master=frame, text="LOGIN", corner_radius=6, command=login_event, width=400)
    button_login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    root_login.mainloop()

def new_window():
    
    #Define the new window
    root_new = customtkinter.CTk()
    root_new.geometry(f"{500}x{500}")
    root_new.title("New Window")
    
    #Add your widgets for new_window...
    frame_new = customtkinter.CTkFrame(master=root_new,width=450, height=450, corner_radius=10)
    frame_new.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_new = customtkinter.CTkLabel(master=frame_new, width=200, height=60, corner_radius=10,
                                       fg_color=("gray70", "gray35"), text="You have successfully logged-in")
    label_new.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    
    root_new.mainloop()
    
login_window()
