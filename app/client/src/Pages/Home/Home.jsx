import { Box, Typography, List, ListItem } from '@mui/material'
import React from 'react'

import text from '../../constants/text'

const Home = () => {
    return (
        <Box sx={{ height: 'calc(100% - 150px)', gap: '25px', p: '50px', display: 'flex', flexDirection: 'column' }} gap="50px">
            <Box>
                <Typography variant="h5">About this project</Typography>
                <Typography>{text.description}</Typography>
                <Typography>{text.about}</Typography>
            </Box>
            <Box>
                <Typography variant="h6">Summary</Typography>
                <Typography>{text.longtext}</Typography>
            </Box>
            <Box>
                <Typography variant="h6">Features</Typography>
                <Typography>{text.listHeading}</Typography>
                <List>
                    {text.listItems.map(item => (
                        <ListItem><Typography>{item}</Typography></ListItem>
                    ))}
                </List>
            </Box>
            <Typography>{text.disc}</Typography>
        </Box>
    )
}

export default Home