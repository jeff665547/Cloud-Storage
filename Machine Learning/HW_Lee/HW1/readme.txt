
本次作業的資料是從中央氣象局網站下載的真實觀測資料，
希望大家利用linear regression或其他方法預測PM2.5的數值。
作業使用豐原站的觀測記錄，
分成train set跟test set，
train set是豐原站每個月的前20天所有資料。
test set則是從豐原站剩下的資料中取樣出來。
train.csv：每個月前20天的完整資料。
test_X.csv：從剩下的10天資料中取樣出連續的10小時為一筆，
前九小時的所有觀測數據當作feature，
第十小時的PM2.5當作answer。
一共取出240筆不重複的test data，
請根據feauure預測這240筆的PM2.5。

train.csv - the training set
test.csv - the test set
sampleSubmission.csv - a sample submission file in the correct format