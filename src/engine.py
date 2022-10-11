
import pandas as pd
import numpy as np
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from datetime import datetime
from copy import deepcopy
from sklearn.cluster import MiniBatchKMeans, KMeans
import gpxpy.geo
from datetime import datetime, timedelta
from joblib import dump, load

from ML_Pipeline.data_prep_basic import data_prep_basic
from ML_Pipeline.data_prep_advanced import data_prep_advanced
from ML_Pipeline.data_prep_geospatial import data_prep_geospatial
from ML_Pipeline.model_training import model_training
from ML_Pipeline.prediction_pipeline import prediction_pipeline


geolocator = Nominatim(user_agent="OLABikes")

df = pd.read_csv('../input/raw_data.csv', low_memory=False, compression='gzip')


df = data_prep_basic(df)


df = data_prep_advanced(df, '../input/clean_data.csv')


df = pd.read_csv('../input/clean_data.csv', compression='gzip')


df = data_prep_geospatial(
    df, '../output/pickup_cluster_model_1.joblib', '../input/Data_prepared.csv')


df = pd.read_csv('../input/Data_prepared.csv', compression='gzip')


model_training(df, '../output/prediction_model_without_lag.joblib','../output/prediction_model_with_lag.joblib')


prediction_pipeline(
    cleaned_data_path='E:\PROJECTpro\PROJECTS\project_3_demand_prediction\Project3_OLABikes\modular_code\input\cleaned_test_booking_data.csv',
    cluster_model_path='E:\PROJECTpro\PROJECTS\project_3_demand_prediction\Project3_OLABikes\modular_code\output\pickup_cluster_model_1.joblib',
    predict_without_lag_path='E:\PROJECTpro\PROJECTS\project_3_demand_prediction\Project3_OLABikes\modular_code\output\prediction_model_without_lag_1.joblib',
    predict_with_lag_path='E:\PROJECTpro\PROJECTS\project_3_demand_prediction\Project3_OLABikes\modular_code\output\prediction_model_with_lag.joblib',
    data_with_lag_path='E:\PROJECTpro\PROJECTS\project_3_demand_prediction\Project3_OLABikes\modular_code\output\data_with_lag.csv',
    data_without_lag_path='E:\PROJECTpro\PROJECTS\project_3_demand_prediction\Project3_OLABikes\modular_code\output\data_without_lag.csv'
)