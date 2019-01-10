call activate spark-performance
cd src
spark-submit rnn.py --training_path ../dataset/iris.data --labels_path ../dataset/labels.data --output_path train_dir_iris --partitions 8
@pause