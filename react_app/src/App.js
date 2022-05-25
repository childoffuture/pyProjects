import React, { Component } from 'react';
import { Outlet, Link } from "react-router-dom";
import './App.css';
import SwaggerUI from "swagger-ui-react"
import "swagger-ui-react/swagger-ui.css"
import "./openapi.json"

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
        items: [],
        isLoaded: false,
    }
  }

  componentDidMount()
  {
     fetch('http://127.0.0.1:8000/').then(res => res.json())
     .then(json => {
        this.setState({
            isLoaded: true,
            items: json,
        })
     });
  }

  render()
  {
    var {isLoaded, items} = this.state;

    if (!isLoaded) {
        return <div>Loading...</div>
    }

    return (
    <div className="App">
        <h1>Меню рецептов</h1>
        <nav>
            <Link to="/">На главную</Link>
        </nav>
        <ul>
            {items.map(item => (
                <li key={item.id}>
                   <a href={'http://127.0.0.1:3000/category/'+ item.id}>{item.name}</a>
                </li>
            ))}
        </ul>
        <Outlet />
        <SwaggerUI url="./openapi.json" />
    </div>
    );

  }
}

export default App;
