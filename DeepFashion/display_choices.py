import csv
from matplotlib.pyplot import figure, imshow, axis
from matplotlib.image import imread

class visual_display:
    def showImagesMatrix(list_of_files, col=10):
        mypath = '.'
        hSize = 5
        wSize = 5
        fig = figure( figsize=(wSize, hSize))
        number_of_files = len(list_of_files)
        row = number_of_files/col
        if (number_of_files%col != 0):
            row += 1
        for i in range(number_of_files):
            a=fig.add_subplot(row,col,i+1)
            image = imread(mypath+'/'+list_of_files[i])
            imshow(image,cmap='Greys_r')
            axis('off')
    def show_image_Choices(user):
        all_files = []
        with open(user+'.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for index,row in enumerate(spamreader):
                if index > 0:
                    try: 
                        # print(row[1])
                        all_files.append(row[1])
                    except:
                        print('error')
        return all_files


visual_display.showImagesMatrix(visual_display.show_image_Choices('Matt'))