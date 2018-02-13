

```python
# import dependencies
import pandas as pd
import os
```


```python
# import files
school_file = os.path.join('Data', 'schools_complete.csv')
students_file = os.path.join('Data', 'students_complete.csv')
```


```python
# read csvs using pandas
school_pd = pd.read_csv(school_file)
student_pd = pd.read_csv(students_file)
```


```python
# make dataframes
school_df = pd.DataFrame(school_pd)
student_df = pd.DataFrame(student_pd)
```


```python
# get totals
total_schools = len(school_df)
total_students = len(student_df)
total_budget = school_df['budget'].sum()
```


```python
# get averages
avg_math = student_df['math_score'].mean()
avg_reading = student_df['reading_score'].mean()
```


```python
# get % of students passing math
num_passing_math = len(student_df.loc[student_df['math_score'] >= 70, :])
passing_math = num_passing_math / total_students

# get % of students passing reading
num_passing_reading = len(student_df.loc[student_df['reading_score'] >= 70, :])
passing_reading = num_passing_reading / total_students

# get overall % of passing students
overall_passing = (passing_math + passing_reading) / 2
```


```python
# create dictionary
d = {"Total Schools" : total_schools,
     "Total Students" : "{:,}".format(total_students),
     "Total Budget" : "${:,}".format(total_budget),
     "Average Math Score" : avg_math,
     "Average Reading Score" : avg_reading,
     "% Passing Math" : '{:.2%}'.format(passing_math),
     "% Passing Reading" : '{:.2%}'.format(passing_reading),
     "Overall Passing %" : '{:.2%}'.format(overall_passing)}
# create dataframe from dictionary
high_level_df = pd.DataFrame(d, index=[0])
# print table
high_level_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing %</th>
      <th>Total Budget</th>
      <th>Total Schools</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>74.98%</td>
      <td>85.81%</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>80.39%</td>
      <td>$24,649,428</td>
      <td>15</td>
      <td>39,170</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get grouped summaries
grouped_school_summary = student_df.groupby('school').count()
average_score_group = student_df.groupby('school').mean()
# get school type
grouped_school_summary['School Type'] = school_pd['type'].values

# get school budgets
grouped_school_summary['Budget'] = school_pd['budget'].values

# Get Per student budget
grouped_school_summary['Budget per Student'] = grouped_school_summary['Budget'].values / grouped_school_summary['Student ID'].values

# get average math and reading scores
grouped_school_summary['Average Math Score'] = average_score_group['math_score'].values
grouped_school_summary['Average Reading Score'] = average_score_group['reading_score'].values

# get % passing
passing_math_df = student_df.loc[student_df['math_score'] >= 70, :].groupby('school').count()
passing_reading_df = student_df.loc[student_df['reading_score'] >= 70, :].groupby('school').count()
grouped_school_summary['% Passing Math'] = passing_math_df['Student ID'].values / grouped_school_summary['Student ID'].values
grouped_school_summary['% Passing Reading'] = passing_reading_df['Student ID'].values / grouped_school_summary['Student ID'].values
grouped_school_summary['Overall Passing %'] = (grouped_school_summary['% Passing Math'].values + grouped_school_summary['% Passing Reading'].values) / 2

# remove unecessary columns
cleaned_grouped_school_df = grouped_school_summary.iloc[ : , [0,6,7,8,9,10,11,12,13]]

# rename columns
cleaned_grouped_school_df = cleaned_grouped_school_df.rename(columns={"Student ID" : "Total Students"})
# print table
cleaned_grouped_school_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Students</th>
      <th>School Type</th>
      <th>Budget</th>
      <th>Budget per Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing %</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>4976</td>
      <td>District</td>
      <td>1910635</td>
      <td>383.970056</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>0.666801</td>
      <td>0.819333</td>
      <td>0.743067</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>1858</td>
      <td>District</td>
      <td>1884411</td>
      <td>1014.214747</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>0.955867</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>358.290946</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>0.733639</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739</td>
      <td>District</td>
      <td>3022020</td>
      <td>1103.329682</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>0.738043</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468</td>
      <td>Charter</td>
      <td>917500</td>
      <td>625.000000</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>0.952657</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>4635</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>284.697735</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>0.667530</td>
      <td>0.808630</td>
      <td>0.738080</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>427</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>2532.449649</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>0.925059</td>
      <td>0.962529</td>
      <td>0.943794</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>2917</td>
      <td>District</td>
      <td>3124928</td>
      <td>1071.281454</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>0.656839</td>
      <td>0.813164</td>
      <td>0.735002</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>4761</td>
      <td>Charter</td>
      <td>248087</td>
      <td>52.108171</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>0.660576</td>
      <td>0.812224</td>
      <td>0.736400</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>962</td>
      <td>Charter</td>
      <td>585858</td>
      <td>609.000000</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>0.952703</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>3999</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>262.415604</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>0.732933</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>1761</td>
      <td>District</td>
      <td>2547363</td>
      <td>1446.543441</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>0.938671</td>
      <td>0.958546</td>
      <td>0.948609</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>1635</td>
      <td>District</td>
      <td>3094650</td>
      <td>1892.752294</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>0.952905</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>2283</td>
      <td>District</td>
      <td>1763916</td>
      <td>772.630749</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>0.938677</td>
      <td>0.965396</td>
      <td>0.952037</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>1800</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>579.516667</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>0.933333</td>
      <td>0.966111</td>
      <td>0.949722</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get top 5 schools
top_5_schools_df = cleaned_grouped_school_df.sort_values(['Overall Passing %'], ascending = False).head()
top_5_schools_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Students</th>
      <th>School Type</th>
      <th>Budget</th>
      <th>Budget per Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing %</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>1858</td>
      <td>District</td>
      <td>1884411</td>
      <td>1014.214747</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>0.955867</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>1635</td>
      <td>District</td>
      <td>3094650</td>
      <td>1892.752294</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>0.952905</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>962</td>
      <td>Charter</td>
      <td>585858</td>
      <td>609.000000</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>0.952703</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468</td>
      <td>Charter</td>
      <td>917500</td>
      <td>625.000000</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>0.952657</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>2283</td>
      <td>District</td>
      <td>1763916</td>
      <td>772.630749</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>0.938677</td>
      <td>0.965396</td>
      <td>0.952037</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get bottom 5 schools
bottom_5_schools_df = cleaned_grouped_school_df.sort_values(['Overall Passing %'], ascending = True).head()
bottom_5_schools_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Students</th>
      <th>School Type</th>
      <th>Budget</th>
      <th>Budget per Student</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing %</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>3999</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>262.415604</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>0.732933</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>358.290946</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>0.733639</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>2917</td>
      <td>District</td>
      <td>3124928</td>
      <td>1071.281454</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>0.656839</td>
      <td>0.813164</td>
      <td>0.735002</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>4761</td>
      <td>Charter</td>
      <td>248087</td>
      <td>52.108171</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>0.660576</td>
      <td>0.812224</td>
      <td>0.736400</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739</td>
      <td>District</td>
      <td>3022020</td>
      <td>1103.329682</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>0.738043</td>
    </tr>
  </tbody>
</table>
</div>




```python
# grab certain columns
grouped_grade_math_df = student_df.iloc[ : , [3,4,6]]
# group by school and grade
grouped_grade_math_df = grouped_grade_math_df.groupby(['school', 'grade']).mean()
grouped_grade_math_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>math_score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.083676</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Cabrera High School</th>
      <th>10th</th>
      <td>83.154506</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>82.765560</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.094697</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Figueroa High School</th>
      <th>10th</th>
      <td>76.539974</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.884344</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.403037</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Ford High School</th>
      <th>10th</th>
      <td>77.672316</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.918058</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.361345</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Griffin High School</th>
      <th>10th</th>
      <td>84.229064</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.842105</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>82.044010</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hernandez High School</th>
      <th>10th</th>
      <td>77.337408</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.136029</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.438495</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Holden High School</th>
      <th>10th</th>
      <td>83.429825</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>85.000000</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.787402</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Huang High School</th>
      <th>10th</th>
      <td>75.908735</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.446602</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.027251</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Johnson High School</th>
      <th>10th</th>
      <td>76.691117</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.491653</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.187857</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Pena High School</th>
      <th>10th</th>
      <td>83.372000</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.328125</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.625455</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Rodriguez High School</th>
      <th>10th</th>
      <td>76.612500</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.395626</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.859966</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Shelton High School</th>
      <th>10th</th>
      <td>82.917411</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.383495</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.420755</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Thomas High School</th>
      <th>10th</th>
      <td>83.087886</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.498795</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.590022</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wilson High School</th>
      <th>10th</th>
      <td>83.724422</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.195326</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.085578</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wright High School</th>
      <th>10th</th>
      <td>84.010288</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.836782</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.644986</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
