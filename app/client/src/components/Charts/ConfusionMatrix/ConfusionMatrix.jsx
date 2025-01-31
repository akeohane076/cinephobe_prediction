import React from "react";
import chroma from "chroma-js";
import { Grid2 as Grid, Paper, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Box } from "@mui/material";

// ConfusionMatrix Component
const ConfusionMatrix = ({ matrix }) => {
    // Assuming matrix is a 2D array: [[TN, FP], [FN, TP]]
    const tn = matrix[0][0];
    const fp = matrix[0][1];
    const fn = matrix[1][0];
    const tp = matrix[1][1];

    const allValues = [tn, fp, fn, tp];
    const minValue = Math.min(...allValues);
    const maxValue = Math.max(...allValues);

    // Create the color scale
    const colorScale = chroma.scale(['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', '#4292c6', '#2171b5', '#08519c', '#08306b']).padding(0.35).domain([minValue, maxValue]);

    return (
        <Box sx={{ padding: 3 }}>
            <Typography variant="h5" gutterBottom align="center">
                Confusion Matrix
            </Typography>

            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 300 }} aria-label="confusion matrix">
                    <TableHead>
                        <TableRow>
                            <TableCell align="center">Predicted Positive</TableCell>
                            <TableCell align="center">Predicted Negative</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        <TableRow>
                            <TableCell
                                align="center"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: colorScale(tn).hex(), // Color based on TN value
                                }}
                            >
                                True Negative (TN): {tn}
                            </TableCell>
                            <TableCell
                                align="center"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: colorScale(fp).hex(), // Color based on FP value
                                }}
                            >
                                False Positive (FP): {fp}
                            </TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell
                                align="center"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: colorScale(fn).hex(), // Color based on FN value
                                }}
                            >
                                False Negative (FN): {fn}
                            </TableCell>
                            <TableCell
                                align="center"
                                sx={{
                                    fontWeight: "bold",
                                    backgroundColor: colorScale(tp).hex(), // Color based on TP value
                                }}
                            >
                                True Positive (TP): {tp}
                            </TableCell>
                        </TableRow>
                    </TableBody>
                </Table>
            </TableContainer>

            <Grid container spacing={2} sx={{ marginTop: 3 }}>
                <Grid item xs={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="h6">Accuracy: </Typography>
                        <Typography>{((tp + tn) / (tp + tn + fp + fn)).toFixed(2)}</Typography>
                    </Paper>
                </Grid>
                <Grid item xs={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="h6">Precision: </Typography>
                        <Typography>{(tp / (tp + fp)).toFixed(2)}</Typography>
                    </Paper>
                </Grid>
            </Grid>
        </Box>
    );
};

export default ConfusionMatrix;