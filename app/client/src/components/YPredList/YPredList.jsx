import React from 'react'

import { Box, List, ListItem, Typography } from '@mui/material'

import { convertText } from '../../constants/features'

const BestFeaturesMap = ({predition}) => {
  return (
    <Box>
        <Typography variant="h5">Best Features:</Typography>
        <List>
            {features.map((feature, index) => (
                <ListItem>
                    <Typography>{index + 1}: {convertText(feature)}</Typography>
                </ListItem>
            ))}
        </List>
    </Box>
  )
}

export default BestFeaturesMap