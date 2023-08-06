import numpy as np
import pandas as pd

class SyntheticData():
    def __init__(self) -> None:
        self.data = pd.DataFrame()
    def generate(self, n):
        # Generate random data
        X = np.random.rand(n, 1)
        y = 2 + 3 * X + np.random.randn(n, 1)
        
        # Convert to pandas DataFrame
        self.data = pd.DataFrame(np.hstack([X, y]), columns=['X', 'y'])
        
        return self.data