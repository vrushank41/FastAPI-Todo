import React from "react";
import ReactDOM from "react-dom/client";
import '../static/app.css'

function Hello() {
  return(
    <>
    <div className="back"></div>
        <div className="main">

        <label className="switch">
        <input type="radio" name="value-radio"/>
        <div className="button">
            <div className="light"></div>
            <div className="dots"></div>
        </div>
        </label>

        <label className="switch1">
        <input type="radio" checked="" name="value-radio"/>
        <div className="button">
            <div className="light"></div>
            <div className="dots"></div>
        </div>
        </label>

        <label className="switch2">
        <input type="radio" name="value-radio"/>
        <div className="button">
            <div className="light"></div>
            <div className="dots"></div>
        </div>
        </label>
</div>
</>
);
}

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<Hello />);