import os.path

if os.path.isfile('main.py'):
	print("Yup, I exist")
	print("Now kill me")
	os.remove('main.py')
	print("Boom, dead")
else:
	print("You created a logical anomaly, the Universe is about to break in half")