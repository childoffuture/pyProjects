import React from 'react';
import ReactDOM from 'react-dom/client';
import {  BrowserRouter,  Routes,  Route, } from 'react-router-dom'
import './index.css';
import App from './App';
import Category from "./Category"
import Dish from "./Dish"
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="category/" element={<Category />} />
        <Route path="category/:id" element={<Category />} />
        <Route path="dish/:id" element={<Dish />} />
      </Route>
    </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
