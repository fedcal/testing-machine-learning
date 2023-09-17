from sklearn.datasets import load_diabetes
# regressione lineare
from sklearn.linear_model import LinearRegression
#metriche
from sklearn.metrics import mean_absolute_error
#validazione
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    dataset = load_diabetes()
    X = dataset['data']
    y = dataset['target']

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    # modello non addestrato
    model = LinearRegression()
    #addestramento
    model.fit(X,y)

    # predizioni
    p_train = model.predict(X_train)
    p_test = model.predict(X_test)
    # Misura di errore
    mae_train = mean_absolute_error(y_train,p_train)
    mae = mean_absolute_error(y_test,p_test)
    print(mae)
    print(mae_train)



