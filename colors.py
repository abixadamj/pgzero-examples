#-------------------------------------------------------------------------------
# Name:        Colors
# Purpose:     Color library for Python/Pygame
#
# Author:      Joshua Smith
#
# Created:     08/29/2012
# Modified:    08/29/2014
# Copyright:   (c) Joshua Smith 2012, Steve Clement 2014
# Licence:     GNU Public License
#-------------------------------------------------------------------------------

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]

def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

#----------Start of colors----------#
RED1=(50,0,0)
RED2=(75,0,0)
RED3=(100,0,0)
RED4=(125,0,0)
RED5=(150,0,0)
RED6=(175,0,0)
RED7=(200,0,0)
RED8=(225,0,0)
RED=RED9=(255,0,0)
RED10=(255,150,150)
#-----------------------------------#
ORANGE=(255,127,0)
ORANGE1=(150,75,0)
ORANGE2=(175,80,0)
ORANGE3=(200,85,0)
ORANGE4=(225,90,0)
ORANGE5=(235,95,0)
ORANGE6=(245,100,0)
ORANGE7=(255,105,0)
ORANGE8=(255,125,0)
ORANGE9=(255,150,50)
ORANGE10=(255,200,100)
#-----------------------------------#
YELLOW=(255,255,0)
YELLOW1=(75,75,0)
YELLOW2=(100,100,0)
YELLOW3=(125,125,0)
YELLOW4=(150,150,0)
YELLOW5=(175,175,0)
YELLOW6=(200,200,0)
YELLOW7=(225,225,0)
YELLOW8=(250,250,0)
YELLOW9=(255,255,100)
YELLOW10=(255,255,150)
#-----------------------------------#
GREEN1=(0,50,0)
GREEN2=(0,75,0)
GREEN3=(0,100,0)
GREEN4=(0,125,0)
GREEN5=(0,150,0)
GREEN6=(0,175,0)
GREEN7=(0,200,0)
GREEN8=(0,225,0)
GREEN=GREEN9=(0,255,0)
GREEN10=(150,255,150)
#-----------------------------------#
CYAN1=(0,50,50)
CYAN2=(0,75,75)
CYAN3=(0,100,100)
CYAN4=(0,125,125)
CYAN5=(0,150,150)
CYAN6=(0,175,175)
CYAN7=(0,200,200)
CYAN8=(0,225,225)
CYAN=CYAN9=(0,255,255)
CYAN10=(150,255,255)
#-----------------------------------#
BLUE1=(0,0,50)
BLUE2=(0,0,75)
BLUE3=(0,0,100)
BLUE4=(0,0,125)
BLUE5=(0,0,150)
BLUE6=(0,0,175)
BLUE7=(0,0,200)
BLUE8=(0,0,225)
BLUE=BLUE9=(0,0,255)
BLUE10=(125,125,255)
#-----------------------------------#
PURPLE=(128,0,128)
PURPLE1=(50,0,50)
PURPLE2=(75,0,75)
PURPLE3=(100,0,100)
PURPLE4=(125,0,125)
PURPLE5=(150,0,150)
PURPLE6=(175,0,175)
PURPLE7=(200,0,200)
PURPLE8=(225,0,225)
PURPLE9=(240,0,240)
PURPLE10=(255,150,255)
#-----------------------------------#
BROWN1=(50,25,0)
BROWN2=(75,38,0)
BROWN3=(100,50,0)
BROWN4=(125,62,0)
BROWN=BROWN5=(150,75,0)
BROWN6=(175,88,0)
BROWN7=(200,101,0)
BROWN8=(225,114,0)
BROWN9=(250,127,0)
BROWN10=(255,140,25)
#-----------------------------------#
GRAY=(128,128,128)
GRAY1=(25,25,25)
GRAY2=(50,50,50)
GRAY3=(75,75,75)
GRAY4=(100,100,100)
GRAY5=(125,125,125)
GRAY6=(150,150,150)
GRAY7=(175,175,175)
GRAY8=(200,200,200)
GRAY9=(225,225,225)
GRAY10=(245,245,245)
#-----------------------------------#
PINK=(255,192,203)
#-----------------------------------#
VIOLET=(127,0,255)
#-----------------------------------#
MAGENTA=(255,0,255)
#-----------------------------------#
WHITE=(255,255,255)
BLACK=(0,0,0)
#-----------End of colors-----------#


