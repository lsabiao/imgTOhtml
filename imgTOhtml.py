from PIL import Image
import sys

#TODO "a" problem

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

if (len(sys.argv) >= 2):
    try:
        output = open(sys.argv[2],"w")
    except:
        print "Can't Open Output File"
        sys.exit(1)
    header = '''<table border='0' cellspacing='0' width='1'>
    <tr>\n'''
    output.write(header)
    try:
        original = Image.open(sys.argv[1])
    except:
        print "Can't open Image File"
        sys.exit(1)
    if (len(sys.argv)>3):
        try:
            original = original.resize((int(sys.argv[3]),int(sys.argv[4])))
        except:
            print "fail to resize"
            print "using original size"
    original.convert("RGB")
    width,height = original.size
    aux = 0
    auxHeight = 0
    for a in original.getdata():
        aux+=1
        output.write("        <td bgcolor='"+rgb_to_hex(a[:3])+"'> </td>\n")
        if aux == width:
            output.write("    </tr>\n")
            aux = 0
            auxHeight+=1
            if (auxHeight != height):
                output.write("    <tr>\n")
    output.write("</table>")
    output.close()
else:
    print "Usage: python imgTOhtml.py <Image> <output> <x> <y>"
    print "Example: python imgTOhtml.py logo.png logo.html 30 30"
    
