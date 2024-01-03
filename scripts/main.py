from modules import scripts

class MyxTools(scripts.Script):
    def __init__(self):
        pass

    def title(self):
        return 'MyxTools'

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def postprocess(self, p, processed, *args):

        print("MyxTools")
