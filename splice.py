from os import system
import sys
def splice(video, audio, out):
    cmd = 'ffmpeg -i ' + video + ' -i ' + audio + ' -shortest -vcodec copy -acodec aac -strict experimental -map 0:v:0 -map 1:a:0 ' + out
    system(cmd)
def main():
    splice(sys.argv[1], sys.argv[2], sys.argv[3])
if __name__ == '__main__':
    main()
