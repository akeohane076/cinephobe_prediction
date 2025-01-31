import React from 'react'

import { Box, Typography, Button } from '@mui/material'

const PredictionResponse = ({ data, clearForm }) => {
    const answers = Object.entries(data)
    return (
        <Box
            sx={{
                display: 'flex',
                flexDirection: 'column',
                gap: '25px'
            }}
        >
            {answers.map(answer => {
                return <Typography>{answer[0]}: {answer[1]}</Typography>
            })}
            <Button sx={{ maxWidth: 'fit-content' }} variant='contained' onClick={clearForm}>Back</Button>
        </Box>
    )
}

export default PredictionResponse