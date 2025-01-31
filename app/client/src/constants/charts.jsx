import { Apps, BarChart, Leaderboard, StackedBarChart, SignalCellularAlt, Grid3x3, Grid4x4 } from "@mui/icons-material"

const binFeatures = ['Cost', 'Pick_0', 'Pick_1', 'Pick_2', 'Pick_3',]
const numericFeatures = ["Time", "RT Crit", "RT Aud", 'Aud #', 'Combo', 'Budget', 'Box Off WW',]
const genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Animation', 'Thriller', 'Martial Arts', 'Superhero', 'Sports', 'Musical', 'Western',]
import { targets } from "./targets"


const chartChoicesIcons = {
    "Binary Box Plot": <BarChart/>,
    "Genre Count Plot": <StackedBarChart/>,
    "Histogram": <Leaderboard/>,
    "Correlation Matrix": <Grid4x4 />,
    "Feature Count Plot": <SignalCellularAlt />
}

export default {
    choices: targets,
    numericFeatures,
    allTargetsChoices: ["Binary Box Plot"],
    targetChoices: ['Feature Count Plot', "Genre Count Plot", "Histogram", "Correlation Matrix"],
    genres,
    featureChoices: [...binFeatures],
    chartChoicesIcons
}