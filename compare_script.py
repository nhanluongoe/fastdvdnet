import cv2
import os
import argparse


def concat_func(ns, num_file):
    ns = int(ns)
    num_file = int(num_file)

    # load images into a list and sort the list (so it will be concatinated according to the )
    before = sorted(os.listdir(os.path.join('/content', 'drive',
                                            'MyDrive', 'demo', 'middle', 'input_frames')))
    print(before)
    after = sorted(os.listdir(os.path.join('/content', 'drive',
                                           'MyDrive', 'demo', 'middle', 'output_frames', 'ns_' + ns)), key=lambda item: int(item.split('_')[-1].split('.')[0]))
    print(after)

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


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Denoise a sequence with FastDVDnet")
    parser.add_argument("--noise_sigma", type=str,
                        help='value of noise sigma')
    parser.add_argument("--num_file", type=str,
                        help='number of file to concat')

    argspar = parser.parse_args()

    concat_func(**vars(argspar))
