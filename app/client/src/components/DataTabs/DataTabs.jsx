import * as React from 'react';
import PropTypes from 'prop-types';
import Tabs, { tabsClasses } from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import { featureText } from '../../constants/features';

import charts from '../../constants/charts';


function CustomTabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
        </div>
    );
}

CustomTabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.number.isRequired,
    value: PropTypes.number.isRequired,
};

function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        'aria-controls': `simple-tabpanel-${index}`,
    };
}

export default function DataTabs({ setFeature, feature, choices }) {
    const [value, setValue] = React.useState(0);

    const handleChange = (event, newValue) => {
        setFeature(newValue);
    };


    return (
        <Box sx={{ maxWidth: '600px', overflowWrap: 'normal' }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                <Tabs
                    value={feature} onChange={handleChange} aria-label="basic tabs example" variant="scrollable"
                    sx={{
                        [`& .${tabsClasses.scrollButtons}`]: {
                            '&.Mui-disabled': { opacity: 0.3 },
                        },
                    }}
                >
                    {choices.map(_choice => (
                        <Tab label={featureText[_choice]} value={_choice} {...a11yProps(0)} />
                    ))}
                </Tabs>
            </Box>
        </Box>
    );
}