# grab certain columns
grouped_grade_reading_df = student_df.iloc[ : , [4,3,5]]
# group by school and grade
grouped_grade_reading_df = grouped_grade_reading_df.groupby(['school', 'grade']).mean()
grouped_grade_reading_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reading_score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>80.907183</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.945643</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.303155</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Cabrera High School</th>
      <th>10th</th>
      <td>84.253219</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.788382</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.676136</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Figueroa High School</th>
      <th>10th</th>
      <td>81.408912</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.640339</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.198598</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Ford High School</th>
      <th>10th</th>
      <td>81.262712</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.403642</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.632653</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Griffin High School</th>
      <th>10th</th>
      <td>83.706897</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.288089</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.369193</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hernandez High School</th>
      <th>10th</th>
      <td>80.660147</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.396140</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.866860</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Holden High School</th>
      <th>10th</th>
      <td>83.324561</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.815534</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.677165</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Huang High School</th>
      <th>10th</th>
      <td>81.512386</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.417476</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.290284</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Johnson High School</th>
      <th>10th</th>
      <td>80.773431</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.616027</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.260714</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Pena High School</th>
      <th>10th</th>
      <td>83.612000</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.335938</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.807273</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Rodriguez High School</th>
      <th>10th</th>
      <td>80.629808</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.864811</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.993127</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Shelton High School</th>
      <th>10th</th>
      <td>83.441964</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.373786</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>84.122642</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Thomas High School</th>
      <th>10th</th>
      <td>84.254157</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.585542</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.728850</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wilson High School</th>
      <th>10th</th>
      <td>84.021452</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.764608</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.939778</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wright High School</th>
      <th>10th</th>
      <td>83.812757</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.156322</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.073171</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# set bin ranges
