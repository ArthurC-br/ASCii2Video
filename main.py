import cv2
import pickle

class Image2ASCii:
    def __init__(self, path, val):
        self.path = path
        self.frameList = []
        self.density = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2", "1", '0', "!", "a", "b", "c",
                        ";", ":", "+", "=", "-", ".", "_"]
        self.resize = val

    def load_image(self):
        image = cv2.imread(self.path)
        image = cv2.resize(image, (image.shape[1]//self.resize,
                           image.shape[0]//self.resize))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image
    def image_ascii(self, *args, **kwargs):
        try:
            if args:
                img = args[0]
            else:
                img = self.load_image()

            rows, cols = img.shape
            frame = "\n"
            for i in range(rows):
                for j in range(cols):
                    im_res = img.item(i,j)
                    frame += self.density[im_res//30]
                frame +="\n"
            return frame
        except Exception as e:
            print(e)

    def video_ascii(self):
        self.video = cv2.VideoCapture(self.path)
        while(True):
            try:
                _, image = self.video.read()
                image = cv2.resize(image, (image.shape[1] // self.resize,
                                           image.shape[0] // self.resize))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                self.frameList.append(self.image_ascii(image))
            except Exception as e:
                print(e)
                break
        with open("output.txt", "wb") as file:
            pickle.dump(self.frameList, file)

