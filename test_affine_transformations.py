from PIL import Image
import numpy as np

def main():
    test_image = Image.open("test_image.jpg")
    field_of_view_lim = np.pi / 12
    trap_height = 750
    trap_bot = 500
    start_pos = round(test_image.width / 2)
    trap_top = trap_bot + 2 * trap_height * np.tan(field_of_view_lim)
    new_coordinates = np.array([round(test_image.width/2), test_image.height]) 
    
    
    
    
    new_image = Image.new(test_image.mode,(test_image.width, test_image.height))
    trapapzoid = Image.new(test_image.mode,(test_image.width, test_image.height))
    
    for y in range(0, trap_height):
        width_start = start_pos - round((1/2 * trap_bot + (y * np.tan(field_of_view_lim))))
        width_finish = start_pos + round((1/2 * trap_bot + (y * np.tan(field_of_view_lim))))
        for x in range(width_start, width_finish):
            trapapzoid.putpixel((x,y),test_image.getpixel((x,y)))
            
    trapapzoid.show()
    
    for y in range(0, trap_height):
        width_start = start_pos - round((1/2 * trap_bot + (y * np.tan(field_of_view_lim))))
        width_finish = start_pos + round((1/2 * trap_bot + (y * np.tan(field_of_view_lim))))
        num_itter = width_finish - width_start 
        field_of_view_itter = (2 * field_of_view_lim /num_itter)
        field_of_view = field_of_view_lim

        for x in range(width_start, width_finish):
            test_transform = np.array([[1, np.sin(field_of_view)],[0,.5]])
            pos_vec = np.array([x,y])
            new_pos = np.matmul(test_transform, pos_vec)
            new_pos = np.around(new_pos)
            new_pos = np.int_(new_pos)
            new_pos = new_pos
            color = test_image.getpixel((x,y))
            new_image.putpixel(new_pos, color)
            field_of_view -= field_of_view_itter
            
    new_image = new_image.transpose(Image.FLIP_TOP_BOTTOM)
        
    new_image.show()
if __name__ == "__main__":
    main()

