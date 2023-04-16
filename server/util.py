import json
import pickle
import sklearn
import numpy as np
import sklearn
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    loc_index = __data_columns.index(location.lower())
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...Start")
    global __data_columns
    global  __locations
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loaing saved artifacts is done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 3))
    print(get_estimated_price('ambalipura', 1000, 2, 2))
    print(get_estimated_price('ambedkar nagar', 1000, 2, 3))