/*
  COMP90024 - Group 34 - Semester 1 2022:
  - Juny Kesumadewi (197751); Melbourne, Australia
  - Georgia Lewis (982172); Melbourne, Australia
  - Vilberto Noerjanto (553926); Melbourne, Australia
  - Matilda O’Connell (910394); Melbourne, Australia
  - Rizky Totong (1139981); Melbourne, Australia
*/

import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import './index.css'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
