from flask import Flask
from flask import render_template
from forms import InputForm
import pickle
from datetime import date
from utils import assign_owner, assign_fuel, assign_seller, assign_trans


app = Flask(__name__)

app.config["SECRET_KEY"] = "5ad178c8e9a34b20f994fb55894f8455"  # for the forms and stuff. Best to keep it as an environment variable

model = pickle.load(open("random_forest_regression_model.pkl", "rb"))


@app.route("/", methods=["POST", "GET"])
def home():
    form = InputForm()
    if form.validate_on_submit():
        year = int(date.today().year - form.years_old.data)
        km = int(form.km_driven.data)
        owners = assign_owner(form.num_owners.data)
        fuel_Diesel, fuel_Electric, fuel_LPG, fuel_Petrol = assign_fuel(form.fuel_type.data)
        seller_individual, seller_trustmark = assign_seller(form.seller_type.data)
        trans_manual = assign_trans(form.trans_type.data)

        prediction = model.predict([[year, km, owners, fuel_Diesel, fuel_Electric, fuel_LPG, fuel_Petrol, seller_individual, seller_trustmark, trans_manual]])[0]
        prediction = round(prediction, 2)
        if prediction <= 0.0:
            prediction = "Sorry! You can't sell this car"
        return render_template("predict.html", prediction=prediction)
    return render_template("home.html", form=form)


if __name__ == "__main__":
    # app.run()  # debug turned off after deployment
    app.run(debug=True)  # running in debug mode
