import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
sns.set(color_codes=True)
sns.set(font_scale=1.4)
sns.set_style("whitegrid", {'axes.edgecolor': '0.0',
                            'grid.color': '.8', 'legend.frameon': True})
if os.environ.get('DISPLAY', '') == '':
    plt.switch_backend('agg')

# other useful params:
# marker, markeredgecolor(mec), markeredgewidth(mew), markerfacecolor(mfc)
# markersize, markerevery(means mark/data_nodes)
# example: mew=2, ms=4, markevery=10


class DrawCurves(object):
    def __init__(self, file_path, fig_path="./", label_list=None):
        self.fig_params = {"figure_path": "./",
                           "figure_name": "iter",
                           "label": [],
                           "xlabel": "Layers",
                           "ylabel": "Pruning Rate (%)",
                           "title": "",
                           "line_width": 3.3,
                           "line_style": "-",
                           "color": "blue",
                           "xlim": [],
                           "ylim": [],
                           "inverse": True,
                           "figure_format": "png"}
        self.file_path = file_path
        if not os.path.isfile(self.file_path):
            print "File not exist! %s" % self.file_path[i]
            return False

        self.fig_path = fig_path
        if not os.path.isdir(self.fig_path):
            os.mkdir(self.fig_path)

    @staticmethod
    def logparse(file_path):
        log_file = open(file_path)
        content = log_file.readline()

        log_data = []
        while content:
            inf = content.split('\t')
            tmp_data = []
            for item in inf:
                if item != "\n":
                    tmp_data.append(float(item))
            log_data.append(tmp_data)
            content = log_file.readline()
        return log_data

    def draw(self):

        log_data = self.logparse(file_path=self.file_path)
        fig_count = 0
        for item in log_data:
            plt.figure()
            input_data = item
            data_len = len(input_data)

            x = np.linspace(1, data_len, data_len)
            plt.plot(x, input_data, self.fig_params["line_style"], linewidth=self.fig_params["line_width"],
                     color=self.fig_params["color"])

            plt.xlabel(self.fig_params["xlabel"])
            plt.ylabel(self.fig_params["ylabel"])
            if not self.fig_params["title"] == "":
                plt.title(self.fig_params["title"])
            if len(self.fig_params["xlim"]) > 0:
                plt.xlim(self.fig_params["xlim"])
            if len(self.fig_params["ylim"]) > 0:
                plt.ylim(self.fig_params["ylim"])
            if not self.fig_path == "":
                self.fig_params["figure_path"] = self.fig_path

            # plt.grid()
            # plt.legend(loc=0, fontsize="small")
            # plt.show()
            plt.savefig(self.fig_params["figure_path"]
                        + self.fig_params["figure_name"]
                        + str(fig_count)
                        + "."
                        + self.fig_params["figure_format"],
                        format=self.fig_params["figure_format"])
            plt.close()
            fig_count += 1
            # break


file_path = "./d_mask.txt"
drawer = DrawCurves(file_path=file_path,
                    fig_path="./fig/")
drawer.draw()
