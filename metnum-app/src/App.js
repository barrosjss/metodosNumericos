import React from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom"

import Navbar from './components/Navbar.js'
import Footer from './components/Footer.js'

import Home from './pages/Home.js'
import Secante from './pages/Secante.js'
import Lagranje from './pages/Lagranje.js'

export default function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/secante' element={<Secante />} />
          <Route path='/lagranje' element={<Lagranje />} />
        </Routes>
        <Footer />
      </Router>
    </div>
  );
}
