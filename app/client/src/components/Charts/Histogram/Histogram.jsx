import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';


const makeHistogramData = (data) => {
    const series = [
        {
            data: data.Phobe.hist,
            label: 'Phobe'
        },
        {
            data: data.Phile.hist
            ,
            label: 'Phile'
        },
    ]

    return series
}

export default function BasicBars({ data }) {
    if (!data){
        return null
    }
    console.log(data)
    const bins = data.Phobe.bins.slice(1)

    console.log(bins)

    console.log(makeHistogramData(data))

  return (
    <BarChart
      xAxis={[{ scaleType: 'band', data: [...bins] }]}
      series={makeHistogramData(data)}
      width={500}
      height={300}
    />
  );
}