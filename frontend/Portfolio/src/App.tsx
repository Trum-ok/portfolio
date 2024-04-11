import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import './App.css'
import './index.css'
import NavBar from './components/navbar';
import Home from './pages/index';
import E404 from "./pages/404";

function App() {
  return (
    <>
    <noscript>Необходимо активировать Javascript в настройках вашего браузера</noscript>
    <Router>
      <NavBar />
      <Routes>
          <Route path="/" element={<Home />} />
          {/* <Route path="/books" element={<Books />} /> */}
          <Route path="*" element={<E404 />} /> 
      </Routes>
    </Router>
    </>
  )
}

export default App;