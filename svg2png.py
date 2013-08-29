import cairo
import rsvg
import sys
import os

def convertSvgFolder(path, outputDir):
    fileList = os.listdir(path)
    map(lambda x : convertSvg2Png(path, x, outputDir), fileList)
    print len(fileList), " file(s) written to folder ", outputDir

def convertSvg2Png(path, svgFileName,output_dir):
    handler = rsvg.Handle(path+svgFileName)
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, handler.props.width,handler.props.height)
    handler.render_cairo(cairo.Context(img))
    img.write_to_png( output_dir + svgFileName.replace(".svg",".png"))

def main(argv):
    usage = 'Usage: '+ argv[0] + " <Path to SVG>\n"
    usage = usage + "Converts all svg files to png."
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




