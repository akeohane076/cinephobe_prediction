import { AccountTree, CheckCircle, FileUpload, Forest, Insights, SsidChart, StackedLineChart } from "@mui/icons-material"

import { targets } from "./targets"

const models = {
    "DecisionTree": {
        name: 'Decision Tree',
        path: '/api/dt',
        icon: <AccountTree />
    },
    'AdaBoost': {
        name: 'Ada_boost',
        path: '/api/ada_boost',
        icon: <FileUpload />
    },
    'K Best Features': {
        name: 'K Best Features',
        path: '/api/kbest',
        icon: <CheckCircle />
    },
    'Logistic Regression': {
        name: 'Logistic Regression',
        path: '/api/best_log_reg',
        icon: <Insights />
    },
    'RFE': {
        name: 'RFE',
        path: '/api/rfe',
        icon: 'lll'
    },
    'Random Forest': {
        name: 'Random Forest',
        path: '/api/random_forest',
        icon: <Forest />
    },
    'SVC': {
        name: 'SVC',
        path: '/api/svc',
        icon: <StackedLineChart />
    },
    'Polynomial': {
        name: 'Polinomial PreProcessing',
        path: '/api/poly',
        icon: <SsidChart />
    },
}

const modelsList = Object.keys(models)

export default {
    targets,
    models,
    modelsList

}