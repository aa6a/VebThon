#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣

import asyncio
import os
import random
from urllib.parse import quote_plus
from collections import deque
from ..core.logger import logging
from VebThon import zedub
from ..Config import Config
from ..helpers import get_user_from_event
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "الترفيه"

from . import ALIVE_NAME, deEmojify

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "zed"


M = (
    "┈┈ ╱▔▔▔▔▔▔▔▔▔▔▔▏\n"
    "┈╱╭▏╮╭┻┻╮╭┻┻╮ ╭▏ \n"
    "▕╮╰▏╯┃╭╮┃┃╭╮┃ ╰▏ \n"
    "▕╯┈▏┈┗┻┻┛┗┻┻┻╮ ▏ \n"
    "▕╭╮▏╮┈┈┈┈┏━━━╯ ▏\n"
    "▕╰╯▏╯╰┳┳┳┳┳┳╯ ╭▏ \n"
    "▕┈╭▏╭╮┃┗┛┗┛┃┈ ╰▏ \n"
    "▕┈╰▏╰╯╰━━━━╯┈┈ ▏I'm سبـونـج بــوب\n"
)


@zedub.zed_cmd(pattern="سبونج بوب")
async def kek(kek):
    await kek.edit(M)


D = (
    "╭━┳━╭━╭━╮╮\n"
    "┃┈┈┈┣▅╋▅┫┃\n"
    "┃┈┃┈╰━╰━━━━━━╮\n"
    "╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉\n"
    "╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤\n"
    "╲┃┈┈┈┈╭━┳━━━━╯\n"
    "╲┣━━━━━━┫You are كـلبي الــمدلل\n"
)


@zedub.zed_cmd(pattern="جلبي")
async def dog(dog):
    await dog.edit(D)

P = (
    "┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┃┏┗┛┓┃╭┫U   خنـزيـر┃\n"
    "┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)


F = (
    "╱▏┈┈┈┈┈┈ ▕╲▕╲┈┈┈\n"
    "▏▏┈┈┈┈┈┈ ▕▏▔▔╲┈┈\n"
    "▏╲┈┈┈┈┈┈╱┈▔┈ ▔ ╲┈\n"
    "╲▏▔▔▔▔▔▔╯╯╰┳━━▀\n"
    "┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈\n"
    "┈┃┏┳┳━━━┫┣┳┃┈┈┈\n"
    "┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈\n"
    "┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈You are ثعلــب مــاكر\n"
)

E = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈ν2.ο\n"
)

H = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈I'm ضــايج\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈So لا تعصــبني\n"
)


@zedub.zed_cmd(pattern="ثعلب")
async def fox(fox):
    await fox.edit(F)


@zedub.zed_cmd(pattern="فيل")
async def elephant(elephant):
    await elephant.edit(E)


@zedub.zed_cmd(pattern="معصب")
async def homer(homer):
    await homer.edit(H)


@zedub.zed_cmd(pattern="خنزير")
async def pig(pig):
    await pig.edit(P)


A = (
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀\n"
    "⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀\n"
    "⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄\n"
    "⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷\n"
    "⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏\n"
    "⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀\n"
    "⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
)


@zedub.zed_cmd(pattern="مان")
async def man(man):
    await man.edit(A)
    

C = (
    "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
    "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
    "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
    "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
    "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
    "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
    "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
    "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
    "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
    "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
    "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
)


@zedub.zed_cmd(pattern="صدمه")
async def sdma(sdma):
    await sdma.edit(C)


