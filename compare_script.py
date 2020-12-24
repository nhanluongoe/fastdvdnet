import cv2
import os

# load images into a list and sort the list (so it will be concatinated according to the )
before = sorted(os.listdir(os.path.join('/content', 'drive',
                                        'MyDrive', 'demo', 'middle', 'input_frames')))
print(len(before))
after = sorted(os.listdir(os.path.join('/content', 'drive',
                                       'MyDrive', 'demo', 'middle', 'output_frames')))
print(len(after))

# loop through 1986 frames
for i in range(108):
    # img on the left
    ip = cv2.imread(os.path.join('content', 'drive', 'MyDrive',
                                 'demo', 'middle', 'input_frames', before[i]))
    # print(images[i])
    # img on the right
    op = cv2.imread(os.path.join('content', 'drive', 'MyDrive',
                                 'demo', 'middle', 'output_frames', after[i]))
    # print(plots[i])
    # concat 2 image horizontally
    concat = cv2.hconcat([ip, op])
    # check output shape
    print(concat.shape)
    # save output image
    cv2.imwrite(os.path.join('content', 'drive', 'MyDrive', 'demo',
                             'middle', 'compare_frames', after[i]), concat)
