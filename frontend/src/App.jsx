import { useState } from "react";
import "./App.css";
import cowSVG from "./assets/beef_001.svg"

function App() {
  return (
    <div className="app">
      <h1>🥩MeatMap🥩</h1>
      <p>Explore meat cuts in different languages.</p>
      <<img
        src={cowSVG}
        alt="CowDiag"
        className="cow-diag"
        onClick={() => alert("Clicked!")}
      </div>
    </div>
  );
}

export default App;
