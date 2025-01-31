import React from 'react'

import Box from '@mui/material/Box';

const Layout = (props) => {

    const {
        children
    } = props
    return (
        <Box sx={{ display: 'flex' }}>
            {children}
        </Box>
    )
}

export default Layout