print("Made By Unique Gaming")


url = input("your url is: ")

url = (""+url)

if url.__contains__("youtu.be"):
    slice = slice(17, -1)

    print("your video id is: " + url[slice])
elif  url.__contains__("youtube.com/watch"):
    slice1 = slice(28,-14)
    print("your video id is: "+ url[slice1])
elif url.__contains__("shorts"):
    slice2 = slice(27,-14)
    print("your video id is: "+ url[slice2])
else:
    print("sorry but we can't find your video id please check your url once")