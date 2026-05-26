from typing import Optional, Union, Tuple, List, Literal
import pandas as pd
import numpy as np

class Descriptive:
    def __init__(self, data: pd.DataFrame, show_info: bool = True):
        self.data = data
        if data is not None:
            self._numerical_cols = data.select_dtypes(include=["int", "float"]).columns.tolist()
            self._categorical_cols = data.select_dtypes(include=["object"]).columns.tolist()
        else:
            print("No data provided")


    def mean(self, column: Optional[str] = None) -> Union[float, pd.Series]:
        """
        Media aritmética / Arithmetic mean
        
        Parametros / Parameters:
        ------------------------
        **column** : str
            Nombre de la columna
            Name of the column
        """
        if column:
            return self.data[column].mean()
        return self.data[self._numerical_cols].mean()
    
    def median(self, column: Optional[str] = None) -> Union[float, pd.Series]:
        """
        Mediana / Median
        
        Parametros / Parameters:
        ------------------------
        **column** : str
            Nombre de la columna
            Name of the column
        """
        if column:
            return self.data[column].median()
        return self.data[self._numeric_cols].median()
    
    def mode(self, column: Optional[str] = None):
        """
        Moda / Mode
        
        Parametros / Parameters:
        ------------------------
        column : str
            Nombre de la columna
            Name of the column
        """
        if column:
            return self.data[column].mode()[0]
        return self.data[self._numeric_cols].mode().iloc[0]
    
    def variance(self, column: Optional[str] = None) -> Union[float, pd.Series]:
        """
        Varianza / Variance
        
        Parametros / Parameters:
        ------------------------
        column : str
            Nombre de la columna
            Name of the column
        """
        if column:
            return self.data[column].var()
        return self.data[self._numeric_cols].var()
    
    def std(self, column: Optional[str] = None) -> Union[float, pd.Series]:
        """
        Desviación estándar / Standard deviation

        Parametros / Parameters:
        ------------------------
        column : str
            Nombre de la columna
            Name of the column
        
        """
        if column:
            return self.data[column].std()
        return self.data[self._numeric_cols].std()
    
    def skewness(self, column: Optional[str] = None) -> Union[float, pd.Series]:
        """
        Asimetría / Asymmetry
        
        Parametros / Parameters:
        ------------------------
        column : str
            Nombre de la columna
            Name of the column        
        """
        if column:
            return self.data[column].skew()
        return self.data[self._numeric_cols].skew()
    
    def kurtosis(self, column: Optional[str] = None) -> Union[float, pd.Series]:
        """
        Curtosis / Kurtosis
        
        Parametros / Parameters:
        ------------------------
        column : str
            Nombre de la columna
            Name of the column
        """
        if column:
            return self.data[column].kurtosis()
        return self.data[self._numeric_cols].kurtosis()
    
    def quantile(self, q: Union[float, List[float]], column: Optional[str] = None):
        """
        Cuantiles - Percentiles / Quantiles - Percentiles
        
        Parametros / Parameters:
        ------------------------
        q : float / List[float]
            Cuantiles a calcular
            Quantiles to calculate
        column : str
            Nombre de la columna
            Name of the column
        """
        if column:
            return self.data[column].quantile(q)
        return self.data[self._numeric_cols].quantile(q)
    
    def outliers(self, column: str, method: Literal['iqr', 'zscore'] = 'iqr', 
                 threshold: float = 1.5) -> pd.Series:
        """
        Detectar outliers en una columna / Detecting outliers in a column

        
        Parametros / Parameters:
        ------------------------
        column : str
            Nombre de la columna
            Name of the column
        method : str
            'iqr' o 'zscore'
        threshold : float
            1.5 para IQR, 3 para zscore típicamente
            1.5 for IQR, 3 for zscore typically
        """
        col_data = self.data[column]
        
        if method == 'iqr':
            q1 = col_data.quantile(0.25)
            q3 = col_data.quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr
            outliers = (col_data < lower_bound) | (col_data > upper_bound)
        else:  # zscore
            z_scores = np.abs((col_data - col_data.mean()) / col_data.std())
            outliers = z_scores > threshold
        
        return outliers
    
    # ============= MÉTODOS MULTIVARIADOS =============
    
    def correlation(self, method: Literal['pearson', 'spearman', 'kendall'] = 'pearson',
                    columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Matriz de correlación / Correlation matrix
        
        Parametros / Parameters:
        ------------------------
        method : str
            'pearson', 'spearman' o 'kendall'
        columns : list, optional
            Lista de columnas a incluir
            List of columns to include
        """
        data_subset = self.data[columns] if columns else self.data[self._numeric_cols]
        return data_subset.corr(method=method)
    
    def covariance(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Matriz de covarianza
        
        Parametros / Parameters:
        ------------------------
        columns: list, optional
            Lista de columnas a incluir
            List of columns to include
        """
        data_subset = self.data[columns] if columns else self.data[self._numeric_cols]
        return data_subset.cov()