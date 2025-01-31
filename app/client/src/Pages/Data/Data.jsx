import React, { useContext, useEffect, useState } from 'react'

import { Box, Typography, FormControl, MenuItem, InputLabel, Select } from '@mui/material'


import Layout from '../../components/Layout/Layout'
import HeatMap from '../../components/Charts/Heatmap/Heatmap'
import DataContext from '../../context/dataContext'
import LeftNav from '../../components/LeftNav/LeftNav'
import BarChart from '../../components/Charts/BarChart/BarChart'
import CountPlot from '../../components/Charts/BarChart/CountPlot'
import charts from '../../constants/charts'

import DataTabs from '../../components/DataTabs/DataTabs'

import { targets } from '../../constants/shared'
import { createCountPlot, createAllUsersBarData } from '../../utils/helpers/chartData'
import HistogramChart from '../../components/Charts/Histogram/Histogram'
import { targetIndexes } from '../../constants/targets'


const customGradient = ['#FF0000', '#FF7F00', '#FFFF00', '#7FFF00', '#00FF00'];

const Data = (props) => {
    const [selectedChart, setSelectedChart] = useState('Binary Box Plot')
    const [selectedUser, setSelectedUser] = useState('All Targets')
    const [feature, setFeature] = useState('Cost');
    const data = useContext(DataContext)

    useEffect(() => {
        if (selectedUser !== charts.choices[0]) {
            setSelectedChart(charts.targetChoices[0])
        }
        else {
            setSelectedChart(charts.allTargetsChoices[0])
        }
    }, [selectedUser])

    const renderChart = () => {
        switch (selectedUser) {
            case charts.choices[0]:
                switch (selectedChart) {
                    case "Binary Box Plot":
                        return (
                            <BarChart series={createAllUsersBarData(data.models)} xAxisData={targets} />
                        )
                    default:
                        return (
                            <Typography>select chart</Typography>
                        )
                }
            default:
                switch (selectedChart) {
                    case "Feature Count Plot":
                        return (
                            <>
                                <DataTabs setFeature={setFeature} feature={feature} choices={charts.featureChoices} />
                                <CountPlot series={createCountPlot(feature, selectedUser, data.movie_data, 1)} xAxisData={[selectedUser]} />
                            </>
                        )
                    case "Genre Count Plot":
                        return (
                            <>
                                <DataTabs setFeature={setFeature} feature={feature} choices={charts.genres} />
                                <CountPlot series={createCountPlot(feature, selectedUser, data.movie_data, 1)} xAxisData={[selectedUser]} />
                            </>
                        )
                    case "Histogram":
                        return (
                            <>
                                <DataTabs setFeature={setFeature} feature={feature} choices={charts.numericFeatures} />
                                <HistogramChart data={data.models[targetIndexes[selectedUser]].histograms[feature] && data.models[targetIndexes[selectedUser]].histograms[feature]} />
                            </>
                        )
                    case "Correlation Matrix":
                        return (
                            <HeatMap correlationMatrix={data.models[targetIndexes[selectedUser]].correlation_matrix} width={600} height={600} colorGradient={customGradient} />
                        )
                    default:
                        return (
                            <Typography>select chart</Typography>
                        )
                }
        }
    }

    return (
        <Layout>
            <LeftNav
                setSelectedChart={setSelectedChart}
                selectedUser={selectedUser}
                selectedChart={selectedChart}
                setSelectedUser={setSelectedUser}
            />
            <Box
                sx={{
                    display: 'flex', px: '50px', py: '25px', flexGrow: 1, gap: '40px',
                    flexDirection: 'column'
                }}
            >
                <Typography variant='h4'>{selectedUser}</Typography>
                <Typography variant='h5'>{selectedChart}</Typography>
                {/* {(selectedUser !== charts.choices[0]) &&
                    <DataTabs setFeature={setFeature} feature={feature} />
                } */}
                {renderChart()}
            </Box>
        </Layout>
    )
}

export default Data