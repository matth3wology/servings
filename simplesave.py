import tensorflow as tf

export_path = '/Users/whiterabbit/Desktop/servings/model/1'

tf.reset_default_graph()

#Main graph and model input/output go here.
x = tf.placeholder(tf.float32,[1],name='input')

w = tf.Variable(tf.constant([100.0]),name='weights')

z = x*w

tf.identity(z,name='prediction')

with tf.Session() as sess:

    sess.run(tf.global_variables_initializer())

    tf.saved_model.simple_save(
        sess,
        inputs={'x_in':x},
        outputs={'z_out':z},
        export_dir=export_path)
