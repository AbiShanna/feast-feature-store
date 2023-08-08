# Feature definition file

from feast import Entity, FeatureView, FileSource, ValueType, Field
from feast.types import Int64, Float64
from datetime import timedelta

## Patient entity
patient = Entity(name="patient_id", 
                 value_type = ValueType.INT64,
                 description = "Patient identifier")

## File Sources
predictors_source = FileSource(path = r"data/predictors_df.parquet",
                          event_timestamp_column = "event_timestamp")
target_source = FileSource(path = r"data/target_df.parquet",
                      event_timestamp_column = "event_timestamp")

## Feature Views

predictors_fv = FeatureView(
    name = "predictors_df_feature_view",
    ttl = timedelta(days=2),
    entities = ["patient_id"],
    schema = [
        Field(name = "Pregnancies", dtype = Int64),
        Field(name = "Glucose", dtype = Int64),
        Field(name = "BloodPressure", dtype = Int64),
        Field(name = "SkinThickness", dtype = Int64),
        Field(name = "Insulin", dtype = Int64),
        Field(name = "BMI", dtype = Float64),
        Field(name = "DiabetesPedigreeFunction", dtype = Float64),
        Field(name = "Age", dtype = Int64),
    ],
    source = predictors_source,
    online = True,
    tags = {},
)

target_fv = FeatureView(
    name = "target_df_feature_view",
    ttl = timedelta(days=2),
    entities = ["patient_id"],
    schema = [
        Field(name = "Outcome", dtype = Int64),
    ],
    source = target_source,
    online = True,
    tags = {},
)



















