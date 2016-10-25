import pickle
import sklearn

traindata = pickle.load(open('/mnt/hgfs/data/yixin/traindata.pkl', 'rb'))
labe      = pickle.load(open('/mnt/hgfs/data/yixin/labe.pkl', 'rb'))

from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
#分割样本训练集
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(traindata[:], labe[:], test_size=.2, random_state=42)


#尝试选择分类器
from sklearn import svm
sklearn.metrics.accuracy_score(y_test,svm.SVC(decision_function_shape='ovo',kernel='linear').fit(X_train, y_train).predict(X_test)) #0.92969048528849829
sklearn.metrics.accuracy_score(y_test,svm.SVC(decision_function_shape='ovo',kernel='poly').fit(X_train, y_train).predict(X_test))
sklearn.metrics.accuracy_score(y_test,svm.SVC(decision_function_shape='ovo',kernel='rbf').fit(X_train, y_train).predict(X_test))

sklearn.metrics.accuracy_score(y_test,svm.SVC(decision_function_shape='ovr',kernel='linear').fit(X_train, y_train).predict(X_test))



from sklearn.naive_bayes import GaussianNB 
sklearn.metrics.accuracy_score(y_test,OneVsRestClassifier(GaussianNB()).fit(X_train, y_train).predict(X_test)) #0.087886893389377149
sklearn.metrics.accuracy_score(y_test,OneVsOneClassifier(GaussianNB()).fit(X_train, y_train).predict(X_test))  




#训练并保存分类器
from sklearn import svm
allclc=svm.SVC(decision_function_shape='ovo',kernel='linear').fit(traindata, labe)

from sklearn.externals import joblib
joblib.dump(allclc, '/mnt/hgfs/data/yixin/allclc.pkl') 







