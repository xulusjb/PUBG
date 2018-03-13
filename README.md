# Introduction
⚠⚠⚠ Dear Users, please [download the latest 0313 version](https://github.com/xulusjb/PUBG/releases/download/1.3/pubg0313.zip) after the 9Gb update(which added emotes). The 0108 version is depricated. ⚠⚠⚠  <br />
It is the python script for bot / farming in PUBG PC 1.0. <br />
[Chinese version|中文说明](https://github.com/xulusjb/PUBG/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E) </br>
[日本語版](https://github.com/xulusjb/PUBG/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E%E7%89%88wiki) </br>
You may use it to earn bp or lower your leaderboard rank. <br />
[Our suggestion for farming efficiency](https://github.com/xulusjb/PUBG/wiki/Farming-efficiency)
<br />
<!--
[![Support via PayPal](https://cdn.rawgit.com/twolfson/paypal-github-button/1.0.0/dist/button.svg)](https://www.paypal.me/htakatoshi/)
-->
# Usage

For security reason, strongly recommend you to compile the executable file by yourself!</br>
We assume NO responsibility for any kind of loss caused by using this bot.</br>
If you want to use the bot directly, you may download the release version [here](https://github.com/xulusjb/PUBG/releases)</br>
This bot currently only works for 1920*1080 screen. For other resolution, you need to adjust parameters by yourself.
1. Set the game as required below
1. Start main.exe
1. Get back to the game
1. Enjoy boting~~~
<br />
  

# Configuration

<p>Servers: NA:1|EU:2|KRJP:3|AS:4|OC:5|SA:6|SEA:7 </p>
<p>Modes: SOLO:1|DUO:2|SQUAD:3 </p>
<p>Example: If you want to farm for NA-Solo, set config.json as "11",  if you want to bot for AS-DUO, set as "42". </p>
<p>If you want to farm for BP, set waittime as "220". If you only want to lower your rank, set waittime as "0".</p>
<p>Attention: Must set and only set 5 models. The probability to choose one certain model is same for the five models.</p>
<br />
<h1>
Compile
</h1>
<p>Use “pyinstaller --onefile main.py” to generate the exe file. </p>
<br />
<h1>
IMPORTANT!
</h1>
1. Must set language as 'English' and resolution as 'Fullscreen(Windowed)' and '1920*1080'!!!.<br />
2. You may set the mode and server you want to farm in the 'config.json'.<br />
<br />

# Dependency

To run the python script, the following dependencies are required:
* PyUserInput
* psutil 
* webbrowser 
* win32gui 
* win32con 
* win32process

To compile the python script, "pyinstaller" is required.

For many of these packages it's hard to get it on windows. First try to search if there's an official guidance. Many of these packages can be downloaded from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs). Many occasions still you have to build directly from source, take [this thread](https://github.com/xulusjb/PUBG/issues/5#issuecomment-369245480) for proper reference.


# Disclaimer

<p>This sample code aims for programming education purpose only. Please delete the depository within 24hrs of downloading. The authors of the code oppose AFK farming, cheating and other kind of aimbot usage of ANYKIND. The game developing company, Bluehole Inc, reserves all rights to persue improper in-game activities. </p>

<br/>
