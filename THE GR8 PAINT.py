## FIFA PAINT
## By Luka David
## Welcome to FIFA Paint, a paint program with the theme of european football. One of the most popular sports around the world.
## This program is equipped with pencil, pen, eraser, marker and even spraypaint tools. You can change colours and listen to reknown
## football songs and fifa theme tracks. This paint program has more stamp selections than ever before, complete with six of the 
## best soccer players around the world. Each with invididual stamp rotations and sound effects. This program is equipped with all
## the basic tools of an ordinary program like the line, circle and rectangle tools but with much more. We even have added vital 
## features like the save and load functions. Enjoy creating masterpieces about the beautiful game today and start using FIFA Paint!
## (S.E == Self Explanatory)

from tkinter import * 										## Import used for saving and loading functions
from pygame import *											## Imports pygame functions
from random import *
from math import *
from os import environ										## Used for editing the location of where the program will load on your screen

mixer.pre_init()											## More imported elements being started...
mixer.init()
init()
inf = display.Info()
w,h = inf.current_w,inf.current_h
environ['SDL_VIDEO_WINDOW_POS'] = '350,25'					## This sets the program in the screen, for me specifically in the top right hand side

screen=display.set_mode((1000,700))
screen.fill(16777215)

#-----------------------------VARIABLES-----------------------------

omx,omy=300,300												## Variables for old mouse positions, this will change
colour=(0,0,0)
colourT=colour[:3]+(5,)										## Variable for tranparency
size=2														## Standard size, followed by individual sizes for all tools and stamps (S.E)
pensize=2
spraysize=20
erasersize=2
markersize=10
ellipsesize=2
linesize=2
rectsize=2
CristianoSize=1
ZlatanSize=1
LionelSize=1
SergioSize=1
MartialSize=1
KevinSize=1
LegendSize=1
GreatSize=1
root = Tk()
root.withdraw()

#-------------------------------IMAGES-------------------------------

#Background Items
Background=image.load("images/soccer_background.jpg")		## Pictures for title and vaious background elements and icons
Background=transform.scale(Background,(1000,700))
ColSpect=image.load("images/Cspect.png")
ColSpect=transform.scale(ColSpect,(200,34))
BWspect=image.load("images/BW.jpg")
BWspect=transform.scale(BWspect,(200,34))
fifalogo=image.load("images/fifa.logo.png")
fifalogo=transform.scale(fifalogo,(300,94))
paintlogo=image.load("images/paint.png")
paintlogo=transform.scale(paintlogo,(410,410))
screen.blit(Background,(0,0))
screen.blit(fifalogo,(250,20))
screen.blit(paintlogo,(500,-68))
Colourspect=screen.blit(ColSpect,(700,610))
BWSpect=screen.blit(BWspect,(480,610))
save=image.load("images/save.png")
save=transform.scale(save,(30,30))
save=screen.blit(save,(15,15))
play=image.load("images/pause.png")
play=transform.scale(play,(30,30))
play=screen.blit(play,(50,15))
fast=image.load("images/fast.png")
fast=transform.scale(fast,(30,30))
fast=screen.blit(fast,(80,15))

