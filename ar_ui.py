import customtkinter
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from DetectionAPI import detecte_api

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "spain.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "mini.jpeg")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "mini.jpeg")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "search.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "search.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "sofa.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "sofa.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "recycle.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "recycle.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" EcoSpark", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Eco Scan",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Green Furniture",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="R.R.R",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#012a34")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        #self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        #self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        #self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
        #self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        #self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
        #self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        #self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        #self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.upload_button = customtkinter.CTkButton(self.home_frame, text="Upload Image", command=self.upload_image_and_detect)
        self.upload_button.grid(row=3, column=0, padx=20, pady=20)

        # Placeholder for the uploaded image
        self.image_label = customtkinter.CTkLabel(self.home_frame, text="")
        self.image_label.grid(row=4, column=0, padx=20, pady=20)
        
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def show_dialog(text):
    # Create a Toplevel window (which acts as a dialog box)
        dialog = customtkinter.customtkinterToplevel(app)
        dialog.geometry("300x200")
        dialog.title("Message")

        # Add a label to the dialog box with a message
        label = customtkinter.customtkinterLabel(dialog, text=text)
        label.pack(pady=20)

        # Add an 'OK' button to close the dialog
        ok_button = customtkinter.CTkButton(dialog, text="OK", command=dialog.destroy)
        ok_button.pack(pady=10)
    def upload_image_and_detect(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Get file extension
            ext = os.path.splitext(file_path)[1]
            # Save the uploaded file to the assets directory
            save_path = os.path.join("assets", f"test{ext}")
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(file_path, "rb") as f_src:
                with open(save_path, "wb") as f_dst:
                    f_dst.write(f_src.read())

            # Detecting the bulbs in the image
            num_of_bulbs_detected, status, img = detecte_api(save_path)
            #save_path = os.path.join("assets", "obj.jpg")
            im_path="dummy\\assets\\obj.jpg"
            # if status == "Light Bulb On":
            #     show_dialog("The bulb is on! off it!")
            #     # update

            # Display the image
            self.display_image(im_path)
    

    def display_image(self, image_path):
        #image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        uploaded_image = customtkinter.CTkImage(Image.open(image_path), size=(400, 400))  # Set desired size here
        self.image_label.configure(image=uploaded_image)
        self.image_label.image = uploaded_image  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    app = App()
    app.mainloop()
