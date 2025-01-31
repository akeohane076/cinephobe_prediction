import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import MailIcon from '@mui/icons-material/Mail';

import models from '../../constants/models';

import charts from '../../constants/charts'
import { targets } from '../../constants/shared';

const drawerWidth = 240;


export default function PermanentDrawerLeft(props) {

    const {
        setSelectedModel,
        selectedUser,
        setSelectedUser,
        selectedModel,
    } = props;

    const onModelSelect = (key) => {
        setSelectedModel(key)
    }

    const onUserSelect = (key) => {
        setSelectedUser(key)
    }


    console.log(models.modelsList)
    return (
        <Box sx={{ display: 'flex' }}>
            <Drawer
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    '& .MuiDrawer-paper': {
                        width: drawerWidth,
                        boxSizing: 'border-box',
                    },
                }}
                variant="permanent"
                anchor="left"
            >
                <Toolbar />
                <Divider />
                <List >
                    {targets.map((text, index) => (
                        <ListItem key={text} disablePadding >
                            <ListItemButton onClick={() => onUserSelect(text)} selected={selectedUser === text}>
                                <ListItemIcon>
                                    {index % 2 === 0 ? <InboxIcon /> : <MailIcon />}
                                </ListItemIcon>
                                <ListItemText primary={text} />
                            </ListItemButton>
                        </ListItem>
                    ))}
                </List>
                <Divider />
                <List>
                    {models.modelsList.map((_model) => (
                        <ListItem key={_model} disablePadding>
                            <ListItemButton onClick={() => onModelSelect(_model)} selected={selectedModel === _model}>
                                <ListItemIcon>
                                    {models.models[_model].icon}
                                </ListItemIcon>
                                <ListItemText primary={_model} />
                            </ListItemButton>
                        </ListItem>
                    ))
                    }
                </List>
            </Drawer>
        </Box >
    );
}