#Tools
pencilCon=image.load("images/pencil.png")					## Pictures for tool icons such as pencil, eraser and marker
pencilCon=transform.scale(pencilCon,(52,25))
penIcon=screen.blit(pencilCon,(894,130))
eraserCon=image.load("images/eraser.png")
eraserCon=transform.scale(eraserCon,(50,20))
erasIcon=screen.blit(eraserCon,(889,157))
penCon=image.load("images/pen.png")
penCon=transform.scale(penCon,(110,10))
metpenIcon=screen.blit(penCon,(840,240))
markerCon=image.load("images/marker.png")
markerCon=transform.scale(markerCon,(81,20))
markIcon=screen.blit(markerCon,(868,183))
sprayCon=image.load("images/spraypaint.png")
sprayCon=transform.scale(sprayCon,(38,20))
sprayIcon=screen.blit(sprayCon,(900,212))
tCoverPenc=screen.subsurface(900,130,90,300).copy()			## Subsurface used to create small animation in tools
tCoverDel=screen.subsurface(940,20,40,40).copy()    		## Subsurface used to create small animation in delete button
lineCon=image.load("images/line.jpg")						## More tool icon pictures (S.E)
lineIcon=screen.blit(lineCon,(250,610))
rectCon=image.load("images/rect.jpg")
rectIcon=screen.blit(rectCon,(310,610))
circleCon=image.load("images/circle.jpg")
circleIcon=screen.blit(circleCon,(370,610))
delButun=image.load("images/But.un.png")					## Various images used to create animation in delete button
delButun=transform.scale(delButun,(40,36))
delButpres=image.load("images/But.pres.png")
delButpres=transform.scale(delButpres,(40,32))
delUn=screen.blit(delButun,(940,20))     
brushHead = Surface((20,20))       							## Surface used in the alpha brush marker tool
#Stamps icons
Zlatan=image.load("images/Ibrahimovic.png")					## Pictures imported for stamp icons
Zlatan=transform.scale(Zlatan,(90,80))						## Variable format: Player First Name: Icon, Last Name: Stamp
Zlatan=screen.blit(Zlatan,(105,118))
Cristiano=image.load("images/Cristiano.png")
Cristiano=transform.scale(Cristiano,(90,78))
Cristiano=screen.blit(Cristiano,(5,118))
Lionel=image.load("images/Messi.png")
Lionel=transform.scale(Lionel,(90,75))
Lionel=screen.blit(Lionel,(105,205))
Sergio=image.load("images/Aguero.png")
Sergio=transform.scale(Sergio,(90,75))
Sergio=screen.blit(Sergio,(6,205))
Martial=image.load("images/martial.png")
Martial=transform.scale(Martial,(90,77))
Martial=screen.blit(Martial,(7,288))
Kevin=image.load("images/KDB.png")
Kevin=transform.scale(Kevin,(90,77))
Kevin=screen.blit(Kevin,(106,288))
Legend=image.load("images/legend.png")
Legend=transform.scale(Legend,(90,90))
Legend=screen.blit(Legend,(9,368))


#Stamps
Ibrahimovic=image.load("images/Ibra.png")					## Pictures for stamp rotations
Ibrahimovic=transform.scale(Ibrahimovic,(400,256))			## Variable format: Current club, Previous club, Previous club, National team
Ibrahimovic2=image.load("images/Ibra2.png")
Ibrahimovic2=transform.scale(Ibrahimovic2,(275,379))
Ibrahimovic3=image.load("images/Ibra3.png")
Ibrahimovic3=transform.scale(Ibrahimovic3,(275,294))
Ibrahimovic4=image.load("images/Ibra4.png")
Ibrahimovic4=transform.scale(Ibrahimovic4,(275,293))
Ronaldo=image.load("images/Ronaldo.png")
Ronaldo=transform.scale(Ronaldo,(235,345))
Ronaldo2=image.load("images/Ronaldo2.png")
Ronaldo2=transform.scale(Ronaldo2,(300,404))
Ronaldo3=image.load("images/Ronaldo3.png")
Ronaldo3=transform.scale(Ronaldo3,(300,409))
Ronaldo4=image.load("images/Ronaldo4.png")
Ronaldo4=transform.scale(Ronaldo4,(217,320))
LioMessi=image.load("images/LioMessi.png")
LioMessi=transform.scale(LioMessi,(300,345))
LioMessi2=image.load("images/LioMessi2.png")
LioMessi2=transform.scale(LioMessi2,(300,245))
LioMessi3=image.load("images/LioMessi3.png")
LioMessi3=transform.scale(LioMessi3,(400,256))
LioMessi4=image.load("images/LioMessi4.png")
LioMessi4=transform.scale(LioMessi4,(285,340))
AgueroKun=image.load("images/AgueroKun.png")
AgueroKun=transform.scale(AgueroKun,(250,348))
AgueroKun2=image.load("images/AgueroKun2.png")
AgueroKun2=transform.scale(AgueroKun2,(350,308))
AgueroKun3=image.load("images/AgueroKun3.png")
AgueroKun3=transform.scale(AgueroKun3,(300,348))
AgueroKun4=image.load("images/AgueroKun4.png")
AgueroKun4=transform.scale(AgueroKun4,(300,347))
AntMartial=image.load("images/martial1.png")
AntMartial=transform.scale(AntMartial,(250,410))
AntMartial2=image.load("images/martial2.png")
AntMartial2=transform.scale(AntMartial2,(270,374))
AntMartial3=image.load("images/martial3.png")
AntMartial3=transform.scale(AntMartial3,(275,375))
AntMartial4=image.load("images/martial4.png")
AntMartial4=transform.scale(AntMartial4,(300,270))
DeBruyne=image.load("images/KDB1.png")
DeBruyne=transform.scale(DeBruyne,(125,361))
DeBruyne2=image.load("images/KDB2.png")
DeBruyne2=transform.scale(DeBruyne2,(275,412))
DeBruyne3=image.load("images/KDB3.png")
DeBruyne3=transform.scale(DeBruyne3,(300,168))
DeBruyne4=image.load("images/KDB4.png")
DeBruyne4=transform.scale(DeBruyne4,(300,376))
Gullit=image.load("images/Gullit.png")						## Pictures for older or 'legendary' players
Gullit=transform.scale(Gullit,(315,350))
Henry=image.load("images/Henry.png")
Henry=transform.scale(Henry,(300,338))
Ronaldinho=image.load("images/Ronaldinho.png")
Ronaldinho=transform.scale(Ronaldinho,(300,224))
Ronaldinho2=image.load("images/Ronaldinho2.png")




