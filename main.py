from PIL import Image
import argparse

def get_image(image_path):
    im = Image.open(image_path, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    return pixel_values

def get_width(image_path):
    im = Image.open(image_path, 'r')
    width, height = im.size
    return width

def pretty_print(arr, outfile):
    with open(outfile, 'w') as text_pic:
        for line in arr:
            line_string = ""
            for pix in line:
                line_string = line_string + str(pix)
            print(line_string)
            text_pic.write(line_string + '\n')

    

def main(args):
    # pic = './pic.jpg'
    pic = args.path # comes from cmd line arg
    outfile = './photo.txt' #text rep
    raw_data = get_image(pic) #convert to rgb
    simplified_list = [] #simplified rep holder
    temp_list = [] #holds data per line
    max_val = 765 
    count = 0
    width = get_width(pic)

    for pixel in raw_data:
        total = 0
        for val in pixel:
            total += val
        
        temp_list.append(round((abs(max_val - total) * .01)))
        count+=1

        if len(temp_list) == width:
            simplified_list.append(temp_list)
            temp_list = []
    
    pretty_print(simplified_list, outfile) # writes to file
    
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="str path to picture eg: --path './path/to/pic.jpg'", default="./pic.jpg")
    args = parser.parse_args()
    main(args)