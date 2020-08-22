from sklearn.base import BaseEstimator, TransformerMixin
# All sklearn Transforms must have the `transform` and `fit` methods
class StudentCategory(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        def classificaFaltas(elem):
            if elem <= 3:
                return 1
            elif elem <= 6:
                return 0
            else:
                return -1
        
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe com as colunas FALTAS e TEM_REPROVACAO categorizadas
        data["FALTAS"] = data.iloc[:,10].apply(classificaFaltas)
        data["TEM_REPROVACAO"] = data.iloc[:,0:4].apply(lambda row: bool(row[0] or row[1] or row[2] or row[3]), axis=1)
        
        return data

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
