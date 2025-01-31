const description = "Cinephobe: The Podcast Where Zach Harper, Amin Elhassan and Anthony Mayes review movies that are poorly rated on Rotten Tomatoes, and try to ascertain whether or not theose movies are accurately rated, or maybe didn't get a fair shake."

const about = `At the conclusion of each episode of Cinephobe, each of the three hosts will either “Phobe” or “Phile” the movie - effectively a binary review of the movie. Phobe meaning bad and Phile meaning good.`

const longtext = `Much to the host Zach Harper's chagrin, (sorry Zach) I decided to take a stab at creating a regression model to predict the review that each host would give a movie. Using a 80-20 Train/Test split, the accuracy of predictive models topped out around 75-80%. 

I was able to achieve accuracy above 80%, often pushing 85%, but those models were ascertained by running every possible combination of features, getting the accuracy, and keeping the highest score. I would hypothesize that this is overfitting to the test data, and that It is not likely that this would scale well with future Movie selections. 

This is a supervised model, so all of the data is labeled during analysis, and the nature of the data (categorical, numerical, or binary) is considered as well.`

const listHeading = 'The features considered for these models included:'

const listItems = [
    'Which host chose the movie. ',
    "Whether or not the movie cost money to stream",
    'The length of the movie',
    'Year the movie was released',
    'The Number of audience reviews on Rotten Tomatoes',
    'The Critics Score on Rotten Tomatoes, (expressed as a %)',
    'The Audience Score on Rotten Tomatoes, (expressed as a %)',
    'The combination of Critics and Audience score.',
    'The Budget of the movie,',
    'The Wordwide gross of the movie',
    'Genre – in this case movies can be multiple genres. And each is expressed as a binary value. For example, Space Jam 2 (phobe, btw) would be a 1 for animated, comedy and sports.',
    'Repeat Offender. A repeat offender is a member of the Cast/Crew of the featured movie that has appeared in multiple films featured on Cinephobe. I took the top ten most common repeat offenders and added them as a binary vector as well.',

]

const disc = `Open source tech used for this project includes Sklearn, React, Flask, Material UI and MUX charts, Seaborn, Pandas and Numpy. The front end is JS and React, the back end is a Flask API running sklearn models.

This is for educational purposes only, I hope that this is groundbreaking enough to guarantee me an A in this course. 
`

export default {
    description,
    about,
    longtext,
    listHeading,
    listItems,
    disc
}