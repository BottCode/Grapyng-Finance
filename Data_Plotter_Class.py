import matplotlib.pyplot as plt

class Data_Plotter_Class:
    def __init__(self):
        pass

    def expenditure_hist(self, data):
        x_labels = list(data.keys())
        print(x_labels)
        for i in range(len(x_labels)):
            print(x_labels[i])
            if len(x_labels[i]) > 10:
                x_labels[i] = str(x_labels[i][0:8]) + ".."
                print(x_labels[i])

        plt.bar(x_labels, data.values())
        plt.show()
        # print(data)