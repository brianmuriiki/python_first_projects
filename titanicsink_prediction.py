{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOLfDl16dWLs47/fLuaY/1h",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/brianmuriiki/python_first_projects/blob/main/titanicsink_prediction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vqYGkqvTVPkr"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "PREDICTION OF TITANIC SINKING\n"
      ],
      "metadata": {
        "id": "09AYKFooVYwr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler, LabelEncoder\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, confusion_matrix, classification_report\n",
        "import joblib\n",
        "#Load Dataset FROM seaborn\n",
        "df = sns.load_dataset('titanic')\n",
        "\n",
        "print(\"First 5 rows:\")\n",
        "print(df.head())\n",
        "#  Explore Data\n",
        "print(\"\\nInfo:\")\n",
        "print(df.info())\n",
        "\n",
        "print(\"\\nMissing Values:\") #data cleaning\n",
        "print(df.isnull().sum())\n",
        "#Handle Missing Values\n",
        "\n",
        "# Fill 'age' with median\n",
        "df['age'].fillna(df['age'].median(), inplace=True)\n",
        "\n",
        "# Fill 'embarked' with most frequent value\n",
        "df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)\n",
        "\n",
        "# Drop 'deck' (too many missing values)\n",
        "df.drop('deck', axis=1, inplace=True)\n",
        " # Drop Irrelevant Columns\n",
        "df.drop(['alive', 'who', 'adult_male', 'class', 'embark_town'], axis=1, inplace=True)\n",
        "#Convert Categorical Data\n",
        "le = LabelEncoder()\n",
        "\n",
        "categorical_cols = ['sex', 'embarked']\n",
        "\n",
        "for col in categorical_cols:\n",
        "    df[col] = le.fit_transform(df[col])\n",
        "# Define Features & Target\n",
        "X = df.drop('survived', axis=1)\n",
        "y = df['survived']\n",
        "#Feature Scaling\n",
        "scaler = StandardScaler()\n",
        "X_scaled = scaler.fit_transform(X)\n",
        "#Train/Test Split\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X_scaled, y, test_size=0.2, random_state=42\n",
        ")\n",
        "#Train Model\n",
        "model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
        "model.fit(X_train, y_train)\n",
        "#Predictions\n",
        "y_pred = model.predict(X_test)\n",
        "#Evaluation\n",
        "print(\"\\nAccuracy:\", accuracy_score(y_test, y_pred))\n",
        "\n",
        "print(\"\\nConfusion Matrix:\")\n",
        "print(confusion_matrix(y_test, y_pred))\n",
        "\n",
        "print(\"\\nClassification Report:\")\n",
        "print(classification_report(y_test, y_pred))\n",
        "\n",
        "#Save Model\n",
        "joblib.dump(model, \"titanic_model.pkl\")\n",
        "print(\"\\nModel saved as titanic_model.pkl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sYDPHN1HViAO",
        "outputId": "b9ed9cba-1039-425f-9804-f71af6f62470"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First 5 rows:\n",
            "   survived  pclass     sex   age  sibsp  parch     fare embarked  class  \\\n",
            "0         0       3    male  22.0      1      0   7.2500        S  Third   \n",
            "1         1       1  female  38.0      1      0  71.2833        C  First   \n",
            "2         1       3  female  26.0      0      0   7.9250        S  Third   \n",
            "3         1       1  female  35.0      1      0  53.1000        S  First   \n",
            "4         0       3    male  35.0      0      0   8.0500        S  Third   \n",
            "\n",
            "     who  adult_male deck  embark_town alive  alone  \n",
            "0    man        True  NaN  Southampton    no  False  \n",
            "1  woman       False    C    Cherbourg   yes  False  \n",
            "2  woman       False  NaN  Southampton   yes   True  \n",
            "3  woman       False    C  Southampton   yes  False  \n",
            "4    man        True  NaN  Southampton    no   True  \n",
            "\n",
            "Info:\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 891 entries, 0 to 890\n",
            "Data columns (total 15 columns):\n",
            " #   Column       Non-Null Count  Dtype   \n",
            "---  ------       --------------  -----   \n",
            " 0   survived     891 non-null    int64   \n",
            " 1   pclass       891 non-null    int64   \n",
            " 2   sex          891 non-null    object  \n",
            " 3   age          714 non-null    float64 \n",
            " 4   sibsp        891 non-null    int64   \n",
            " 5   parch        891 non-null    int64   \n",
            " 6   fare         891 non-null    float64 \n",
            " 7   embarked     889 non-null    object  \n",
            " 8   class        891 non-null    category\n",
            " 9   who          891 non-null    object  \n",
            " 10  adult_male   891 non-null    bool    \n",
            " 11  deck         203 non-null    category\n",
            " 12  embark_town  889 non-null    object  \n",
            " 13  alive        891 non-null    object  \n",
            " 14  alone        891 non-null    bool    \n",
            "dtypes: bool(2), category(2), float64(2), int64(4), object(5)\n",
            "memory usage: 80.7+ KB\n",
            "None\n",
            "\n",
            "Missing Values:\n",
            "survived         0\n",
            "pclass           0\n",
            "sex              0\n",
            "age            177\n",
            "sibsp            0\n",
            "parch            0\n",
            "fare             0\n",
            "embarked         2\n",
            "class            0\n",
            "who              0\n",
            "adult_male       0\n",
            "deck           688\n",
            "embark_town      2\n",
            "alive            0\n",
            "alone            0\n",
            "dtype: int64\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipykernel_3598/875978241.py:24: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['age'].fillna(df['age'].median(), inplace=True)\n",
            "/tmp/ipykernel_3598/875978241.py:27: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
            "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
            "\n",
            "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
            "\n",
            "\n",
            "  df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Accuracy: 0.8268156424581006\n",
            "\n",
            "Confusion Matrix:\n",
            "[[91 14]\n",
            " [17 57]]\n",
            "\n",
            "Classification Report:\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.84      0.87      0.85       105\n",
            "           1       0.80      0.77      0.79        74\n",
            "\n",
            "    accuracy                           0.83       179\n",
            "   macro avg       0.82      0.82      0.82       179\n",
            "weighted avg       0.83      0.83      0.83       179\n",
            "\n",
            "\n",
            "Model saved as titanic_model.pkl\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "jnUjcCXHWI04"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}