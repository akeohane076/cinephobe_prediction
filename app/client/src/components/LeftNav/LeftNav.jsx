import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import MailIcon from '@mui/icons-material/Mail';

import charts from '../../constants/charts'

const drawerWidth = 240;

export default function PermanentDrawerLeft(props) {

    const {
        setSelectedChart,
        selectedUser,
        setSelectedUser,
        selectedChart,
    } = props;

    const onChartSelect = (key) => {
        setSelectedChart(key)
    }

    const onUserSelect = (key) => {
        setSelectedUser(key)
    }

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
                    {charts.choices.map((text, index) => (
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
                    {selectedUser === charts.choices[0] ? charts.allTargetsChoices.map((text, index) => (
                        <ListItem key={text} disablePadding>
                            <ListItemButton onClick={() => onChartSelect(text)} selected={selectedChart === text}>
                                <ListItemIcon>
                                    {charts.chartChoicesIcons[text]}

                                </ListItemIcon>
                                <ListItemText primary={text} />
                            </ListItemButton>
                        </ListItem>
                    )) :
                        charts.targetChoices.map((text, index) => (
                            <ListItem key={text} disablePadding>
                                <ListItemButton onClick={() => onChartSelect(text)} selected={selectedChart === text}>
                                    <ListItemIcon>
                                        {charts.chartChoicesIcons[text]}
                                    </ListItemIcon>
                                    <ListItemText primary={text} />
                                </ListItemButton>
                            </ListItem>
                        ))
                    }
                </List>
            </Drawer>
        </Box >
    );
}
