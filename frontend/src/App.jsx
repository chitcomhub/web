import React from 'react';
import './assets/css/App.css';
import Footer from './components/Footer';
import NavBar from './components/NavBar';
import PageWithContent from './components/PageWithContent';
import UnitFilter from './components/UnitFilter';

function App() {
  return (
    <div className="container-fluid">
      <NavBar/>
      <PageWithContent title="Наши специалисты" name="Специалисты">
        <UnitFilter />
      </PageWithContent>

      <Footer />
    </div>
  );
}

export default App;
