from sklearn.linear_model import LogisticRegression

import MySQLdb
import random
from numpy import array

con=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="root",db="landslide")

cmd=con.cursor()
secure_random = random.SystemRandom()




def svm_classifier(prset):
    cmd.execute("select * from landslide")
    data=cmd.fetchall()

    dataset=[]
    class_set=[]



    cs=[]
    cs1=[]

    for d in data:
        try:
            datarow=[]
            datarow.append(float(d[2]))
            datarow.append(float(d[3]))
            datarow.append(float(d[6]))


            class_set.append(float(d[5]))
            cs.append((d[5]))

            dataset.append(datarow)
        except:
            print(d)
    yyy=[]


    yy = []
    yy.append(float(prset[1]))
    yy.append(float(prset[2]))
    yy.append(float(prset[3]))

    yyy.append(yy)


    datasetarray = array( dataset )

    yyy1=array(yyy)

    # fit final model
    X=datasetarray
    y=cs

    model = LogisticRegression()
    model.fit(X, y)
    # # new instances where we do not know the answer

    Xnew=yyy1

    ynew = model.predict(Xnew)

    print((ynew))
    #
    # # show the inputs and predicted outputs
    for i in range(len(Xnew)):
        print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))
    return ynew