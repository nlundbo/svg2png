import cairo
import rsvg
import sys
import os

def convertSvgFolder(path, outputDir):
    map(lambda x : convertSvg2Png(path, x, outputDir),  os.listdir(path))

def convertSvg2Png(path, svgFileName,output_dir):
    handler = rsvg.Handle(path+svgFileName)
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, handler.props.width,handler.props.height)
    handler.render_cairo(cairo.Context(img))
    img.write_to_png( output_dir + svgFileName.replace(".svg",".png"))

def main(argv):
    usage = 'Usage: '+ argv[0] + " <Path to SVG>\n"
    usage = usage + "Converts all svg files to png."
    print argv
    if len(argv) == 1:
        print usage
    elif len(argv) == 2:
        convertSvgFolder(argv[1],"")
    elif len(argv) == 3:
        convertSvgFolder(argv[1],argv[2])
    else:
        print usage

if __name__ == "__main__":
   main(sys.argv[:])




