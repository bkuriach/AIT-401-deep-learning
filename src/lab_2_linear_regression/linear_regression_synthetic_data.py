# Importing libraries  
import numpy as np  
import pandas as pd  
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from sklearn.metrics import (
    r2_score,
    mean_squared_error
)
from lab_1_python.create_synthetic_data import SyntheticData

class LinearRegression() :
      
    def __init__( self, learning_rate, iterations ) :          
        self.learning_rate = learning_rate          
        self.iterations = iterations
          
    # Function for model training              
    def fit( self, X, Y ) :          
        # no_of_training_examples, no_of_features          
        self.m, self.n = X.shape

        # weight initialization          
        self.W = np.zeros( self.n )          
        self.b = 0          
        self.X = X          
        self.Y = Y          
          
        # gradient descent learning                  
        for i in range( self.iterations ) :              
            self.update_weights()
              
        return self
    
    # Function to update weights in gradient descent      
    def update_weights( self ) :

        Y_pred = self.predict( self.X ) 

        # calculate gradients        
        dW = - ( 2 * ( self.X.T ).dot( self.Y - Y_pred )  ) / self.m       
        db = - 2 * np.sum( self.Y - Y_pred ) / self.m 
          
        # update weights      
        self.W = self.W - self.learning_rate * dW      
        self.b = self.b - self.learning_rate * db
          
        return self
      
    # Predict function  h( x ) 
      
    def predict( self, X ) :
      
        return X.dot( self.W ) + self.b


def main() :
      
    # Importing dataset      
    df = SyntheticData().generate(1000)
  
    X = df.iloc[:,:-1].values  
    Y = df.iloc[:,1].values
      
    # Splitting dataset into train and test set  
    X_train, X_test, Y_train, Y_test = train_test_split( 
    X, Y, test_size = 1/3, random_state = 0 )
      
    # Model training      
    model = LinearRegression( iterations = 1000, learning_rate = 0.01 )  
    model.fit( X_train, Y_train )
      
    # Prediction on test set  
    Y_pred = model.predict( X_test )
      
    print( "Predicted values ", np.round( Y_pred[:3], 2 ) )       
    print( "Real values      ", Y_test[:3] )      
    print( "Trained W        ", round( model.W[0], 2 ) )      
    print( "Trained b        ", round( model.b, 2 ) )

    print("Root Mean Squared Error",np.sqrt(mean_squared_error(Y_test,Y_pred)))
    r2 = r2_score(Y_test,Y_pred)
    print("R^2", r2)

    adjusted_r_squared = 1 - (1-r2)*(len(Y)-1)/(len(Y)-X.shape[1]-1)
    print("Adjusted R^2",adjusted_r_squared)
      
    # Visualization on test set       
    plt.scatter( X_test, Y_test, color = 'blue' )      
    plt.plot( X_test, Y_pred, color = 'orange' )      
    plt.title( 'Synthetic Data' )      
    plt.xlabel( 'Feature 1' )      
    plt.ylabel( 'Y' )
      
    plt.show()