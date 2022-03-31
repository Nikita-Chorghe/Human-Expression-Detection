import train
import numpy as np
import xlsxwriter

import keras
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

import matplotlib.pyplot as plt



print("Enter name of class:")
name=input()
file = open(name+"/"+name+".txt") 
lines=file.readlines()



print("Enter time in minutes for class:")
number_of_minutes=int(input())

print("Enter the minutes for break between images:")
minutes_break=int(input())

number_of_faces=0

number_of_loops=int(number_of_minutes/minutes_break)

 # Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook(name+'/'+'results.xlsx')
worksheet = workbook.add_worksheet()

 # Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})


 # Adjust the column width.
worksheet.set_column(1, 1, 15)

 # Write some data headers.
worksheet.write('A1', 'IMAGE', bold)
worksheet.write('B1', 'FACE', bold)
worksheet.write('C1', 'ANGRY', bold)
worksheet.write('D1', 'DISGUST', bold)
worksheet.write('E1', 'FEAR', bold)
worksheet.write('F1', 'HAPPY', bold)
worksheet.write('G1', 'SAD', bold)
worksheet.write('H1', 'SURPRISE', bold)
worksheet.write('I1', 'NEUTRAL', bold)


#function for drawing bar chart for emotion preditions

def emotion_analysis(emotions):

    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

    y_pos = np.arange(len(objects))

    

    plt.bar(y_pos, emotions, align='center', alpha=0.5)
 

    plt.xticks(y_pos, objects)

    plt.ylabel('percentage')

    plt.title('emotion')

    

    plt.show()
#------------------------------


    

#------------------------------

#make prediction for custom image out of test set
num=0
row =2
while(num!=number_of_loops):

    fnumber=0
    number_of_faces=int(lines[num*2])

    while True:

        
        img = image.load_img("C:/Users/HP/Desktop/PROJECT/"+name+"/"+str(num)+"."+str(fnumber)+".jpg", color_mode = "grayscale", target_size=(48, 48))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)



        x /= 255



        custom = train.model.predict(x)

        emotion_analysis(custom[0])

        # Start from the first cell below the headers.
        row=row+1
        col = 2
        worksheet.write(row, col-2,   num    )
        worksheet.write(row, col-1,   fnumber    )        
        worksheet.write(row, col,     custom[0][0]       )
        worksheet.write(row, col+1,   custom[0][1]       )
        worksheet.write(row, col+2,   custom[0][2]       )
        worksheet.write(row, col+3,   custom[0][3]       )
        worksheet.write(row, col+4,   custom[0][4]       )
        worksheet.write(row, col+5,   custom[0][5]       )
        worksheet.write(row, col+6,   custom[0][6]       )

      
        #Write a total using a formula.
        #worksheet.write(row, 0, 'Total', bold)
        #worksheet.write(row, 2, '=SUM(C2:C5)', money_format)

        #print(custom[0])

        fnumber=fnumber+1
        if(fnumber==(number_of_faces)):
            break
        
    row=row+2
    num=num+1

workbook.close()
#------------------------------
