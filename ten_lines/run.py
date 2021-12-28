from autogluon.tabular import TabularDataset,TabularPredictor
#训练
train_data = TabularDataset('train.csv')
id,label = 'PassengerId','Survived'
predictor = TabularPredictor(label=label).fit(train_data.drop(columns=[id]))

# 自动提取特征，并用多个分类器进行分类

# 预测
import pandas as pd
test_data = TabularDataset('test.csv')
preds = predictor.predict(test_data.drop(columns=[id]))
submission = pd.DataFrame({id:test_data[id],label:preds})
submission.to_csv('submission.csv',index=False)

# 用transformer抽取文本特征