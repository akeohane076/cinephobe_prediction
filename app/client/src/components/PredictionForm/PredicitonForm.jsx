import React, { useState } from 'react'

import { Box, TextField, Typography, Button, CircularProgress } from '@mui/material'
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

import { omdpApiKey } from '../../constants/shared'
import { getBody } from '../../utils/helpers/predictMoviePayload'
import useApi from '../../hooks/useApi/useApi'

import { apiPath } from '../../constants/shared'


const PredictionForm = () => {
    const [movie, setMovie] = useState('')
    const [data, setData] = useState('')
    const [audience, setAudienceScore] = useState('')
    const [numberOfReviews, setNumberOfReviews] = useState('')
    const [budget, setBudget] = useState('')
    const [gross, setGross] = useState('')
    const [isLoading, setIsLoading] = useState(false)
    const [pick, setPick] = useState(0)


    const onSubmit = async () => {
        setIsLoading(true)
        const response = await fetch(`https://www.omdbapi.com/?t=${movie}&apikey=${omdpApiKey}&r=json`);


        const d = await response.json()
        console.log(d)
        const d_1 = getBody(d, audience, numberOfReviews, gross, budget)
        setData(d_1)
        const response1 = await fetch(`${apiPath}/api/prediction`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(d_1), // Convert object to JSON string
        });

        const result = await response1.json();
        console.log(result)

    }

    const handleRadioChange = (e) => {
        setPick(e.target.value)
    }


    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: "25px" }} >
            <TextField
                label={'Movie'}
                value={movie}
                onChange={(event) => {
                    setMovie(event.target.value);
                }}
            />
            <TextField
                label={'Number of Reviews'}
                value={numberOfReviews}
                onChange={(event) => {
                    setNumberOfReviews(event.target.value);
                }}
            />
            <TextField
                label={'Budget'}
                value={budget}
                onChange={(event) => {
                    setBudget(event.target.value);
                }}
            />
            <TextField
                label={'Gross'}
                value={gross}
                onChange={(event) => {
                    setGross(event.target.value);
                }}
            />
            <TextField
                label={'Audience Score'}
                value={audience}
                onChange={(event) => {
                    setAudienceScore(event.target.value);
                }}
            />
            <FormControl>
                <FormLabel id="demo-radio-buttons-group-label">Who Picked It?</FormLabel>
                <RadioGroup
                    value={pick}
                    onChange={handleRadioChange}
                >
                    <FormControlLabel value={0} control={<Radio />} label="Zach" />
                    <FormControlLabel value={1} control={<Radio />} label="Amin" />
                    <FormControlLabel value={2} control={<Radio />} label="Mayes" />
                </RadioGroup>
            </FormControl>
            <Button sx={{ maxWidth: 'fit-content' }} variant="contained" onClick={onSubmit}>Submit</Button>
        </Box>
    )
}

export default PredictionForm