import React from 'react'

import { CustomTabPanel } from '../../components/ModelTabs/ModelTabs'

import AccuracyPieChart from "../../components/Charts/AccuracyPieChart/AccuracyPieChart"
import ConfusionMatrix from '../../components/Charts/ConfusionMatrix/ConfusionMatrix'
import { labels } from "../../constants/shared"
import LineChart from '../../components/Charts/LineChart/LineChart'
import BestFeaturesMap from '../../components/BestFeaturesMap/BestFeaturesMap'

export const createCountPlot = (feature, target, data, featureLabel) => {
    let count1 = 0
    let count2 = 0
    data.map(row => {
        if (row[feature] === featureLabel) {
            if (row[target] === "Phobe") {
                count1 += 1
            }
            if (row[target] === "Phile") {
                count2 += 1
            }
        }
    })
    return [{ data: [count1], label: "Phobe" }, { data: [count2], label: "Phile" }]
}

export const createAllUsersBarData = (models) => {
    const retrunArr = labels.map(label => (
        {
            label: label,
            data: models.map(model => (
                model.distribution[label]
            ))
        }
    ))
    return retrunArr
}


export const createModelTabs = ({ model }) => {
    const keys = Object.keys(model)
    const tabs = keys.filter(tab => (tab !== 'y_pred')).map(tab => {
        return { label: tab.replace("_", " ") }
    })

    return tabs

}

export const createModelTabsContent = ({ model, value }) => {
    const keys = Object.keys(model)
    const entries = Object.entries(model)
    const content = keys.map((_key, index) => {
        switch (_key) {
            case 'accuracy':
                return (
                    <CustomTabPanel value={value} index={index}>
                        <AccuracyPieChart accuracy={model.accuracy} />
                    </CustomTabPanel>
                )
            case 'confusion_matrix':
                return (
                    <CustomTabPanel value={value} index={index}>
                        <ConfusionMatrix matrix={model.confusion_matrix} />
                    </CustomTabPanel>
                )
            case 'best_features':
                return (
                    <CustomTabPanel value={value} index={index}>
                        <BestFeaturesMap features={model.best_features} bestNum={model.best_features} ></BestFeaturesMap>
                    </CustomTabPanel>
                )
            case 'models':
                return (
                    <CustomTabPanel value={value} index={index}>
                        <LineChart data={makeLineChartData(model.models)} />
                    </CustomTabPanel>
                )
        }

    })
    return content
}


const makeLineChartData = (models) => {
    return models.map(model => (
        [
            model.num_features,
            model.accuracy
        ]
    ))

}