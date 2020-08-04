# load packages
import pandas as pd
import scipy.stats as stats
# load data file

a = 1
# the total number of 'x' sets of 'y'frames each
for i in range(0, 31):
    path = r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\testdata' + str(i) + '.csv'
    # reading the csv file and storing into data frame 'd'
    # skiprows is the used for defining the frames to be skipped
    # skiprows is useful in iteration so we don't repeat the frames to be read
    # nrows is used for the number of frames we will be reading
    d = pd.read_csv(r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\blur_testdata.csv', sep=',', skiprows=a, nrows=125, dtype=float, names=['360p', '720p', '1080p'])
    # incrementing frames to be skipped for next iteration so it wont be repeated
    a += 125
    print(d)
    # Storing read data in new csv file
    d.to_csv(r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\testdata' + str(i) + '.csv')
    # assigning the newly created csv files to new data frame nd
    nd = pd.read_csv(r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\testdata' + str(i) + '.csv', sep=",")
    # calculating the p value from the newly created csv files
    # stats f_oneway functions takes the groups as input and returns F and P-value
    fvalue, pvalue = stats.f_oneway(nd['360p'], nd['720p'], nd['1080p'])
    print(pvalue)
    mean1 = nd['360p'].mean()
    sum1 = nd['360p'].sum()
    mean2 = nd['720p'].mean()
    sum2 = nd['720p'].sum()
    mean3 = nd['1080p'].mean()
    sum3 = nd['1080p'].sum()
    print(" 360 - Sum:" + str(format(sum1,'.2f')) + " Mean:" + str(format(mean1,'.2f')))
    print(" 720 - Sum:" + str(format(sum2,'.2f')) + " Mean:" + str(format(mean2,'.2f')))
    print(" 1080 - Sum:" + str(format(sum3,'.2f')) + " Mean:" + str(format(mean3,'.2f')))

    f = open(r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\P.csv', 'a')
    f.write("\n" + path + "," + str(pvalue) + "," + str(format(sum1,'.2f')) + "," + str(format(sum2,'.2f')) + "," + str(format(sum3,'.2f')) + "," + str(format(mean1,'.2f')) + "," + str(format(mean2,'.2f')) + "," + str(format(mean3,'.2f')))
    f.close()
nd2 = pd.read_csv(r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\P.csv', sep=",", names=['Frame_ID', 'P-value', '360p - SUM', '720p - SUM', '1080p - SUM', '360p - AVG', '720p - AVG', '1080p - AVG'])
nd2.to_csv(r'C:\Users\training\Desktop\Internship\My NOTES\Notes\Week2\31.05.19\Analysis 2\P.csv')
