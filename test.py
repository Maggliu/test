import tensorflow as tf
a=tf.Variable(2)
b=tf.Variable(5)
c=tf.Variable(3)
z=a*b+c
an="Answer is :\n"
init=tf.initialize_all_variables()
with tf.Session() as sess:
	sess.run(init)
	print(an)
	print(sess.run(z))
