# Dependencies:
# tensorflow: 1.9.0
# python 3.6.0

import tensorflow as tf
#create placeholder
a1 = tf.placeholder(dtype=tf.float32, shape=None)
b1 = tf.placeholder(dtype=tf.float32, shape=None)
c1 = a1 + b1

#create placeholder
a2 = tf.placeholder(dtype=tf.float32, shape=[3, 1])
b2 = tf.placeholder(dtype=tf.float32, shape=[1, 3])
c2 = tf.matmul(a2, b2)

with tf.Session() as sess:
    #run single operation
    c1_result = sess.run(c1, feed_dict={a1:5, b1:10})
    print(c1_result)

    #run multiple operation
    c1_result, c2_result = sess.run(
        [c1, c2],    # run them together
        feed_dict={   #fill in the values for placeholder
            a1: 5, b1: 10,
            a2: [[1], [2], [3]], b2: [[3, 2, 1]]
        })
    print(c1_result)
    print(c2_result)