import React from 'react'

import { LineChart as LC } from '@mui/x-charts';

const LineChart = (props) => {
  const { data } = props
  return (
    <LC
      xAxis={[{ data: data.map(_d => (_d[0])), label: 'Number of Features' }]}
      series={[
        {
          data: data.map(_d => (_d[1])),
          label: 'accuracy score'
        },
      ]}
      width={800}
      height={600}
      grid={{ vertical: true, horizontal: true }}
    />
  )
}

export default LineChart