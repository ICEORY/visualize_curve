import os
import datetime
import imageio
import pdf2image

VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(folder, duration):
    images = []
    file_names = os.listdir(folder)
    file_names.sort(key=lambda x:int(x[4:-4])) 
    for filename in file_names:
        images.append(imageio.imread(os.path.join(folder, filename)))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":
    create_gif("./fig/", 0.1)