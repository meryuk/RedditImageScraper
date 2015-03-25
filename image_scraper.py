import urllib.request

import praw

user_agent = ("Image scraper 0.1 by /u/-Ryuk/")
r = praw.Reddit(user_agent=user_agent)


def download_image():
    submissions = r.get_subreddit('wallpapers').get_top(limit=10)
    for submission in submissions:
        print(submission.url)
        if submission.url.endswith('.jpg'):
            image = urllib.request.urlopen(submission.url)
            local_file = open(next(filename_generator) + '.jpg', 'w+b')
            local_file.write(image.read())
            local_file.close()
        elif submission.url.endswith('.png'):
            image = urllib.request.urlopen(submission.url)
            local_file = open(next(filename_generator) + '.png', 'w+b')
            local_file.write(image.read())
            local_file.close()


def filename():
    base_filename = "img"
    count = 1
    while True:
        yield(base_filename + str(count))
        count += 1


filename_generator = filename()

download_image()
