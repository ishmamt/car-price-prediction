# Car price prediction
This project was made to learn about the complete life cycle of a data science project. Specially:
- EDA
- Feature engineering & Feature selection
- Model building & tuning hyperparameters
- Deployment

## Getting started
### Prerequisites
All the dependancies are listed in <a href="https://github.com/ishmamt/car-price-prediction/blob/master/requirements.txt">requirements</a>.

### Installation
To install, first create a virtual environment and activate it.
```
//windows
python3 -m venv env_name
source env_name/bin/activate
```
If you have anaconda installed, create an environment using that.
```
conda create --name env_name python=[python version]  // 3.6 and over
```
**"env_name"** should contain the name of the environment. Then install all the packadges from the <a href="https://github.com/ishmamt/car-price-prediction/blob/master/requirements.txt">requirements</a>.
```
pip install -r requirements.txt
```

### Running the app
Run this command on cmd
```
python app.py
```
It will run it on a local server. You can access it from any browser.

## Deployment
The app is deployed using heroku.

### Acknowledgements
Followed the end to end <a href="https://youtu.be/p_tpQSY1aTs">implementation tutorial</a> by <a href="https://www.youtube.com/user/krishnaik06">Krish Naik</a>.
