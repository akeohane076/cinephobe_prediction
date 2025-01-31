const whoPickedIt = (val) => {
    if (val === 0) {
        return {
            "Pick_0": 1
        }
    }
    if (val === 1) {
        return {
            "Pick_1": 1
        }
    }
    if (val === 2) {
        return {
            "Pick_2": 1
        }
    }

}

export const getBody = (data, aud = 0, numReviews, ww, budget, pick) => {

    const rtCrit = parseInt(data.Ratings.filter(rating => rating.Source === "Rotten Tomatoes")[0].Value)

    console.log(data)
    const modData = {
        'RT Crit': rtCrit,
        'RT Aud': aud,
        "Time": parseInt(data.Runtime),
        "Comedy": data.Genre.toLowerCase().includes("comedy") ? 1 : 0,
        "Combo": aud + rtCrit,
        "Box Off WW": ww,
        "Budget": budget,
        "Aud #": numReviews,
        ...whoPickedIt(pick)

    }

    const payload = {
        'data': modData
    }

    return modData

}