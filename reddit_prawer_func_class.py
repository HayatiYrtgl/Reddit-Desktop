import os.path
from art import text2art
from praw import Reddit
from praw.models import InlineImage, InlineGif, InlineVideo
from tkinter import messagebox, END

# creating class for reddit search


class PrawerRedditSearcher:
    # create constructor
    def __init__(self, username, password, secretkey, client_id, app_name):

        # logging in account

        self.reddit = Reddit(client_id=client_id, client_secret=secretkey, user_agent=app_name, username=username,
                             password=password)

        self.reddit.user.me()

    def subreddit_search(self, topic, category, number_of_subreddit, text_area_object):

        # subreddit searchin function

        subreddit = self.reddit.subreddit(f"{topic.replace(' ', '+')}")

        # according to gui set settings

        if category == "Hot":

            hot = subreddit.hot(limit=number_of_subreddit)

            # find subreddits

            num = 0

            for hot_sub in hot:

                num += 1

                # insert text area extract features

                string = f"{num}-------->"f"URL :{hot_sub.url}\n\nTİTLE :{hot_sub.title}\n\nAUTHOR :{hot_sub.author}\n\n"\
                         f"CREATED TİME :{hot_sub.created_utc}\n\n"\
                         f"ID (search for comments) :{hot_sub.id}\n\n\n\n"

                text_area_object.insert(END, string)

                self.inserter_for_comments(string)

        elif category == "New":

            new = subreddit.new(limit=number_of_subreddit)

            num = 0

            # find subreddits

            for nes_sub in new:

                num += 1

                # insert text area extract features

                string = f"{num}-------->"f"URL :{nes_sub.url}\n\nTİTLE :{nes_sub.title}\n\nAUTHOR :{nes_sub.author}\n\n" \
                         f"CREATED TİME :{nes_sub.created_utc}\n\n" \
                         f"ID (search for comments) :{nes_sub.id}\n\n\n\n"

                text_area_object.insert(END, string)

                self.inserter_for_comments(string)

        elif category == "Controversial":

            controversial = subreddit.controversial(limit=number_of_subreddit)

            # find subreddit

            num = 0

            for contro_sub in controversial:

                num += 1

                # insert text area extract features

                string = f"{num}-------->"f"URL :{contro_sub.url}\n\nTİTLE :{contro_sub.title}\n\n" \
                         f"AUTHOR :{contro_sub.author}\n\n" \
                         f"CREATED TİME :{contro_sub.created_utc}\n\n" \
                         f"ID (search for comments) :{contro_sub.id}\n\n\n\n"

                print(string)

                text_area_object.insert(END, string)

                self.inserter_for_comments(string)

        elif category == "Top":

            top = subreddit.top(limit=number_of_subreddit)

            # find subreddit

            num = 0

            for top_sub in top:
                num += 1

                # insert text area extract features

                string = f"{num}-------->"f"URL :{top_sub.url}\n\nTİTLE :{top_sub.title}\n\n" \
                         f"AUTHOR :{top_sub.author}\n\n" \
                         f"CREATED TİME :{top_sub.created_utc}\n\n" \
                         f"ID (search for comments) :{top_sub.id}\n\n\n\n"

                text_area_object.insert(END, string)

                self.inserter_for_comments(string)

        else:

            messagebox.showerror("HATA", "GEÇERSİZ KATEGORİ")

    # insert the txt to use after
    @staticmethod
    def inserter_for_comments(text):

        # create file

        with open("for_comments.txt", "a", encoding="utf-8") as comment:

            comment.write(text)

    # comments viewer

    def comment_search(self, reddit_post_id, comments_number, text_area_object):

        text_area_object.delete("0.0", END)

        # get comment id and create submisson class

        comments = self.reddit.submission(id=f"{reddit_post_id}").comments

        # get determined number of comments

        num_com = 0

        for comment in comments[0:comments_number]:

            num_com += 1

            text_area_object.insert(END, f"{num_com}------->"
                                         f"AUTHOR :{comment.author}\n\nCOMMENT :{comment.body}\n\n"
                                         f"CREATED DATE :{comment.created_utc}\n\n"
                                         f"COMMENT ID : {comment.id}\n\n\n\n")

    # upvote and downvote operations

    def upvote_reddit_comment(self, comment_id):

        # find comment and upvote

        comment = self.reddit.comment(f"{comment_id}")

        comment.upvote()

    def downvote_reddit_comment(self, comment_id):

        # find comment and downvote

        comment = self.reddit.comment(f"{comment_id}")

        comment.downvote()

    # replying comment

    def reply_comment(self, reply, comment_id):

        # replty comment according to parameters
        # if anything not find gives error

        try:

            reply_comment = self.reddit.comment(comment_id)

            reply_comment.reply(reply)

        except TypeError:

            messagebox.showerror("ERROR", "FILL AREAS MUSN'T BE EMPTY")

    # save comment from id

    def save_comment(self, id_of_object):

        save_item = self.reddit.comment(id_of_object)

        save_item.save()

    # save post from id

    def save_post(self, id_of_object):

        save_item = self.reddit.submission(id_of_object)

        save_item.save(category="view later")

    # send post section
    # normal
    def send_post_normal(self, title, text, group_name="test"):

        self.reddit.subreddit(group_name).submit(title, selftext=text)

    # with image

    def send_post_image(self, img_path, title, self_text, group_name="test"):

        img = InlineImage(img_path)

        text = self_text + "{img}"

        media = {"img": img}

        self.reddit.subreddit(group_name).submit(title, inline_media=media, selftext=text)

    # with video

    def send_post_video(self, video_path, title, self_text, group_name="test"):

        video = InlineVideo(video_path)

        text = self_text + "{video}"

        media = {"video": video}

        self.reddit.subreddit(group_name).submit(title, inline_media=media, selftext=text)

    # with gif

    def send_post_gif(self, gif_path, title, self_text, group_name="test"):

        gif = InlineGif(gif_path)

        text = self_text + "{gif}"

        media = {"gif": gif}

        self.reddit.subreddit(group_name).submit(title, inline_media=media, selftext=text)

    # send survey

    def send_survey(self, title=None, self_text=None, options=None, duration=10):

        list_of_options = [options.split("+")]

        self.reddit.subreddit("test").submit_poll(title, self_text=self_text,
                                                  options=list_of_options, duration=duration)


