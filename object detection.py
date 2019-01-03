#importing all dependencies 
from keras.models import Sequential
from keras.layers import Dense, Flatten, MaxPooling2D, Convolution2D
from keras.preprocessing.image import ImageDataGenerator

#Building the model
model = Sequential() #Creating the instance of sequential model
model.add(Convolution2D(32,3,3, input_shape=(64,64,3), activation='relu')) #adding a coyenvolutional layer with relu as a activation funtion.
model.add(MaxPooling2D(pool_size=(2, 2))) #Adding pooling layer to the convolutional layer.
model.add(Flatten()) #converting the matrix to the fully connected feture vector.
model.add(Dense(output_dim=128,activation='relu')) # Adding a hidden layer ith relu as a activation function.
model.add(Dense(output_dim=1, activation='sigmoid')) #Output Layer with sigmoid as a activation function.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
mdel.summary()

#Training the model
train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('path of your training dataset',target_size=(64,64),batch_size=32,class_mode='binary')
test_set= test_datagen.flow_from_directory('path of your test data set',target_size=(64, 64),batch_size=32,class_mode='binary')
model.fit_generator(training_set,steps_per_epoch=2000,epochs=15,validation_data=test_set,validation_steps=2000)

