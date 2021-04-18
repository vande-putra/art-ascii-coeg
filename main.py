import time, os

if __name__ == '__main__':
	i = open('play.txt', 'r')
	frame = i.read()
	frame = frame.replace('.', ' ')
	i.close()
	frames = frame.split('SPLIT')
	os.system('mpg123 audio.mp3 & ')
	index_time = time.time()
	while time.time() <= index_time + 60*3+39:
		os.system('clear')
		print(frames[int((time.time()-index_time)*10)])
		time.sleep(0.1)
