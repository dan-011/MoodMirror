import About from "./About";
import ImageCollection from "./ImageCollection";
import Model from "./Model";
import Navbar from "./Navbar";
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/" element={<ImageCollection />} />
        <Route path="/model" element={<Model />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;