from flask import flash,render_template,Flask,request
import requests




app = Flask(__name__)


def GetCurrencies():
    url = "http://data.fixer.io/api/latest?access_key=aff91f0f6bce8f2fd8335b085752edd6"

    result = requests.get(url).json()

    return result["rates"]






@app.route("/",methods = ["GET","POST"])
def MainPage():
    if request.method == "GET":
        return render_template("mainPage.html")

    else :
        formCurrency1 = request.form.get("firstCurrency")
        formCurrency2 = request.form.get("secondCurrency")
        amount = request.form.get("amount")
        result = (GetCurrencies()[formCurrency2] / GetCurrencies()[formCurrency1]) * float(amount)


        resultDict = {"result":result,"amount":amount,"curr1":formCurrency1,"curr2":formCurrency2}


        app.logger.info(amount)

        return render_template("mainPage.html",result = resultDict)





if __name__ == "__main__":
    app.run(debug=True)