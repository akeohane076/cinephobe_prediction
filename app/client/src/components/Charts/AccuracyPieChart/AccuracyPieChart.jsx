import * as React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';
import { Box } from '@mui/material';
// import { desktopOS, valueFormatter } from './webUsageStats';

const AccuracyPieChart = ({ accuracy }) => {

    console.log(accuracy)
    const ac = parseFloat(accuracy)

    const bad = 1 - ac

    return (
        <PieChart
            series={[
                {
                    data: [{ label: 'correct', value: parseFloat(accuracy) }, { label: 'incorrect', value: bad }],
                    highlightScope: { fade: 'global', highlight: 'item' },
                    faded: { innerRadius: 30, additionalRadius: -30, color: 'gray' },
                    innerRadius: 100,
                },
            ]}
            height={500}
        />
    );
}

export default AccuracyPieChart