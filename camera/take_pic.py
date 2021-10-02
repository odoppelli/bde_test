from picamera import PiCamera
from time import sleep
import os


class picture_camera:
    def __init__(self):
        self.camera = PiCamera()
        self.pic_counter = 0
        self.path = '/photos'

    def update_number_of_pictures(self):
        files = os.listdir(self.path)
        counter = 0
        for _ in files:
            counter += 1
        self.pic_counter = counter
        return counter

    def take_pictures(self, number = 1,break_timer = 2):
        self.update_number_of_pictures()
        try:
            self.camera.start_preview()
            # Camera warm-up time
            sleep(3)

            for _ in range(0,number):
                self.pic_counter +=1
                self.camera.capture('pic_'+str(self.pic_counter))
                sleep(break_timer)
            self.camera.stop_preview()
        finally:
            self.camera.close()

def main():
    fotograf = picture_camera()
    fotograf.take_pictures

if __name__ == '__main__':
    main()


