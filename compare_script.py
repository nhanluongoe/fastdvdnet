import cv2
import os
import argparse


def concat_func(ns, num_file):
    # load images into a list and sort the list (so it will be concatinated according to the )
    before = sorted(os.listdir(os.path.join('/content', 'drive',
                                            'MyDrive', 'demo', 'middle', 'input_frames')))
    print(before)
    after = sorted(os.listdir(os.path.join('/content', 'drive',
                                           'MyDrive', 'demo', 'middle', 'output_frames', 'ns_' + str(ns))), key=lambda item: int(item.split('_')[-1].split('.')[0]))
    print(after)

    for i in range(num_file):
        # img on the left
        ip = cv2.imread(os.path.join('/content', 'drive', 'MyDrive',
                                     'demo', 'middle', 'input_frames', before[i]))
        # print(images[i])
        # img on the right
        op = cv2.imread(os.path.join('/content', 'drive', 'MyDrive',
                                     'demo', 'middle', 'output_frames', 'ns_' + str(ns), after[i]))
        # print(plots[i])
        # concat 2 image horizontally
        concat = cv2.hconcat([ip, op])
        # check output shape
        # save output image
        cv2.imwrite(os.path.join('/content', 'drive', 'MyDrive', 'demo',
                                 'middle', 'compare_frames', 'ns_' + str(ns), after[i]), concat)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Denoise a sequence with FastDVDnet")
    parser.add_argument("--noise_sigma", type=int,
                        help='value of noise sigma')
    parser.add_argument("--num_file", type=int,
                        help='number of file to concat')

    argspar = parser.parse_args()

    # print(argspar.noise_sigma, argspar.num_file)

    concat_func(argspar.noise_sigma, argspar.num_file)
