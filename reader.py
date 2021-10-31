import tensorflow.compat.v1 as tf

def read_npy_file(item):
    data = np.load(item.decode())
    print("data: ", data)
    return data.astype(np.float32)

file_list = ['/foo/bar.npy', '/foo/baz.npy']

dataset = tf.data.Dataset.from_tensor_slices(file_list)

dataset = dataset.map(
        lambda item: tuple(tf.py_func(read_npy_file, [item], [tf.float32,])))