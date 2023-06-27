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
        OUTPUT_FOLDER,
        f'output_image_{filename}.jpg'
    )
    print(f"========================\nImage processed: {output_image_path}\n")  # Print current image's filename

    image = imutils.resize(image, height=800)
    image = imutils.rotate_bound(image, 0)

    channel_names = ['Blue', 'Green', 'Red']
    channels = cv2.split(image)
    masks = []
    for i, channel in enumerate(channels):
        channel = cv2.blur(channel, (11, 11))
        channel = cv2.Canny(channel, 20, 50)
        masks.append(channel)

    mask = cv2.bitwise_or(masks[0], cv2.bitwise_or(masks[1], masks[2]))

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    cv2.drawContours(image, cnts, -1, (0, 255, 255), 2)

    cv2.imwrite(output_image_path, image)

    return output_image_path, None, None
