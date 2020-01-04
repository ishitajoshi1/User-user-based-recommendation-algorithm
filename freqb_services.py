#import libraries
import pandas as pd
import numpy as np
import math
import random
import time
def freqb_prod(user_id):
    path1 = "C:/Users/Ishita Joshi/Desktop/data/eUsers.csv"
    path2 = "C:/Users/Ishita Joshi/Desktop/data/eProducts.csv"
    path3 = "C:/Users/Ishita Joshi/Desktop/data/ePscoring.csv"
    last_time = time.time()#Comment it if we don't want to know how much time algo takes
    Ratings = pd.read_csv(path1)
    Products = pd.read_csv(path2)
    data = pd.merge(Ratings, Products, on='PID')
    data = data.fillna(0)
    #Finding the products purchased
    purchased_pro = data.loc[data['user_id'] == user_id]
    categ = list(purchased_pro['Category'])#all categories whose product are to be shown
    rat_exist = list(purchased_pro['Ratings'])
    #Check if ratings not given
    rating=0
    for value in rat_exist:
        if(value!=0):
            rating = 1
    if (rating != 0):
        #print('hey')
        # Calculate mean rating of all categories
        data.groupby('Category')['Ratings'].mean().sort_values(ascending=False)
        data.groupby('Category')['Ratings'].count().sort_values(ascending=False)
        ratings = pd.DataFrame(data.groupby('Category')['Ratings'].mean().round(2))
        ratings['Total Ratings'] = pd.DataFrame(data.groupby('Category')['Ratings'].count())
        datamat = data.pivot_table(index ='user_id', columns ='Category', values ='Ratings')
        datamat = datamat.fillna(0)
        #ML on all categories so for loop
        for i in categ:
            prod_usr_ratings = datamat[i]
            similarto_prod = datamat.corrwith(prod_usr_ratings,axis=0,drop=False,method='pearson')
            corr_prod = pd.DataFrame(similarto_prod,columns=['Correlation'])
            corr_prod.dropna(inplace = True)
            corr_prod = pd.DataFrame(corr_prod['Correlation'].round(2))
            corr_prod =corr_prod.sort_values('Correlation', ascending = False)
            corr_prod = corr_prod.join(ratings['Total Ratings'])
            #result_df = corr_prod.loc[corr_prod['Correlation']>0 & corr_prod['Correlation']!=1]
            result_df = corr_prod.loc[corr_prod['Correlation']>0]
            fresult_df = corr_prod.loc[corr_prod['Correlation']==1]
            selected_category= list(set(result_df.index)^set(fresult_df.index))
            for j in selected_category:
                recommended_pro = data.loc[data['Category']==j]
                recommended_pro = recommended_pro.fillna(0)
                recommended_pro = recommended_pro.sort_values('Ratings',ascending=False)#3 products from category
        product_frame = list(recommended_pro['ProductName'])
        print("Recommending services' model is taking {} seconds with ratings\n".format((time.time()-last_time)))#Comment it if we don't want to know how much time algo takes
        last_time=time.time()#Comment it if we don't want to know how much time algo takes
        print(product_frame[0]) #3outputs
        print(product_frame[1])
        print(product_frame[2])
    else:
        #print('hello')
        #when ratings are not given, load custom matrix
        Scoring = pd.read_csv(path3,skiprows=0)
        products_df = pd.DataFrame(data[['PID','user_id','ProductName']])
        score_merged = pd.merge(products_df,Scoring,on='PID')
        score_merged = pd.DataFrame(score_merged)
        score_merged = score_merged.drop(['PID','ProductName'],axis=1)
        p_pro = pd.DataFrame(score_merged.loc[score_merged['user_id'] == user_id])
        p_pro = p_pro.set_index('user_id')
        list_1 = p_pro.columns
        required_catg = list(set(categ)^set(list_1))
        final_list=[]
        for i in required_catg:
            value = max(p_pro.loc[:,i])
            if value>2:
                r_pro = Products.loc[Products['Category']==i]
                r_prol = list(r_pro['ProductName'])
                final_list.append(r_prol)
        flattened_list = [y for x in final_list for y in x]
        products = random.sample(flattened_list,k=3)
        print("Frequently bought services' model is taking {} seconds without rating\n".format(time.time()-last_time))#Comment it if we don't want to know how much time algo takes
        last_time = time.time()
        print(products[0])#output is list of 3 products
        print(products[1])
        print(products[2])
#freqb_prod('deb@gmail.com') #-with ratings       
#freqb_prod('tarun@gmail.com') #-no ratings

