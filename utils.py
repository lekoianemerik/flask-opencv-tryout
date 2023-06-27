import os   
import imutils
import cv2

UPLOAD_FOLDER = os.path.join('static', 'uploads')
OUTPUT_FOLDER = os.path.join('static', 'output')

def blur_it_up(img_path):
    image = cv2.imread(img_path)
    if image is not None:
        print('File loaded into cv2!')
    else:
        raise Exception('cv2 fail')
    
    filename = img_path.split("/")[-1].split(".")[0]
    output_image_path = os.path.join(
        OUTPUT_FOLDER,  # Specified path using the image filename
        'output_image_{name}.jpg'.format(name=filename)
    )
    print(f"========================\nImage processed: {output_image_path}\n")  # Print current image's filename

    output = cv2.blur(image, (17, 17))

    cv2.imwrite(output_image_path, output)

    return output_image_path, None, None
