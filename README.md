## Reddit Image Downloader ##

This program downloads "top" submission from [r/wallpapers/](https://www.reddit.com/r/wallpapers/) subreddit.

### Requirements
* Python3.1<sup>[1]</sup>
* [Praw](https://github.com/praw-dev/praw#installation)


[1] I only tested it with Python 3.4.0 but it should work from Python 3.1 onwards.

### Usage
Open the terminal and write:
```python3 image_scraper.py```

### TODO
* Add support for non-direct links to images
* Add support for command-line arguments (e.g.: "-r pics" will download pictures from r/pics subreddit)