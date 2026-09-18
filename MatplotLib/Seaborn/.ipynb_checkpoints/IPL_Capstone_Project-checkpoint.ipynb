{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "20ddbce6-8ca0-4846-8903-f3c42a0f07af",
   "metadata": {},
   "source": [
    "### IPL 2022 Capstone Project"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "894aafbc-4081-4584-9f05-8f1a9d6ca082",
   "metadata": {},
   "source": [
    "**The Indian Premier League (IPL) is a professional T20 cricket league in India, featuring franchises representing cities. This project explores IPL 2022 match-level data to derive meaningful insights and understand match outcomes, player performances, and team dynamics.**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "912338f7-2478-4b1a-8421-b8305fbf8ecc",
   "metadata": {},
   "source": [
    "**These are some of the important columns that we'll focus on for meaningful insights in this project.**\n",
    "\n",
    "**column names: Variable Type**\n",
    "* date : string  \r\n",
    "* venue : string  \r\n",
    "* stage : string  \r\n",
    "* team1 : string  \r\n",
    "* team2 : string  \r\n",
    "* toss_winner : string  \r\n",
    "* toss_decision : string  \r\n",
    "* first_ings_score : integer  \r\n",
    "* second_ings_score : integer  \r\n",
    "* match_winner : string  \r\n",
    "* won_by : string  \r\n",
    "* margin : integer  \r\n",
    "* player_of_the_match : string  \r\n",
    "* top_scorer : string  \r\n",
    "* highscore : integer  \r\n",
    "* best_bowling : string  \r\n",
    "* best_bowling_fgure : string  \r\n",
    "gure : string  \r\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "460f0d67-bb6a-41b6-bba7-899b6d324bd7",
   "metadata": {},
   "source": [
    "### Loading the Libraries and Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9edc7567-369a-4405-a80a-846291278fe2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>date</th>\n",
       "      <th>venue</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>stage</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>first_ings_score</th>\n",
       "      <th>first_ings_wkts</th>\n",
       "      <th>second_ings_score</th>\n",
       "      <th>second_ings_wkts</th>\n",
       "      <th>match_winner</th>\n",
       "      <th>won_by</th>\n",
       "      <th>margin</th>\n",
       "      <th>player_of_the_match</th>\n",
       "      <th>top_scorer</th>\n",
       "      <th>highscore</th>\n",
       "      <th>best_bowling</th>\n",
       "      <th>best_bowling_figure</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>March 26,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Group</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Field</td>\n",
       "      <td>131</td>\n",
       "      <td>5</td>\n",
       "      <td>133</td>\n",
       "      <td>4</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>6</td>\n",
       "      <td>Umesh Yadav</td>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>50</td>\n",
       "      <td>Dwayne Bravo</td>\n",
       "      <td>3--20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Brabourne Stadium, Mumbai</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>Group</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Field</td>\n",
       "      <td>177</td>\n",
       "      <td>5</td>\n",
       "      <td>179</td>\n",
       "      <td>6</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>4</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>Ishan Kishan</td>\n",
       "      <td>81</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>3--18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Dr DY Patil Sports Academy, Mumbai</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Group</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Field</td>\n",
       "      <td>205</td>\n",
       "      <td>2</td>\n",
       "      <td>208</td>\n",
       "      <td>5</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Odean Smith</td>\n",
       "      <td>Faf du Plessis</td>\n",
       "      <td>88</td>\n",
       "      <td>Mohammed Siraj</td>\n",
       "      <td>2--59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>March 28,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Lucknow</td>\n",
       "      <td>Group</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Field</td>\n",
       "      <td>158</td>\n",
       "      <td>6</td>\n",
       "      <td>161</td>\n",
       "      <td>5</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>Deepak Hooda</td>\n",
       "      <td>55</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>3--25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>March 29,2022</td>\n",
       "      <td>Maharashtra Cricket Association Stadium,Pune</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Group</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Field</td>\n",
       "      <td>210</td>\n",
       "      <td>6</td>\n",
       "      <td>149</td>\n",
       "      <td>7</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Runs</td>\n",
       "      <td>61</td>\n",
       "      <td>Sanju Samson</td>\n",
       "      <td>Aiden Markram</td>\n",
       "      <td>57</td>\n",
       "      <td>Yuzvendra Chahal</td>\n",
       "      <td>3--22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_id           date                                         venue  \\\n",
       "0         1  March 26,2022                      Wankhede Stadium, Mumbai   \n",
       "1         2  March 27,2022                     Brabourne Stadium, Mumbai   \n",
       "2         3  March 27,2022            Dr DY Patil Sports Academy, Mumbai   \n",
       "3         4  March 28,2022                      Wankhede Stadium, Mumbai   \n",
       "4         5  March 29,2022  Maharashtra Cricket Association Stadium,Pune   \n",
       "\n",
       "       team1      team2  stage toss_winner toss_decision  first_ings_score  \\\n",
       "0    Chennai    Kolkata  Group     Kolkata         Field               131   \n",
       "1      Delhi     Mumbai  Group       Delhi         Field               177   \n",
       "2   Banglore     Punjab  Group      Punjab         Field               205   \n",
       "3    Gujarat    Lucknow  Group     Gujarat         Field               158   \n",
       "4  Hyderabad  Rajasthan  Group   Hyderabad         Field               210   \n",
       "\n",
       "   first_ings_wkts  second_ings_score  second_ings_wkts match_winner   won_by  \\\n",
       "0                5                133                 4      Kolkata  Wickets   \n",
       "1                5                179                 6        Delhi  Wickets   \n",
       "2                2                208                 5       Punjab  Wickets   \n",
       "3                6                161                 5      Gujarat  Wickets   \n",
       "4                6                149                 7    Rajasthan     Runs   \n",
       "\n",
       "   margin player_of_the_match      top_scorer  highscore      best_bowling  \\\n",
       "0       6         Umesh Yadav        MS Dhoni         50      Dwayne Bravo   \n",
       "1       4       Kuldeep Yadav    Ishan Kishan         81     Kuldeep Yadav   \n",
       "2       5         Odean Smith  Faf du Plessis         88    Mohammed Siraj   \n",
       "3       5      Mohammed Shami    Deepak Hooda         55    Mohammed Shami   \n",
       "4      61        Sanju Samson   Aiden Markram         57  Yuzvendra Chahal   \n",
       "\n",
       "  best_bowling_figure  \n",
       "0               3--20  \n",
       "1               3--18  \n",
       "2               2--59  \n",
       "3               3--25  \n",
       "4               3--22  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np \n",
    "import pandas as pd \n",
    "import seaborn as sns \n",
    "import matplotlib.pyplot as plt \n",
    "import warnings \n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "df = pd.read_csv( 'IPL.csv')\n",
    "\n",
    "df.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "761027b0-490c-47d7-bae8-3b73e95d36e9",
   "metadata": {},
   "source": [
    "### Basic Information"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b6d0c558-47b3-4d36-bb38-311235c2c784",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 74 entries, 0 to 73\n",
      "Data columns (total 20 columns):\n",
      " #   Column               Non-Null Count  Dtype \n",
      "---  ------               --------------  ----- \n",
      " 0   match_id             74 non-null     int64 \n",
      " 1   date                 74 non-null     object\n",
      " 2   venue                74 non-null     object\n",
      " 3   team1                74 non-null     object\n",
      " 4   team2                74 non-null     object\n",
      " 5   stage                74 non-null     object\n",
      " 6   toss_winner          74 non-null     object\n",
      " 7   toss_decision        74 non-null     object\n",
      " 8   first_ings_score     74 non-null     int64 \n",
      " 9   first_ings_wkts      74 non-null     int64 \n",
      " 10  second_ings_score    74 non-null     int64 \n",
      " 11  second_ings_wkts     74 non-null     int64 \n",
      " 12  match_winner         74 non-null     object\n",
      " 13  won_by               74 non-null     object\n",
      " 14  margin               74 non-null     int64 \n",
      " 15  player_of_the_match  74 non-null     object\n",
      " 16  top_scorer           74 non-null     object\n",
      " 17  highscore            74 non-null     int64 \n",
      " 18  best_bowling         74 non-null     object\n",
      " 19  best_bowling_figure  74 non-null     object\n",
      "dtypes: int64(7), object(13)\n",
      "memory usage: 11.7+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d717c591-238a-43eb-88f2-cf2ec966edb0",
   "metadata": {},
   "source": [
    "Check the size of rows and columns of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0eb3785b-8ce8-4205-b381-1d868f0a8983",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "your rows are 74 and your columns are 20\n"
     ]
    }
   ],
   "source": [
    "print(f\"your rows are {df.shape[0]} and your columns are {df.shape[1]}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71728207-924f-4024-a0ad-3e61591d5d0a",
   "metadata": {},
   "source": [
    "Now let's see how many columns have null values in total."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "b64f2f03-5c60-4654-b0e1-9ddf8542c218",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "match_id               0\n",
       "date                   0\n",
       "venue                  0\n",
       "team1                  0\n",
       "team2                  0\n",
       "stage                  0\n",
       "toss_winner            0\n",
       "toss_decision          0\n",
       "first_ings_score       0\n",
       "first_ings_wkts        0\n",
       "second_ings_score      0\n",
       "second_ings_wkts       0\n",
       "match_winner           0\n",
       "won_by                 0\n",
       "margin                 0\n",
       "player_of_the_match    0\n",
       "top_scorer             0\n",
       "highscore              0\n",
       "best_bowling           0\n",
       "best_bowling_figure    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "552e17c7-7dc8-4caf-a583-0c06e7415fa1",
   "metadata": {},
   "source": [
    "**Now, Here comes some Basic Questions**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80396e96-8356-4dba-9f1b-7907d333d750",
   "metadata": {},
   "source": [
    "1. Which team won the most matches?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "53ff2191-7738-415f-a83c-e22c4ab878b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "match_winner\n",
       "Gujarat      12\n",
       "Rajasthan    10\n",
       "Banglore      9\n",
       "Lucknow       9\n",
       "Delhi         7\n",
       "Punjab        7\n",
       "Kolkata       6\n",
       "Hyderabad     6\n",
       "Chennai       4\n",
       "Mumbai        4\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "match_wins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "af24080f-9531-426f-aa06-7165db3817f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Most match win by team ')"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "match_wins = df['match_winner'].value_counts()\n",
    "sns.barplot(y = match_wins.index,x = match_wins.values,palette='viridis')\n",
    "plt.title(\"Most match win by team \")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b011bdbf-b57f-4cd2-99fc-ae43109b0f59",
   "metadata": {},
   "source": [
    "2. Toss Decision Trends"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "9e73a24d-cf5f-4c6c-92cb-cde758948ab9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Toss Decision Trends ')"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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11h+6ap8n+Vuv/121arlOfl+zTXX6OOPP9Zjjz2mlStX6vDhw+fhLAHvI8wAXrZnzx65XC45HA6P9oYNG6pWrVruSwDXX3+93n//fZWWlmrIkCFq3LixWrZs6XG/Q2pqqp555hllZ2crMTFRYWFh6t69u9atW3fOde7YsUNOp1P16tWTJP3666/617/+JT8/P4/l6quvliT99ttvkqTdu3crMjJSNWpU7tdNVc6l/LU61dNNkZGRFS6nBAUFKSAgwKPN6XTqyJEjlar1dE6u49dff5UkjRkzpsLrlpSUJOn/f93KhYWFVahPkjuIlJ+Ty+XyGFerVq0K2z777LMaO3as3n//fXXt2lX16tVT//799f3335/LaQJeR5gBvCwsLEy//vprhZmPgoIClZaWqn79+u62m2++WcuWLVNRUZFWrlypxo0ba/Dgwe5HhWvVqqVRo0bpyy+/1N69e/XGG28oNzdXvXr10qFDh6pc4y+//KL169fr2muvdf9vv379+urZs6fWrl17ymX48OGSfn/6Z9euXSorK6vUMatyLuV/vPPy8ir07dq1y+O1vBBODqjlx09NTT3t69a2bdtKHaP8nPPz8z3aS0tLK4S32rVra9KkSfr222+Vn5+v2bNnKzs7u8LsFGAbwgzgZd27d9eBAwf0/vvve7S/+uqr7v6TOZ1OdenSRU8//bQkacOGDRXG1K1bV7feeqseeOAB7d27t8ofLHf48GHdc889Ki0tVUpKiru9T58+2rx5sy6//HLFxsZWWCIjIyVJiYmJOnLkiObNm1el41fmXOLj4xUYGKjXX3/do/3nn3/W8uXLT/laXkjNmzdXTEyMNm3adMrXLDY2VsHBwZXaZ0JCgiRpwYIFHu1vv/12hafKThQeHq5hw4Zp0KBB2rZt2zmFXcDbeJoJ8LIhQ4bo+eef19ChQ7V9+3a1atVK//nPf5Senq7evXvrhhtukCRNmDBBP//8s7p3767GjRtr3759mjlzpvz8/NSlSxdJUt++fdWyZUvFxsaqQYMG2rFjh2bMmKEmTZp4PMVzOjt37lR2drbKyspUVFTk/tC8HTt2aNq0aerZs6d77BNPPKGlS5eqU6dOevjhh9W8eXMdOXJE27dv17///W+9+OKLaty4sQYNGqS5c+fqvvvu07Zt29S1a1eVlZVpzZo1atGihe64445T1lKV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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = df['toss_decision'],palette='rainbow')\n",
    "plt.title(\"Toss Decision Trends \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb31ae50-6ec0-4c4e-8575-435f779ca116",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a530b3c-5d25-4485-a3ef-93401a6da03b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "07c65194-6e99-4be5-9b53-caa890f0864b",
   "metadata": {},
   "source": [
    "3. Toss Winner vs Match Winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a33d90bb-1af6-4fe6-a065-3f51c97439aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "1f95b051-88f8-4133-8794-9671ed47057b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "48.65"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count = df[df['toss_winner'] == df['match_winner']]['match_id'].count()\n",
    "percentage = (count *100)/df.shape[0]\n",
    "percentage.round(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf63d31e-dcbe-4908-9499-b74d2c9338e7",
   "metadata": {},
   "source": [
    "4. How do teams win? (Runs vs Wickets)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "fe487b4f-4266-4ad1-89b7-d03a0efd9d21",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Won by')"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x = df['won_by'])\n",
    "plt.title(\"Won by\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bce756ef-99a1-4251-b55f-a1bb47f77d1c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "4a5635a5-a7b3-4527-8580-114462ec6b20",
   "metadata": {},
   "source": [
    "###  Key Player Performances"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03366105-9157-4d50-873c-ee79cb3b85b3",
   "metadata": {},
   "source": [
    "1 Most \"Player of the Match\" Awards"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "034ad7ce-f010-4ab0-b490-5b1f90c11834",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player_of_the_match\n",
       "Kuldeep Yadav      4\n",
       "Jos Buttler        3\n",
       "Umesh Yadav        2\n",
       "Quinton de Kock    2\n",
       "David Miller       2\n",
       "Umran Malik        2\n",
       "K L Rahul          2\n",
       "Rahul Tripathi     2\n",
       "Hardik Pandya      2\n",
       "Jasprit Bumrah     2\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count = df['player_of_the_match'].value_counts().head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "ce562d96-00c2-4fc7-91dc-f73a431029e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Top 10 plauers with man of the match')"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = count.values , y = count.index,palette='mako')\n",
    "plt.title(\"Top 10 plauers with man of the match\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6fb8509a-85ac-4193-9876-8a6902461f7b",
   "metadata": {},
   "source": [
    "2 Top Scorers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "f6f9a798-c26c-46b6-9d98-4c4651c8232f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>date</th>\n",
       "      <th>venue</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>stage</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>first_ings_score</th>\n",
       "      <th>first_ings_wkts</th>\n",
       "      <th>second_ings_score</th>\n",
       "      <th>second_ings_wkts</th>\n",
       "      <th>match_winner</th>\n",
       "      <th>won_by</th>\n",
       "      <th>margin</th>\n",
       "      <th>player_of_the_match</th>\n",
       "      <th>top_scorer</th>\n",
       "      <th>highscore</th>\n",
       "      <th>best_bowling</th>\n",
       "      <th>best_bowling_figure</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>March 26,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Group</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Field</td>\n",
       "      <td>131</td>\n",
       "      <td>5</td>\n",
       "      <td>133</td>\n",
       "      <td>4</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>6</td>\n",
       "      <td>Umesh Yadav</td>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>50</td>\n",
       "      <td>Dwayne Bravo</td>\n",
       "      <td>3--20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Brabourne Stadium, Mumbai</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>Group</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Field</td>\n",
       "      <td>177</td>\n",
       "      <td>5</td>\n",
       "      <td>179</td>\n",
       "      <td>6</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>4</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>Ishan Kishan</td>\n",
       "      <td>81</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>3--18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Dr DY Patil Sports Academy, Mumbai</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Group</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Field</td>\n",
       "      <td>205</td>\n",
       "      <td>2</td>\n",
       "      <td>208</td>\n",
       "      <td>5</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Odean Smith</td>\n",
       "      <td>Faf du Plessis</td>\n",
       "      <td>88</td>\n",
       "      <td>Mohammed Siraj</td>\n",
       "      <td>2--59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>March 28,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Lucknow</td>\n",
       "      <td>Group</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Field</td>\n",
       "      <td>158</td>\n",
       "      <td>6</td>\n",
       "      <td>161</td>\n",
       "      <td>5</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>Deepak Hooda</td>\n",
       "      <td>55</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>3--25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>March 29,2022</td>\n",
       "      <td>Maharashtra Cricket Association Stadium,Pune</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Group</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Field</td>\n",
       "      <td>210</td>\n",
       "      <td>6</td>\n",
       "      <td>149</td>\n",
       "      <td>7</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Runs</td>\n",
       "      <td>61</td>\n",
       "      <td>Sanju Samson</td>\n",
       "      <td>Aiden Markram</td>\n",
       "      <td>57</td>\n",
       "      <td>Yuzvendra Chahal</td>\n",
       "      <td>3--22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_id           date                                         venue  \\\n",
       "0         1  March 26,2022                      Wankhede Stadium, Mumbai   \n",
       "1         2  March 27,2022                     Brabourne Stadium, Mumbai   \n",
       "2         3  March 27,2022            Dr DY Patil Sports Academy, Mumbai   \n",
       "3         4  March 28,2022                      Wankhede Stadium, Mumbai   \n",
       "4         5  March 29,2022  Maharashtra Cricket Association Stadium,Pune   \n",
       "\n",
       "       team1      team2  stage toss_winner toss_decision  first_ings_score  \\\n",
       "0    Chennai    Kolkata  Group     Kolkata         Field               131   \n",
       "1      Delhi     Mumbai  Group       Delhi         Field               177   \n",
       "2   Banglore     Punjab  Group      Punjab         Field               205   \n",
       "3    Gujarat    Lucknow  Group     Gujarat         Field               158   \n",
       "4  Hyderabad  Rajasthan  Group   Hyderabad         Field               210   \n",
       "\n",
       "   first_ings_wkts  second_ings_score  second_ings_wkts match_winner   won_by  \\\n",
       "0                5                133                 4      Kolkata  Wickets   \n",
       "1                5                179                 6        Delhi  Wickets   \n",
       "2                2                208                 5       Punjab  Wickets   \n",
       "3                6                161                 5      Gujarat  Wickets   \n",
       "4                6                149                 7    Rajasthan     Runs   \n",
       "\n",
       "   margin player_of_the_match      top_scorer  highscore      best_bowling  \\\n",
       "0       6         Umesh Yadav        MS Dhoni         50      Dwayne Bravo   \n",
       "1       4       Kuldeep Yadav    Ishan Kishan         81     Kuldeep Yadav   \n",
       "2       5         Odean Smith  Faf du Plessis         88    Mohammed Siraj   \n",
       "3       5      Mohammed Shami    Deepak Hooda         55    Mohammed Shami   \n",
       "4      61        Sanju Samson   Aiden Markram         57  Yuzvendra Chahal   \n",
       "\n",
       "  best_bowling_figure  \n",
       "0               3--20  \n",
       "1               3--18  \n",
       "2               2--59  \n",
       "3               3--25  \n",
       "4               3--22  "
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "8a0ef222-ab5e-462a-ba65-f01f25ced131",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "top_scorer\n",
       "Jos Buttler        651\n",
       "Quinton de Kock    377\n",
       "Name: highscore, dtype: int64"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "high = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2)\n",
    "high"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "50fc58de-b716-4f4d-aba1-82e9c486c427",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='top_scorer'>"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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Cg0NdV7hfOaZZ7R27Vq1bdtWc+fOdW6/lg0bNmjMmDGaNGmS8vLy9Morr2jVqlWaP3++y3EpKSm67777lJubq7Fjx17zXOXl5SotLXV5AACAxsvb0wM0JGfOnNHSpUu1atUqDR06VJK0fPlyZWZmasWKFfr973+vw4cP6+abb1ZiYqKkK+9ZvJ5169YpODjY+RyRkZFat26dvLxq1vq+vr4KCwuTw+FQRESEy75mzZopJCSk0vYfmj9/vmbOnKlHH31UkhQbG6vnn39e06dPV0pKivO43/zmN1VG5FULFixQampqjeYGAAANH1cm3bB//35dvHhRt912m3Obj4+PbrnlFuXn50uSnnzySa1evVq9evXS9OnTtX379uue9/bbb1dOTo5ycnK0Y8cO3X333Ro6dKgOHTpUZ9/LD+3atUtz585VcHCw8/HEE0+oqKhIZ8+edR53NZCrM2vWLJWUlDgfhYWFdTk6AADwMK5MusEYI0mV3ntojHFuuxqBH374oTZu3Kg777xTTz31lP793/+9yvMGBQUpLi7O+eeEhASFhYVp+fLlmjdvnvMK5dXnl2r3AzAVFRVKTU3Vgw8+WGmfv7+/y5zX4+fnJz8/v1qbDQAA1G9cmXRDXFycfH19tXXrVue2ixcv6rPPPlOXLl2c28LDw/XYY4/pjTfe0IsvvqhXX33VredxOBzy8vLSuXPnnOeT5PKex5ycHJev8fX11eXLlyudq6rtP9S7d2/t27dPcXFxlR41fakdAAA0TVyZdENQUJCefPJJ/f73v1fLli3Vrl07LVq0SGfPntW4ceMkSbNnz1ZCQoK6deum8vJyrVu3ziU0r6W8vFzHjx+XdOXT4Onp6SorK9OvfvUrSVciNjo6WnPmzNG8efNUUFCgF154weUc7du3V1lZmbKyshQfH6/AwEAFBgaqffv22rJlix566CH5+fld88NAs2fP1vDhwxUdHa1f//rX8vLy0p49e5Sbm8untgEAQLW47FQDFRUV8va+0t1paWkaMWKEfvvb36p37976+uuvtWHDBrVo0ULSlSuBs2bNUs+ePTVgwAA1a9ZMq1evrvb869evV2RkpCIjI3Xrrbdq586d+q//+i8lJydLuvK+zLfeektffvml4uPjtXDhwkqR169fP40fP16jRo1SeHi4Fi1aJEmaO3euDh48qJtuusl5hfPH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fmD16tXavXu3FixYUGkf6yTdeuutev3117VhwwYtX75cx48fV79+/fT999+zPpK++eYbLV26VB07dtSGDRs0fvx4TZo0Sa+//rok/g65w9vTA6DxcjgcLn82xlTa1pTZrE9jXMOnn35ae/bs0datWyvta8pr9Itf/EI5OTk6deqU1qxZo0cffVTZ2dnO/U15bSSpsLBQkydPVkZGhvz9/as8rimv09ChQ53/3KNHDyUlJemmm27SX/7yF/Xt21dS016fiooKJSYm6t/+7d8kSTfffLO++OILLV26VI888ojzuKa8RjXFlUnUulatWqlZs2aV/l/ZiRMnKv0/vKbo6qcpq1ufiIgIXbhwQSdPnqzymMZg4sSJev/997Vp0ya1bdvWuZ01knx9fRUXF6fExEQtWLBA8fHxWrJkCWvz/3bt2qUTJ04oISFB3t7e8vb2VnZ2tv74xz/K29vb+X029XX6oaCgIPXo0UMFBQX8PZIUGRmprl27umzr0qWLDh8+LIn/DrmDmESt8/X1VUJCgjIzM122Z2Zmql+/fh6aqv7o0KGDIiIiXNbnwoULys7Odq5PQkKCfHx8XI4pKirS3r17G8UaGmP09NNPa+3atfqf//kfdejQwWU/a1SZMUbl5eWszf+78847lZubq5ycHOcjMTFRo0ePVk5OjmJjY1mnHykvL1d+fr4iIyP5eyTptttuq3RLsq+++koxMTGS+O+QW37+z/ygKbh6a6AVK1aYvLw8M2XKFBMUFGQOHjzo6dF+FqdPnzaff/65+fzzz40ks3jxYvP55587b42UlpZmwsLCzNq1a01ubq55+OGHr3m7ibZt25qNGzea3bt3mzvuuKPR3G7iySefNGFhYWbz5s0uty05e/as85imvEazZs0yW7ZsMQcOHDB79uwxf/jDH4yXl5fJyMgwxjTttanODz/NbQzrNG3aNLN582bzzTffmE8++cQMHz7chISEOP873NTX59NPPzXe3t5m/vz5pqCgwLz55psmMDDQvPHGG85jmvoa1RQxiTrzpz/9ycTExBhfX1/Tu3dv521fmoJNmzYZSZUejz76qDHmyi0nUlJSTEREhPHz8zMDBgwwubm5Luc4d+6cefrpp03Lli1NQECAGT58uDl8+LAHvpvad621kWRWrlzpPKYpr9HYsWOd/+6Eh4ebO++80xmSxjTttanOj2Oyqa/T1Xsi+vj4mKioKPPggw+aL774wrm/qa+PMcZ88MEHpnv37sbPz8907tzZvPrqqy77WaOacRhjjGeuiQIAAKCh4z2TAAAAsEZMAgAAwBoxCQAAAGvEJAAAAKwRkwAAALBGTAIAAMAaMQkAAABrxCQAAACsEZMAAACwRkwCAADAGjEJAAAAa8QkAAAArP0f7+dYiT7gK/UAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "high.plot(kind = 'barh')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e267058-ce05-4bc6-9a7f-2265ab4f4f29",
   "metadata": {},
   "source": [
    "10 Best Bowling Figures"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "556b4c9f-56f3-4496-b6c5-b274ab41c318",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>date</th>\n",
       "      <th>venue</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>stage</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>first_ings_score</th>\n",
       "      <th>first_ings_wkts</th>\n",
       "      <th>second_ings_score</th>\n",
       "      <th>second_ings_wkts</th>\n",
       "      <th>match_winner</th>\n",
       "      <th>won_by</th>\n",
       "      <th>margin</th>\n",
       "      <th>player_of_the_match</th>\n",
       "      <th>top_scorer</th>\n",
       "      <th>highscore</th>\n",
       "      <th>best_bowling</th>\n",
       "      <th>best_bowling_figure</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>March 26,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Group</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Field</td>\n",
       "      <td>131</td>\n",
       "      <td>5</td>\n",
       "      <td>133</td>\n",
       "      <td>4</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>6</td>\n",
       "      <td>Umesh Yadav</td>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>50</td>\n",
       "      <td>Dwayne Bravo</td>\n",
       "      <td>3--20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Brabourne Stadium, Mumbai</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>Group</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Field</td>\n",
       "      <td>177</td>\n",
       "      <td>5</td>\n",
       "      <td>179</td>\n",
       "      <td>6</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>4</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>Ishan Kishan</td>\n",
       "      <td>81</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>3--18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Dr DY Patil Sports Academy, Mumbai</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Group</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Field</td>\n",
       "      <td>205</td>\n",
       "      <td>2</td>\n",
       "      <td>208</td>\n",
       "      <td>5</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Odean Smith</td>\n",
       "      <td>Faf du Plessis</td>\n",
       "      <td>88</td>\n",
       "      <td>Mohammed Siraj</td>\n",
       "      <td>2--59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>March 28,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Lucknow</td>\n",
       "      <td>Group</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Field</td>\n",
       "      <td>158</td>\n",
       "      <td>6</td>\n",
       "      <td>161</td>\n",
       "      <td>5</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>Deepak Hooda</td>\n",
       "      <td>55</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>3--25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>March 29,2022</td>\n",
       "      <td>Maharashtra Cricket Association Stadium,Pune</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Group</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Field</td>\n",
       "      <td>210</td>\n",
       "      <td>6</td>\n",
       "      <td>149</td>\n",
       "      <td>7</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Runs</td>\n",
       "      <td>61</td>\n",
       "      <td>Sanju Samson</td>\n",
       "      <td>Aiden Markram</td>\n",
       "      <td>57</td>\n",
       "      <td>Yuzvendra Chahal</td>\n",
       "      <td>3--22</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_id           date                                         venue  \\\n",
       "0         1  March 26,2022                      Wankhede Stadium, Mumbai   \n",
       "1         2  March 27,2022                     Brabourne Stadium, Mumbai   \n",
       "2         3  March 27,2022            Dr DY Patil Sports Academy, Mumbai   \n",
       "3         4  March 28,2022                      Wankhede Stadium, Mumbai   \n",
       "4         5  March 29,2022  Maharashtra Cricket Association Stadium,Pune   \n",
       "\n",
       "       team1      team2  stage toss_winner toss_decision  first_ings_score  \\\n",
       "0    Chennai    Kolkata  Group     Kolkata         Field               131   \n",
       "1      Delhi     Mumbai  Group       Delhi         Field               177   \n",
       "2   Banglore     Punjab  Group      Punjab         Field               205   \n",
       "3    Gujarat    Lucknow  Group     Gujarat         Field               158   \n",
       "4  Hyderabad  Rajasthan  Group   Hyderabad         Field               210   \n",
       "\n",
       "   first_ings_wkts  second_ings_score  second_ings_wkts match_winner   won_by  \\\n",
       "0                5                133                 4      Kolkata  Wickets   \n",
       "1                5                179                 6        Delhi  Wickets   \n",
       "2                2                208                 5       Punjab  Wickets   \n",
       "3                6                161                 5      Gujarat  Wickets   \n",
       "4                6                149                 7    Rajasthan     Runs   \n",
       "\n",
       "   margin player_of_the_match      top_scorer  highscore      best_bowling  \\\n",
       "0       6         Umesh Yadav        MS Dhoni         50      Dwayne Bravo   \n",
       "1       4       Kuldeep Yadav    Ishan Kishan         81     Kuldeep Yadav   \n",
       "2       5         Odean Smith  Faf du Plessis         88    Mohammed Siraj   \n",
       "3       5      Mohammed Shami    Deepak Hooda         55    Mohammed Shami   \n",
       "4      61        Sanju Samson   Aiden Markram         57  Yuzvendra Chahal   \n",
       "\n",
       "  best_bowling_figure  \n",
       "0               3--20  \n",
       "1               3--18  \n",
       "2               2--59  \n",
       "3               3--25  \n",
       "4               3--22  "
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "112a07ed-9800-4b85-a3dd-5ed2e30d8ebe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='best_bowling'>"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df['highest_wickets'] = df['best_bowling_figure'].apply(lambda x :x.split('--')[0])\n",
    "df['highest_wickets'] = df['highest_wickets'].astype(int)\n",
    "top_bowlers = df.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10)\n",
    "top_bowlers.plot(kind = 'barh')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f6084e57-0568-4849-8413-220cff2ff8e3",
   "metadata": {},
   "source": [
    "###  Venue Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d4e26f1-2479-4456-bda2-2a639c382d2e",
   "metadata": {},
   "source": [
    "Most Matches Played by Venue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "07a58ac4-d8ee-4917-a98a-33e85121c893",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "venue\n",
       "Wankhede Stadium, Mumbai                        21\n",
       "Dr DY Patil Sports Academy, Mumbai              20\n",
       "Brabourne Stadium, Mumbai                       16\n",
       "Maharashtra Cricket Association Stadium,Pune    13\n",
       "Eden Gardens, Kolkata                            2\n",
       "Narendra Modi Stadium, Ahmedabad                 2\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "venue_count = df['venue'].value_counts()\n",
    "venue_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "f427aff8-a677-405e-9224-f9daf1c0044d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='venue'>"
      ]
     },
     "execution_count": 161,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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A9G6dWt4enrC3d0dnTt3lns2r6IKJ/IozwQeWlpaRW5J/RS1Am+Cl4+PD9zd3dGhQwfY2trKzWgZHh6OJ0+ewMHBAb6+vggICEDt2rU/yL6JiIjo8yORleXBGCKijywuLg5dunTBjRs3oKOjI3Y5lVJWVha0tbXhMeYSqqmU7TZcIiIier8dc4w/Wt+F378zMzNL/YUyR8yIqFKIiYnBjz/+yFBGREREXyRO/kFElcLcuXPFLoGIiIhINBwxIyIiIiIiEhmDGRERERERkcgYzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRMZgRERERERGJjMGMiIiIiIhIZAxmREREREREImMwIyIiIiIiEhmDGRERERERkcgYzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRMZgRERERERGJjMGMiIiIiIhIZAxmREREREREIlMSuwAiIiqf/wUbQUtLS+wyiIiI6APiiBkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMiWxCyAiovJxPvgnFNWlYpdBRET0yV1wdxK7hI+GI2ZEREREREQiYzAjIiIiIiISGYMZERERERGRyBjMiIiIiIiIRMZgRkREREREJDIGMyIiIiIiIpExmBEREREREYmMwYyIiIiIiEhkDGZEREREREQiYzAjIiIiIiISGYMZERERERGRyBjMiIiIiIiIRMZgRkREREREJDIGMyIiIiIiIpExmBEREREREYmMwYyIiIiIiEhkDGZEREREREQiYzAjIiIiIiISGYMZERERERGRyBjMqNK5desWJBIJkpOTAQBxcXGQSCR4+vSpqHV9rvz9/dG5c2exy6hSgoOD0bhx4//cj0Qiwc6dO/9zP0RERFT1MZhVMv7+/pBIJJBIJKhWrRrq1KmD9u3bIzw8HAUFBRXq09XVVehTRUUFdevWhZeXF7Zv3w4AyM3NhY2NDYYMGVJk24kTJ6JevXrIysoqtu/CfiUSCTQ1NeHk5CT0W9bjfTcUGBkZISMjA7a2tmXu59y5c/D09ETt2rWhqqoKExMT9OzZEw8fPixzHxX1bpD8r4YMGQJFRUVs3rz5g/T3OSn8+hg2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TOChpaVV6t/YCwwMROvWreHp6Ql3d3d07txZmIzlvzIzM4OPjw/c3d3RoUMH2Nrayn09hYeH48mTJ3BwcICvry8CAgLkbvUlIiIieptE9r75xYk+A3FxcWjTpg2ePHmC6tWri13OF619+/awsrLCsmXL5JbHxcWhS5cuuHHjBnR0dESqrnLLysqCtrY2rLfGQlFdKnY5REREn9wF9/828Z0YCr9/Z2ZmlvoLZd7KSESfxOPHj3Hw4EEcPXoUK1asKLI+JiYGP/74I0MZERERfZEYzIjok3B0dMSTJ08wb948WFhYFFk/d+5cEaoiIiIiqhwYzOiL4OrqWuzU9/TpFP4hbiIiIiIqipN/EBERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMiWxCyAiovI52cERWlpaYpdBREREHxBHzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRMZgRERERERGJjMGMiIiIiIhIZAxmREREREREImMwIyIiIiIiEhmDGRERERERkcgYzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRKYldABERlc/EjONQea4hdhlERPSWpQYuYpdAVRxHzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRMZgRERERERGJjMGMiIiIiIhIZAxmREREREREImMwIyIiIiIiEhmDGRERERERkcgYzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRMZgRERERERGJjMGMiIiIiIhIZAxmREREREREImMwIyIiIiIiEhmDGRERERERkcgYzIiIiIiIiETGYEZERERERCQyBjMiIiIiIiKRMZjRZ8XV1RWjR48Wu4wqzd/fH507dxbe85wW9e45qohbt25BIpEgOTn5g9REREREVRuDGX1S/v7+kEgkwktXVxcdO3bEhQsXxC6t0srPz8ecOXNgaWkJNTU11KhRAy1atEBERITQ5mOGp+3btyMkJOSj9F1erq6ukEgkmDt3bpF17u7ukEgkCA4O/vSFVYCRkREyMjJga2srdilERERUCTCY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mzcjKSkJtra2GDNmDBYsWPBB9ktERESfJ4mspIduiIg+ocjISMyaNQspKSmijMBVBVlZWdDW1sbQy3uhollyICUiok9vqYGL2CVQJVX4/TszM7PUO7A4YkZElUJMTAxmz57NUEZERERfJD5jRkSVwubNm8UugYiIiEg0HDEjIiIiIiISGYMZERERERGRyP5TMMvJyflQdRAREREREX2xyh3MCgoKEBISgrp160IqleLGjRsA3kxlHhYW9sELJCIiIiIi+tyVO5jNnDkTkZGRmD9/PpSVlYXldnZ2+PXXXz9ocURERERERF+CcgezdevW4ZdffkGfPn2gqKgoLG/UqBEuX778QYsjIiIiIiL6EpQ7mP3zzz8wMzMrsrygoACvX7/+IEURERERERF9ScodzGxsbBAfH19k+datW+Hg4PBBiiIiIiIiIvqSlPsPTE+fPh2+vr74559/UFBQgO3bt+PKlStYt24d9uzZ8zFqJCIiIiIi+qyVe8TMy8sLW7Zswb59+yCRSDBt2jSkpqZi9+7daN++/ceokYiIiIiI6LNW7hEzAHBzc4Obm9uHroWIiIiIiOiL9J/+wDQRERERERH9d+UeMVNQUIBEIilxfX5+/n8qiIiIiIiI6EtT7mC2Y8cOufevX7/GuXPnEBUVhRkzZnywwoiIiIiIiL4U5Q5m3t7eRZZ169YNNjY22LJlCwYOHPhBCiMiIiIiIvpSSGQymexDdJSWloZGjRohOzv7Q3RHRETvyMrKgra2NjIzM6GlpSV2OURERFQGZf3+/UEm/3j58iWWL18OQ0PDD9EdERERERHRF6XctzLq6OjITf4hk8nw7NkzqKurY8OGDR+0OCIiIiIioi9BuYPZkiVL5N4rKCigVq1aaN68OXR0dD5UXURERERERF+Mcgezfv36fYw6iIiIiIiIvljlDmYA8PTpU5w+fRr3799HQUGB3Do/P78PUhgREREREdGXotzBbPfu3ejTpw+ys7Ohqakp97yZRCJhMCMiIiIiIiqncs/KOG7cOAwYMADPnj3D06dP8eTJE+H1+PHjj1EjERERERHRZ63cweyff/5BQEAA1NXVP0Y9REREREREX5xyBzM3NzecPXv2Y9RCRERERET0RSr3M2YeHh6YMGECUlJSYGdnh2rVqsmt//bbbz9YcURERERERF8CiUwmk5VnAwWFkgfZ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PLjINPWFFi9ejB49eqBt27a4evUqBg0ahF9//RWRkZGws7ODi4sLIiMjhWCppKSEZcuWYc2aNTAwMIC3t3eRPpOSknD+/Pkik8IAb27H69ChA8LCwqClpYU//vgD7u7uMDc3x9SpUxEaGopOnTpBXV0dly9fRteuXWFubo4hQ4Zg5MiRGDp0KACgc+fOWLp0KRYsWAAbGxusWbMGERERctP3b9u2DU2bNkWvXr1gbW2NiRMnljjitXjxYujo6KBly5bw8vKCm5sbHB0d5dr89NNPuHXrFho0aFDic35lqau8DA0NYWJighkzZqB58+ZwdHTE0qVLMWPGDCFElXRdwsPD8eTJEzg4OMDX1xcBAQFyf3dNQUEBO3bsQG5uLpo1a4ZBgwa9dwr7GjVqYMOGDdi3b5/wZy2Cg4MrfHxv8/f3L9e5srKywsqVK/Hzzz/D3t4ep0+flptEqKwiIiLg5+eHcePGwcLCAt9++y1OnToFIyOjcvdFREREnxeJrLiHP4iIPmOurq5wdXX9YEHvU8nKyoK2tjY23IyEupa62OUQ0ReuS43uYpdAVCUUfv/OzMws9W6bSnMrIxHRp/Ds2TOkpaUJfwSciIiIqDJgMCOiL4qmpiannSciIqJKp1I9Y0ZERERERPQlYjAjIiIiIiISGYMZERERERGRyBjMiIiIiIiIRMZgRkREREREJDIGMyIiIiIiIpExmBEREREREYmMwYyIiIiIiEhkDGZEREREREQiYzAjIiIiIiISGYMZERERERGRyBjMiIiIiIiIRMZgRkREREREJDIGMyIiIiIiIpExmBEREREREYmMwYyIiIiIiEhkSmIXQERE5eNVowu0tLTELoOIiIg+II6YERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJTErsAIiIqn5sn5kBTQ0XsMsqsfutgsUsgIiKq9DhiRkREREREJDIGMyIiIiIiIpExmBEREREREYmMwYyIiIiIiEhkDGZEREREREQiYzAjIiIiIiISGYMZERERERGRyBjMiIiIiIiIRMZgRkREREREJDIGMyIiIiIiIpExmBEREREREYmMwYyIiIiIiEhkDGZE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ly5ybUJCQjBt2jTMmTMHVlZWcHNzw+7du2FqalqmfSgqKuLRo0fw8/ODubk5evTogU6dOslNdiGRSEqdofJdWlpaOHDgAOrUqQNXV1cUFBRg3759OH36NOzt7TFs2DAMHDgQU6dOLVN/rVq1wt69exEUFIRly5ahcePGWLRoEebNmwdbW1ts3LixyN+Ma9myJYYNG4aePXuiVq1amD9/PmrVqoXIyEhs3boV1tbWmDt3LhYuXFjm4yIiIqLPn0RW3MMyREQiu3XrFho2bIiUlJQKzdb4OcrKyoK2tjaS902Gpob4f+y8rOq3Dha7BCIiItEUfv/OzMws9ZfzHDEjokopJiYGQ4YMYSgjIiKiLwKnyyeiSmnYsGFil0BERET0yXDEjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiUxJ7AKIiKh8TFsFQktLS+wyiIiI6APiiBkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMiWxCyAiovK5N6MPslWqiV1GmenP3i52CURERJUeR8yIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYzIiIiIiIikTGYERERERERiYzBjIiIiIiISGQMZkRERERERCJjMCMiIiIiIhIZgxkREREREZHIGMyIiIiIiIhExmBGREREREQkMgYz+s8kEgl27twpdhkVZmJigiVLlgjvK9vxVPb63sff3x+dO3cWuwzBu+fzfSIjI1G9evVKUQsRERF9vhjMKgl/f39IJBLMnTtXbvnOnTshkUhEqkpccXFxkEgk0NHRQU5Ojty606dPQyKRfJRzk5GRgU6dOpW4/v79+xg6dCiMjY2hoqICPT09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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(y = venue_count.index,x = venue_count.values,palette='rainbow')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9bb61b7c-5810-4d9a-a475-aacd8d403721",
   "metadata": {},
   "source": [
    "### Custom Questions & Insights\n",
    "Q1: Who won the highest margin by runs?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "98841e09-4523-42fa-890b-d44dd734cae1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_winner</th>\n",
       "      <th>margin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>Chennai</td>\n",
       "      <td>91</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_winner  margin\n",
       "54      Chennai      91"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['won_by'] == 'Runs'].sort_values(by = 'margin',ascending=False).head(1)[['match_winner','margin']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "071eb3ad-5e4a-4ceb-af04-ba1b4871cd3d",
   "metadata": {},
   "source": [
    "Q2: Which player had the highest individual score?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "0150db8d-fbcd-432a-8594-0dcff4d3a73d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>top_scorer</th>\n",
       "      <th>highscore</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>65</th>\n",
       "      <td>Quinton de Kock</td>\n",
       "      <td>140</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         top_scorer  highscore\n",
       "65  Quinton de Kock        140"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['highscore'] == df['highscore'].max()][['top_scorer','highscore']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8504e7bf-5d54-4e1f-8d8b-4054df1fd5fd",
   "metadata": {},
   "source": [
    "Q3: Which bowler had the best bowling figures?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "c03ea3d0-80d8-4982-9710-5fc113f19d48",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>date</th>\n",
       "      <th>venue</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>stage</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>first_ings_score</th>\n",
       "      <th>first_ings_wkts</th>\n",
       "      <th>...</th>\n",
       "      <th>second_ings_wkts</th>\n",
       "      <th>match_winner</th>\n",
       "      <th>won_by</th>\n",
       "      <th>margin</th>\n",
       "      <th>player_of_the_match</th>\n",
       "      <th>top_scorer</th>\n",
       "      <th>highscore</th>\n",
       "      <th>best_bowling</th>\n",
       "      <th>best_bowling_figure</th>\n",
       "      <th>highest_wickets</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>March 26,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Group</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Field</td>\n",
       "      <td>131</td>\n",
       "      <td>5</td>\n",
       "      <td>...</td>\n",
       "      <td>4</td>\n",
       "      <td>Kolkata</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>6</td>\n",
       "      <td>Umesh Yadav</td>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>50</td>\n",
       "      <td>Dwayne Bravo</td>\n",
       "      <td>3--20</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Brabourne Stadium, Mumbai</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>Group</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Field</td>\n",
       "      <td>177</td>\n",
       "      <td>5</td>\n",
       "      <td>...</td>\n",
       "      <td>6</td>\n",
       "      <td>Delhi</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>4</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>Ishan Kishan</td>\n",
       "      <td>81</td>\n",
       "      <td>Kuldeep Yadav</td>\n",
       "      <td>3--18</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>March 27,2022</td>\n",
       "      <td>Dr DY Patil Sports Academy, Mumbai</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Group</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Field</td>\n",
       "      <td>205</td>\n",
       "      <td>2</td>\n",
       "      <td>...</td>\n",
       "      <td>5</td>\n",
       "      <td>Punjab</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Odean Smith</td>\n",
       "      <td>Faf du Plessis</td>\n",
       "      <td>88</td>\n",
       "      <td>Mohammed Siraj</td>\n",
       "      <td>2--59</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>March 28,2022</td>\n",
       "      <td>Wankhede Stadium, Mumbai</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Lucknow</td>\n",
       "      <td>Group</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Field</td>\n",
       "      <td>158</td>\n",
       "      <td>6</td>\n",
       "      <td>...</td>\n",
       "      <td>5</td>\n",
       "      <td>Gujarat</td>\n",
       "      <td>Wickets</td>\n",
       "      <td>5</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>Deepak Hooda</td>\n",
       "      <td>55</td>\n",
       "      <td>Mohammed Shami</td>\n",
       "      <td>3--25</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>March 29,2022</td>\n",
       "      <td>Maharashtra Cricket Association Stadium,Pune</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Group</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>Field</td>\n",
       "      <td>210</td>\n",
       "      <td>6</td>\n",
       "      <td>...</td>\n",
       "      <td>7</td>\n",
       "      <td>Rajasthan</td>\n",
       "      <td>Runs</td>\n",
       "      <td>61</td>\n",
       "      <td>Sanju Samson</td>\n",
       "      <td>Aiden Markram</td>\n",
       "      <td>57</td>\n",
       "      <td>Yuzvendra Chahal</td>\n",
       "      <td>3--22</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_id           date                                         venue  \\\n",
       "0         1  March 26,2022                      Wankhede Stadium, Mumbai   \n",
       "1         2  March 27,2022                     Brabourne Stadium, Mumbai   \n",
       "2         3  March 27,2022            Dr DY Patil Sports Academy, Mumbai   \n",
       "3         4  March 28,2022                      Wankhede Stadium, Mumbai   \n",
       "4         5  March 29,2022  Maharashtra Cricket Association Stadium,Pune   \n",
       "\n",
       "       team1      team2  stage toss_winner toss_decision  first_ings_score  \\\n",
       "0    Chennai    Kolkata  Group     Kolkata         Field               131   \n",
       "1      Delhi     Mumbai  Group       Delhi         Field               177   \n",
       "2   Banglore     Punjab  Group      Punjab         Field               205   \n",
       "3    Gujarat    Lucknow  Group     Gujarat         Field               158   \n",
       "4  Hyderabad  Rajasthan  Group   Hyderabad         Field               210   \n",
       "\n",
       "   first_ings_wkts  ...  second_ings_wkts  match_winner   won_by margin  \\\n",
       "0                5  ...                 4       Kolkata  Wickets      6   \n",
       "1                5  ...                 6         Delhi  Wickets      4   \n",
       "2                2  ...                 5        Punjab  Wickets      5   \n",
       "3                6  ...                 5       Gujarat  Wickets      5   \n",
       "4                6  ...                 7     Rajasthan     Runs     61   \n",
       "\n",
       "   player_of_the_match      top_scorer highscore      best_bowling  \\\n",
       "0          Umesh Yadav        MS Dhoni        50      Dwayne Bravo   \n",
       "1        Kuldeep Yadav    Ishan Kishan        81     Kuldeep Yadav   \n",
       "2          Odean Smith  Faf du Plessis        88    Mohammed Siraj   \n",
       "3       Mohammed Shami    Deepak Hooda        55    Mohammed Shami   \n",
       "4         Sanju Samson   Aiden Markram        57  Yuzvendra Chahal   \n",
       "\n",
       "  best_bowling_figure highest_wickets  \n",
       "0               3--20               3  \n",
       "1               3--18               3  \n",
       "2               2--59               2  \n",
       "3               3--25               3  \n",
       "4               3--22               3  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "b36806a8-e52f-46e7-86b3-f1496a0f192c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>best_bowling</th>\n",
       "      <th>best_bowling_figure</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Yuzvendra Chahal</td>\n",
       "      <td>5--40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>Umran Malik</td>\n",
       "      <td>5--25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>53</th>\n",
       "      <td>Wanindu Hasaranga</td>\n",
       "      <td>5--18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>55</th>\n",
       "      <td>Jasprit Bumrah</td>\n",
       "      <td>5--10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         best_bowling best_bowling_figure\n",
       "29   Yuzvendra Chahal               5--40\n",
       "39        Umran Malik               5--25\n",
       "53  Wanindu Hasaranga               5--18\n",
       "55     Jasprit Bumrah               5--10"
      ]
     },
     "execution_count": 183,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['highest_wickets'] == df['highest_wickets'].max()][['best_bowling','best_bowling_figure']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "680e5385-687f-43e9-9f2f-4384ddc08925",
   "metadata": {},
   "source": [
    "# Good Work"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
