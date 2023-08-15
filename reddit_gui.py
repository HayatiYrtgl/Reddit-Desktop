import os.path
from shutil import rmtree
from tkinter import messagebox as message
from tkinter import Menu
from tkinter.filedialog import askopenfilename as fd
import customtkinter
from reddit_prawer_func_class import PrawerRedditSearcher
from customtkinter import CTk, CTkImage, CTkButton, CTkFont, CTkFrame, CTkEntry, CTkLabel, CTkTextbox, \
    CTkOptionMenu, CTkInputDialog
import json
from PIL import Image
from art import text2art
import webbrowser

# user login operation later

client_id = "GaWxOhfSAMviytpvby4CTw"
scret_key = "5LpMMTujuCXgoXLDNVtKjzNIZevRlA"
user_name = "hytby"
password = "Hayati71."
user_agent = "deneme"

class RedditGui(CTk):
    # override
    def __init__(self):
        super().__init__()

        # empty value to use for login operations

        self.reddit_login = None

        # to post define variables

        self.img_path = ""

        self.gif_path = ""

        self.video_path = ""

        # main cons

        self.geometry("900x500+380+190")

        self.title("Reddit User")

        self.resizable(True, False)

        customtkinter.set_default_color_theme("green")

        customtkinter.set_appearance_mode("dark")
        """----------------------------------------------------------------------------------------------------------"""
        """LOGIN FRAME FEATURES """
        """----------------------------------------------------------------------------------------------------------"""
        # frame button images
        comment_image = CTkImage(dark_image=Image.open("media/comment.png"))
        search_image = CTkImage(dark_image=Image.open("media/search.png"))
        post_image = CTkImage(dark_image=Image.open("media/post.png"))
        # frame navbar items to pack after
        # everytime it has to be opened (navbar frame)
        self.navbar_frame = CTkFrame(master=self, fg_color="gray75")

        # login main frame

        self.main_frame = CTkFrame(master=self, fg_color="chocolate4")

        # controlling json file to login if it exists no frame, else frame will be

        if os.path.exists("login_configurations/load_data.json"):
            # menu section

            menubar = Menu(self)

            menu_elemt = Menu(menubar)

            # main commands of menu items

            menubar.add_command(label="Log Out", command=self.log_out_func)

            menubar.add_command(label="HELP", command=self.help_menu)

            self.configure(menu=menubar)

            # read the json data func

            self.login_function_if_load_data_exists()

            # if logged in see the navbar

            self.navbar_frame.pack(side=customtkinter.LEFT, fill="y", padx=15, pady=5)

            # pack and label info if logged

            self.main_frame.pack(side=customtkinter.LEFT, fill="both", expand=True, padx=5, pady=5,)

            # after logged

            beauty_label = CTkLabel(master=self.main_frame, text_color="black",
                                    text="CODE-DEM©",
                                    font=CTkFont("Rosewood Std Regular", 51, weight="bold"),
                                    compound="top")

            beauty_label.pack(pady=20)

            image = CTkImage(dark_image=Image.open("media/login_page_reddit.png"), size=(200, 200))

            self.logged_label = CTkLabel(master=self.main_frame, text="%s LOGGED\nWELCOME TO REDDIT!!" % user_name,
                                         font=CTkFont("Times New Roman", 35, weight="bold"), text_color="black",
                                         image=image, compound="bottom")

            self.logged_label.pack(pady=50)

        # else define function to login and set gui settings

        else:

            # disable the navbar items

            self.navbar_frame.pack_forget()

            self.main_frame.pack(side=customtkinter.LEFT, fill="both", expand=True, padx=5, pady=5)

            # and another frame for beauty

            self.login_frame = CTkFrame(master=self.main_frame, fg_color="chocolate3")

            self.login_frame.pack(padx=50, pady=50, expand=True, fill="both")

            # labels for info

            self.title_label = CTkLabel(master=self.login_frame, text_color="gray34",
                                        text="-----REDDITTOR APP LOGIN PAGE------",
                                        font=CTkFont("Mesquite Std", 55, weight="bold"),
                                        compound="top")

            self.title_label.pack(pady=10)

            # image and beautiful code dem text

            image = CTkImage(dark_image=Image.open("media/login_page_reddit.png"), size=(128, 128))

            image_label = CTkLabel(text="", master=self.login_frame, image=image)

            image_label.place(x=70, y=110)

            beauty_label = CTkLabel(master=self.login_frame, text_color="black",
                                    text="CODE-DEM©",
                                    font=CTkFont("Rosewood Std Regular", 51, weight="bold"),
                                    compound="top")

            beauty_label.place(x=520, y=150)

            # login entries
            # 1
            self.client_id_entry = CTkEntry(master=self.login_frame, placeholder_text="CLIENT ID", width=180,
                                            show="*")

            self.client_id_entry.pack(pady=8, padx=15)

            # 2
            self.scret_key_entry = CTkEntry(master=self.login_frame, placeholder_text="SECRET KEY", width=180,
                                            show="*")

            self.scret_key_entry.pack(pady=8, padx=15)

            # 3
            self.username_entry = CTkEntry(master=self.login_frame, placeholder_text="USERNAME", width=180)

            self.username_entry.pack(pady=8, padx=15)

            # 4
            self.password_entry = CTkEntry(master=self.login_frame, placeholder_text="PASSWORD", width=180,
                                           show="*")

            self.password_entry.pack(pady=8, padx=15)

            # 5

            self.appname_entry = CTkEntry(master=self.login_frame, placeholder_text="APP NAME", width=180)

            self.appname_entry.pack(pady=8, padx=15)

            # login button

            self.login_button = CTkButton(text="LOGIN", master=self.login_frame, fg_color="blue", text_color="snow",
                                          width=180, hover_color="blue4",
                                          command=self.login_function_if_load_data_not_exists)

            self.login_button.pack(pady=10)

        """----------------------------------------------------------------------------------------------------------"""
        """MAIN FRAME FEATURES """
        """----------------------------------------------------------------------------------------------------------"""

        # OTHER frames

        self.search_frame = CTkFrame(master=self, fg_color="gray75")

        self.comment_frame = CTkFrame(master=self, fg_color="gray75")

        self.post_frame = CTkFrame(master=self, fg_color="gray75")

        # frame navbar items
        # appereance mode
        self.appereance_mode_button = CTkOptionMenu(master=self.navbar_frame, values=["Dark", "System"],
                                                    command=self.appearance_mode_function)
        self.appereance_mode_button.pack(side=customtkinter.BOTTOM, fill="x", padx=5, pady=10)
        # search button
        self.search_button = CTkButton(text="Search", fg_color="transparent", master=self.navbar_frame, corner_radius=5,
                                       bg_color="transparent", text_color="black", hover_color="gray35",
                                       command=self.search_section_command, image=search_image, compound="left")
        self.search_button.pack(padx=5, pady=25)

        # comment button

        self.comment_button = CTkButton(text="Comment", fg_color="transparent", master=self.navbar_frame,
                                        corner_radius=5,
                                        bg_color="transparent", text_color="black", hover_color="gray35",
                                        command=self.comment_section_command, image=comment_image, compound="left")
        self.comment_button.pack(padx=5, pady=25)

        # post button

        self.post = CTkButton(text="Post", fg_color="transparent", master=self.navbar_frame, corner_radius=5,
                              bg_color="transparent", text_color="black", hover_color="gray35",
                              command=self.post_section_command, image=post_image, compound="left")
        self.post.pack(padx=5, pady=25)

        """----------------------------------------------------------------------------------------------------------"""
        """SEARCH FRAME FEATURES"""
        """----------------------------------------------------------------------------------------------------------"""
        # text area to insert texts

        self.text_area_search = CTkTextbox(master=self.search_frame, height=300, fg_color="gray1", text_color="snow")
        self.text_area_search.configure(font=("Courier", 13))
        self.text_area_search.pack(fill="both", padx=10, pady=10)

        # art include

        self.text_area_search.insert(customtkinter.END, text2art("-CODE-DEM-"))

        # topic , category ,number_of_subreddit, text_area_object

        # topic

        self.topic = CTkEntry(master=self.search_frame, width=200, height=30, corner_radius=10, border_width=6,
                              placeholder_text="Search Reddit TOPİC")
        self.topic.pack(side=customtkinter.TOP, padx=5, pady=10, fill="x")

        # category

        self.category = CTkOptionMenu(master=self.search_frame, values=["Hot", "New", "Controversial", "Top"],
                                      fg_color="brown4", button_color="brown3", button_hover_color="brown2")
        self.category.pack(side=customtkinter.TOP, padx=5, pady=10, fill="x")

        # redit num

        self.number_of_reddit = CTkOptionMenu(master=self.search_frame,
                                              values=["Number Of reddit", "10", "20", "30", "40",
                                                      "50", "60", "70",
                                                      "80", "90", "100"], )
        self.number_of_reddit.pack(side=customtkinter.LEFT, padx=5, pady=10, fill="x")

        # search button

        self.search_reddit_button = CTkButton(master=self.search_frame, text="Search REDDİT", text_color="snow",
                                              fg_color="magenta", command=self.command_search_reddits, width=500,
                                              hover_color="magenta3")

        self.search_reddit_button.pack(side=customtkinter.RIGHT, fill="x", padx=5)

        """----------------------------------------------------------------------------------------------------------"""
        """COMMENT FRAME FEATURES """
        """----------------------------------------------------------------------------------------------------------"""

        # text area to get comments from ids

        self.text_area_comments = CTkTextbox(master=self.comment_frame, height=300, fg_color="gray1", text_color="snow")
        self.text_area_comments.pack(fill="both", padx=10, pady=10)

        # comment id searcher

        self.reddit_id_entry = CTkEntry(master=self.comment_frame, width=200, height=30, corner_radius=10,
                                        border_width=6,
                                        placeholder_text="Search Reddit Comment by Reddit id")
        self.reddit_id_entry.pack(side=customtkinter.TOP, padx=5, pady=10, fill="x")

        # comment numbers

        self.number_of_comment = CTkOptionMenu(master=self.comment_frame,
                                               values=["Number Of Comments", "10", "20", "30", "40",
                                                       "50", "60", "70",
                                                       "80", "90", "100"], )
        self.number_of_comment.pack(side=customtkinter.LEFT, padx=5, pady=10, fill="x")

        # search button

        self.comment_find_button = CTkButton(master=self.comment_frame, text="Search Comments", text_color="snow",
                                             fg_color="magenta", width=500,
                                             hover_color="magenta3", command=self.command_find_comments)

        self.comment_find_button.pack(side=customtkinter.RIGHT, fill="x", padx=5)

        # comment id to upvote downvote by own buttons with images

        img_upvote = CTkImage(dark_image=Image.open("media/upvote.png"))
        img_downvote = CTkImage(dark_image=Image.open("media/downvote.png"))

        self.upvote_button = CTkButton(master=self.comment_frame, image=img_upvote, text="", fg_color="blue4",
                                       corner_radius=50, hover_color="blue2", width=50, command=self.upvote_comment)
        self.upvote_button.place(x=5, y=460)

        self.downvote_button = CTkButton(master=self.comment_frame, image=img_downvote, text="", fg_color="red2",
                                         corner_radius=50, hover_color="red", width=50, command=self.downvote_comment)
        self.downvote_button.place(x=105, y=460)

        # downvote or upvote by id entry

        self.d_u_entry = CTkEntry(master=self.comment_frame, width=150, border_width=1,
                                  fg_color="DarkSeaGreen", placeholder_text="id to upvote or downvote",
                                  placeholder_text_color="snow")
        self.d_u_entry.place(x=205, y=460)

        # save post image and button

        save_img = CTkImage(dark_image=Image.open("media/save.png"))

        self.save_button = CTkButton(master=self.comment_frame, text_color="black", fg_color="snow",
                                     image=save_img, compound="left", text="SAVE POST OR COMMENT", corner_radius=15,
                                     hover_color="gray75", command=self.save_post_or_comment)

        self.save_button.place(x=370, y=460)

        # reply comments

        self.reply_comment_button = CTkButton(master=self.comment_frame, text="Reply Comment", fg_color="tan2",
                                              hover_color="tan1", width=100, command=self.reply_comment_func)
        self.reply_comment_button.place(x=600, y=460)

        """----------------------------------------------------------------------------------------------------------"""
        """POST FRAME FEATURES """
        """----------------------------------------------------------------------------------------------------------"""
        self.text_area_post = CTkTextbox(master=self.post_frame, height=300, fg_color="gray1", text_color="snow")
        self.text_area_post.pack(fill="both", padx=10, pady=10)
        self.text_area_post.insert(customtkinter.END, "ENTER THE POST CONTENT")

        # image open

        self.image_open_fd = CTkButton(master=self.post_frame, text="ADD IMAGE", text_color="black",
                                       fg_color="burlywood4", border_color="burlywood4",
                                       hover_color="burlywood2", corner_radius=10, command=self.select_image)
        self.image_open_fd.pack(anchor="w", padx=5, pady=10)

        # video

        self.video_open_fd = CTkButton(master=self.post_frame, text="ADD VIDEO", text_color="black",
                                       fg_color="burlywood4", border_color="burlywood4",
                                       hover_color="burlywood2", corner_radius=10, command=self.select_video)
        self.video_open_fd.pack(anchor="w", padx=5, pady=10)

        # add gif

        self.gif_open_fd = CTkButton(master=self.post_frame, text="ADD GIF", text_color="black",
                                     fg_color="burlywood4", border_color="burlywood4",
                                     hover_color="burlywood2", corner_radius=10, command=self.select_gif)
        self.gif_open_fd.pack(anchor="w", padx=5, pady=10)

        # labels for awarness of ımages

        # icons for labels

        self.approved = CTkImage(dark_image=Image.open("media/approve.png"))
        self.disapporved = CTkImage(dark_image=Image.open("media/disapprove.png"))

        # labels section

        self.label1 = CTkLabel(master=self.post_frame, text="Image Not Selected", font=CTkFont("Times New Roman", 12,
                                                                                               weight="bold"),
                               text_color="black", image=self.disapporved, compound="left")
        self.label1.place(x=165, y=327)

        self.label2 = CTkLabel(master=self.post_frame, text="Video Not Selected", font=CTkFont("Times New Roman", 12,
                                                                                               weight="bold"),
                               text_color="black", image=self.disapporved, compound="left")
        self.label2.place(x=165, y=377)

        self.label3 = CTkLabel(master=self.post_frame, text="GIF Not Selected", font=CTkFont("Times New Roman", 12,
                                                                                             weight="bold"),
                               text_color="black", image=self.disapporved, compound="left")
        self.label3.place(x=165, y=427)

        # send button

        self.post_send_button = CTkOptionMenu(master=self.post_frame, fg_color="brown3", corner_radius=12,
                                              values=["Send post with image", "Send post with video",
                                                      "Send post with gif", "Send post normally"],
                                              command=self.send_post, button_color="brown1", button_hover_color="brown2")
        self.post_send_button.pack(anchor="w", padx=5, fill="x")

    """LOGIN OPERATIONS"""

    # login function

    def login_function_if_load_data_not_exists(self):

        # get gui info

        load_data_dictionary = {"secret_key_login": self.scret_key_entry.get(),

                                "client_id_login": self.client_id_entry.get(),

                                "username_login": self.username_entry.get(),

                                "password_login": self.password_entry.get(),

                                "app_name_login": self.appname_entry.get()
                                }

        # control with if

        if self.client_id_entry.get() == "" or self.client_id_entry.get() == " ":

            message.showerror("ERROR", "ENTER FULL AREA")

        elif self.scret_key_entry.get() == "" or self.scret_key_entry.get() == " ":

            message.showerror("ERROR", "ENTER FULL AREA")

        elif self.username_entry.get() == "" or self.username_entry.get() == " ":

            message.showerror("ERROR", "ENTER FULL AREA")

        elif self.password_entry.get() == "" or self.password_entry.get() == " ":

            message.showerror("ERROR", "ENTER FULL AREA")

        elif self.appname_entry.get() == "" or self.appname_entry.get() == " ":

            message.showerror("ERROR", "ENTER FULL AREA")

        else:

            # write into json file

            with open("login_configurations/load_data.json", "w") as file:

                # write file

                json.dump(load_data_dictionary, file, ensure_ascii=False, indent=4)

            # login
            try:
                self.reddit_login = PrawerRedditSearcher(username=load_data_dictionary["username_login"],
                                                         client_id=load_data_dictionary["client_id_login"],
                                                         password=load_data_dictionary["password_login"],
                                                         secretkey=load_data_dictionary["secret_key_login"],
                                                         app_name=load_data_dictionary["app_name_login"])


                # give message

                message.showinfo("INFO", "SAVED YOUR INFORMATION, LOGGING IN")

                # if logged forget frame and dive into search section

                self.login_frame.pack_forget()

                self.main_frame.pack_forget()

                self.navbar_frame.pack(side=customtkinter.LEFT, fill="y", padx=15, pady=5)

                self.main_frame.pack(side=customtkinter.LEFT, fill="both", expand=True, padx=5, pady=5)

                # menu section

                menubar = Menu(self)

                menu_elemt = Menu(menubar, tearoff=0)

                # main functions of menu items

                menubar.add_command(label="Log Out", command=self.log_out_func)

                menubar.add_command(label="HELP", command=self.help_menu)

                self.configure(menu=menubar)

            except:
                message.showerror("ERROR", "YOUR INFORMATION IS NOT TRUE CHECK IT OUT")

    # read json if it exists and log in

    def login_function_if_load_data_exists(self):

        with open("login_configurations/load_data.json", "r") as file:

            load_data_dictionary = json.load(file)

        # login

        self.reddit_login = PrawerRedditSearcher(username=load_data_dictionary["username_login"],
                                                 client_id=load_data_dictionary["client_id_login"],
                                                 password=load_data_dictionary["password_login"],
                                                 secretkey=load_data_dictionary["secret_key_login"],
                                                 app_name=load_data_dictionary["app_name_login"])

        # give message

        message.showinfo("INFO", "WELCOME BACK!")

    """posting with reddits"""

    """POST SENDER SECTİON"""
    # selecting post arguments

    def select_image(self):

        # select image command

        file_path = fd(filetypes=(("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg")), initialdir="/",
                       title="Select img file to post")

        # control with os

        if os.path.exists(file_path):

            self.label1.configure(text=file_path, image=self.approved)

            self.img_path = file_path

    def select_gif(self):
        file_path = fd(filetypes=(("GIF", "*.gif"),), initialdir="/",
                       title="Select gif file to post")

        # control with os

        if os.path.exists(file_path):

            self.label3.configure(text=file_path, image=self.approved)

            self.gif_path = file_path

    def select_video(self):
        file_path = fd(filetypes=(("VID", "*.mp4"), ("VID", "*.av")), initialdir="/",
                       title="Select video file to post")

        # control with os

        if os.path.exists(file_path):

            self.label2.configure(text=file_path, image=self.approved)

            self.video_path = file_path

    # the main post function

    def send_post(self, post_method):

        # title input

        title = CTkInputDialog(text="ENTER THE TITLE OF SUBREDDIT", title="SET TITLE")

        title = title.get_input()

        # subreddit class

        group_name = CTkInputDialog(text="ENTER THE GROUP NAME (r/testing is default value)", title="SET GROUP")

        group_name = group_name.get_input()

        # get content of reddit

        content = self.text_area_post.get("0.0", customtkinter.END)

        # according to selected method, do func

        # option 1

        if post_method == "Send post with image":
            # with try except cath if user select more than one options
            try:

                img_path = self.img_path

                self.reddit_login.send_post_image(img_path=img_path, title=title, self_text=content, group_name=group_name)

                message.showinfo("DONE", "POSTED!!")

            except:

                message.showerror("ERROR", "AN EXCEPTİON OCCURED!")

        # option 2

        elif post_method == "Send post with video":
            # with try except cath if user select more than one options
            try:

                video_path = self.video_path

                self.reddit_login.send_post_image(img_path=video_path, title=title, self_text=content, group_name=group_name)

                message.showinfo("DONE", "POSTED!!")

            except:

                message.showerror("ERROR", "AN EXCEPTİON OCCURED!")

        # option 3

        elif post_method == "Send post with gif":
            # with try except cath if user select more than one options
            try:
                gif_path = self.gif_path

                self.reddit_login.send_post_image(img_path=gif_path, title=title, self_text=content, group_name=group_name)

                message.showinfo("DONE", "POSTED!!")

            except:

                message.showerror("ERROR", "AN EXCEPTİON OCCURED!")

        # option 4

        else:
            # with try except cath if user select more than one options
            try:
                self.reddit_login.send_post_normal(title=title, text=content, group_name=group_name)

                message.showinfo("DONE", "POSTED!!")

            except:

                message.showerror("ERROR", "AN EXCEPTİON OCCURED!")

    """SEARCHİNG BY REDDİTS"""

    # research reddits by id
    def command_search_reddits(self):
        # if fie is exists delete it

        if os.path.exists("for_comments.txt"):
            os.remove("for_comments.txt")

        # clear text area
        self.text_area_search.delete("0.0", customtkinter.END)
        # get gui value and search it

        topic = self.topic.get()

        category = self.category.get()

        num_red = int(self.number_of_reddit.get())

        # create object from class and use its' function

        self.reddit_login.subreddit_search(topic, category, num_red, self.text_area_search)

    """COMMENTS FUNCTİONSS SECTİON"""

    # find comments by ids

    def command_find_comments(self):

        # get values

        try:

            # reddit post id

            id = self.reddit_id_entry.get()

            # comments_numbber

            comments_number = int(self.number_of_comment.get())

            # give text are to func

            self.reddit_login.comment_search(reddit_post_id=id, comments_number=comments_number,
                                        text_area_object=self.text_area_comments)
        except ValueError:
            message.showerror("ERROR", "PLEASE SET COMMENT VALUE")

    # upvote and downvote

    def upvote_comment(self):

        self.reddit_login.upvote_reddit_comment(self.d_u_entry.get())

        message.showinfo("LİKED", "COMMENT LIKED")

    def downvote_comment(self):

        self.reddit_login.downvote_reddit_comment(self.d_u_entry.get())

        message.showinfo("LİKED", "COMMENT DISLIKED")

    def reply_comment_func(self):
        # get id

        comment_id = CTkInputDialog(text="PLEASE ENTER THE COMMENT ID", title="COMMENT ID")

        comment_id = comment_id.get_input()

        # get reply

        response = CTkInputDialog(text="PLEASE ENTER THE REPLY", title="COMMENT REPLY")

        response = response.get_input()

        # load

        self.reddit_login.reply_comment(comment_id=comment_id, reply=response)

        message.showinfo("DONE", "REPLİED THE COMMENT")

    # save post or comment
    def save_post_or_comment(self):

        id_question = CTkInputDialog(title="Post id or Comment id", text="ENTER THE POST İD OR COMMENT İD BELOW")

        get_id = id_question.get_input()
        # with try except we will understand what id is gonna be
        # you can not prevent with one try-catch block to type error because in exception there is a function,
        # so you have to use second try-catch block to prevent bypassing input area
        # if get id is empty it will not work
        if get_id != "" or " ":

            # try to save as post
            try:
                # in try to catch type error
                try:
                    self.reddit_login.save_post(get_id)

                    message.showinfo("SAVED", "SAVED İD AS POST")

                except TypeError:
                    message.showwarning("WARNING", "YOU SHOULDN'T BYPASS ID AREA\nPLEASE TRY AGAIN")

            except:
                # in try to catch type error
                try:
                    self.reddit_login.save_comment(get_id)

                    message.showinfo("SAVED", "SAVED İD AS COMMENT")

                except TypeError:
                    message.showwarning("WARNING", "YOU SHOULDN'T BYPASS ID AREA\nPLEASE TRY AGAIN")

        # else give message
        else:
            message.showwarning("WARNING", "YOU SHOULDN'T BYPASS ID AREA\nPLEASE TRY AGAIN")

    """MENU ITEMS COMMANDS"""

    # logout
    @staticmethod
    def log_out_func():

        # ask quit

        ask_quit = message.askyesno("LOGGIN OUT", "ARE YOU SURE TO LOG OUT FROM YOUR ACCOUNT ?")

        if ask_quit:
            # clear user informations
            rmtree("login_configurations", ignore_errors=True)

            message.showinfo("INFO", "LOGGED OUT")

            exit()

    # help
    @staticmethod
    def help_menu():

        webbrowser.open("https://github.com/HayatiYrtgl")

    """Appearence mode funciton"""

    def appearance_mode_function(self, mode):

        customtkinter.set_appearance_mode(mode)

    """CONSTRUCTOR OF FRAMES DO NOT TOUCH IF ISN'T NECCESARY"""

    # frame generator to tab slide

    def frame_generator_by_name(self, frame_name):
        # erase login frame

        try:

            self.login_frame.pack_forget()

        except AttributeError:

            pass

        # erase main frame

        self.main_frame.pack_forget()

        # create frame by name

        self.search_button.configure(fg_color=("gray75", "gray25") if frame_name == "search" else "transparent")

        self.comment_button.configure(fg_color=("gray75", "gray25") if frame_name == "comment" else "transparent")

        self.post.configure(fg_color=("gray75", "gray25") if frame_name == "post" else "transparent")

        # show selected frame else forget pack
        if frame_name == "search":
            self.search_frame.pack(side=customtkinter.LEFT, fill="both", expand=True, padx=5, pady=5)
        else:
            self.search_frame.pack_forget()
        if frame_name == "comment":
            self.comment_frame.pack(side=customtkinter.LEFT, fill="both", expand=True, padx=5, pady=5)
        else:
            self.comment_frame.pack_forget()
        if frame_name == "post":
            self.post_frame.pack(side=customtkinter.LEFT, fill="both", expand=True, padx=5, pady=5)
        else:
            self.post_frame.pack_forget()

    # navbar items commands

    def search_section_command(self):
        self.frame_generator_by_name(frame_name="search")

    def comment_section_command(self):
        # when the button  clicked again clear and get again

        self.text_area_comments.delete("0.0", customtkinter.END)

        # create frame

        self.frame_generator_by_name(frame_name="comment")

        # insert reddits txt with try except blocks

        try:
            with open("for_comments.txt", "r", encoding="utf-8") as file:

                self.text_area_comments.insert(customtkinter.END, file.read())

        except FileNotFoundError:

            message.showerror("HATA", "ÖNCE REDDİTTE GEZİNMELİSİNİZ...")

    def post_section_command(self):
        self.frame_generator_by_name(frame_name="post")


if __name__ == "__main__":
    # create folder
    if os.path.exists("login_configurations"):
        pass
    else:
        os.mkdir("login_configurations")
    # run gui
    c = RedditGui()
    c.mainloop()
