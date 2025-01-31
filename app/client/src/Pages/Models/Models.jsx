import React, { useState } from 'react'

import { CircularProgress } from '@mui/material'
import { Box } from '@mui/material'
import Layout from '../../components/Layout/Layout'
import LeftNavModels from '../../components/LeftNav/LeftNavModels'

import models from '../../constants/models'
import { targets } from '../../constants/shared'

import useApi from '../../hooks/useApi/useApi'
import ModelTabs from '../../components/ModelTabs/ModelTabs'

const Models = () => {
  const [selectedUser, setSelectedUser] = useState(targets[0])
  const [selectedModel, setSelectedModel] = useState(models.modelsList[0])

  const {
    data,
    isLoading
  } = useApi({ path: models.models[selectedModel].path, params: { target: selectedUser }, target: selectedUser, model: selectedModel })

  return (
    <Layout>
      <LeftNavModels
        selectedModel={selectedModel}
        setSelectedModel={setSelectedModel}
        selectedUser={selectedUser}
        setSelectedUser={setSelectedUser}
      />
      {isLoading ? <Box sx={{ m: '40px', alignItems: 'center', justifyContent: 'center', display: 'flex', flexGrow: 1 }}><CircularProgress size={'200px'} /> </Box> : <ModelTabs model={data} />}
    </Layout>
  )
}

export default Models