# Configuration

HyCAN uses a YAML-based configuration system. Below is an example of a configuration file:

```yaml
model:
  hidden_dim: 128
  num_layers: 3

training:
  epochs: 100
  learning_rate: 0.001
  batch_size: 64

data:
  dataset: 'cora'
  train_ratio: 0.8
  val_ratio: 0.1
  test_ratio: 0.1
```

### Parameters

- **model**
  - `hidden_dim`: Number of hidden dimensions.
  - `num_layers`: Number of layers in the model.

- **training**
  - `epochs`: Number of training epochs.
  - `learning_rate`: Learning rate for optimization.
  - `batch_size`: Batch size for training.

- **data**
  - `dataset`: Name of the dataset.
  - `train_ratio`: Ratio of data for training.
  - `val_ratio`: Ratio of data for validation.
  - `test_ratio`: Ratio of data for testing.

Refer to `configs/` for predefined configuration examples.