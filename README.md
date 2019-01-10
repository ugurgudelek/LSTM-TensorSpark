# LSTM-TensorSpark for python3

Forked python2 version from : [EmanuelOverflow/LSTM-TensorSpark](https://github.com/EmanuelOverflow/LSTM-TensorSpark)


Implementation of a LSTM with [TensorFlow](https://www.tensorflow.org/) and distributed on [Apache Spark](http://spark.apache.org/)

There are provided two different implementations:

- Distributed on Spark;
- Standalone;

Detailed explanation here: [Distributed implementation of a LSTM on Spark and Tensorflow](http://www.slideshare.net/emanueldinardo/distributed-implementation-of-a-lstm-on-spark-and-tensorflow-69787635)

Developed for academic purpose


## Installation

Run ```install.bat```
Simply it runs
```
conda env create -f environment.yml
```

You need apply the fix below if you are on Windows Computer  
[Windows Fix for pyspark=2.4.0](https://github.com/ugurgudelek/LSTM-TensorSpark/tree/master/fix)


## Usage

### Example using Spark:

Run ```run_with_spark.bat```  
Simply it runs
```
spark-submit rnn.py --training_path ../dataset/iris.data --labels_path ../dataset/labels.data --output_path train_dir_iris --partitions 8
```

```
usage: rnn.py [-h] [--master MASTER] [--spark_exec_memory SPARK_EXEC_MEMORY]
              [--partitions PARTITIONS] [--epochs EPOCHS]
              [--hidden_units HIDDEN_UNITS] [--batch_size BATCH_SIZE]
              [--num_classes NUM_CLASSES] [--in_features IN_FEATURES]
              [--evaluate_every EVALUATE_EVERY]
              [--learning_rate LEARNING_RATE] [--training_path TRAINING_PATH]
              [--labels_path LABELS_PATH] [--output_path OUTPUT_PATH]
              [--mode MODE] [--checkpoint_path CHECKPOINT_PATH]
```

```
optional arguments:
  -h, --help            show this help message and exit
  --master MASTER       Host or master node location (can be node name)
  --spark_exec_memory SPARK_EXEC_MEMORY
                        Spark executor memory
  --partitions PARTITIONS
                        Number of distributed partitions
  --epochs EPOCHS       Number of epochs
  --hidden_units HIDDEN_UNITS
                        List of hidden units per layer (seprated by comma)
  --batch_size BATCH_SIZE
                        Mini batch size
  --num_classes NUM_CLASSES
                        Number of classes in dataset
  --in_features IN_FEATURES
                        Number of input features
  --evaluate_every EVALUATE_EVERY
                        Numbers of steps for each evaluation
  --learning_rate LEARNING_RATE
                        Learning rate
  --training_path TRAINING_PATH
                        Path to training set
  --labels_path LABELS_PATH
                        Path to training_labels
  --output_path OUTPUT_PATH
                        Path for store network state
  --mode MODE           Execution mode
  --checkpoint_path CHECKPOINT_PATH
                        Directory where to save network model and logs
```

### Example without Spark:

Run ```run_without_spark.bat```  
Simply it runs

```
python lstm-no-spark.py

```

```
usage: rnn.py [-h] [--hidden_units HIDDEN_UNITS] [--batch_size BATCH_SIZE]
              [--num_classes NUM_CLASSES] [--in_features IN_FEATURES]
              [--evaluate_every EVALUATE_EVERY]
              [--learning_rate LEARNING_RATE] [--training_path TRAINING_PATH]
              [--labels_path LABELS_PATH] [--output_path OUTPUT_PATH]
              [--mode MODE] [--checkpoint_path CHECKPOINT_PATH]
```

```
optional arguments:
  --epochs EPOCHS       Number of epochs
  --hidden_units HIDDEN_UNITS
                        List of hidden units per layer (seprated by comma)
  --batch_size BATCH_SIZE
                        Mini batch size
  --num_classes NUM_CLASSES
                        Number of classes in dataset
  --in_features IN_FEATURES
                        Number of input features
  --evaluate_every EVALUATE_EVERY
                        Numbers of steps for each evaluation
  --learning_rate LEARNING_RATE
                        Learning rate
  --training_path TRAINING_PATH
                        Path to training set
  --labels_path LABELS_PATH
                        Path to training_labels
  --output_path OUTPUT_PATH
                        Path for store network state
  --mode MODE           Execution mode
  --checkpoint_path CHECKPOINT_PATH
                        Directory where to save network model and logs
```
