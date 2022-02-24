import React from 'react';
import './shared/assets/css/App.css';
import Footer from './shared/components/Footer';
import NavBar from './shared/components/NavBar';
import { Router } from "./pages/router";

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
