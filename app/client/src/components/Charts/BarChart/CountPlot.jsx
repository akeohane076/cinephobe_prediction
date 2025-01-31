import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';

export default function CountPlot(props) {
    const {
        xAxisData,
        series,

    } = props
    return (
        <BarChart
            xAxis={[{ scaleType: 'band', data: xAxisData }]}
            series={series}
            width={800}
            height={500}
        />
    );
}