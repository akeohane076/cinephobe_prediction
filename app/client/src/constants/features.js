export const featureText = {
    'Cost':"Did the Movie cost $ to stream?",
    'Pick_0':"Zach's Pick",
    'Pick_1':"Amin's Pick",
    'Pick_2':"Mayes' Pick",
    'Pick_3':"Guest Pick",
    "Time":"Movie Length",
    "RT Crit":"Rotten Tomatoes Critic Rating",
    "RT Aud":"Rotten Tomatoes Audience Rating",
    'Aud #':"Number of Audience Ratings",
    'Combo':"Audience score + Critics score",
    'Budget':"Filming Budget",
    'Box Off WW':"World Wide Box Office Gross",
    'Action':'Action',
     'Comedy':'Comedy',
     'Drama':'Drama',
     'Horror':'Horror',
     'Romance':'Romance',
     'Sci-Fi':'Sci-Fi',
     'Animation':'Animation',
     'Thriller':'Thriller',
     'Martial Arts': 'Martial Arts',
     'Superhero':'Superhero',
     'Sports':'Sports',
     'Musical':'Musical',
     'Western':'Western',
     "Pick": 'Who Picked It?'
}

export const convertText = (text) => {
    if (featureText[text]){
        return featureText[text]
    }
    return text
}