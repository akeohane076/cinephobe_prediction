import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import { Link } from '@mui/material';
import { NavLink } from 'react-router';

const NavBar = () => {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>
                    <Box sx={{ ml: 'auto' }}>
                        <Button color="inherit">
                            <Link component={NavLink} to="/" color="text.primary" >
                                Home
                            </Link>
                        </Button>
                        <Button color="inherit">
                            <Link component={NavLink} to="/data" color="text.primary" >
                                Data
                            </Link>
                        </Button>
                        <Button color="inherit" >
                            <Link component={NavLink} to="/models" color="text.primary" >
                                Models
                            </Link>
                        </Button>
                        <Button color="inherit" >
                            <Link component={NavLink} to="/predict" color="text.primary" >
                                Predict
                            </Link>
                        </Button>
                    </Box>
                </Toolbar>
            </AppBar>
        </Box>
    );
}

export default NavBar