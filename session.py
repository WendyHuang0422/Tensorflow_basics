# Dependencies:
# tensorflow: 1.9.0
# python 3.6.0

import tensorflow as tf

m1 = tf.constant([[5,3]])
m2 = tf.constant([[3],
                  [3]])
dot_operation = tf.matmul(m1,m2)

#wrong demo: no result, only print tensor Tensor("MatMul:0", shape=(1, 1), dtype=int32)
print(dot_operation)

#Method 1: use session
sess = tf.Session()
result = sess.run(dot_operation)
print(result)
sess.close()

#Method 2: use session
with tf.Session() as sess:
    result_2 = sess.run(dot_operation)
    print(result_2)