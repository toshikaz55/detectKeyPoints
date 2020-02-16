import os
import glob
import argparse

import cv2

def detectKeyPoints(detect_image):

    detector = cv2.AKAZE_create()
    keypoints = detector.detect(detect_image)

    return keypoints

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='detect keypoints from imagefile and do data argumentation.')
    parser.add_argument('-p', required=True, help='set files path.', metavar='imagefile_path')
    args = parser.parse_args()

    detect_dir = args.p + "/_detectedKeypoints"
    if not os.path.exists(detect_dir):
        os.makedirs(detect_dir)

    # pngファイル取得
    detected_files = glob.glob("%s/*.png" % (args.p))

    for file_name in detected_files:
        before_path = file_name
        filename = os.path.basename(file_name)
        after_path = '%s/%s' % ( detect_dir, filename )

        print("filename = "+filename)

    for detected_file_name in detected_files:
        print(" detect key points on file:"+detected_file_name)

        # 画像のロード
        image = cv2.imread(detected_file_name)
        #print(image)

        if image is None:
            # 読み込み失敗
            print("image is None")
            continue


        detectKeyPoints_list = detectKeyPoints(image)
        if len(detectKeyPoints_list) == 0:
            continue

        basename = os.path.basename(detected_file_name)

        out_image = cv2.drawKeypoints(image, detectKeyPoints_list, None)
        
        # 出力
        cv2.imwrite(detect_dir+"/"+"KeyPoints_"+basename+".png", out_image)


    print("Done.")