budget_bins = [0,500,1500,2000,3000]
# set bin names
budget_bin_names = ['Low Spending', 'Average Spending', 'High Spending', 'Very High Spending']
# grab certain columns
budget_binned_df = cleaned_grouped_school_df.iloc[ : , [5,6,7,8]]
# cut into bins
budget_binned_df['Budget Summary'] = pd.cut(cleaned_grouped_school_df['Budget per Student'], budget_bins, labels = budget_bin_names)
# print table
budget_binned_df
```

    /Users/ddrossi93/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing %</th>
      <th>Budget Summary</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.033963</td>
      <td>0.666801</td>
      <td>0.819333</td>
      <td>0.743067</td>
      <td>Low Spending</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.975780</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>0.955867</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.158020</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>0.733639</td>
      <td>Low Spending</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.746258</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>0.738043</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.816757</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>0.952657</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.934412</td>
      <td>0.667530</td>
      <td>0.808630</td>
      <td>0.738080</td>
      <td>Low Spending</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.814988</td>
      <td>0.925059</td>
      <td>0.962529</td>
      <td>0.943794</td>
      <td>Very High Spending</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.182722</td>
      <td>0.656839</td>
      <td>0.813164</td>
      <td>0.735002</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.966394</td>
      <td>0.660576</td>
      <td>0.812224</td>
      <td>0.736400</td>
      <td>Low Spending</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.044699</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>0.952703</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.744686</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>0.732933</td>
      <td>Low Spending</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.725724</td>
      <td>0.938671</td>
      <td>0.958546</td>
      <td>0.948609</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.848930</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>0.952905</td>
      <td>High Spending</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.989488</td>
      <td>0.938677</td>
      <td>0.965396</td>
      <td>0.952037</td>
      <td>Average Spending</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.955000</td>
      <td>0.933333</td>
      <td>0.966111</td>
      <td>0.949722</td>
      <td>Average Spending</td>
    </tr>
  </tbody>
</table>
</div>




```python
# set bin ranges
size_bins = [0,1000,3000,5000]
# set bin names
size_bin_names = ['Small', 'Medium', 'Large']
# grab certain columns
size_binned_df = cleaned_grouped_school_df.iloc[ : , [5,6,7,8]]
# cut into bins
size_binned_df['School Size'] = pd.cut(cleaned_grouped_school_df['Total Students'], size_bins, labels = size_bin_names)
# print table
size_binned_df
```

    /Users/ddrossi93/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing %</th>
      <th>School Size</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.033963</td>
      <td>0.666801</td>
      <td>0.819333</td>
      <td>0.743067</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.975780</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>0.955867</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.158020</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>0.733639</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.746258</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>0.738043</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.816757</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>0.952657</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.934412</td>
      <td>0.667530</td>
      <td>0.808630</td>
      <td>0.738080</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.814988</td>
      <td>0.925059</td>
      <td>0.962529</td>
      <td>0.943794</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.182722</td>
      <td>0.656839</td>
      <td>0.813164</td>
      <td>0.735002</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.966394</td>
      <td>0.660576</td>
      <td>0.812224</td>
      <td>0.736400</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>84.044699</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>0.952703</td>
      <td>Small</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.744686</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>0.732933</td>
      <td>Large</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.725724</td>
      <td>0.938671</td>
      <td>0.958546</td>
      <td>0.948609</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.848930</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>0.952905</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.989488</td>
      <td>0.938677</td>
      <td>0.965396</td>
      <td>0.952037</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.955000</td>
      <td>0.933333</td>
      <td>0.966111</td>
      <td>0.949722</td>
      <td>Medium</td>
    </tr>
  </tbody>
</table>
</div>




```python
# group by school type and get averages
grouped_school_type_df = cleaned_grouped_school_df.groupby('School Type').mean()
# only grab needed columns
grouped_school_type_df = grouped_school_type_df.iloc[ :, [3,4,5,6,7]]
# print table
grouped_school_type_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing %</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>80.324201</td>
      <td>82.429369</td>
      <td>0.798740</td>
      <td>0.886242</td>
      <td>0.842491</td>
    </tr>
    <tr>
      <th>District</th>
      <td>80.556334</td>
      <td>82.643266</td>
      <td>0.822592</td>
      <td>0.898988</td>
      <td>0.860790</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
