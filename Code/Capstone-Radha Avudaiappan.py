{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing packages\n",
    "import pandas as pd\n",
    "import csv\n",
    "import plotly.express as px\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline \n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#loading in csv files from data sources\n",
    "type_det=pd.read_csv('VehicleTypes.csv', sep='\\t', lineterminator='\\r')\n",
    "types=pd.read_csv('Type.csv',sep='\\t',lineterminator='\\r')\n",
    "age=pd.read_csv('Age.csv')\n",
    "state=pd.read_csv('State.csv',sep='\\t',lineterminator='\\r')\n",
    "weather=pd.read_csv('Weather.csv',sep='\\t',lineterminator='\\r')\n",
    "urban_rural=pd.read_csv('Urban_Rural.csv')\n",
    "dem=pd.read_csv('veh_demo.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#for the year 2010\n",
    "\n",
    "type_det=type_det.drop(0)\n",
    "type_det=type_det.drop(67)\n",
    "type_det=type_det.drop(columns=['Unnamed: 3'])\n",
    "\n",
    "types=types.drop(0)\n",
    "types=types.drop(8)\n",
    "types=types.drop(7)\n",
    "types=types.drop(columns=['Unnamed: 3'])\n",
    "\n",
    "#final row is total for USA\n",
    "state=state.drop(0)\n",
    "state=state.drop(53)\n",
    "state=state.drop(columns=['Unnamed: 4'])\n",
    "\n",
    "\n",
    "#weather dataframe had to be recreated because csv was not coming in properly\n",
    "weather=pd.DataFrame({'Daylight':[13530,834,365,118,62],'Dark, but Lighted':[4818,479,71,50,15],'Dark':[7518,570,210,177,71],'Dawn or Dark':[1090,110,39,38,6],'Other/Unknown':[60,2,0,1,62],'Total':[27016,1995,685,384,216]},index=['Normal','Rain','Snow/Sleet','Other','Unknown'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#trend for multiple years not just 2010\n",
    "urban_rural=urban_rural.drop(43)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#data cleaning\n",
    "type_det['Body Type']=type_det['Body Type'].str.replace('\\n','')\n",
    "types['Vehicle Type']=types['Vehicle Type'].str.replace('\\n','')\n",
    "state['State']=state['State'].str.replace('\\n','')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#relabeling indcies\n",
    "types.index=[0,1,2,3,4,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "    Year Rural Deaths Rural Miles Traveled (Millions)  Rural Death Rate  \\\n",
       "0   1977       28,463                         654,596              4.35   \n",
       "1   1978       30,018                         689,953              4.35   \n",
       "2   1979       29,135                         670,079              4.35   \n",
       "3   1980       29,114                         672,030              4.33   \n",
       "4   1981       27,692                         688,308              4.02   \n",
       "5   1982       25,005                         689,226              3.63   \n",
       "6   1983       24,486                         700,517              3.50   \n",
       "7   1984       25,636                         718,132              3.57   \n",
       "8   1985       25,185                         730,728              3.45   \n",
       "9   1986       26,484                         747,780              3.54   \n",
       "10  1987       27,131                         780,450              3.48   \n",
       "11  1988       27,793                         817,534              3.40   \n",
       "12  1989       26,392                         847,225              3.12   \n",
       "13  1990       25,761                         868,878              2.96   \n",
       "14  1991       24,328                         883,553              2.75   \n",
       "15  1992       22,821                         884,097              2.58   \n",
       "16  1993       23,459                         886,706              2.65   \n",
       "17  1994       23,841                         908,341              2.62   \n",
       "18  1995       24,449                         933,285              2.62   \n",
       "19  1996       24,561                         960,194              2.56   \n",
       "20  1997       25,135                         999,920              2.51   \n",
       "21  1998       25,185                       1,033,310              2.44   \n",
       "22  1999       25,547                       1,062,623              2.40   \n",
       "23  2000       24,835                       1,083,152              2.29   \n",
       "24  2001       25,148                       1,110,697              2.26   \n",
       "25  2002       25,896                       1,128,160              2.30   \n",
       "26  2003       24,957                       1,085,385              2.30   \n",
       "27  2004       25,179                       1,070,248              2.35   \n",
       "28  2005       24,587                       1,037,937              2.37   \n",
       "29  2006       23,646                       1,037,069              2.28   \n",
       "30  2007       23,254                       1,035,303              2.25   \n",
       "31  2008       20,987                         990,418              2.12   \n",
       "32  2009       19,323                         982,180              1.97   \n",
       "33  2010       18,089                         984,065              1.84   \n",
       "34  2011       17,769                         974,038              1.82   \n",
       "35  2012       18,367                         977,078              1.88   \n",
       "36  2013       17,740                         941,912              1.88   \n",
       "37  2014       16,791                         920,928              1.82   \n",
       "38  2015       17,572                         928,905              1.89   \n",
       "39  2016       18,321                         949,545              1.93   \n",
       "40  2017       17,405                         963,206              1.81   \n",
       "41  2018       16,323                         978,802              1.67   \n",
       "42  2019       16,340                         983,853              1.66   \n",
       "\n",
       "   Urban Deaths Urban Miles Traveled (Millions)  Urban Death Rate  \\\n",
       "0        19,296                         821,971              2.35   \n",
       "1        19,863                         858,260              2.31   \n",
       "2        21,507                         859,054              2.50   \n",
       "3        21,560                         855,265              2.52   \n",
       "4        20,782                         867,000              2.40   \n",
       "5        18,678                         905,784              2.06   \n",
       "6        18,027                         952,271              1.89   \n",
       "7        18,590                       1,002,137              1.86   \n",
       "8        18,613                       1,044,098              1.78   \n",
       "9        19,581                       1,087,092              1.80   \n",
       "10       19,217                       1,140,754              1.68   \n",
       "11       19,253                       1,208,428              1.59   \n",
       "12       19,160                       1,249,262              1.53   \n",
       "13       18,807                       1,275,484              1.47   \n",
       "14       17,126                       1,288,497              1.33   \n",
       "15       16,223                       1,363,054              1.19   \n",
       "16       16,429                       1,409,672              1.17   \n",
       "17       16,811                       1,449,247              1.16   \n",
       "18       17,163                       1,489,490              1.15   \n",
       "19       17,368                       1,523,886              1.14   \n",
       "20       16,829                       1,560,452              1.08   \n",
       "21       16,219                       1,592,057              1.02   \n",
       "22       16,059                       1,627,618              0.99   \n",
       "23       16,116                       1,663,773              0.97   \n",
       "24       16,990                       1,686,642              1.01   \n",
       "25       17,013                       1,727,596              0.98   \n",
       "26       17,783                       1,805,508              0.98   \n",
       "27       17,581                       1,892,265              0.93   \n",
       "28       18,627                       1,951,870              0.95   \n",
       "29       18,791                       1,977,047              0.95   \n",
       "30       17,908                       1,994,519              0.90   \n",
       "31       16,218                       1,983,091              0.82   \n",
       "32       14,501                       1,974,583              0.73   \n",
       "33       14,659                       1,983,200              0.74   \n",
       "34       14,575                       1,972,094              0.74   \n",
       "35       15,371                       1,992,355              0.77   \n",
       "36       15,119                       2,046,369              0.74   \n",
       "37       15,917                       2,104,728              0.76   \n",
       "38       16,830                       2,166,468              0.78   \n",
       "39       19,357                       2,224,863              0.87   \n",
       "40       19,976                       2,249,142              0.89   \n",
       "41       20,408                       2,261,525              0.90   \n",
       "42       19,595                       2,277,919              0.86   \n",
       "\n",
       "   Total Deaths Total Miles Traveled (Millions)  Total Death Rate  \n",
       "0        47,878                       1,476,567              3.24  \n",
       "1        50,331                       1,548,213              3.25  \n",
       "2        51,093                       1,529,133              3.34  \n",
       "3        51,091                       1,527,295              3.35  \n",
       "4        49,301                       1,555,308              3.17  \n",
       "5        43,945                       1,595,010              2.76  \n",
       "6        42,589                       1,652,788              2.58  \n",
       "7        44,257                       1,720,269              2.57  \n",
       "8        43,825                       1,774,826              2.47  \n",
       "9        46,087                       1,834,872              2.51  \n",
       "10       46,390                       1,921,204              2.41  \n",
       "11       47,087                       2,025,962              2.32  \n",
       "12       45,582                       2,096,487              2.17  \n",
       "13       44,599                       2,144,362              2.08  \n",
       "14       41,508                       2,172,050              1.91  \n",
       "15       39,250                       2,247,151              1.75  \n",
       "16       40,150                       2,296,378              1.75  \n",
       "17       40,716                       2,357,588              1.73  \n",
       "18       41,817                       2,422,775              1.73  \n",
       "19       42,065                       2,484,080              1.69  \n",
       "20       42,013                       2,560,372              1.64  \n",
       "21       41,501                       2,625,367              1.58  \n",
       "22       41,717                       2,690,241              1.55  \n",
       "23       41,945                       2,746,925              1.53  \n",
       "24       42,196                       2,797,339              1.51  \n",
       "25       43,005                       2,855,756              1.51  \n",
       "26       42,884                       2,890,893              1.48  \n",
       "27       42,836                       2,962,513              1.45  \n",
       "28       43,510                       2,989,807              1.46  \n",
       "29       42,708                       3,014,116              1.42  \n",
       "30       41,259                       3,029,822              1.36  \n",
       "31       37,423                       2,973,509              1.26  \n",
       "32       33,883                       2,956,763              1.15  \n",
       "33       32,999                       2,967,265              1.11  \n",
       "34       32,479                       2,946,132              1.10  \n",
       "35       33,782                       2,969,433              1.14  \n",
       "36       32,894                       2,988,281              1.10  \n",
       "37       32,744                       3,025,656              1.08  \n",
       "38       35,485                       3,095,373              1.15  \n",
       "39       37,806                       3,174,408              1.19  \n",
       "40       37,473                       3,212,348              1.17  \n",
       "41       36,835                       3,240,327              1.14  \n",
       "42       36,096                       3,261,772              1.11  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Year</th>\n      <th>Rural Deaths</th>\n      <th>Rural Miles Traveled (Millions)</th>\n      <th>Rural Death Rate</th>\n      <th>Urban Deaths</th>\n      <th>Urban Miles Traveled (Millions)</th>\n      <th>Urban Death Rate</th>\n      <th>Total Deaths</th>\n      <th>Total Miles Traveled (Millions)</th>\n      <th>Total Death Rate</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1977</td>\n      <td>28,463</td>\n      <td>654,596</td>\n      <td>4.35</td>\n      <td>19,296</td>\n      <td>821,971</td>\n      <td>2.35</td>\n      <td>47,878</td>\n      <td>1,476,567</td>\n      <td>3.24</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1978</td>\n      <td>30,018</td>\n      <td>689,953</td>\n      <td>4.35</td>\n      <td>19,863</td>\n      <td>858,260</td>\n      <td>2.31</td>\n      <td>50,331</td>\n      <td>1,548,213</td>\n      <td>3.25</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>1979</td>\n      <td>29,135</td>\n      <td>670,079</td>\n      <td>4.35</td>\n      <td>21,507</td>\n      <td>859,054</td>\n      <td>2.50</td>\n      <td>51,093</td>\n      <td>1,529,133</td>\n      <td>3.34</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>1980</td>\n      <td>29,114</td>\n      <td>672,030</td>\n      <td>4.33</td>\n      <td>21,560</td>\n      <td>855,265</td>\n      <td>2.52</td>\n      <td>51,091</td>\n      <td>1,527,295</td>\n      <td>3.35</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>1981</td>\n      <td>27,692</td>\n      <td>688,308</td>\n      <td>4.02</td>\n      <td>20,782</td>\n      <td>867,000</td>\n      <td>2.40</td>\n      <td>49,301</td>\n      <td>1,555,308</td>\n      <td>3.17</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>1982</td>\n      <td>25,005</td>\n      <td>689,226</td>\n      <td>3.63</td>\n      <td>18,678</td>\n      <td>905,784</td>\n      <td>2.06</td>\n      <td>43,945</td>\n      <td>1,595,010</td>\n      <td>2.76</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>1983</td>\n      <td>24,486</td>\n      <td>700,517</td>\n      <td>3.50</td>\n      <td>18,027</td>\n      <td>952,271</td>\n      <td>1.89</td>\n      <td>42,589</td>\n      <td>1,652,788</td>\n      <td>2.58</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>1984</td>\n      <td>25,636</td>\n      <td>718,132</td>\n      <td>3.57</td>\n      <td>18,590</td>\n      <td>1,002,137</td>\n      <td>1.86</td>\n      <td>44,257</td>\n      <td>1,720,269</td>\n      <td>2.57</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>1985</td>\n      <td>25,185</td>\n      <td>730,728</td>\n      <td>3.45</td>\n      <td>18,613</td>\n      <td>1,044,098</td>\n      <td>1.78</td>\n      <td>43,825</td>\n      <td>1,774,826</td>\n      <td>2.47</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>1986</td>\n      <td>26,484</td>\n      <td>747,780</td>\n      <td>3.54</td>\n      <td>19,581</td>\n      <td>1,087,092</td>\n      <td>1.80</td>\n      <td>46,087</td>\n      <td>1,834,872</td>\n      <td>2.51</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>1987</td>\n      <td>27,131</td>\n      <td>780,450</td>\n      <td>3.48</td>\n      <td>19,217</td>\n      <td>1,140,754</td>\n      <td>1.68</td>\n      <td>46,390</td>\n      <td>1,921,204</td>\n      <td>2.41</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>1988</td>\n      <td>27,793</td>\n      <td>817,534</td>\n      <td>3.40</td>\n      <td>19,253</td>\n      <td>1,208,428</td>\n      <td>1.59</td>\n      <td>47,087</td>\n      <td>2,025,962</td>\n      <td>2.32</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>1989</td>\n      <td>26,392</td>\n      <td>847,225</td>\n      <td>3.12</td>\n      <td>19,160</td>\n      <td>1,249,262</td>\n      <td>1.53</td>\n      <td>45,582</td>\n      <td>2,096,487</td>\n      <td>2.17</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>1990</td>\n      <td>25,761</td>\n      <td>868,878</td>\n      <td>2.96</td>\n      <td>18,807</td>\n      <td>1,275,484</td>\n      <td>1.47</td>\n      <td>44,599</td>\n      <td>2,144,362</td>\n      <td>2.08</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>1991</td>\n      <td>24,328</td>\n      <td>883,553</td>\n      <td>2.75</td>\n      <td>17,126</td>\n      <td>1,288,497</td>\n      <td>1.33</td>\n      <td>41,508</td>\n      <td>2,172,050</td>\n      <td>1.91</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>1992</td>\n      <td>22,821</td>\n      <td>884,097</td>\n      <td>2.58</td>\n      <td>16,223</td>\n      <td>1,363,054</td>\n      <td>1.19</td>\n      <td>39,250</td>\n      <td>2,247,151</td>\n      <td>1.75</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>1993</td>\n      <td>23,459</td>\n      <td>886,706</td>\n      <td>2.65</td>\n      <td>16,429</td>\n      <td>1,409,672</td>\n      <td>1.17</td>\n      <td>40,150</td>\n      <td>2,296,378</td>\n      <td>1.75</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>1994</td>\n      <td>23,841</td>\n      <td>908,341</td>\n      <td>2.62</td>\n      <td>16,811</td>\n      <td>1,449,247</td>\n      <td>1.16</td>\n      <td>40,716</td>\n      <td>2,357,588</td>\n      <td>1.73</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>1995</td>\n      <td>24,449</td>\n      <td>933,285</td>\n      <td>2.62</td>\n      <td>17,163</td>\n      <td>1,489,490</td>\n      <td>1.15</td>\n      <td>41,817</td>\n      <td>2,422,775</td>\n      <td>1.73</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>1996</td>\n      <td>24,561</td>\n      <td>960,194</td>\n      <td>2.56</td>\n      <td>17,368</td>\n      <td>1,523,886</td>\n      <td>1.14</td>\n      <td>42,065</td>\n      <td>2,484,080</td>\n      <td>1.69</td>\n    </tr>\n    <tr>\n      <th>20</th>\n      <td>1997</td>\n      <td>25,135</td>\n      <td>999,920</td>\n      <td>2.51</td>\n      <td>16,829</td>\n      <td>1,560,452</td>\n      <td>1.08</td>\n      <td>42,013</td>\n      <td>2,560,372</td>\n      <td>1.64</td>\n    </tr>\n    <tr>\n      <th>21</th>\n      <td>1998</td>\n      <td>25,185</td>\n      <td>1,033,310</td>\n      <td>2.44</td>\n      <td>16,219</td>\n      <td>1,592,057</td>\n      <td>1.02</td>\n      <td>41,501</td>\n      <td>2,625,367</td>\n      <td>1.58</td>\n    </tr>\n    <tr>\n      <th>22</th>\n      <td>1999</td>\n      <td>25,547</td>\n      <td>1,062,623</td>\n      <td>2.40</td>\n      <td>16,059</td>\n      <td>1,627,618</td>\n      <td>0.99</td>\n      <td>41,717</td>\n      <td>2,690,241</td>\n      <td>1.55</td>\n    </tr>\n    <tr>\n      <th>23</th>\n      <td>2000</td>\n      <td>24,835</td>\n      <td>1,083,152</td>\n      <td>2.29</td>\n      <td>16,116</td>\n      <td>1,663,773</td>\n      <td>0.97</td>\n      <td>41,945</td>\n      <td>2,746,925</td>\n      <td>1.53</td>\n    </tr>\n    <tr>\n      <th>24</th>\n      <td>2001</td>\n      <td>25,148</td>\n      <td>1,110,697</td>\n      <td>2.26</td>\n      <td>16,990</td>\n      <td>1,686,642</td>\n      <td>1.01</td>\n      <td>42,196</td>\n      <td>2,797,339</td>\n      <td>1.51</td>\n    </tr>\n    <tr>\n      <th>25</th>\n      <td>2002</td>\n      <td>25,896</td>\n      <td>1,128,160</td>\n      <td>2.30</td>\n      <td>17,013</td>\n      <td>1,727,596</td>\n      <td>0.98</td>\n      <td>43,005</td>\n      <td>2,855,756</td>\n      <td>1.51</td>\n    </tr>\n    <tr>\n      <th>26</th>\n      <td>2003</td>\n      <td>24,957</td>\n      <td>1,085,385</td>\n      <td>2.30</td>\n      <td>17,783</td>\n      <td>1,805,508</td>\n      <td>0.98</td>\n      <td>42,884</td>\n      <td>2,890,893</td>\n      <td>1.48</td>\n    </tr>\n    <tr>\n      <th>27</th>\n      <td>2004</td>\n      <td>25,179</td>\n      <td>1,070,248</td>\n      <td>2.35</td>\n      <td>17,581</td>\n      <td>1,892,265</td>\n      <td>0.93</td>\n      <td>42,836</td>\n      <td>2,962,513</td>\n      <td>1.45</td>\n    </tr>\n    <tr>\n      <th>28</th>\n      <td>2005</td>\n      <td>24,587</td>\n      <td>1,037,937</td>\n      <td>2.37</td>\n      <td>18,627</td>\n      <td>1,951,870</td>\n      <td>0.95</td>\n      <td>43,510</td>\n      <td>2,989,807</td>\n      <td>1.46</td>\n    </tr>\n    <tr>\n      <th>29</th>\n      <td>2006</td>\n      <td>23,646</td>\n      <td>1,037,069</td>\n      <td>2.28</td>\n      <td>18,791</td>\n      <td>1,977,047</td>\n      <td>0.95</td>\n      <td>42,708</td>\n      <td>3,014,116</td>\n      <td>1.42</td>\n    </tr>\n    <tr>\n      <th>30</th>\n      <td>2007</td>\n      <td>23,254</td>\n      <td>1,035,303</td>\n      <td>2.25</td>\n      <td>17,908</td>\n      <td>1,994,519</td>\n      <td>0.90</td>\n      <td>41,259</td>\n      <td>3,029,822</td>\n      <td>1.36</td>\n    </tr>\n    <tr>\n      <th>31</th>\n      <td>2008</td>\n      <td>20,987</td>\n      <td>990,418</td>\n      <td>2.12</td>\n      <td>16,218</td>\n      <td>1,983,091</td>\n      <td>0.82</td>\n      <td>37,423</td>\n      <td>2,973,509</td>\n      <td>1.26</td>\n    </tr>\n    <tr>\n      <th>32</th>\n      <td>2009</td>\n      <td>19,323</td>\n      <td>982,180</td>\n      <td>1.97</td>\n      <td>14,501</td>\n      <td>1,974,583</td>\n      <td>0.73</td>\n      <td>33,883</td>\n      <td>2,956,763</td>\n      <td>1.15</td>\n    </tr>\n    <tr>\n      <th>33</th>\n      <td>2010</td>\n      <td>18,089</td>\n      <td>984,065</td>\n      <td>1.84</td>\n      <td>14,659</td>\n      <td>1,983,200</td>\n      <td>0.74</td>\n      <td>32,999</td>\n      <td>2,967,265</td>\n      <td>1.11</td>\n    </tr>\n    <tr>\n      <th>34</th>\n      <td>2011</td>\n      <td>17,769</td>\n      <td>974,038</td>\n      <td>1.82</td>\n      <td>14,575</td>\n      <td>1,972,094</td>\n      <td>0.74</td>\n      <td>32,479</td>\n      <td>2,946,132</td>\n      <td>1.10</td>\n    </tr>\n    <tr>\n      <th>35</th>\n      <td>2012</td>\n      <td>18,367</td>\n      <td>977,078</td>\n      <td>1.88</td>\n      <td>15,371</td>\n      <td>1,992,355</td>\n      <td>0.77</td>\n      <td>33,782</td>\n      <td>2,969,433</td>\n      <td>1.14</td>\n    </tr>\n    <tr>\n      <th>36</th>\n      <td>2013</td>\n      <td>17,740</td>\n      <td>941,912</td>\n      <td>1.88</td>\n      <td>15,119</td>\n      <td>2,046,369</td>\n      <td>0.74</td>\n      <td>32,894</td>\n      <td>2,988,281</td>\n      <td>1.10</td>\n    </tr>\n    <tr>\n      <th>37</th>\n      <td>2014</td>\n      <td>16,791</td>\n      <td>920,928</td>\n      <td>1.82</td>\n      <td>15,917</td>\n      <td>2,104,728</td>\n      <td>0.76</td>\n      <td>32,744</td>\n      <td>3,025,656</td>\n      <td>1.08</td>\n    </tr>\n    <tr>\n      <th>38</th>\n      <td>2015</td>\n      <td>17,572</td>\n      <td>928,905</td>\n      <td>1.89</td>\n      <td>16,830</td>\n      <td>2,166,468</td>\n      <td>0.78</td>\n      <td>35,485</td>\n      <td>3,095,373</td>\n      <td>1.15</td>\n    </tr>\n    <tr>\n      <th>39</th>\n      <td>2016</td>\n      <td>18,321</td>\n      <td>949,545</td>\n      <td>1.93</td>\n      <td>19,357</td>\n      <td>2,224,863</td>\n      <td>0.87</td>\n      <td>37,806</td>\n      <td>3,174,408</td>\n      <td>1.19</td>\n    </tr>\n    <tr>\n      <th>40</th>\n      <td>2017</td>\n      <td>17,405</td>\n      <td>963,206</td>\n      <td>1.81</td>\n      <td>19,976</td>\n      <td>2,249,142</td>\n      <td>0.89</td>\n      <td>37,473</td>\n      <td>3,212,348</td>\n      <td>1.17</td>\n    </tr>\n    <tr>\n      <th>41</th>\n      <td>2018</td>\n      <td>16,323</td>\n      <td>978,802</td>\n      <td>1.67</td>\n      <td>20,408</td>\n      <td>2,261,525</td>\n      <td>0.90</td>\n      <td>36,835</td>\n      <td>3,240,327</td>\n      <td>1.14</td>\n    </tr>\n    <tr>\n      <th>42</th>\n      <td>2019</td>\n      <td>16,340</td>\n      <td>983,853</td>\n      <td>1.66</td>\n      <td>19,595</td>\n      <td>2,277,919</td>\n      <td>0.86</td>\n      <td>36,096</td>\n      <td>3,261,772</td>\n      <td>1.11</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 10
    }
   ],
   "source": [
    "#new data frame with just rates\n",
    "urban_rural_rate=urban_rural[['Year','Rural Death Rate','Urban Death Rate','Total Death Rate']]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#importing clean data to csvs\n",
    "state.to_csv('state_clean.csv')\n",
    "types.to_csv('vehicle_types.csv')\n",
    "weather.to_csv('weather.csv')\n",
    "urban_rural.to_csv('urban_rural_traffic.csv')\n",
    "dem.to_csv('miles_veh_types.csv')\n",
    "age.to_csv('age_crash_fatalities.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "variable=Rural Death Rate<br>Year=%{x%Y}<br>value=%{y}<extra></extra>",
         "legendgroup": "Rural Death Rate",
         "line": {
          "color": "#636efa",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "Rural Death Rate",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "1977",
          "1978",
          "1979",
          "1980",
          "1981",
          "1982",
          "1983",
          "1984",
          "1985",
          "1986",
          "1987",
          "1988",
          "1989",
          "1990",
          "1991",
          "1992",
          "1993",
          "1994",
          "1995",
          "1996",
          "1997",
          "1998",
          "1999",
          "2000",
          "2001",
          "2002",
          "2003",
          "2004",
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019"
         ],
         "xaxis": "x",
         "y": [
          4.35,
          4.35,
          4.35,
          4.33,
          4.02,
          3.63,
          3.5,
          3.57,
          3.45,
          3.54,
          3.48,
          3.4,
          3.12,
          2.96,
          2.75,
          2.58,
          2.65,
          2.62,
          2.62,
          2.56,
          2.51,
          2.44,
          2.4,
          2.29,
          2.26,
          2.3,
          2.3,
          2.35,
          2.37,
          2.28,
          2.25,
          2.12,
          1.97,
          1.84,
          1.82,
          1.88,
          1.88,
          1.82,
          1.89,
          1.93,
          1.81,
          1.67,
          1.66
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=Urban Death Rate<br>Year=%{x%Y}<br>value=%{y}<extra></extra>",
         "legendgroup": "Urban Death Rate",
         "line": {
          "color": "#EF553B",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "Urban Death Rate",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "1977",
          "1978",
          "1979",
          "1980",
          "1981",
          "1982",
          "1983",
          "1984",
          "1985",
          "1986",
          "1987",
          "1988",
          "1989",
          "1990",
          "1991",
          "1992",
          "1993",
          "1994",
          "1995",
          "1996",
          "1997",
          "1998",
          "1999",
          "2000",
          "2001",
          "2002",
          "2003",
          "2004",
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019"
         ],
         "xaxis": "x",
         "y": [
          2.35,
          2.31,
          2.5,
          2.52,
          2.4,
          2.06,
          1.89,
          1.86,
          1.78,
          1.8,
          1.68,
          1.59,
          1.53,
          1.47,
          1.33,
          1.19,
          1.17,
          1.16,
          1.15,
          1.14,
          1.08,
          1.02,
          0.99,
          0.97,
          1.01,
          0.98,
          0.98,
          0.93,
          0.95,
          0.95,
          0.9,
          0.82,
          0.73,
          0.74,
          0.74,
          0.77,
          0.74,
          0.76,
          0.78,
          0.87,
          0.89,
          0.9,
          0.86
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "variable=Total Death Rate<br>Year=%{x%Y}<br>value=%{y}<extra></extra>",
         "legendgroup": "Total Death Rate",
         "line": {
          "color": "#00cc96",
          "dash": "solid"
         },
         "mode": "lines",
         "name": "Total Death Rate",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          "1977",
          "1978",
          "1979",
          "1980",
          "1981",
          "1982",
          "1983",
          "1984",
          "1985",
          "1986",
          "1987",
          "1988",
          "1989",
          "1990",
          "1991",
          "1992",
          "1993",
          "1994",
          "1995",
          "1996",
          "1997",
          "1998",
          "1999",
          "2000",
          "2001",
          "2002",
          "2003",
          "2004",
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019"
         ],
         "xaxis": "x",
         "y": [
          3.24,
          3.25,
          3.34,
          3.35,
          3.17,
          2.76,
          2.58,
          2.57,
          2.47,
          2.51,
          2.41,
          2.32,
          2.17,
          2.08,
          1.91,
          1.75,
          1.75,
          1.73,
          1.73,
          1.69,
          1.64,
          1.58,
          1.55,
          1.53,
          1.51,
          1.51,
          1.48,
          1.45,
          1.46,
          1.42,
          1.36,
          1.26,
          1.15,
          1.11,
          1.1,
          1.14,
          1.1,
          1.08,
          1.15,
          1.19,
          1.17,
          1.14,
          1.11
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "legend": {
         "title": {
          "text": "variable"
         },
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Fatality of Accidents Per Million Miles Traveled"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Year"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Rate"
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "#urban/rural fatal accident line graph\n",
    "ur = px.line(urban_rural_rate, x=\"Year\", y=urban_rural_rate.columns,\n",
    "              hover_data={\"Year\": \"%Y\"},\n",
    "              title='Fatality of Accidents Per Million Miles Traveled')\n",
    "ur.update_yaxes(title='Rate')\n",
    "ur.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "     Vehicle Type  Rate of Fatal Accidents (Per 1000 Miles)\n",
       "0  Passenger Cars                               1552.629284\n",
       "1    Light Trucks                               1515.290652\n",
       "2    Large Trucks                                 55.680388\n",
       "3     Motorcycles                               2011.678201\n",
       "4           Buses                                  2.950303\n",
       "5   Other/Unknown                                 31.280887"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Vehicle Type</th>\n      <th>Rate of Fatal Accidents (Per 1000 Miles)</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Passenger Cars</td>\n      <td>1552.629284</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Light Trucks</td>\n      <td>1515.290652</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Large Trucks</td>\n      <td>55.680388</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Motorcycles</td>\n      <td>2011.678201</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Buses</td>\n      <td>2.950303</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Other/Unknown</td>\n      <td>31.280887</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 15
    }
   ],
   "source": [
    "#new dataframe to find accident rates based on vehicle type\n",
    "new=pd.DataFrame()\n",
    "new['Vehicle Type']=types['Vehicle Type']\n",
    "new['Rate of Fatal Accidents (Per 1000 Miles)']=types['Total']/dem['Number']*1000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "Vehicle Type=%{x}<br>Rate of Fatal Accidents (Per 1000 Miles)=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Passenger Cars",
          "Light Trucks",
          "Large Trucks",
          "Motorcycles",
          "Buses",
          "Other/Unknown"
         ],
         "xaxis": "x",
         "y": [
          1552.6292840324409,
          1515.2906523434115,
          55.680387563544805,
          2011.6782006920414,
          2.9503032582632,
          31.280886870575667
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Rate of Fatal Accidents by Vehicle Type (Per 1000 miles)"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Vehicle Type"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Rate of Fatal Accidents (Per 1000 Miles)"
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "#create vehicle type by accident graph\n",
    "corr_graph=px.bar(new,y='Rate of Fatal Accidents (Per 1000 Miles)', x='Vehicle Type',title='Rate of Fatal Accidents by Vehicle Type (Per 1000 miles)')\n",
    "corr_graph.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "             Daylight  Dark, but Lighted       Dark  Dawn or Dark  \\\n",
       "Normal      50.081433          17.833876  27.827954      4.034646   \n",
       "Rain        41.804511          24.010025  28.571429      5.513784   \n",
       "Snow/Sleet  53.284672          10.364964  30.656934      5.693431   \n",
       "Other       30.729167          13.020833  46.093750      9.895833   \n",
       "Unknown     28.703704           6.944444  32.870370      2.777778   \n",
       "\n",
       "            Other/Unknown  \n",
       "Normal           0.222091  \n",
       "Rain             0.100251  \n",
       "Snow/Sleet       0.000000  \n",
       "Other            0.260417  \n",
       "Unknown         28.703704  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Daylight</th>\n      <th>Dark, but Lighted</th>\n      <th>Dark</th>\n      <th>Dawn or Dark</th>\n      <th>Other/Unknown</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>Normal</th>\n      <td>50.081433</td>\n      <td>17.833876</td>\n      <td>27.827954</td>\n      <td>4.034646</td>\n      <td>0.222091</td>\n    </tr>\n    <tr>\n      <th>Rain</th>\n      <td>41.804511</td>\n      <td>24.010025</td>\n      <td>28.571429</td>\n      <td>5.513784</td>\n      <td>0.100251</td>\n    </tr>\n    <tr>\n      <th>Snow/Sleet</th>\n      <td>53.284672</td>\n      <td>10.364964</td>\n      <td>30.656934</td>\n      <td>5.693431</td>\n      <td>0.000000</td>\n    </tr>\n    <tr>\n      <th>Other</th>\n      <td>30.729167</td>\n      <td>13.020833</td>\n      <td>46.093750</td>\n      <td>9.895833</td>\n      <td>0.260417</td>\n    </tr>\n    <tr>\n      <th>Unknown</th>\n      <td>28.703704</td>\n      <td>6.944444</td>\n      <td>32.870370</td>\n      <td>2.777778</td>\n      <td>28.703704</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 21
    }
   ],
   "source": [
    "#creating new dataframe to weather/light correlations\n",
    "weather_corr=pd.DataFrame(columns=['Daylight','Dark, but Lighted','Dark','Dawn or Dark','Other/Unknown'],index=['Normal','Rain','Snow/Sleet','Other','Unknown'])\n",
    "weather_corr['Daylight']=weather['Daylight']/weather['Total']*100\n",
    "weather_corr['Dark, but Lighted']=weather['Dark, but Lighted']/weather['Total']*100\n",
    "weather_corr['Dark']=weather['Dark']/weather['Total']*100\n",
    "weather_corr['Dawn or Dark']=weather['Dawn or Dark']/weather['Total']*100\n",
    "weather_corr['Other/Unknown']=weather['Other/Unknown']/weather['Total']*100\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Percent of crashes for Different Lighting and Weather ')"
      ]
     },
     "metadata": {},
     "execution_count": 22
    },
    {
     "output_type": "display_data",
     "data": {
      "text/plain": "<Figure size 864x432 with 2 Axes>",
      "image/svg+xml": "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\r\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\r\n  \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\r\n<svg height=\"372.35625pt\" version=\"1.1\" viewBox=\"0 0 636.271125 372.35625\" width=\"636.271125pt\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\r\n <metadata>\r\n  <rdf:RDF xmlns:cc=\"http://creativecommons.org/ns#\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\">\r\n   <cc:Work>\r\n    <dc:type rdf:resource=\"http://purl.org/dc/dcmitype/StillImage\"/>\r\n    <dc:date>2021-07-08T11:35:53.890782</dc:date>\r\n    <dc:format>image/svg+xml</dc:format>\r\n    <dc:creator>\r\n     <cc:Agent>\r\n      <dc:title>Matplotlib v3.4.2, https://matplotlib.org/</dc:title>\r\n     </cc:Agent>\r\n    </dc:creator>\r\n   </cc:Work>\r\n  </rdf:RDF>\r\n </metadata>\r\n <defs>\r\n  <style type=\"text/css\">*{stroke-linecap:butt;stroke-linejoin:round;}</style>\r\n </defs>\r\n <g id=\"figure_1\">\r\n  <g id=\"patch_1\">\r\n   <path d=\"M 0 372.35625 \r\nL 636.271125 372.35625 \r\nL 636.271125 0 \r\nL 0 0 \r\nz\r\n\" style=\"fill:none;\"/>\r\n  </g>\r\n  <g id=\"axes_1\">\r\n   <g id=\"patch_2\">\r\n    <path d=\"M 23.878125 348.478125 \r\nL 559.558125 348.478125 \r\nL 559.558125 22.318125 \r\nL 23.878125 22.318125 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"QuadMesh_1\">\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 23.878125 22.318125 \r\nL 131.014125 22.318125 \r\nL 131.014125 87.550125 \r\nL 23.878125 87.550125 \r\nL 23.878125 22.318125 \r\n\" style=\"fill:#f8d4bc;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 131.014125 22.318125 \r\nL 238.150125 22.318125 \r\nL 238.150125 87.550125 \r\nL 131.014125 87.550125 \r\nL 131.014125 22.318125 \r\n\" style=\"fill:#841e5a;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 238.150125 22.318125 \r\nL 345.286125 22.318125 \r\nL 345.286125 87.550125 \r\nL 238.150125 87.550125 \r\nL 238.150125 22.318125 \r\n\" style=\"fill:#d2204c;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 345.286125 22.318125 \r\nL 452.422125 22.318125 \r\nL 452.422125 87.550125 \r\nL 345.286125 87.550125 \r\nL 345.286125 22.318125 \r\n\" style=\"fill:#1d112c;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 452.422125 22.318125 \r\nL 559.558125 22.318125 \r\nL 559.558125 87.550125 \r\nL 452.422125 87.550125 \r\nL 452.422125 22.318125 \r\n\" style=\"fill:#04051a;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 23.878125 87.550125 \r\nL 131.014125 87.550125 \r\nL 131.014125 152.782125 \r\nL 23.878125 152.782125 \r\nL 23.878125 87.550125 \r\n\" style=\"fill:#f5966c;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 131.014125 87.550125 \r\nL 238.150125 87.550125 \r\nL 238.150125 152.782125 \r\nL 131.014125 152.782125 \r\nL 131.014125 87.550125 \r\n\" style=\"fill:#b71657;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 238.150125 87.550125 \r\nL 345.286125 87.550125 \r\nL 345.286125 152.782125 \r\nL 238.150125 152.782125 \r\nL 238.150125 87.550125 \r\n\" style=\"fill:#d72549;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 345.286125 87.550125 \r\nL 452.422125 87.550125 \r\nL 452.422125 152.782125 \r\nL 345.286125 152.782125 \r\nL 345.286125 87.550125 \r\n\" style=\"fill:#271534;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 452.422125 87.550125 \r\nL 559.558125 87.550125 \r\nL 559.558125 152.782125 \r\nL 452.422125 152.782125 \r\nL 452.422125 87.550125 \r\n\" style=\"fill:#03051a;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 23.878125 152.782125 \r\nL 131.014125 152.782125 \r\nL 131.014125 218.014125 \r\nL 23.878125 218.014125 \r\nL 23.878125 152.782125 \r\n\" style=\"fill:#faebdd;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 131.014125 152.782125 \r\nL 238.150125 152.782125 \r\nL 238.150125 218.014125 \r\nL 131.014125 218.014125 \r\nL 131.014125 152.782125 \r\n\" style=\"fill:#491d49;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 238.150125 152.782125 \r\nL 345.286125 152.782125 \r\nL 345.286125 218.014125 \r\nL 238.150125 218.014125 \r\nL 238.150125 152.782125 \r\n\" style=\"fill:#e23442;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 345.286125 152.782125 \r\nL 452.422125 152.782125 \r\nL 452.422125 218.014125 \r\nL 345.286125 218.014125 \r\nL 345.286125 152.782125 \r\n\" style=\"fill:#281535;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 452.422125 152.782125 \r\nL 559.558125 152.782125 \r\nL 559.558125 218.014125 \r\nL 452.422125 218.014125 \r\nL 452.422125 152.782125 \r\n\" style=\"fill:#03051a;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 23.878125 218.014125 \r\nL 131.014125 218.014125 \r\nL 131.014125 283.246125 \r\nL 23.878125 283.246125 \r\nL 23.878125 218.014125 \r\n\" style=\"fill:#e23442;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 131.014125 218.014125 \r\nL 238.150125 218.014125 \r\nL 238.150125 283.246125 \r\nL 131.014125 283.246125 \r\nL 131.014125 218.014125 \r\n\" style=\"fill:#5e1f52;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 238.150125 218.014125 \r\nL 345.286125 218.014125 \r\nL 345.286125 283.246125 \r\nL 238.150125 283.246125 \r\nL 238.150125 218.014125 \r\n\" style=\"fill:#f6b893;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 345.286125 218.014125 \r\nL 452.422125 218.014125 \r\nL 452.422125 283.246125 \r\nL 345.286125 283.246125 \r\nL 345.286125 218.014125 \r\n\" style=\"fill:#461c48;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 452.422125 218.014125 \r\nL 559.558125 218.014125 \r\nL 559.558125 283.246125 \r\nL 452.422125 283.246125 \r\nL 452.422125 218.014125 \r\n\" style=\"fill:#04051a;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 23.878125 283.246125 \r\nL 131.014125 283.246125 \r\nL 131.014125 348.478125 \r\nL 23.878125 348.478125 \r\nL 23.878125 283.246125 \r\n\" style=\"fill:#d72549;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 131.014125 283.246125 \r\nL 238.150125 283.246125 \r\nL 238.150125 348.478125 \r\nL 131.014125 348.478125 \r\nL 131.014125 283.246125 \r\n\" style=\"fill:#31183b;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 238.150125 283.246125 \r\nL 345.286125 283.246125 \r\nL 345.286125 348.478125 \r\nL 238.150125 348.478125 \r\nL 238.150125 283.246125 \r\n\" style=\"fill:#eb463e;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 345.286125 283.246125 \r\nL 452.422125 283.246125 \r\nL 452.422125 348.478125 \r\nL 345.286125 348.478125 \r\nL 345.286125 283.246125 \r\n\" style=\"fill:#140e26;stroke:#ffffff;stroke-width:0.5;\"/>\r\n    <path clip-path=\"url(#pe6085c41b8)\" d=\"M 452.422125 283.246125 \r\nL 559.558125 283.246125 \r\nL 559.558125 348.478125 \r\nL 452.422125 348.478125 \r\nL 452.422125 283.246125 \r\n\" style=\"fill:#d72549;stroke:#ffffff;stroke-width:0.5;\"/>\r\n   </g>\r\n   <g id=\"matplotlib.axis_1\">\r\n    <g id=\"xtick_1\">\r\n     <g id=\"line2d_1\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 0 3.5 \r\n\" id=\"m037c47bdee\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"77.446125\" xlink:href=\"#m037c47bdee\" y=\"348.478125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_1\">\r\n      <!-- Daylight -->\r\n      <g transform=\"translate(56.491438 363.076563)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 1259 4147 \r\nL 1259 519 \r\nL 2022 519 \r\nQ 2988 519 3436 956 \r\nQ 3884 1394 3884 2338 \r\nQ 3884 3275 3436 3711 \r\nQ 2988 4147 2022 4147 \r\nL 1259 4147 \r\nz\r\nM 628 4666 \r\nL 1925 4666 \r\nQ 3281 4666 3915 4102 \r\nQ 4550 3538 4550 2338 \r\nQ 4550 1131 3912 565 \r\nQ 3275 0 1925 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-44\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2194 1759 \r\nQ 1497 1759 1228 1600 \r\nQ 959 1441 959 1056 \r\nQ 959 750 1161 570 \r\nQ 1363 391 1709 391 \r\nQ 2188 391 2477 730 \r\nQ 2766 1069 2766 1631 \r\nL 2766 1759 \r\nL 2194 1759 \r\nz\r\nM 3341 1997 \r\nL 3341 0 \r\nL 2766 0 \r\nL 2766 531 \r\nQ 2569 213 2275 61 \r\nQ 1981 -91 1556 -91 \r\nQ 1019 -91 701 211 \r\nQ 384 513 384 1019 \r\nQ 384 1609 779 1909 \r\nQ 1175 2209 1959 2209 \r\nL 2766 2209 \r\nL 2766 2266 \r\nQ 2766 2663 2505 2880 \r\nQ 2244 3097 1772 3097 \r\nQ 1472 3097 1187 3025 \r\nQ 903 2953 641 2809 \r\nL 641 3341 \r\nQ 956 3463 1253 3523 \r\nQ 1550 3584 1831 3584 \r\nQ 2591 3584 2966 3190 \r\nQ 3341 2797 3341 1997 \r\nz\r\n\" id=\"DejaVuSans-61\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2059 -325 \r\nQ 1816 -950 1584 -1140 \r\nQ 1353 -1331 966 -1331 \r\nL 506 -1331 \r\nL 506 -850 \r\nL 844 -850 \r\nQ 1081 -850 1212 -737 \r\nQ 1344 -625 1503 -206 \r\nL 1606 56 \r\nL 191 3500 \r\nL 800 3500 \r\nL 1894 763 \r\nL 2988 3500 \r\nL 3597 3500 \r\nL 2059 -325 \r\nz\r\n\" id=\"DejaVuSans-79\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 603 4863 \r\nL 1178 4863 \r\nL 1178 0 \r\nL 603 0 \r\nL 603 4863 \r\nz\r\n\" id=\"DejaVuSans-6c\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 603 3500 \r\nL 1178 3500 \r\nL 1178 0 \r\nL 603 0 \r\nL 603 3500 \r\nz\r\nM 603 4863 \r\nL 1178 4863 \r\nL 1178 4134 \r\nL 603 4134 \r\nL 603 4863 \r\nz\r\n\" id=\"DejaVuSans-69\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2906 1791 \r\nQ 2906 2416 2648 2759 \r\nQ 2391 3103 1925 3103 \r\nQ 1463 3103 1205 2759 \r\nQ 947 2416 947 1791 \r\nQ 947 1169 1205 825 \r\nQ 1463 481 1925 481 \r\nQ 2391 481 2648 825 \r\nQ 2906 1169 2906 1791 \r\nz\r\nM 3481 434 \r\nQ 3481 -459 3084 -895 \r\nQ 2688 -1331 1869 -1331 \r\nQ 1566 -1331 1297 -1286 \r\nQ 1028 -1241 775 -1147 \r\nL 775 -588 \r\nQ 1028 -725 1275 -790 \r\nQ 1522 -856 1778 -856 \r\nQ 2344 -856 2625 -561 \r\nQ 2906 -266 2906 331 \r\nL 2906 616 \r\nQ 2728 306 2450 153 \r\nQ 2172 0 1784 0 \r\nQ 1141 0 747 490 \r\nQ 353 981 353 1791 \r\nQ 353 2603 747 3093 \r\nQ 1141 3584 1784 3584 \r\nQ 2172 3584 2450 3431 \r\nQ 2728 3278 2906 2969 \r\nL 2906 3500 \r\nL 3481 3500 \r\nL 3481 434 \r\nz\r\n\" id=\"DejaVuSans-67\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-68\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 1172 4494 \r\nL 1172 3500 \r\nL 2356 3500 \r\nL 2356 3053 \r\nL 1172 3053 \r\nL 1172 1153 \r\nQ 1172 725 1289 603 \r\nQ 1406 481 1766 481 \r\nL 2356 481 \r\nL 2356 0 \r\nL 1766 0 \r\nQ 1100 0 847 248 \r\nQ 594 497 594 1153 \r\nL 594 3053 \r\nL 172 3053 \r\nL 172 3500 \r\nL 594 3500 \r\nL 594 4494 \r\nL 1172 4494 \r\nz\r\n\" id=\"DejaVuSans-74\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-44\"/>\r\n       <use x=\"77.001953\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"138.28125\" xlink:href=\"#DejaVuSans-79\"/>\r\n       <use x=\"197.460938\" xlink:href=\"#DejaVuSans-6c\"/>\r\n       <use x=\"225.244141\" xlink:href=\"#DejaVuSans-69\"/>\r\n       <use x=\"253.027344\" xlink:href=\"#DejaVuSans-67\"/>\r\n       <use x=\"316.503906\" xlink:href=\"#DejaVuSans-68\"/>\r\n       <use x=\"379.882812\" xlink:href=\"#DejaVuSans-74\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_2\">\r\n     <g id=\"line2d_2\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"184.582125\" xlink:href=\"#m037c47bdee\" y=\"348.478125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_2\">\r\n      <!-- Dark, but Lighted -->\r\n      <g transform=\"translate(140.918063 363.076563)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2631 2963 \r\nQ 2534 3019 2420 3045 \r\nQ 2306 3072 2169 3072 \r\nQ 1681 3072 1420 2755 \r\nQ 1159 2438 1159 1844 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1341 3275 1631 3429 \r\nQ 1922 3584 2338 3584 \r\nQ 2397 3584 2469 3576 \r\nQ 2541 3569 2628 3553 \r\nL 2631 2963 \r\nz\r\n\" id=\"DejaVuSans-72\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 581 4863 \r\nL 1159 4863 \r\nL 1159 1991 \r\nL 2875 3500 \r\nL 3609 3500 \r\nL 1753 1863 \r\nL 3688 0 \r\nL 2938 0 \r\nL 1159 1709 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nz\r\n\" id=\"DejaVuSans-6b\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 750 794 \r\nL 1409 794 \r\nL 1409 256 \r\nL 897 -744 \r\nL 494 -744 \r\nL 750 256 \r\nL 750 794 \r\nz\r\n\" id=\"DejaVuSans-2c\" transform=\"scale(0.015625)\"/>\r\n        <path id=\"DejaVuSans-20\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3116 1747 \r\nQ 3116 2381 2855 2742 \r\nQ 2594 3103 2138 3103 \r\nQ 1681 3103 1420 2742 \r\nQ 1159 2381 1159 1747 \r\nQ 1159 1113 1420 752 \r\nQ 1681 391 2138 391 \r\nQ 2594 391 2855 752 \r\nQ 3116 1113 3116 1747 \r\nz\r\nM 1159 2969 \r\nQ 1341 3281 1617 3432 \r\nQ 1894 3584 2278 3584 \r\nQ 2916 3584 3314 3078 \r\nQ 3713 2572 3713 1747 \r\nQ 3713 922 3314 415 \r\nQ 2916 -91 2278 -91 \r\nQ 1894 -91 1617 61 \r\nQ 1341 213 1159 525 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 4863 \r\nL 1159 4863 \r\nL 1159 2969 \r\nz\r\n\" id=\"DejaVuSans-62\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 544 1381 \r\nL 544 3500 \r\nL 1119 3500 \r\nL 1119 1403 \r\nQ 1119 906 1312 657 \r\nQ 1506 409 1894 409 \r\nQ 2359 409 2629 706 \r\nQ 2900 1003 2900 1516 \r\nL 2900 3500 \r\nL 3475 3500 \r\nL 3475 0 \r\nL 2900 0 \r\nL 2900 538 \r\nQ 2691 219 2414 64 \r\nQ 2138 -91 1772 -91 \r\nQ 1169 -91 856 284 \r\nQ 544 659 544 1381 \r\nz\r\nM 1991 3584 \r\nL 1991 3584 \r\nz\r\n\" id=\"DejaVuSans-75\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 628 4666 \r\nL 1259 4666 \r\nL 1259 531 \r\nL 3531 531 \r\nL 3531 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4c\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3597 1894 \r\nL 3597 1613 \r\nL 953 1613 \r\nQ 991 1019 1311 708 \r\nQ 1631 397 2203 397 \r\nQ 2534 397 2845 478 \r\nQ 3156 559 3463 722 \r\nL 3463 178 \r\nQ 3153 47 2828 -22 \r\nQ 2503 -91 2169 -91 \r\nQ 1331 -91 842 396 \r\nQ 353 884 353 1716 \r\nQ 353 2575 817 3079 \r\nQ 1281 3584 2069 3584 \r\nQ 2775 3584 3186 3129 \r\nQ 3597 2675 3597 1894 \r\nz\r\nM 3022 2063 \r\nQ 3016 2534 2758 2815 \r\nQ 2500 3097 2075 3097 \r\nQ 1594 3097 1305 2825 \r\nQ 1016 2553 972 2059 \r\nL 3022 2063 \r\nz\r\n\" id=\"DejaVuSans-65\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 2906 2969 \r\nL 2906 4863 \r\nL 3481 4863 \r\nL 3481 0 \r\nL 2906 0 \r\nL 2906 525 \r\nQ 2725 213 2448 61 \r\nQ 2172 -91 1784 -91 \r\nQ 1150 -91 751 415 \r\nQ 353 922 353 1747 \r\nQ 353 2572 751 3078 \r\nQ 1150 3584 1784 3584 \r\nQ 2172 3584 2448 3432 \r\nQ 2725 3281 2906 2969 \r\nz\r\nM 947 1747 \r\nQ 947 1113 1208 752 \r\nQ 1469 391 1925 391 \r\nQ 2381 391 2643 752 \r\nQ 2906 1113 2906 1747 \r\nQ 2906 2381 2643 2742 \r\nQ 2381 3103 1925 3103 \r\nQ 1469 3103 1208 2742 \r\nQ 947 2381 947 1747 \r\nz\r\n\" id=\"DejaVuSans-64\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-44\"/>\r\n       <use x=\"77.001953\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"138.28125\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"179.394531\" xlink:href=\"#DejaVuSans-6b\"/>\r\n       <use x=\"237.304688\" xlink:href=\"#DejaVuSans-2c\"/>\r\n       <use x=\"269.091797\" xlink:href=\"#DejaVuSans-20\"/>\r\n       <use x=\"300.878906\" xlink:href=\"#DejaVuSans-62\"/>\r\n       <use x=\"364.355469\" xlink:href=\"#DejaVuSans-75\"/>\r\n       <use x=\"427.734375\" xlink:href=\"#DejaVuSans-74\"/>\r\n       <use x=\"466.943359\" xlink:href=\"#DejaVuSans-20\"/>\r\n       <use x=\"498.730469\" xlink:href=\"#DejaVuSans-4c\"/>\r\n       <use x=\"554.443359\" xlink:href=\"#DejaVuSans-69\"/>\r\n       <use x=\"582.226562\" xlink:href=\"#DejaVuSans-67\"/>\r\n       <use x=\"645.703125\" xlink:href=\"#DejaVuSans-68\"/>\r\n       <use x=\"709.082031\" xlink:href=\"#DejaVuSans-74\"/>\r\n       <use x=\"748.291016\" xlink:href=\"#DejaVuSans-65\"/>\r\n       <use x=\"809.814453\" xlink:href=\"#DejaVuSans-64\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_3\">\r\n     <g id=\"line2d_3\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"291.718125\" xlink:href=\"#m037c47bdee\" y=\"348.478125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_3\">\r\n      <!-- Dark -->\r\n      <g transform=\"translate(279.853281 363.076563)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-44\"/>\r\n       <use x=\"77.001953\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"138.28125\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"179.394531\" xlink:href=\"#DejaVuSans-6b\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_4\">\r\n     <g id=\"line2d_4\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"398.854125\" xlink:href=\"#m037c47bdee\" y=\"348.478125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_4\">\r\n      <!-- Dawn or Dark -->\r\n      <g transform=\"translate(364.524438 363.076563)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 269 3500 \r\nL 844 3500 \r\nL 1563 769 \r\nL 2278 3500 \r\nL 2956 3500 \r\nL 3675 769 \r\nL 4391 3500 \r\nL 4966 3500 \r\nL 4050 0 \r\nL 3372 0 \r\nL 2619 2869 \r\nL 1863 0 \r\nL 1184 0 \r\nL 269 3500 \r\nz\r\n\" id=\"DejaVuSans-77\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3513 2113 \r\nL 3513 0 \r\nL 2938 0 \r\nL 2938 2094 \r\nQ 2938 2591 2744 2837 \r\nQ 2550 3084 2163 3084 \r\nQ 1697 3084 1428 2787 \r\nQ 1159 2491 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1366 3272 1645 3428 \r\nQ 1925 3584 2291 3584 \r\nQ 2894 3584 3203 3211 \r\nQ 3513 2838 3513 2113 \r\nz\r\n\" id=\"DejaVuSans-6e\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 1959 3097 \r\nQ 1497 3097 1228 2736 \r\nQ 959 2375 959 1747 \r\nQ 959 1119 1226 758 \r\nQ 1494 397 1959 397 \r\nQ 2419 397 2687 759 \r\nQ 2956 1122 2956 1747 \r\nQ 2956 2369 2687 2733 \r\nQ 2419 3097 1959 3097 \r\nz\r\nM 1959 3584 \r\nQ 2709 3584 3137 3096 \r\nQ 3566 2609 3566 1747 \r\nQ 3566 888 3137 398 \r\nQ 2709 -91 1959 -91 \r\nQ 1206 -91 779 398 \r\nQ 353 888 353 1747 \r\nQ 353 2609 779 3096 \r\nQ 1206 3584 1959 3584 \r\nz\r\n\" id=\"DejaVuSans-6f\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-44\"/>\r\n       <use x=\"77.001953\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"138.28125\" xlink:href=\"#DejaVuSans-77\"/>\r\n       <use x=\"220.068359\" xlink:href=\"#DejaVuSans-6e\"/>\r\n       <use x=\"283.447266\" xlink:href=\"#DejaVuSans-20\"/>\r\n       <use x=\"315.234375\" xlink:href=\"#DejaVuSans-6f\"/>\r\n       <use x=\"376.416016\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"417.529297\" xlink:href=\"#DejaVuSans-20\"/>\r\n       <use x=\"449.316406\" xlink:href=\"#DejaVuSans-44\"/>\r\n       <use x=\"526.318359\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"587.597656\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"628.710938\" xlink:href=\"#DejaVuSans-6b\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"xtick_5\">\r\n     <g id=\"line2d_5\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"505.990125\" xlink:href=\"#m037c47bdee\" y=\"348.478125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_5\">\r\n      <!-- Other/Unknown -->\r\n      <g transform=\"translate(466.8995 363.076563)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2522 4238 \r\nQ 1834 4238 1429 3725 \r\nQ 1025 3213 1025 2328 \r\nQ 1025 1447 1429 934 \r\nQ 1834 422 2522 422 \r\nQ 3209 422 3611 934 \r\nQ 4013 1447 4013 2328 \r\nQ 4013 3213 3611 3725 \r\nQ 3209 4238 2522 4238 \r\nz\r\nM 2522 4750 \r\nQ 3503 4750 4090 4092 \r\nQ 4678 3434 4678 2328 \r\nQ 4678 1225 4090 567 \r\nQ 3503 -91 2522 -91 \r\nQ 1538 -91 948 565 \r\nQ 359 1222 359 2328 \r\nQ 359 3434 948 4092 \r\nQ 1538 4750 2522 4750 \r\nz\r\n\" id=\"DejaVuSans-4f\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 1625 4666 \r\nL 2156 4666 \r\nL 531 -594 \r\nL 0 -594 \r\nL 1625 4666 \r\nz\r\n\" id=\"DejaVuSans-2f\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 556 4666 \r\nL 1191 4666 \r\nL 1191 1831 \r\nQ 1191 1081 1462 751 \r\nQ 1734 422 2344 422 \r\nQ 2950 422 3222 751 \r\nQ 3494 1081 3494 1831 \r\nL 3494 4666 \r\nL 4128 4666 \r\nL 4128 1753 \r\nQ 4128 841 3676 375 \r\nQ 3225 -91 2344 -91 \r\nQ 1459 -91 1007 375 \r\nQ 556 841 556 1753 \r\nL 556 4666 \r\nz\r\n\" id=\"DejaVuSans-55\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-4f\"/>\r\n       <use x=\"78.710938\" xlink:href=\"#DejaVuSans-74\"/>\r\n       <use x=\"117.919922\" xlink:href=\"#DejaVuSans-68\"/>\r\n       <use x=\"181.298828\" xlink:href=\"#DejaVuSans-65\"/>\r\n       <use x=\"242.822266\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"283.935547\" xlink:href=\"#DejaVuSans-2f\"/>\r\n       <use x=\"317.626953\" xlink:href=\"#DejaVuSans-55\"/>\r\n       <use x=\"390.820312\" xlink:href=\"#DejaVuSans-6e\"/>\r\n       <use x=\"454.199219\" xlink:href=\"#DejaVuSans-6b\"/>\r\n       <use x=\"512.109375\" xlink:href=\"#DejaVuSans-6e\"/>\r\n       <use x=\"575.488281\" xlink:href=\"#DejaVuSans-6f\"/>\r\n       <use x=\"636.669922\" xlink:href=\"#DejaVuSans-77\"/>\r\n       <use x=\"718.457031\" xlink:href=\"#DejaVuSans-6e\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"matplotlib.axis_2\">\r\n    <g id=\"ytick_1\">\r\n     <g id=\"line2d_6\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL -3.5 0 \r\n\" id=\"m54bf258493\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"23.878125\" xlink:href=\"#m54bf258493\" y=\"54.934125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_6\">\r\n      <!-- Normal -->\r\n      <g transform=\"translate(14.798438 87.317719)rotate(-90)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 628 4666 \r\nL 1478 4666 \r\nL 3547 763 \r\nL 3547 4666 \r\nL 4159 4666 \r\nL 4159 0 \r\nL 3309 0 \r\nL 1241 3903 \r\nL 1241 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-4e\" transform=\"scale(0.015625)\"/>\r\n        <path d=\"M 3328 2828 \r\nQ 3544 3216 3844 3400 \r\nQ 4144 3584 4550 3584 \r\nQ 5097 3584 5394 3201 \r\nQ 5691 2819 5691 2113 \r\nL 5691 0 \r\nL 5113 0 \r\nL 5113 2094 \r\nQ 5113 2597 4934 2840 \r\nQ 4756 3084 4391 3084 \r\nQ 3944 3084 3684 2787 \r\nQ 3425 2491 3425 1978 \r\nL 3425 0 \r\nL 2847 0 \r\nL 2847 2094 \r\nQ 2847 2600 2669 2842 \r\nQ 2491 3084 2119 3084 \r\nQ 1678 3084 1418 2786 \r\nQ 1159 2488 1159 1978 \r\nL 1159 0 \r\nL 581 0 \r\nL 581 3500 \r\nL 1159 3500 \r\nL 1159 2956 \r\nQ 1356 3278 1631 3431 \r\nQ 1906 3584 2284 3584 \r\nQ 2666 3584 2933 3390 \r\nQ 3200 3197 3328 2828 \r\nz\r\n\" id=\"DejaVuSans-6d\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-4e\"/>\r\n       <use x=\"74.804688\" xlink:href=\"#DejaVuSans-6f\"/>\r\n       <use x=\"135.986328\" xlink:href=\"#DejaVuSans-72\"/>\r\n       <use x=\"175.349609\" xlink:href=\"#DejaVuSans-6d\"/>\r\n       <use x=\"272.761719\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"334.041016\" xlink:href=\"#DejaVuSans-6c\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_2\">\r\n     <g id=\"line2d_7\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"23.878125\" xlink:href=\"#m54bf258493\" y=\"120.166125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_7\">\r\n      <!-- Rain -->\r\n      <g transform=\"translate(14.798438 138.334094)rotate(-90)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 2841 2188 \r\nQ 3044 2119 3236 1894 \r\nQ 3428 1669 3622 1275 \r\nL 4263 0 \r\nL 3584 0 \r\nL 2988 1197 \r\nQ 2756 1666 2539 1819 \r\nQ 2322 1972 1947 1972 \r\nL 1259 1972 \r\nL 1259 0 \r\nL 628 0 \r\nL 628 4666 \r\nL 2053 4666 \r\nQ 2853 4666 3247 4331 \r\nQ 3641 3997 3641 3322 \r\nQ 3641 2881 3436 2590 \r\nQ 3231 2300 2841 2188 \r\nz\r\nM 1259 4147 \r\nL 1259 2491 \r\nL 2053 2491 \r\nQ 2509 2491 2742 2702 \r\nQ 2975 2913 2975 3322 \r\nQ 2975 3731 2742 3939 \r\nQ 2509 4147 2053 4147 \r\nL 1259 4147 \r\nz\r\n\" id=\"DejaVuSans-52\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-52\"/>\r\n       <use x=\"67.232422\" xlink:href=\"#DejaVuSans-61\"/>\r\n       <use x=\"128.511719\" xlink:href=\"#DejaVuSans-69\"/>\r\n       <use x=\"156.294922\" xlink:href=\"#DejaVuSans-6e\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_3\">\r\n     <g id=\"line2d_8\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"23.878125\" xlink:href=\"#m54bf258493\" y=\"185.398125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_8\">\r\n      <!-- Snow/Sleet -->\r\n      <g transform=\"translate(14.798438 237.303594)rotate(-90)scale(0.1 -0.1)\">\r\n       <defs>\r\n        <path d=\"M 3425 4513 \r\nL 3425 3897 \r\nQ 3066 4069 2747 4153 \r\nQ 2428 4238 2131 4238 \r\nQ 1616 4238 1336 4038 \r\nQ 1056 3838 1056 3469 \r\nQ 1056 3159 1242 3001 \r\nQ 1428 2844 1947 2747 \r\nL 2328 2669 \r\nQ 3034 2534 3370 2195 \r\nQ 3706 1856 3706 1288 \r\nQ 3706 609 3251 259 \r\nQ 2797 -91 1919 -91 \r\nQ 1588 -91 1214 -16 \r\nQ 841 59 441 206 \r\nL 441 856 \r\nQ 825 641 1194 531 \r\nQ 1563 422 1919 422 \r\nQ 2459 422 2753 634 \r\nQ 3047 847 3047 1241 \r\nQ 3047 1584 2836 1778 \r\nQ 2625 1972 2144 2069 \r\nL 1759 2144 \r\nQ 1053 2284 737 2584 \r\nQ 422 2884 422 3419 \r\nQ 422 4038 858 4394 \r\nQ 1294 4750 2059 4750 \r\nQ 2388 4750 2728 4690 \r\nQ 3069 4631 3425 4513 \r\nz\r\n\" id=\"DejaVuSans-53\" transform=\"scale(0.015625)\"/>\r\n       </defs>\r\n       <use xlink:href=\"#DejaVuSans-53\"/>\r\n       <use x=\"63.476562\" xlink:href=\"#DejaVuSans-6e\"/>\r\n       <use x=\"126.855469\" xlink:href=\"#DejaVuSans-6f\"/>\r\n       <use x=\"188.037109\" xlink:href=\"#DejaVuSans-77\"/>\r\n       <use x=\"269.824219\" xlink:href=\"#DejaVuSans-2f\"/>\r\n       <use x=\"303.515625\" xlink:href=\"#DejaVuSans-53\"/>\r\n       <use x=\"366.992188\" xlink:href=\"#DejaVuSans-6c\"/>\r\n       <use x=\"394.775391\" xlink:href=\"#DejaVuSans-65\"/>\r\n       <use x=\"456.298828\" xlink:href=\"#DejaVuSans-65\"/>\r\n       <use x=\"517.822266\" xlink:href=\"#DejaVuSans-74\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_4\">\r\n     <g id=\"line2d_9\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"23.878125\" xlink:href=\"#m54bf258493\" y=\"250.630125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_9\">\r\n      <!-- Other -->\r\n      <g transform=\"translate(14.798438 275.224656)rotate(-90)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-4f\"/>\r\n       <use x=\"78.710938\" xlink:href=\"#DejaVuSans-74\"/>\r\n       <use x=\"117.919922\" xlink:href=\"#DejaVuSans-68\"/>\r\n       <use x=\"181.298828\" xlink:href=\"#DejaVuSans-65\"/>\r\n       <use x=\"242.822266\" xlink:href=\"#DejaVuSans-72\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_5\">\r\n     <g id=\"line2d_10\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"23.878125\" xlink:href=\"#m54bf258493\" y=\"315.862125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_10\">\r\n      <!-- Unknown -->\r\n      <g transform=\"translate(14.798438 358.481656)rotate(-90)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-55\"/>\r\n       <use x=\"73.193359\" xlink:href=\"#DejaVuSans-6e\"/>\r\n       <use x=\"136.572266\" xlink:href=\"#DejaVuSans-6b\"/>\r\n       <use x=\"194.482422\" xlink:href=\"#DejaVuSans-6e\"/>\r\n       <use x=\"257.861328\" xlink:href=\"#DejaVuSans-6f\"/>\r\n       <use x=\"319.042969\" xlink:href=\"#DejaVuSans-77\"/>\r\n       <use x=\"400.830078\" xlink:href=\"#DejaVuSans-6e\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_11\">\r\n    <!-- 50 -->\r\n    <g style=\"fill:#262626;\" transform=\"translate(71.083625 57.6935)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 691 4666 \r\nL 3169 4666 \r\nL 3169 4134 \r\nL 1269 4134 \r\nL 1269 2991 \r\nQ 1406 3038 1543 3061 \r\nQ 1681 3084 1819 3084 \r\nQ 2600 3084 3056 2656 \r\nQ 3513 2228 3513 1497 \r\nQ 3513 744 3044 326 \r\nQ 2575 -91 1722 -91 \r\nQ 1428 -91 1123 -41 \r\nQ 819 9 494 109 \r\nL 494 744 \r\nQ 775 591 1075 516 \r\nQ 1375 441 1709 441 \r\nQ 2250 441 2565 725 \r\nQ 2881 1009 2881 1497 \r\nQ 2881 1984 2565 2268 \r\nQ 2250 2553 1709 2553 \r\nQ 1456 2553 1204 2497 \r\nQ 953 2441 691 2322 \r\nL 691 4666 \r\nz\r\n\" id=\"DejaVuSans-35\" transform=\"scale(0.015625)\"/>\r\n      <path d=\"M 2034 4250 \r\nQ 1547 4250 1301 3770 \r\nQ 1056 3291 1056 2328 \r\nQ 1056 1369 1301 889 \r\nQ 1547 409 2034 409 \r\nQ 2525 409 2770 889 \r\nQ 3016 1369 3016 2328 \r\nQ 3016 3291 2770 3770 \r\nQ 2525 4250 2034 4250 \r\nz\r\nM 2034 4750 \r\nQ 2819 4750 3233 4129 \r\nQ 3647 3509 3647 2328 \r\nQ 3647 1150 3233 529 \r\nQ 2819 -91 2034 -91 \r\nQ 1250 -91 836 529 \r\nQ 422 1150 422 2328 \r\nQ 422 3509 836 4129 \r\nQ 1250 4750 2034 4750 \r\nz\r\n\" id=\"DejaVuSans-30\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-35\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_12\">\r\n    <!-- 18 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(178.219625 57.6935)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 794 531 \r\nL 1825 531 \r\nL 1825 4091 \r\nL 703 3866 \r\nL 703 4441 \r\nL 1819 4666 \r\nL 2450 4666 \r\nL 2450 531 \r\nL 3481 531 \r\nL 3481 0 \r\nL 794 0 \r\nL 794 531 \r\nz\r\n\" id=\"DejaVuSans-31\" transform=\"scale(0.015625)\"/>\r\n      <path d=\"M 2034 2216 \r\nQ 1584 2216 1326 1975 \r\nQ 1069 1734 1069 1313 \r\nQ 1069 891 1326 650 \r\nQ 1584 409 2034 409 \r\nQ 2484 409 2743 651 \r\nQ 3003 894 3003 1313 \r\nQ 3003 1734 2745 1975 \r\nQ 2488 2216 2034 2216 \r\nz\r\nM 1403 2484 \r\nQ 997 2584 770 2862 \r\nQ 544 3141 544 3541 \r\nQ 544 4100 942 4425 \r\nQ 1341 4750 2034 4750 \r\nQ 2731 4750 3128 4425 \r\nQ 3525 4100 3525 3541 \r\nQ 3525 3141 3298 2862 \r\nQ 3072 2584 2669 2484 \r\nQ 3125 2378 3379 2068 \r\nQ 3634 1759 3634 1313 \r\nQ 3634 634 3220 271 \r\nQ 2806 -91 2034 -91 \r\nQ 1263 -91 848 271 \r\nQ 434 634 434 1313 \r\nQ 434 1759 690 2068 \r\nQ 947 2378 1403 2484 \r\nz\r\nM 1172 3481 \r\nQ 1172 3119 1398 2916 \r\nQ 1625 2713 2034 2713 \r\nQ 2441 2713 2670 2916 \r\nQ 2900 3119 2900 3481 \r\nQ 2900 3844 2670 4047 \r\nQ 2441 4250 2034 4250 \r\nQ 1625 4250 1398 4047 \r\nQ 1172 3844 1172 3481 \r\nz\r\n\" id=\"DejaVuSans-38\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-31\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-38\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_13\">\r\n    <!-- 28 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(285.355625 57.6935)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 1228 531 \r\nL 3431 531 \r\nL 3431 0 \r\nL 469 0 \r\nL 469 531 \r\nQ 828 903 1448 1529 \r\nQ 2069 2156 2228 2338 \r\nQ 2531 2678 2651 2914 \r\nQ 2772 3150 2772 3378 \r\nQ 2772 3750 2511 3984 \r\nQ 2250 4219 1831 4219 \r\nQ 1534 4219 1204 4116 \r\nQ 875 4013 500 3803 \r\nL 500 4441 \r\nQ 881 4594 1212 4672 \r\nQ 1544 4750 1819 4750 \r\nQ 2544 4750 2975 4387 \r\nQ 3406 4025 3406 3419 \r\nQ 3406 3131 3298 2873 \r\nQ 3191 2616 2906 2266 \r\nQ 2828 2175 2409 1742 \r\nQ 1991 1309 1228 531 \r\nz\r\n\" id=\"DejaVuSans-32\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-38\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_14\">\r\n    <!-- 4 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(395.672875 57.6935)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 2419 4116 \r\nL 825 1625 \r\nL 2419 1625 \r\nL 2419 4116 \r\nz\r\nM 2253 4666 \r\nL 3047 4666 \r\nL 3047 1625 \r\nL 3713 1625 \r\nL 3713 1100 \r\nL 3047 1100 \r\nL 3047 0 \r\nL 2419 0 \r\nL 2419 1100 \r\nL 313 1100 \r\nL 313 1709 \r\nL 2253 4666 \r\nz\r\n\" id=\"DejaVuSans-34\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-34\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_15\">\r\n    <!-- 0.22 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(494.857313 57.6935)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 684 794 \r\nL 1344 794 \r\nL 1344 0 \r\nL 684 0 \r\nL 684 794 \r\nz\r\n\" id=\"DejaVuSans-2e\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-30\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"159.033203\" xlink:href=\"#DejaVuSans-32\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_16\">\r\n    <!-- 42 -->\r\n    <g style=\"fill:#262626;\" transform=\"translate(71.083625 122.9255)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-34\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-32\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_17\">\r\n    <!-- 24 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(178.219625 122.9255)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-34\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_18\">\r\n    <!-- 29 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(285.355625 122.9255)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 703 97 \r\nL 703 672 \r\nQ 941 559 1184 500 \r\nQ 1428 441 1663 441 \r\nQ 2288 441 2617 861 \r\nQ 2947 1281 2994 2138 \r\nQ 2813 1869 2534 1725 \r\nQ 2256 1581 1919 1581 \r\nQ 1219 1581 811 2004 \r\nQ 403 2428 403 3163 \r\nQ 403 3881 828 4315 \r\nQ 1253 4750 1959 4750 \r\nQ 2769 4750 3195 4129 \r\nQ 3622 3509 3622 2328 \r\nQ 3622 1225 3098 567 \r\nQ 2575 -91 1691 -91 \r\nQ 1453 -91 1209 -44 \r\nQ 966 3 703 97 \r\nz\r\nM 1959 2075 \r\nQ 2384 2075 2632 2365 \r\nQ 2881 2656 2881 3163 \r\nQ 2881 3666 2632 3958 \r\nQ 2384 4250 1959 4250 \r\nQ 1534 4250 1286 3958 \r\nQ 1038 3666 1038 3163 \r\nQ 1038 2656 1286 2365 \r\nQ 1534 2075 1959 2075 \r\nz\r\n\" id=\"DejaVuSans-39\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-39\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_19\">\r\n    <!-- 5.5 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(390.902563 122.9255)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-35\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-35\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_20\">\r\n    <!-- 0.1 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(498.038563 122.9255)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-30\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-31\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_21\">\r\n    <!-- 53 -->\r\n    <g style=\"fill:#262626;\" transform=\"translate(71.083625 188.1575)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 2597 2516 \r\nQ 3050 2419 3304 2112 \r\nQ 3559 1806 3559 1356 \r\nQ 3559 666 3084 287 \r\nQ 2609 -91 1734 -91 \r\nQ 1441 -91 1130 -33 \r\nQ 819 25 488 141 \r\nL 488 750 \r\nQ 750 597 1062 519 \r\nQ 1375 441 1716 441 \r\nQ 2309 441 2620 675 \r\nQ 2931 909 2931 1356 \r\nQ 2931 1769 2642 2001 \r\nQ 2353 2234 1838 2234 \r\nL 1294 2234 \r\nL 1294 2753 \r\nL 1863 2753 \r\nQ 2328 2753 2575 2939 \r\nQ 2822 3125 2822 3475 \r\nQ 2822 3834 2567 4026 \r\nQ 2313 4219 1838 4219 \r\nQ 1578 4219 1281 4162 \r\nQ 984 4106 628 3988 \r\nL 628 4550 \r\nQ 988 4650 1302 4700 \r\nQ 1616 4750 1894 4750 \r\nQ 2613 4750 3031 4423 \r\nQ 3450 4097 3450 3541 \r\nQ 3450 3153 3228 2886 \r\nQ 3006 2619 2597 2516 \r\nz\r\n\" id=\"DejaVuSans-33\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-35\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-33\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_22\">\r\n    <!-- 10 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(178.219625 188.1575)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-31\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_23\">\r\n    <!-- 31 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(285.355625 188.1575)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-33\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-31\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_24\">\r\n    <!-- 5.7 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(390.902563 188.1575)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 525 4666 \r\nL 3525 4666 \r\nL 3525 4397 \r\nL 1831 0 \r\nL 1172 0 \r\nL 2766 4134 \r\nL 525 4134 \r\nL 525 4666 \r\nz\r\n\" id=\"DejaVuSans-37\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-35\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-37\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_25\">\r\n    <!-- 0 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(502.808875 188.1575)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-30\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_26\">\r\n    <!-- 31 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(71.083625 253.3895)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-33\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-31\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_27\">\r\n    <!-- 13 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(178.219625 253.3895)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-31\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-33\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_28\">\r\n    <!-- 46 -->\r\n    <g style=\"fill:#262626;\" transform=\"translate(285.355625 253.3895)scale(0.1 -0.1)\">\r\n     <defs>\r\n      <path d=\"M 2113 2584 \r\nQ 1688 2584 1439 2293 \r\nQ 1191 2003 1191 1497 \r\nQ 1191 994 1439 701 \r\nQ 1688 409 2113 409 \r\nQ 2538 409 2786 701 \r\nQ 3034 994 3034 1497 \r\nQ 3034 2003 2786 2293 \r\nQ 2538 2584 2113 2584 \r\nz\r\nM 3366 4563 \r\nL 3366 3988 \r\nQ 3128 4100 2886 4159 \r\nQ 2644 4219 2406 4219 \r\nQ 1781 4219 1451 3797 \r\nQ 1122 3375 1075 2522 \r\nQ 1259 2794 1537 2939 \r\nQ 1816 3084 2150 3084 \r\nQ 2853 3084 3261 2657 \r\nQ 3669 2231 3669 1497 \r\nQ 3669 778 3244 343 \r\nQ 2819 -91 2113 -91 \r\nQ 1303 -91 875 529 \r\nQ 447 1150 447 2328 \r\nQ 447 3434 972 4092 \r\nQ 1497 4750 2381 4750 \r\nQ 2619 4750 2861 4703 \r\nQ 3103 4656 3366 4563 \r\nz\r\n\" id=\"DejaVuSans-36\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-34\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-36\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_29\">\r\n    <!-- 9.9 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(390.902563 253.3895)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-39\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-39\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_30\">\r\n    <!-- 0.26 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(494.857313 253.3895)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-30\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"159.033203\" xlink:href=\"#DejaVuSans-36\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_31\">\r\n    <!-- 29 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(71.083625 318.6215)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-39\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_32\">\r\n    <!-- 6.9 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(176.630563 318.6215)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-36\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-39\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_33\">\r\n    <!-- 33 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(285.355625 318.6215)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-33\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-33\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_34\">\r\n    <!-- 2.8 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(390.902563 318.6215)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-2e\"/>\r\n     <use x=\"95.410156\" xlink:href=\"#DejaVuSans-38\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_35\">\r\n    <!-- 29 -->\r\n    <g style=\"fill:#ffffff;\" transform=\"translate(499.627625 318.6215)scale(0.1 -0.1)\">\r\n     <use xlink:href=\"#DejaVuSans-32\"/>\r\n     <use x=\"63.623047\" xlink:href=\"#DejaVuSans-39\"/>\r\n    </g>\r\n   </g>\r\n   <g id=\"text_36\">\r\n    <!-- Percent of crashes for Different Lighting and Weather  -->\r\n    <g transform=\"translate(129.488438 16.318125)scale(0.12 -0.12)\">\r\n     <defs>\r\n      <path d=\"M 1259 4147 \r\nL 1259 2394 \r\nL 2053 2394 \r\nQ 2494 2394 2734 2622 \r\nQ 2975 2850 2975 3272 \r\nQ 2975 3691 2734 3919 \r\nQ 2494 4147 2053 4147 \r\nL 1259 4147 \r\nz\r\nM 628 4666 \r\nL 2053 4666 \r\nQ 2838 4666 3239 4311 \r\nQ 3641 3956 3641 3272 \r\nQ 3641 2581 3239 2228 \r\nQ 2838 1875 2053 1875 \r\nL 1259 1875 \r\nL 1259 0 \r\nL 628 0 \r\nL 628 4666 \r\nz\r\n\" id=\"DejaVuSans-50\" transform=\"scale(0.015625)\"/>\r\n      <path d=\"M 3122 3366 \r\nL 3122 2828 \r\nQ 2878 2963 2633 3030 \r\nQ 2388 3097 2138 3097 \r\nQ 1578 3097 1268 2742 \r\nQ 959 2388 959 1747 \r\nQ 959 1106 1268 751 \r\nQ 1578 397 2138 397 \r\nQ 2388 397 2633 464 \r\nQ 2878 531 3122 666 \r\nL 3122 134 \r\nQ 2881 22 2623 -34 \r\nQ 2366 -91 2075 -91 \r\nQ 1284 -91 818 406 \r\nQ 353 903 353 1747 \r\nQ 353 2603 823 3093 \r\nQ 1294 3584 2113 3584 \r\nQ 2378 3584 2631 3529 \r\nQ 2884 3475 3122 3366 \r\nz\r\n\" id=\"DejaVuSans-63\" transform=\"scale(0.015625)\"/>\r\n      <path d=\"M 2375 4863 \r\nL 2375 4384 \r\nL 1825 4384 \r\nQ 1516 4384 1395 4259 \r\nQ 1275 4134 1275 3809 \r\nL 1275 3500 \r\nL 2222 3500 \r\nL 2222 3053 \r\nL 1275 3053 \r\nL 1275 0 \r\nL 697 0 \r\nL 697 3053 \r\nL 147 3053 \r\nL 147 3500 \r\nL 697 3500 \r\nL 697 3744 \r\nQ 697 4328 969 4595 \r\nQ 1241 4863 1831 4863 \r\nL 2375 4863 \r\nz\r\n\" id=\"DejaVuSans-66\" transform=\"scale(0.015625)\"/>\r\n      <path d=\"M 2834 3397 \r\nL 2834 2853 \r\nQ 2591 2978 2328 3040 \r\nQ 2066 3103 1784 3103 \r\nQ 1356 3103 1142 2972 \r\nQ 928 2841 928 2578 \r\nQ 928 2378 1081 2264 \r\nQ 1234 2150 1697 2047 \r\nL 1894 2003 \r\nQ 2506 1872 2764 1633 \r\nQ 3022 1394 3022 966 \r\nQ 3022 478 2636 193 \r\nQ 2250 -91 1575 -91 \r\nQ 1294 -91 989 -36 \r\nQ 684 19 347 128 \r\nL 347 722 \r\nQ 666 556 975 473 \r\nQ 1284 391 1588 391 \r\nQ 1994 391 2212 530 \r\nQ 2431 669 2431 922 \r\nQ 2431 1156 2273 1281 \r\nQ 2116 1406 1581 1522 \r\nL 1381 1569 \r\nQ 847 1681 609 1914 \r\nQ 372 2147 372 2553 \r\nQ 372 3047 722 3315 \r\nQ 1072 3584 1716 3584 \r\nQ 2034 3584 2315 3537 \r\nQ 2597 3491 2834 3397 \r\nz\r\n\" id=\"DejaVuSans-73\" transform=\"scale(0.015625)\"/>\r\n      <path d=\"M 213 4666 \r\nL 850 4666 \r\nL 1831 722 \r\nL 2809 4666 \r\nL 3519 4666 \r\nL 4500 722 \r\nL 5478 4666 \r\nL 6119 4666 \r\nL 4947 0 \r\nL 4153 0 \r\nL 3169 4050 \r\nL 2175 0 \r\nL 1381 0 \r\nL 213 4666 \r\nz\r\n\" id=\"DejaVuSans-57\" transform=\"scale(0.015625)\"/>\r\n     </defs>\r\n     <use xlink:href=\"#DejaVuSans-50\"/>\r\n     <use x=\"56.677734\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"118.201172\" xlink:href=\"#DejaVuSans-72\"/>\r\n     <use x=\"157.064453\" xlink:href=\"#DejaVuSans-63\"/>\r\n     <use x=\"212.044922\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"273.568359\" xlink:href=\"#DejaVuSans-6e\"/>\r\n     <use x=\"336.947266\" xlink:href=\"#DejaVuSans-74\"/>\r\n     <use x=\"376.15625\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"407.943359\" xlink:href=\"#DejaVuSans-6f\"/>\r\n     <use x=\"469.125\" xlink:href=\"#DejaVuSans-66\"/>\r\n     <use x=\"504.330078\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"536.117188\" xlink:href=\"#DejaVuSans-63\"/>\r\n     <use x=\"591.097656\" xlink:href=\"#DejaVuSans-72\"/>\r\n     <use x=\"632.210938\" xlink:href=\"#DejaVuSans-61\"/>\r\n     <use x=\"693.490234\" xlink:href=\"#DejaVuSans-73\"/>\r\n     <use x=\"745.589844\" xlink:href=\"#DejaVuSans-68\"/>\r\n     <use x=\"808.96875\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"870.492188\" xlink:href=\"#DejaVuSans-73\"/>\r\n     <use x=\"922.591797\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"954.378906\" xlink:href=\"#DejaVuSans-66\"/>\r\n     <use x=\"989.583984\" xlink:href=\"#DejaVuSans-6f\"/>\r\n     <use x=\"1050.765625\" xlink:href=\"#DejaVuSans-72\"/>\r\n     <use x=\"1091.878906\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"1123.666016\" xlink:href=\"#DejaVuSans-44\"/>\r\n     <use x=\"1200.667969\" xlink:href=\"#DejaVuSans-69\"/>\r\n     <use x=\"1228.451172\" xlink:href=\"#DejaVuSans-66\"/>\r\n     <use x=\"1263.65625\" xlink:href=\"#DejaVuSans-66\"/>\r\n     <use x=\"1298.861328\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"1360.384766\" xlink:href=\"#DejaVuSans-72\"/>\r\n     <use x=\"1399.248047\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"1460.771484\" xlink:href=\"#DejaVuSans-6e\"/>\r\n     <use x=\"1524.150391\" xlink:href=\"#DejaVuSans-74\"/>\r\n     <use x=\"1563.359375\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"1595.146484\" xlink:href=\"#DejaVuSans-4c\"/>\r\n     <use x=\"1650.859375\" xlink:href=\"#DejaVuSans-69\"/>\r\n     <use x=\"1678.642578\" xlink:href=\"#DejaVuSans-67\"/>\r\n     <use x=\"1742.119141\" xlink:href=\"#DejaVuSans-68\"/>\r\n     <use x=\"1805.498047\" xlink:href=\"#DejaVuSans-74\"/>\r\n     <use x=\"1844.707031\" xlink:href=\"#DejaVuSans-69\"/>\r\n     <use x=\"1872.490234\" xlink:href=\"#DejaVuSans-6e\"/>\r\n     <use x=\"1935.869141\" xlink:href=\"#DejaVuSans-67\"/>\r\n     <use x=\"1999.345703\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"2031.132812\" xlink:href=\"#DejaVuSans-61\"/>\r\n     <use x=\"2092.412109\" xlink:href=\"#DejaVuSans-6e\"/>\r\n     <use x=\"2155.791016\" xlink:href=\"#DejaVuSans-64\"/>\r\n     <use x=\"2219.267578\" xlink:href=\"#DejaVuSans-20\"/>\r\n     <use x=\"2251.054688\" xlink:href=\"#DejaVuSans-57\"/>\r\n     <use x=\"2344.056641\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"2405.580078\" xlink:href=\"#DejaVuSans-61\"/>\r\n     <use x=\"2466.859375\" xlink:href=\"#DejaVuSans-74\"/>\r\n     <use x=\"2506.068359\" xlink:href=\"#DejaVuSans-68\"/>\r\n     <use x=\"2569.447266\" xlink:href=\"#DejaVuSans-65\"/>\r\n     <use x=\"2630.970703\" xlink:href=\"#DejaVuSans-72\"/>\r\n     <use x=\"2672.083984\" xlink:href=\"#DejaVuSans-20\"/>\r\n    </g>\r\n   </g>\r\n  </g>\r\n  <g id=\"axes_2\">\r\n   <g id=\"patch_3\">\r\n    <path d=\"M 593.038125 348.478125 \r\nL 609.346125 348.478125 \r\nL 609.346125 22.318125 \r\nL 593.038125 22.318125 \r\nz\r\n\" style=\"fill:#ffffff;\"/>\r\n   </g>\r\n   <g id=\"patch_4\">\r\n    <path clip-path=\"url(#pfa523019f8)\" d=\"M 593.038125 348.478125 \r\nL 593.038125 347.204062 \r\nL 593.038125 23.592187 \r\nL 593.038125 22.318125 \r\nL 609.346125 22.318125 \r\nL 609.346125 23.592187 \r\nL 609.346125 347.204062 \r\nL 609.346125 348.478125 \r\nL 609.346125 348.478125 \r\nz\r\n\" style=\"fill:#ffffff;stroke:#ffffff;stroke-linejoin:miter;stroke-width:0.01;\"/>\r\n   </g>\r\n   <image height=\"326\" id=\"image4390723aa2\" transform=\"scale(1 -1)translate(0 -326)\" width=\"16\" x=\"593\" xlink:href=\"data:image/png;base64,\r\niVBORw0KGgoAAAANSUhEUgAAABAAAAFGCAYAAABjUx8/AAABuklEQVR4nO2cwQ3DMAwD7dRdovvvmQ5xAo4WlH8E6kxKAdJmf76/d4HrbHL3WuvszUo8UABXcPaiBXQGj86AK/Ah2j4YiAlxTkgjNpJ9ChFGYiL8mViwG+0WWqRxIPoDxVeQkMb7GeAWOAN0e5OxbhsJK4iASBXoRioIkw0xwEg8C1SBPQ8qnAgLNGCgbyb/FHoYiV0RY91W4EPUfeCfQkQasYJhwNOI3jJ1gYgL2E4MYKAbKYABLjAQC+aBDtFnMEbiDHALFUZiPXAG+nYugPhSiFRBAAPdSBsrYAISxrrOACtIcCJMUwQDWGDDZ5zz0AIBIw23YEOseEGBC+hGgi1UQNQZwO2aAJG3cH8aYQnOYIwUwAAr6OFEpiDCSFDB6gDRLkCbCICot4AVVBgJvqgqgCgrqDASfftvM8AtRDhRLhDwwzadwVkPw9AjjbQA3CwBEAtO4X4G9A9Rk8YEiOPEhN1IrXwWX64Y4hjJZ8DXu80gAGJAmOxTmJEWwkBPY8DT+v0QfSf6DMZIXMHeH1QgAeL1pxCRRuaDSWNBmHoYyT4FauUOEOnHhTqkcUZawUem9GOsgMh88AfoPi5LGbweAAAAAABJRU5ErkJggg==\" y=\"-22\"/>\r\n   <g id=\"matplotlib.axis_3\"/>\r\n   <g id=\"matplotlib.axis_4\">\r\n    <g id=\"ytick_6\">\r\n     <g id=\"line2d_11\">\r\n      <defs>\r\n       <path d=\"M 0 0 \r\nL 3.5 0 \r\n\" id=\"mdc3cada612\" style=\"stroke:#000000;stroke-width:0.8;\"/>\r\n      </defs>\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"609.346125\" xlink:href=\"#mdc3cada612\" y=\"348.478125\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_37\">\r\n      <!-- 0 -->\r\n      <g transform=\"translate(616.346125 352.277344)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_7\">\r\n     <g id=\"line2d_12\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"609.346125\" xlink:href=\"#mdc3cada612\" y=\"287.267276\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_38\">\r\n      <!-- 10 -->\r\n      <g transform=\"translate(616.346125 291.066494)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-31\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_8\">\r\n     <g id=\"line2d_13\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"609.346125\" xlink:href=\"#mdc3cada612\" y=\"226.056426\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_39\">\r\n      <!-- 20 -->\r\n      <g transform=\"translate(616.346125 229.855645)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-32\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_9\">\r\n     <g id=\"line2d_14\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"609.346125\" xlink:href=\"#mdc3cada612\" y=\"164.845577\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_40\">\r\n      <!-- 30 -->\r\n      <g transform=\"translate(616.346125 168.644796)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-33\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_10\">\r\n     <g id=\"line2d_15\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"609.346125\" xlink:href=\"#mdc3cada612\" y=\"103.634728\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_41\">\r\n      <!-- 40 -->\r\n      <g transform=\"translate(616.346125 107.433946)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-34\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n    <g id=\"ytick_11\">\r\n     <g id=\"line2d_16\">\r\n      <g>\r\n       <use style=\"stroke:#000000;stroke-width:0.8;\" x=\"609.346125\" xlink:href=\"#mdc3cada612\" y=\"42.423878\"/>\r\n      </g>\r\n     </g>\r\n     <g id=\"text_42\">\r\n      <!-- 50 -->\r\n      <g transform=\"translate(616.346125 46.223097)scale(0.1 -0.1)\">\r\n       <use xlink:href=\"#DejaVuSans-35\"/>\r\n       <use x=\"63.623047\" xlink:href=\"#DejaVuSans-30\"/>\r\n      </g>\r\n     </g>\r\n    </g>\r\n   </g>\r\n   <g id=\"LineCollection_1\"/>\r\n   <g id=\"patch_5\">\r\n    <path d=\"M 593.038125 348.478125 \r\nL 593.038125 347.204062 \r\nL 593.038125 23.592187 \r\nL 593.038125 22.318125 \r\nL 609.346125 22.318125 \r\nL 609.346125 23.592187 \r\nL 609.346125 347.204062 \r\nL 609.346125 348.478125 \r\nz\r\n\" style=\"fill:none;\"/>\r\n   </g>\r\n  </g>\r\n </g>\r\n <defs>\r\n  <clipPath id=\"pe6085c41b8\">\r\n   <rect height=\"326.16\" width=\"535.68\" x=\"23.878125\" y=\"22.318125\"/>\r\n  </clipPath>\r\n  <clipPath id=\"pfa523019f8\">\r\n   <rect height=\"326.16\" width=\"16.308\" x=\"593.038125\" y=\"22.318125\"/>\r\n  </clipPath>\r\n </defs>\r\n</svg>\r\n",
      "image/png": "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\n"
     },
     "metadata": {
      "needs_background": "light"
     }
    }
   ],
   "source": [
    "#creating weather/lighting heatmap\n",
    "f,ax=plt.subplots(figsize=(12,6))\n",
    "sns.heatmap(weather_corr,annot=True, linewidths=.5,ax=ax).set_title(label='Percent of crashes for Different Lighting and Weather ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {},
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "Rate Per 100,000 Drivers=%{x}<br>Age=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "h",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          36,
          26,
          21,
          18
         ],
         "xaxis": "x",
         "y": [
          "18 to 24 years",
          "25 to 44 years",
          "45 to 64 years",
          "65 years and over"
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Rate of Fatal Accidents by Age Group Per 100,000 Drivers"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Rate Per 100,000 Drivers"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Age"
         }
        }
       }
      }
     },
     "metadata": {}
    }
   ],
   "source": [
    "#age distribution bar graph\n",
    "age_graph=px.bar(age,y='Age',x='Rate Per 100,000 Drivers',orientation='h',title='Rate of Fatal Accidents by Age Group Per 100,000 Drivers')\n",
    "age_graph.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.6 64-bit"
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
   "version": "3.7.6"
  },
  "interpreter": {
   "hash": "ebe51bc29cbb86320c2af4d95b8e7378219f15cf78c07a088db8dccd96242301"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}