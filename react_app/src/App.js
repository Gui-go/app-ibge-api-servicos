import React from "react";
import { BrowserRouter as Router, Route, Redirect, Switch } from 'react-router-dom';
import './App.css';

import { Navigation } from './assets/Navigation'
import { Layout } from './assets/Layout'

import Home from './components/Home'
import About from './components/About'
import Micro from './components/Micro'
import Meso from './components/Meso'
import Footer from "./components/Footer";


function App() {

  return (
    <div className="App">
      <Navigation />
      <Layout>
        <Router>
          <Switch>
            <Route exact path='/' component={Home} />
            <Route path='/home' component={Home} />
            <Route path='/micro' component={Micro} />
            <Route path='/meso' component={Meso} />
            <Route exact path='/about' component={About} />
            <Redirect from='*' to='/' />
          </Switch>
        </Router>
      </Layout>
      <Footer />
    </div>
  );
}

export default App;