#Stamp lists
KevinPics=[DeBruyne,DeBruyne2,DeBruyne3,DeBruyne4]			## Stamp rotations for each player or category
Knum=0														## Individual variable for rotations
MartialPics=[AntMartial,AntMartial2,AntMartial3,AntMartial4]
Mnum=0
IbraPics=[Ibrahimovic,Ibrahimovic2,Ibrahimovic3,Ibrahimovic4]
Inum=0
AgueroPics=[AgueroKun,AgueroKun2,AgueroKun3,AgueroKun4]
Anum=0
RonaldoPics=[Ronaldo,Ronaldo2,Ronaldo3,Ronaldo4]
Rnum=0
MessiPics=[LioMessi,LioMessi2,LioMessi3,LioMessi4]
MEnum=0
LegendPics=[Henry,Gullit,Ronaldinho,Ronaldinho2]
Lnum=0

#-------------------------------MUSIC-------------------------------

index=0														## Index number for the background song playlist
BSG1="audio/WavingFlag.ogg"									## Background songs (S.E)
BSG2="audio/This Time for Africa.ogg"
BSG3="audio/Walk.ogg"
BSG4="audio/Are You What You Want To Be.ogg"
BSG5="audio/My Type.ogg"
BSG6="audio/16 Years.ogg"
BSG7="audio/Euro 2016 Theme.ogg"
IbraMusic=mixer.Sound("audio/IBRA.ogg")						## Sound effects for individual players 
RonaldoMusic=mixer.Sound("audio/SI.ogg")
BackGPlaylist=[]											## Playlist for background music
BackGPlaylist.append(BSG1)									## Adding the songs to the playlist (S.E)
BackGPlaylist.append(BSG2)
BackGPlaylist.append(BSG3)
BackGPlaylist.append(BSG4)
BackGPlaylist.append(BSG5)
BackGPlaylist.append(BSG6)
BackGPlaylist.append(BSG7)
shuffle(BackGPlaylist)										## Shuffles the songs in the playlist (S.E)
song=BackGPlaylist[index]									## Lining up the index with the shuffled songs
mixer.music.load(song)										## Loading and playing of the background music
mixer.music.play()

END_MUSIC_EVENT=USEREVENT+0									## Ends the background music
mixer.music.set_endevent(END_MUSIC_EVENT)

#------------------------------SET UP-------------------------------

