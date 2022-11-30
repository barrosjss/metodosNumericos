import React from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom"

import Navbar from './components/Navbar.js'

import Home from './pages/Home.js'
import Secante from './pages/Secante.js'

export default function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/secante' element={<Secante />} />
        </Routes>
      </Router>
    </div>
  );
}
