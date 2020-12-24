import cv2
import os

ns = os.environ["NOISESIGMA"]  # noise sigma value
num_file = os.environ["FILECOUNT"]  # number of frames

# load images into a list and sort the list (so it will be concatinated according to the )
before = sorted(os.listdir(os.path.join('/content', 'drive',
                                        'MyDrive', 'demo', 'middle', 'input_frames')))
print(before)
after = sorted(os.listdir(os.path.join('/content', 'drive',
                                       'MyDrive', 'demo', 'middle', 'output_frames', 'ns_' + ns)), key=lambda item: int(item.split('_')[-1].split('.')[0]))
print(after)

# loop through 1986 frames
for i in range(num_file):
    # img on the left
    ip = cv2.imread(os.path.join('/content', 'drive', 'MyDrive',
                                 'demo', 'middle', 'input_frames', before[i]))
    # print(images[i])
    # img on the right
    op = cv2.imread(os.path.join('/content', 'drive', 'MyDrive',
                                 'demo', 'middle', 'output_frames', 'ns_' + ns, after[i]))
    # print(plots[i])
    # concat 2 image horizontally
    concat = cv2.hconcat([ip, op])
    # check output shape
    # save output image
    cv2.imwrite(os.path.join('/content', 'drive', 'MyDrive', 'demo',
                             'middle', 'compare_frames', 'ns_' + ns, after[i]), concat)
