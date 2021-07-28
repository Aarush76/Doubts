import cv2
import dropbox
import time
import random
start_time = time.time()

def takepicture():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        print(ret)
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        start_time = time.time
        result = False
    return imageName
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2. destroyAllWindows()

def uploadPicture(imageName):
    accessToken = "sl.A1d8byp7rYN_pEsBdGQ5m3Te8UatmGP-VjxnJNunD4FhkHr3OrnkoyKMZJbsCXaeGhQFSGWmSzEUkld5pTERzZlygI0QS-SjDZYaqWnCnFOaFo82yom0SnhOghJkupBo1xnsQ60"
    file = img_counter
    from_file = file
    file_2 = "/NewFolder1/" + (imageName)
    dbx = dropbox.Dropbox(accessToken)

    with open(from_file, 'rb') as f:
        dbx.files_upload(f.read(), file_2, mode = dropbox.files.WriteMode.overwrite)
        print("Files Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = takepicture()
            uploadPicture(name)

main()
    