N = (
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
    "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
    "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
    "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
    "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
    "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
    "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
    "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)


@zedub.zed_cmd(pattern="نادم")
async def nadm(nadm):
    await nadm.edit(N)
    

T = (
    "⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿\n"
    "⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿\n"
    "⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿\n"
    "⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿\n"
    "⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿\n"
    "⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿\n"
    "⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿\n"
    "⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿\n"
    "⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹\n"
    "⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄\n"
    "⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀\n"
    "⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿\n"
    "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘\n"
)


@zedub.zed_cmd(pattern="ترمب")
async def trmb(trmb):
    await trmb.edit(T)


B = (
    "⠀⠀⠀⠀⢀⣀⣀⣀\n"
    "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
    "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
    "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
    "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
    "⠀\n"
    "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
    "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
    "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
    "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
    "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
    "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
    "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
    "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
)


@zedub.zed_cmd(pattern="همم")
async def hmm(hmm):
    await hmm.edit(B)


K = (
    "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
    "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
    "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
    "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
    "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
    "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
    "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
)


@zedub.zed_cmd(pattern="تشان")
async def chan(chan):
    await chan.edit(K)


V = (
    "                     ⣤⣶⣶⣶⣦⣤⣄⡀\n⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n⠀⠀⠀⢀⣾⣿⣿⣿⠿⠿⠟⠻⠿⢿⣿⣿⣿⡆\n⠀⠀⠀⢰⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀ ⠈⠉⢻⡇ \n⠀⠀⠀⠈⠿⣿⣇⣠⠤⠤⠤⢤⣀⣤⠤⠤⣺⡏ \n⠀⠀⠀⠀⠐⢉⣯⠹⣀⣀⣢⡸⠉⢏⡄⣀⣯⠁ \n⠀⠀⠀⠀⠡⠀⢹⣆⠀⠀⠀⣀⡀⡰⠀⢠⠖⠂ \n⠀⠀⠀⠀⠀⠈⠙⣿⣿⠀⠠⠚⢋⡁⠀⡜ \n⠀⠀⠀⠀⠀⠀⢸⠈⠙⠦⣤⣀⣤⣤⡼⠁  \n⠀⠀⠀ ⠀⢀⡌⠀⠀⠀⠀ ⠉⢏⡉  \n⠀⠀⠀⣀⣴⣿⣷⣶⣤⣤⣤⣴⣾⣷⣶⣦⡀ \n⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄ \n⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛",
)


@zedub.zed_cmd(pattern="صاك")
async def sakk(sakk):
    await sakk.edit(V)


L = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


@zedub.zed_cmd(pattern="معارض")
async def marth(marth):
    await marth.edit(L)



@zedub.zed_cmd(pattern="مروحيه(?: |$)(.*)")
async def _(event):
    animation_interval = 1.0
    animation_ttl = range(60)
    animation_chars = [
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔳 ▬▬▬.◙.▬▬▬ 🔲
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""",
        """".
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 👞
                      ╬═╬/▌ 
                      ╬═╬//\👞""""",
    ]
    event = await edit_or_reply(event, "**بـدء اقـلاع المـروحيـه ...🚁**")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])    


@zedub.zed_cmd(pattern="ابره(?:\s|$)([\s\S]*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    zedth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zedth2 = user.last_name.replace("\u2060", "") if user.last_name else user.username
    await edit_or_reply(mention, f"────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀\n\n**🚹 ╎ تنح واخذ الابره عزيزي 👨🏻‍⚕🤭😂** [{zedth}{zedth2}](tg://user?id={user.id})")


Fun1_cmd = (
"**╮•❐ اوامـر التسليـه والكاريكتـر ❿ ⦂ **\n"

"  •  `.سبونج بوب`\n"
"  •  `.ثعلب`\n"
"  •  `.جلبي`\n"
"  •  `.فيل`\n"
"  •  `.معصب`\n"
"  •  `.مان`\n"
"  •  `.صدمه`\n"
"  •  `.نادم`\n"
"  •  `.ترمب`\n"
"  •  `.تشان`\n"
"  •  `.همم`\n"
"  •  `.معارض`\n"
"  •  `.مروحيه`\n"
"  •  `.ابره`\n\n"

"**- اضغـط ع الامـر لـ النسـخ"
)

# Copyright (C) 2022 Zedthon . All Rights Reserved
@zedub.zed_cmd(pattern="تسليه1")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, Fun1_cmd)
