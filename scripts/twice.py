#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BSD 2-Clause License
Copyright (c) 2021, Yamato Yoshinuma and Ryuichi Ueda
All rights reserved.
"""

import rospy
import random
from std_msgs.msg import Int32

n = 0
uns = 0
nyu = 0
tri = 0
a = 0
b = 0
c = 0
h = 0
kyo = ['頭上','足元','後ろ','階段']

def cb(message):
	global n
	n = message.data


rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size = 1)
rate = rospy.Rate(10)

while 1:
	tri = input('君の運勢を占おう。1～10の整数を言ってごらん?-->')
	
	try:
		tri = int(tri)
	except ValueError:
		tri = 0

	if tri < 1 or tri > 10:
		print ("1～10の整数だって言ったろう？やりなおしだ")
	else:
		break

while not rospy.is_shutdown():

	a = random.randint(1, 8)
	c = random.randint(1, 8)
	b = a + c

	h = (n + tri) % 10

	if h == 0:
		print(f"大吉だ。おめでとう。馬連{a}-{b}を買うといい。")
			
	elif h == 1:
		c = random.choice(kyo)
		print(f"凶だ。逆にツイてるかも。{c}に注意だ。")
	elif h == 2:
		print("小吉。自販機の下から500円玉が見つかるかも。探してみては？")
	elif h == 3:
		c = random.choice(kyo)
		print(f"末吉だ。{c}から運命の人が現れるかも。")
	elif h == 4:
		print("それとなく吉っぽい。普段通りにしよう。")
	elif h == 5:
		print(f"まあまあ凶。{a}人と喧嘩になるかもしれない。")
	elif h == 6:
		print(f"猫吉。今日は{a}匹の猫ちゃんと仲良くなれる。")
	elif h == 7:
		print("勘吉。葛飾区に行こう。")
	elif h == 8:
		print("言吉。詰みです。また来週。")
	elif h == 9:
		print("あっ…。うん、生きてればきっといいことあるよ――――。")
	elif h == 10:
		print("もしかしたら違う世界線では大吉だったかもしれない。\n―――悲しいけどこれ、大凶なのよね。")

	rospy.signal_shutdown('finish')
	rospy.spin()
