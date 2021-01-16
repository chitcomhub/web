import React from 'react';
import { Switch, Route } from 'react-router-dom';
import './assets/css/App.css';
import Footer from './components/Footer';
import NavBar from './components/NavBar';
import PageWithContent from './components/PageWithContent';
import UnitFilter from './components/UnitFilter';

function App() {
  return (
    <div className="container-fluid">
      <NavBar />
      <Switch>
        <Route exact path="/">
          <PageWithContent title="Наши специалисты" name="Специалисты">
            <UnitFilter />
          </PageWithContent>
        </Route>
        <Route exact path="/about">
          <PageWithContent title="О нас" name="О нас">
            <p className="alert alert-info">Информацию о проекте можно получить в группе.</p>
          </PageWithContent>
        </Route>
      </Switch>

      <Footer />
    </div>
  );
}

export default App;
