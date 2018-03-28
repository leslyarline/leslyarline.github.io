import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw
from PIL import ImageFont          

def mod_one_image(original_image):

    width, height = original_image.size
    wide=55
    color=(114,2,2)
    
    drawing_layer = PIL.ImageDraw.Draw(original_image)
    
    #DRAW STUFF HERE***********************************************      
    drawing_layer.polygon([(0,0),(wide,0),(wide,height),(0,height)],fill=color)
    drawing_layer.polygon([(0,0),(width,0),(width,wide),(0,wide)],fill=color)
    drawing_layer.polygon([(width-wide,0),(width,0),(width,height),(width-wide,height)],fill=color)
    drawing_layer.polygon([(0,height-wide),(width,height-wide),(width,height),(0,height)],fill=color)    
    
    drawing_layer.polygon([(0,0),(200,0),(200,200),(0,200)],fill=None, outline=color)
    drawing_layer.polygon([(0,170),(0,500),(160,500),(160,170)],fill=None, outline=color)
    drawing_layer.polygon([(0,460),(0,height-460),(200,height-460),(200,460)],fill=None, outline=color)
    drawing_layer.polygon([(0,500),(0,750),(200,750),(200,500)],fill=None, outline=color)
    drawing_layer.polygon([(0,600),(0,750),(230,750),(230,600)],fill=None, outline=color)
    drawing_layer.polygon([(1641,0),(1441,0),(1441,200),(1641,200)],fill=color, outline=color)

    #fontF = ImageFont.truetype("comic.ttf", 80)
    #drawing_layer.text((5000,height-wide-92),"FAMILY",font=fontF,fill=(84,5,5))
    #**************************************************************

    return original_image
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def mod_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print n
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        #print filename
        new_image = mod_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency