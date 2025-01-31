import React from 'react'
import { Routes, Route } from "react-router";
import DataContext from './context/dataContext';
import NavBar from './components/NavBar/NavBar';
import Data from './Pages/Data/Data'
import Models from './Pages/Models/Models'
import useApi from './hooks/useApi/useApi';
import './index.css'
import Prediction from './Pages/Prediction/Prediction';
import Home from './Pages/Home/Home';

const App = () => {
  const {
    data, isLoading
  } = useApi({ path: `/api/start` })


  return (
    <DataContext.Provider value={data}>
      <NavBar />
      <Routes>
        <Route path="" element={<Home />} />
        <Route path="/data" element={<Data />} />
        <Route path="/models" element={<Models />} />
        <Route path="/predict" element={<Prediction />} />
      </Routes>
    </DataContext.Provider>
  )
}

export default App
