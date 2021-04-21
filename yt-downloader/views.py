from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.

from pytube import YouTube

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    if len(str(hour))<2:
        hour = "0" + str(hour)
    minutes = seconds // 60
    if len(str(minutes))<2:
        minutes = "0" + str(minutes)
    seconds %= 60
    if len(str(seconds))<2:
        seconds = "0" + str(seconds)

    return "{0}:{1}:{2}".format(hour, minutes, seconds)

def thankyou(x,y,z,request,*args,**kwargs):
	#request.method=''
	#if request.method == 'POST':
	# 	return render(request,"index.html",{})
	#	return home(request)
	return render(request,"thankyou.html",{"thumbnail_url":x,"title":y,"length":z})
	

def home(request,*args,**kwargs):
	if request.method == 'POST':
		link_1 = request.POST
		url = link_1['item']
		print(url)
		my_video = YouTube(url)

		print("*********************Video Title************************")
		#get Video Title
		y = str(my_video.title) 
		z = convert(int(my_video.length))


		print("********************Tumbnail Image***********************")
		#get Thumbnail Image
		print(my_video.thumbnail_url)
		x = str(my_video.thumbnail_url)


		print("********************Download video*************************")
		#get all the stream resolution for the 
		for stream in my_video.streams:
		     print(stream)

		#set stream resolution
		my_video = my_video.streams.get_highest_resolution()

		#or
		#my_video = my_video.streams.first()

		#Download video
		my_video.download(r'C:\ytvideos')
		return render(request,"thankyou.html",{"thumbnail_url":x,"title":y,"length":z})
		# return render(request,"thankyou.html",{"thumbnail_url":x,"title":y,"length":z})
	return render(request,"index.html",{})