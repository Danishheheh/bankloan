{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "33f52793-faf9-40e6-9567-350800392b3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "# Initialize Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load trained fraud detection model\n",
    "model = joblib.load('fraud_model.pkl')\n",
    "\n",
    "def encode_employment_status(status):\n",
    "    \"\"\"Encode employment status as numerical values\"\"\"\n",
    "    encoding = {\"employed\": 0, \"self-employed\": 1, \"unemployed\": 2}\n",
    "    return encoding.get(status, -1)  # Default to -1 if unknown\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('home.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    try:\n",
    "        # Extract input features\n",
    "        income = float(request.form['income'])\n",
    "        loan_amount = float(request.form['loan_amount'])\n",
    "        credit_score = float(request.form['credit_score'])\n",
    "        employment_status = encode_employment_status(request.form['employment_status'])\n",
    "        previous_loans = float(request.form['previous_loans'])\n",
    "\n",
    "        if employment_status == -1:\n",
    "            return render_template('result.html', prediction=\"Invalid employment status.\")\n",
    "\n",
    "        features = [income, loan_amount, credit_score, employment_status, previous_loans]\n",
    "    except ValueError:\n",
    "        return render_template('result.html', prediction=\"Invalid input. Please enter numeric values.\")\n",
    "\n",
    "    # Make prediction\n",
    "    prediction = model.predict([features])[0]\n",
    "\n",
    "    # Map prediction to readable output\n",
    "    result = \"Fraudulent\" if prediction == 1 else \"Legitimate\"\n",
    "    \n",
    "    return render_template('result.html', prediction=result)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c670bb7b-2dfb-4fb4-a05f-d2c83a1b8700",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
