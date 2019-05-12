# Dance... Or not?

Working with Spotify audio features data and supervised machine learning classification algortihms.

## Motivation

Some say genres are dead, some don't agree. What is true is that the way users consume music has changed drastically in the last 10 years. 

Playlist creation habits are very informative for audio streaming companies to make better music recommendations. It is because of the flexibility playlists offer to users that we set out to discover what other options there were to using genres as the main feature to make recommendation. 

One of those options was a song's danceability.

## What is danceability?

Danceability describes the degree to which a song is good for dancing based on its audio features, e.g. rhythm, tempo, valence.

## Why danceability?

Choosing danceability was a matter of personal opinion. It is our belief that one great option to create playlists and make recommendations is danceability. 

**Danceability** is a direct product of the audio features of a song, and therefore an accurate representation of these features.

This is the reason why we chose danceability as our target variable.

## The Question:

Can we predict the danceability class of a song from its audio features?

## The project

Use supervised learning classification algorithms to predict the danceability class of a track based on a set of audio features. 

The target variable, danceability, comes as a float between 0.0 and 1.0, in order to classify songs, this variable was discretized and binned into three categories:

  - No dancing here (0.0 - 0.49)
  - Dance around a little bit (0.5 - 0.69)
  - Dance like nobody's watching (0.70 - 1.0)
  
Making this a multiclass classification problem.

## The data

The dataset used in this project was build through web scraping and Spotify's API. It consists of 266,000 observations (songs) and the following predictor features:

  - Track name
  - Artist name
  - Album name
  - Playlists the song belongs to
  - Release date
  - Popularity
  - Duration in minutes
  - Acousticness
  - Tempo
  - Mode
  - Key
  - Valence
  - Instrumentalness
  - Speechiness
  - Liveness
  - Energy
  - Loudness
  - Time signature
  
  ## EDA
  
After binning the danceability variable into categories, we plotted the distribution of observations between the three classes to check for class imbalance before moving forward. We also used boxplots to detect outliers and anomalies in our feature columns.

### Categories

![](../master/images/Categories.jpeg) 




Even though the three classes were not perfectly balanced, the difference didn't make it necessary to solve the class imbalance problem through upsampling or downsampling, so once the few outliers we found were removed, we proceeded to a pairplot and correlation matrix in order to study the relationships between the different variables, and check the data for multicollinearity.


### Correlation Matrix

![](../master/images/correlations.png)




As there were **no strong correlations** between the different variables we plotted the histograms of the different continuous variables to check their distribution, and decide if scaling and normalization was needed before proceeding to the modeling phase. Even though some of the distributions were skewed, most were roughly normal, so normalization was not required. For the discrete features we used stacked plots to check the distribution of observation within the categories of each of these features.

Stacked Plot: Danceability vs. Key                          |  Stacked Plot: Danceability vs. Mode
:----------------------------------------------------------:|:------------------------------------------------------------:
![](../master/images/by_key.png)                            |  ![](../master/images/by_mode.png)



To finish our EDA, we created a SQLite3 database that we could query to find interesting patterns and relationships within the data.


Most popular songs                                          |  Songs most used in playlists
:----------------------------------------------------------:|:------------------------------------------------------------:
![](../master/images/Popularity_of_Songs.jpeg)              |  ![](../master/images/playlist_songs.png)




## Modeling

Our goal within modeling was not to minimize Type 1 or Type 2 errors, even though these are of course important, rather we were looking for the most accurate model, and we measured this using the F1 Micro Average score.

We tried a total of eight models and a dummy classifier as a baseline, for each of them our strategy was to use Grid Search in order to find the best hyperparameters, the ones that minimized the bias-variance trade off. The hyperparameters for which we were tuning our models were chosen because of their potential to prevent overfitting and account for small class imbalances.

### Summary

![](../master/images/Summary.png) 




Even though from the F1 Micro Average Scores it looks like the best models were KNN and Random Forest, both of these were overfit, which is why we chose XGBoost as our best model. 



### Confusion Matrix

![](../master/images/confusion_matrix_xgboost.png)



Classification Report                                       |  Feature Importance
:----------------------------------------------------------:|:------------------------------------------------------------:
![](../master/images/classification_report.png)            |  ![](../master/images/xgboost_feature_importance.png)



## Next Steps

  1. Try boosting algorithms: AdaBoost and Gradient Boosting
  
  2. Ensemble the three best models
  
  3. Build a recommendation system
  
