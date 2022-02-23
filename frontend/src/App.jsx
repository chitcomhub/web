import React from 'react';
import './assets/css/App.css';
import Footer from './components/Footer';
import NavBar from './components/NavBar';
import { Router } from "./router";

function App() {
  return (
    <div className="container-fluid">
      <NavBar />
      <Router />
      <Footer />
    </div>
  );
}

export default App;
