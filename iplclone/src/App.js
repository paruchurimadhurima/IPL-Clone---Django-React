import React from 'react';
import logo from './logo.svg';
import './App.css';
//import { BrowserRouter, Route } from 'react-router-dom';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Season from './components/season';
import Match from './components/Match';
import Navbar from 'react-bootstrap/Navbar';

function App() {
  return (
        <Router>
        <div class="container">
            <h1 align="center">IPL WEB</h1>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <ul className="navbar-nav  mr-auto">
                    <li><Link to={'/'} className="nav-link"> Home </Link></li>
                </ul>
            </nav>
            <hr/>
            <Switch>
                <Route path="/" exact component={Season} />
                <Route path="/matches/:match_id" exact component={Match} />
            </Switch>
        </div>
      </Router>
  );
}

export default App;
