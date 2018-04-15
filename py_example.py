background_image_filename='sushiplate.jpg'
mouse_image_filename="fuji.png"
###制定图像文件名称
import pygame
from pygame.locals import *
from sys import exit
##导入一些常用的函数和变量
#pygame.init()
##初始化pygame,为使用硬件做准备
pygame.display.set_mode((640,480),0,32)
#创建了一个窗口
pygame.display.set_caption('hello, world')
##设置窗口标题
background=pygame.image.load(background_image_filename).convert()
mouse_cursor=pygame.image.load(mouse_image_filename).convert_alpha()
###加载并转换图像
###convert()与convert.alpha()区别在哪？
########################################################
#######游戏主循环
while 1:
	for event in pygame.event.get():
		if event.type==QUIT:###接受到退出事件，推出程序
			exit()
	####################################################
	screen.blit(background,(0,0))###将背景图片画上去
	#游戏的主循环是一个无限循环，直到用户跳出。
	#在这个主循环里做的事情就是不停地画背景和更新光标位置，
	#虽然背景是不动的，我们还是需要每次都画它， 
	#否则鼠标覆盖过的位置就不能恢复正常了。
	x,y=pygame.mouse.get_pos()
	###获得鼠标的位置
	x=x-mouse_cursor.get_width()/2
	y=y-mouse_cursor.get_height()/2
	###计算光标的左上角位置
	#####################################################
	screen.blit(mouse_cursor,(x,y))
	#把光标画上去
	pygame.display.update()
	##刷新一下画面
########################################################