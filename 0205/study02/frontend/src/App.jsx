import './App.css'
import { BrowserRouter, Routes, Route } from "react-router";
import NotFound from "./NotFound.jsx"

const Home = () => {

  return (
    <>
      <h1>메인 화면입니다.</h1>
    </>
  )
}

function App() {
  const paths = [
      {path: "/", element: <Home />},
      {path: "*", element: <NotFound />},
  ]

  return (
    <BrowserRouter>
      <Routes>
        {paths.map((v,i)=><Route key={i} path={v.path} element={v.element} />)}
      </Routes>
    </BrowserRouter>
  )
}

export default App
