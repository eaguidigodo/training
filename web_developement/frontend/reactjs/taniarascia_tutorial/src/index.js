import React,{ StrictMode }  from 'react';
import ReactDOM, { createRoot } from 'react-dom';
import App from './App'
import './index.css';


const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
)


