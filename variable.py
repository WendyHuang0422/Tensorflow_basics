# Dependencies:
# tensorflow: 1.9.0
# python 3.6.0

import tensorflow as tf

#variable in the "global variable" set
var = tf.Variable(0)

add_operation = tf.add(var, 1)
update_operation = tf.assign(var, add_operation)

with tf.Session() as sess:
    #once define variables, you have to initialize them by calling initializer
    sess.run(tf.global_variables_initializer())
    for _ in range(3):
        sess.run(update_operation)
        print(sess.run(var))