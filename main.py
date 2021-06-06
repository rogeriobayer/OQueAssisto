from detecto import core, utils, visualize
from datetime import datetime
from cv2 import imwrite, VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_DSHOW
from schedule import every, repeat, run_pending
import time
import tweepy
import os

import customdetecto
from secrets import *


@repeat(every(15).minutes)
def bot():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    filename = "\\" + dt_string + '.jpg'
    print(filename)

    cam = VideoCapture(0, CAP_DSHOW)
    cam.set(CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(CAP_PROP_FRAME_HEIGHT, 1080)
    s, img = cam.read()
    imwrite('foo.jpg', img)

    model = core.Model.load('canais.pth', ['SporTV', 'sportv2', 'SporTV3'])

    image = utils.read_image('foo.jpg')
    predictions = model.predict(image)

    labels, boxes, scores = predictions
    if type(labels[0]) is str:
        customdetecto.save_labeled_image(image, boxes[0], labels[0])

        # os.rename(r'C:\Users\tomat\PycharmProjects\MeuPaiAssisteOQue\detecto\foo.jpg',
        #           r'C:\Users\tomat\PycharmProjects\MeuPaiAssisteOQue\detecto\results' + filename)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)
        status = 'Eu estou assistindo: {}'.format(labels[0])
        api.update_with_media('results' + filename, status)

while True:
    run_pending()
    time.sleep(1)