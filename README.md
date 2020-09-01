# py-youtube-dl-email

## why?

In order to transfer mp3s to an mp3 player that my kids use, I was planning for them to save songs to a youtube playlist, and then I'd download the entire playlist as mp3s. Then I'd transfer the mp3s to the player.

[`youtube-dl`][youtube-dl](https://ytdl-org.github.io/youtube-dl/) already has great support for downloading entire playlists. It's as simple as passing the playlist id:

```
youtube-dl -i PLwJ2VKmefmxpUJEGB1ff6yUZ5Zd7Gegn2
```

**Did you know that kids' content on youtube can't be saved to a playlist?** It's true, try to add [this video](https://www.youtube.com/watch?v=-CSxGHve60E) to a playlist. You'll see that the "Save" button is grey-out. If you click it, you get this message:

> This action is turned off for content made for kids

with a link to [this explanation](https://support.google.com/youtube/answer/9632097?nohelpkit=1&hl=en).

## why!

The plan is that the kids could share youtube videos via email. The recipient email address would be set up for just this purpose. The following Python3 code reads all unread emails and scans them for youtube links. Those links are then sent to youtube-dl, which downloads the youtube content as a local mp3 file. Files can then be manually synced with the mp3 player.

## the code

### Access your mailbox with imap via code

You should be using 2FA! And that means to access your mailbox with code, you need to generate an app password.

**Generating an app password for Gmail:** https://support.google.com/mail/answer/185833

### Installation on Mac OSX

Assuming you have `brew` installed

```
brew install ffmpeg
brew install youtube-dl
```

### Installation on non-Mac

I have no idea, but you'll need youtube-dl and ffmpeg on your $PATH.

## Configure the code

Get the required source code from this rep

```
git clone https://github.com/philshem/py-youtube-dl-email.git
cd py-youtube-dl-email/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Before running the code, first

```
cd py-youtube-dl-email/
cp .env_example .env
```

And then with a text editor, add your private information:

```
USER_IMAP='imap.gmail.com'
USER_EMAIL='your@email.com'
USER_PASSWORD='your app password'
```

Now you are ready to go.

**INFO:** This script is designed for an email account that does nothing else but recieve youtube links. It won't delete any emails, but it does mark any _unread_ email in the Inbox as _read_.

**TO-DO:** Change settings so emails are not necessarily marked as _read_.

## Running the code

As simple as 

```
cd py-youtube-dl-email/
python3 run.py
```

mp3 files will be saved to a folder called `mp3/` in the current working directory.