tool="pencil"												## The program starts with the pencil tool selected
mode="Any"													## Ensures the user from doing two things at once (ex. drawing on the canvas and changing tools)
canvas=draw.rect(screen,(255,255,255),(200,115,700,480),0)	## This variable is the canvas (S.E) 
running=True
bigPshow = False											## The following boolean variables are used in the animations of my tools...
bigPEshow = False											## They are used to prevent the image blited when hovering over the icon from staying on the icon
bigEshow = False											## Variable format: "big" repesenting the overhang of the image, followed by the
bigMshow = False											## First one or two letters of the tool, followed by "show" also represeting the overhang
bigSshow = False
Delpr = False												## Boolean variable representing if the pressed button is showing
Delunpr = True												## Boolean variable representing if the unpressed button is showing
paused = False
SI = False													## Variable for ensuring that the sound effects are only played when the tool is selected
ZI = True
LIO = False													## Same variable usage for the rest of the individual stamp sound effects
while running:
	for evt in event.get():
		if evt.type==QUIT:									## Used if the user wants to manually kill the program (S.E)
			running=False
		if evt.type==MOUSEBUTTONUP:							## Dectects when a mouse button is released
			if evt.button==1:
				mode="Any"									## Resets the mode as the function will be over
		if evt.type==MOUSEBUTTONDOWN:						## Detects when a mouse button is pressed
			if evt.button==1:
				back=screen.copy()							## Takes a picture of the background used for preventing the bliting of multiple images
				startx,starty=mx,my 						## A variable for the mouse postiion when the left click is pressed
				rectx,recty=mx,my 							## The same variable used for shapes
			if evt.button==3:								## Detects if the user right clicks
				if tool=="Cristiano":						## Each stamp has it's own rotation counter and, when you right click the counter increases
					Rnum+=1
					if Rnum==3:								## When the counter reaches it's limit it is reset
						Rnum=Rnum-4
				if tool=="Lionel":
					MEnum+=1
					if MEnum==3:
						MEnum=MEnum-4
				if tool=="Sergio":
					Anum+=1
					if Anum==3:
						Anum=Anum-4
				if tool=="Zlatan":
					if Inum==3:
						Inum=Inum-4
					Inum+=1
				if tool=="Kevin":
					Knum+=1
					if Knum==3:
						Knum=Knum-4
				if tool=="Martial":
					Mnum+=1
					if Mnum==3:
						Mnum=Mnum-4
				if tool=="Legend":							## The legend and great player's stamp rotations also has their own rotation
					Lnum+=1
					if Lnum==3:
						Lnum=Lnum-4
			if evt.button==4:								## Detects if the user scrolls up
				if tool=="spraypaint":						## Each tool and stamp has their own size variable
					spraysize+=3
				if tool=="pen":
					pensize+=5
				if tool=="marker":
					markersize+=5
				if tool=="eraser":
					erasersize+=5
				if tool=="line":
					linesize+=1
				if tool=="ellipseUNfill":
					ellipsesize+=1
				if tool=="Cristiano":
					CristianoSize*=1.1
				if tool=="Zlatan":
					ZlatanSize*=1.1
				if tool=="Lionel":
					LionelSize*=1.1
				if tool=="Sergio":
					SergioSize*=1.1
				if tool=="Martial":
					MartialSize*=1.1
				if tool=="Kevin":
					KevinSize*=1.1
				if tool=="Legend":
					LegendSize*=1.1
				if tool=="Great":
					GreatSize*=1.1
			if evt.button==5:
				if tool=="spraypaint":					## Detects if the user scrolls down
					if spraysize>4:						## Each individual stamp or tool has their own variable
						spraysize-=3
				if tool=="pen":
					if pensize>5:
						pensize-=5
				if tool=="marker":
					if markersize>6:
						markersize-=5
				if tool=="eraser":
					if erasersize>6:
						erasersize-=5
				if tool=="line":
					if linesize>2:
						linesize-=1
				if tool=="ellipseUNfill":
					if ellipsesize>2:
						ellipsesize-=1
				if tool=="Cristiano":
					CristianoSize*=0.9
				if tool=="Zlatan":
					ZlatanSize*=0.9
				if tool=="Lionel":
					LionelSize*=0.9
				if tool=="Sergio":
					SergioSize*=0.9
				if tool=="Martial":
					MartialSize*=0.9
				if tool=="Kevin":
					KevinSize*=0.9
				if tool=="Legend":
					LegendSize*=0.9
		if evt.type==KEYDOWN:								## Detects when any button is pressed
			if evt.key==K_ESCAPE:							## Terminates the program when the escape button is pressed
				running=False
		if evt.type==END_MUSIC_EVENT and evt.code==0:		## Stops the music
			index+=1
			if index==len(BackGPlaylist):					## Resets the playlist
				index=0
			song=BackGPlaylist[index]
			mixer.music.load(song)
			mixer.music.play()
			

		mx,my=mouse.get_pos()
		mb   =list(mouse.get_pressed())
		
