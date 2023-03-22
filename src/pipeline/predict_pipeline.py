import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        Sl_No: int,
        Filler_Material: str,
        Current: float,
        Travel_speed: float,
        Chromium_equivalent: float,
        thickness_of_welding_specimen: float,
        Feed: float,
        Result_of_visual_inspection,
        Percentage_Elongation: float

        ):

        self.Sl_No = Sl_No

        self.Filler_Material = Filler_Material

        self.Current = Current

        self.Travel_speed  = Travel_speed

        self.Chromium_equivalent = Chromium_equivalent

        self.thickness_of_welding_specimen = thickness_of_welding_specimen

        self.Feed = Feed

        self.Result_of_visual_inspection = Result_of_visual_inspection

        self.Percentage_Elongation = Percentage_Elongation

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Sl.No": [self.Sl_No],
                "Filler Material": [self.Filler_Material],
                "Current(A)": [self.Current],
                "Travel speed (cm/min)": [self.Travel_speed],
                "Chromium equivalent": [self.Chromium_equivalent],
                "thickness of welding specimen(mm)": [self.thickness_of_welding_specimen],
                "Feed (m/min)": [self.Feed],
                "Result of visual inspection": [self.Result_of_visual_inspection],
                "Percentage Elongation": [self.Percentage_Elongation]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)