import React from 'react';
import { Box, Grid2 as Grid, Typography } from '@mui/material';
import chroma from 'chroma-js'
// import { Grid } from '@mui/material/Grid2';

const HeatMap = ({ correlationMatrix, width = 600, height = 600, colorGradient = ['#FF0000', '#FFFF00', '#00FF00'] }) => {
    // Get the categories from the matrix keys
    const categories = Object.keys(correlationMatrix);

    const colorScale = chroma.scale('RdYlBu').padding(0.3);;
    const gradientColors = colorScale.colors(10)

    // Function to interpolate colors based on value
    const interpolateColor = (value, min, max, colorGradient) => {
        // Normalize the value to be between 0 and 1
        const normalizedValue = (value - min) / (max - min);

        // Find the color index based on the normalized value
        const colorIndex = Math.min(Math.floor(normalizedValue * (gradientColors.length - 1)), gradientColors.length - 1);

        // Return the color from the gradientColors array
        return gradientColors[colorIndex];
    };

    // Find the min and max correlation values for scaling
    const values = [];
    categories.forEach((category) => {
        values.push(...Object.values(correlationMatrix[category]));
    });
    const minValue = Math.min(...values);
    const maxValue = Math.max(...values);

    // Create grid cells for the heatmap
    const gridCells = categories.map((rowCategory) => (
        <Grid container key={rowCategory} spacing={0}>
            <Typography sx={{ textOverflow: 'ellipsis', fontSize: '14px', textAlign: 'center', flexGrow: 1 }}>{rowCategory}</Typography>
            {categories.map((colCategory) => {
                const value = correlationMatrix[rowCategory][colCategory];
                const color = interpolateColor(value, minValue, maxValue, colorGradient);
                return (
                    <>
                        <Grid
                            item
                            key={colCategory}
                            xs={1}
                            style={{
                                backgroundColor: color,
                                width: `${width / categories.length}px`,
                                height: `${height / categories.length}px`,
                                border: '1px solid #ffffff',
                                transition: 'background-color 0.2s ease-in-out',
                                borderRadius: '4px',
                                justifyContent: 'center',
                                alignItems: 'center',
                                alignSelf: 'center',
                                display: 'flex'

                            }}
                        >
                            <Typography
                                sx={{
                                    textAlign: 'center',
                                    alignItems: 'center',
                                    alignSelf: 'center',
                                    color: value.toFixed(2) > .50 ? 'darkgray' : 'white'
                                }}
                            >{value.toFixed(2)}</Typography>
                        </Grid>
                    </>
                );
            })}
        </Grid>
    ));

    return (
        <Box>

            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'row',
                }}
            >
                <Box
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        minHeight: '100%',
                        alignContent: 'center',
                        textAlign: 'center',
                        pt: '20px'
                    }}
                >
                    {categories.map(c => (
                        <Box
                            sx={{
                                flexGrow: 1,
                                alignContent: 'center',
                                alignSelf: 'center',
                                textAlign: 'center',

                            }}
                        >
                            <Typography
                                sx={{
                                    fontSize: '14px',
                                    alignContent: 'center',
                                    alignSelf: 'center',
                                    flexGrow: 1,
                                    textAlign: 'center',
                                }}>{c}</Typography>
                        </Box>
                    ))}

                </Box>
                <Box
                    sx={{
                        display: 'grid',
                        gridTemplateColumns: `repeat(${categories.length}, 1fr)`,
                        gridTemplateRows: `repeat(${categories.length}, 1fr)`,
                        width: `${width}px`,
                        height: `${height}px`,
                    }}
                >
                    {gridCells}
                </Box>
            </Box>
        </Box>
    );
};

export default HeatMap