#-------------------------------TOOLS-------------------------------

	draw.rect(screen,colour,(200,610,34,34),0)				## Displays colour
	
	if (canvas.collidepoint(mx,my) or canvas.collidepoint(omx,omy)) and mb[0]==1:		## Detects if the user left clicks on the canvas
		screen.set_clip(canvas)								## Ensures that what happens on the canvas stays on the canvas
		mode="Drawing"										## Ensures that only one function can be done at a time
		if tool=="pencil":								    ## Draws small circles from every point inbetween the old mouse position and the new one
			draw.line(screen,colour,(omx,omy),(mx,my),size)
		if tool=="spraypaint":								## Draws random points contained in a circle
			for i in range(4):
				sx=randint(-spraysize,spraysize)
				sy=randint(-spraysize,spraysize)
				if hypot(sx,sy)<spraysize:           
					screen.set_at((mx+sx,my+sy),colour)
		if tool=="pen":										## Pencil tool with adjustable size
			if mb[0]==1:
				dx=mx-omx
				dy=my-omy
				distan=int(sqrt(dx**2+dy**2))
				for i in range(1,distan+1):
					BrX=int(omx+i*dx/distan)
					BrY=int(omy+i*dy/distan)
					draw.circle(screen,colour,(BrX,BrY),pensize)
		if tool=="eraser":									## Performs the same task as the pen tool except in white
			if mb[0]==1:
				dx=mx-omx
				dy=my-omy
				distan=int(sqrt(dx**2+dy**2))  
				for i in range(1,distan+1):
					BrX=int(omx+i*dx/distan)
					BrY=int(omy+i*dy/distan)
					draw.circle(screen,(255,255,255),(BrX,BrY),erasersize)
		if tool=="marker":									## Similar function to the pencil however, the brush is tranparent
			if mx!=omx or my!=omy:
				if mb[0]==1:
					dx=mx-omx
					dy=my-omy
					distan=int(sqrt(dx**2+dy**2))
					colourT=colour[:3]+(5,)
					brushHead = Surface((markersize,markersize),SRCALPHA)  
					for i in range(1,distan+1):
						BrX=(omx+i*dx/distan)
						BrY=(omy+i*dy/distan)
						draw.circle(brushHead,(colourT),(markersize//2,markersize//2),markersize//2)
						screen.blit(brushHead, (BrX-markersize//2,BrY-markersize//2))
		if tool=="line":									## Creates lines from the last point the mouse is left clicked to the current mouse position
				screen.blit(back,(0,0))
				if mb[0]==1:
					dx=mx-startx
					dy=my-starty
					distan=int(sqrt(dx**2+dy**2))
					for i in range(1,distan+1):
						BrX=int(startx+i*dx/distan)
						BrY=int(starty+i*dy/distan)
						draw.circle(screen,colour,(BrX,BrY),linesize)    
		if tool=="rectUNfill":								## Draws an unfilled rectangle from the last point left clicked ot the current mouse position
				screen.blit(back,(0,0))
				draw.rect(screen,colour,(rectx,recty,mx-rectx,my-recty),size)
		if tool=="rectFill":								## Draws a filled rectangle
				screen.blit(back,(0,0))
				draw.rect(screen,colour,(rectx,recty,mx-rectx,my-recty))
		if tool=="ellipseUNfill":							## Draws an unfilled ellipse with a customizable thickness
				try:
					screen.blit(back,(0,0))
					ellimaker=Rect(rectx,recty,mx-rectx,my-recty)
					start1=rectx,recty
					ellimaker.normalize() 
					draw.ellipse(screen,colour,(ellimaker[0],ellimaker[1],ellimaker[2],ellimaker[3]),ellipsesize)
					draw.ellipse(screen,colour,(ellimaker[0]+1,ellimaker[1],ellimaker[2],ellimaker[3]),ellipsesize)
					draw.ellipse(screen,colour,(ellimaker[0]-1,ellimaker[1],ellimaker[2],ellimaker[3]),ellipsesize)
					draw.ellipse(screen,colour,(ellimaker[0],ellimaker[1]+1,ellimaker[2],ellimaker[3]),ellipsesize)
					draw.ellipse(screen,colour,(ellimaker[0],ellimaker[1]-1,ellimaker[2],ellimaker[3]),ellipsesize)
				except:
					pass
		if tool=="ellipseFill":								## Draws a filled ellipse
				screen.blit(back,(0,0))
				ellimaker=Rect(rectx,recty,mx-rectx,my-recty)  
				ellimaker.normalize()
				draw.ellipse(screen,colour,ellimaker)
		if tool=="Zlatan":									## Blits a stamp of a soccer player with rotation of four pictures and sound
				IbraSelec=IbraPics[Inum]					## Each player has adjustable size 
				REzlatan=transform.scale(IbraSelec,(round((IbraSelec.get_width()*ZlatanSize)),round((IbraSelec.get_height()*ZlatanSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					if ZI:
						mixer.Sound.play(IbraMusic)
						ZI=False
					screen.blit(REzlatan,(mx-180*ZlatanSize,my-115*ZlatanSize))
		if tool=="Cristiano":
				CristianoSelec=RonaldoPics[Rnum]			## The same format is used for every individual stamp
				REcristiano=transform.scale(CristianoSelec,(round((CristianoSelec.get_width()*CristianoSize)),round((CristianoSelec.get_height()*CristianoSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					if SI:
						mixer.Sound.play(RonaldoMusic)
						SI=False
					screen.blit(REcristiano,(mx-100*CristianoSize,my-140*CristianoSize))
		if tool=="Lionel":
				LionelSelec=MessiPics[MEnum]
				RElionel=transform.scale(LionelSelec,(round((LionelSelec.get_width()*LionelSize)),round((LionelSelec.get_height()*LionelSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					screen.blit(RElionel,(mx-150*LionelSize,my-130*LionelSize))
		if tool=="Sergio":
				SergioSelec=AgueroPics[Anum]
				REsergio=transform.scale(SergioSelec,(round((SergioSelec.get_width()*SergioSize)),round((SergioSelec.get_height()*SergioSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					screen.blit(REsergio,(mx-105*SergioSize,my-130*SergioSize))
		if tool=="Kevin":
				KevinSelec=KevinPics[Knum]
				REkevin=transform.scale(KevinSelec,(round((KevinSelec.get_width()*KevinSize)),round((KevinSelec.get_height()*KevinSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					screen.blit(REkevin,(mx-82*KevinSize,my-130*KevinSize))
		if tool=="Martial":
				MartialSelec=MartialPics[Mnum]
				REmartial=transform.scale(MartialSelec,(round((MartialSelec.get_width()*MartialSize)),round((MartialSelec.get_height()*MartialSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					screen.blit(REmartial,(mx-150*MartialSize,my-130*MartialSize))
		if tool=="Legend":
				LegendSelec=LegendPics[Lnum]
				RElegend=transform.scale(LegendSelec,(round((LegendSelec.get_width()*LegendSize)),round((LegendSelec.get_height()*LegendSize))))
				if mb[0]==1:
					screen.blit(back,(0,0))
					screen.blit(RElegend,(mx-150*LegendSize,my-130*LegendSize))

	if (Colourspect.collidepoint(mx,my)) and mb[0]==1:		## Used for switching colour, The pixel's colour selected will become the new colour
		colour=screen.get_at((mx,my))
	if (BWSpect.collidepoint(mx,my)) and mb[0]==1:		## Also used for switching colour
		colour=screen.get_at((mx,my))
		
#-----------------------------HIGHLIGHT-----------------------------
		
	if penIcon.collidepoint(mx,my):							## Highlights the tool being used by extending the tool and changes the current tool
		screen.blit(pencilCon,(899,130))
		bigPshow = True
		if mb[0]==1 and mode=="Any":
			tool="pencil"
	elif bigPshow:
		screen.blit(tCoverPenc,(900,130))
		bigPshow = False
	if metpenIcon.collidepoint(mx,my):
		screen.blit(penCon,(845,240))
		bigPEshow = True
		if mb[0]==1 and mode=="Any":
			tool="pen"
	elif bigPEshow:
		screen.blit(tCoverPenc,(900,130))
		bigPEshow = False
	if erasIcon.collidepoint(mx,my):
		screen.blit(eraserCon,(893,157))
		bigEshow = True
		if mb[0]==1 and mode=="Any":
			tool="eraser"
	elif bigEshow:
		screen.blit(tCoverPenc,(900,130))
		bigEshow = False
	if markIcon.collidepoint(mx,my):
		screen.blit(markerCon,(873,183))
		bigMshow = True
		if mb[0]==1 and mode=="Any":
			tool="marker"
	elif bigMshow:
		screen.blit(tCoverPenc,(900,130))
		bigMshow = False
	if sprayIcon.collidepoint(mx,my):
		screen.blit(sprayCon,(907,212))
		bigSshow = True
		if mb[0]==1 and mode=="Any":
			tool="spraypaint"
	elif bigSshow:
		screen.blit(tCoverPenc,(900,130))
		bigSshow = False  
	if lineIcon.collidepoint(mx,my):
		if mb[0]==1:
			tool="line"
	if rectIcon.collidepoint(mx,my):						## If the user right clicks on the icon they draw a filled shape 
		if mb[0]==1:										## If the user left clicks on the icon they draw an unfilled shape 
			tool="rectUNfill"
		if mb[2]==1:
			tool="rectFill"
	if circleIcon.collidepoint(mx,my):
		if mb[0]==1:
			tool="ellipseUNfill"
		if mb[2]==1:
			tool="ellipseFill"
	if Zlatan.collidepoint(mx,my):							## If the user selects a stamp icon the tool is chaneged and the sound effect is unlocked
		if mb[0]==1:
			tool="Zlatan"
			ZI=True
	if Cristiano.collidepoint(mx,my):
		if mb[0]==1:
			tool="Cristiano"
			SI=True
	if Lionel.collidepoint(mx,my):
		if mb[0]==1:
			tool="Lionel"
	if Sergio.collidepoint(mx,my):
		if mb[0]==1:
			tool="Sergio"
	if Martial.collidepoint(mx,my):
		if mb[0]==1:
			tool="Martial"
	if Kevin.collidepoint(mx,my):
		if mb[0]==1:
			tool="Kevin"
	if Legend.collidepoint(mx,my):
		if mb[0]==1:
			tool="Legend"
	if delUn.collidepoint(mx,my):							## Creates 'animation' to blit an unpressed button when not colliding and a pressed when clicked
		screen.blit(tCoverDel,(940,20))
		screen.blit(delButpres,(940,25))
		Delpr = True
		Delunpr = False
	if (delUn.collidepoint(mx,my)) and mb[0]==1:			## Restores blank canvas
		draw.rect(screen,(255,255,255),(200,115,700,480),0) 
	elif Delpr:
		screen.blit(tCoverDel,(940,20))
		screen.blit(delButun,(940,20))
		Delpr = False
		Delunpr = True

	if (fast.collidepoint(mx,my)) and mb[0]==1:
		index+=1
		if index==len(BackGPlaylist):
			index=0
			song=BackGPlaylist[index]
			mixer.music.load(song)
			mixer.music.play()
		song=BackGPlaylist[index]
		mixer.music.load(song)
		mixer.music.play()
		

	if (play.collidepoint(mx,my)) and mb[0]==1:
		if paused==True:
			mixer.music.unpause()
			paused=False
		elif paused==False:
			mixer.music.pause()
			paused=True

	if (save.collidepoint(mx,my)) and mb[0]==1:
		
		fileN=filedialog.asksaveasfilename(defaultextension=".png")

		if fileN:
			image.save(screen.subsurface(canvas),fileN)
			mb[0]=0
		
	if (save.collidepoint(mx,my)) and mb[2]==1:
		fileLoad=filedialog.askopenfilename(defaultextension=".png")
		fileOP=image.load(fileLoad)
		if fileOP:
			screen.blit(fileOP,(200,115))
			mb[0]=0


	screen.set_clip(None)
	omx,omy=mx,my
	display.flip()    
quit()
