import cairo
import rsvg
import sys
import os

filePath = "/home/niklas/android/workspace/PokerHand/res/drawable/"
name = "white_s_q.svg"
def convertSvgFolder(path):
    map(lambda x : convertSvg2Png(path,x),  os.listdir(path))
#    files_in_dir = os.listdir(path)
 #   for file_in_dir in files_in_dir:
  #      print file_in_dir


def convertSvg2Png(path, svgFileName,output_dir):
    handler = rsvg.Handle(path+svgFileName)
    x,y = handler.props.width,handler.props.height 
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, x,y)
    ctx = cairo.Context(img)
    handler.render_cairo(ctx)
    img.write_to_png( svgFileName.replace(".svg",".png"))

def main(argv):
    usage = 'Usage: '+ argv[0] + " <Path to SVG>\n"
    usage = usage + "Converts all svg files to png."
    if len(argv) == 1:
        print usage
    elif len(argv) == 2:
        convertSvgFolder(argv[1])
    else:
        print usage

if __name__ == "__main__":
   main(sys.argv[:])




