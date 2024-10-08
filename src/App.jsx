import './App.css'
import Method from './components/Method'
import { Route, Routes } from 'react-router-dom'
import { useState } from 'react'
import Home from './components/Home'
import SideBar from './components/SideBar'
function App() {
  const [active_method, setActive_method] = useState("");
  const method_list = [['Biseccion', 'biseccion'],
  ['Punto fijo', 'puntoFijo'],
  ['Regla falsa', 'reglaFalsa'],
  ['Newton', 'newton'],
  ['Secante', 'secante'],
  ['Newton M1', 'newton_mod1'],
  ['Newton M2', 'newton_mod2'],
  ]; // Refactorizar a objeto, soy una gueva 

  const get_active_method = (method) => {
    setActive_method(method);
  }
  return (
    <main id="content_wrapper" className='flex h-screen w-full flex-col items-center'>
      <section className='flex h-screen w-full flex-row'>
        {/* Sidebar component */}
        <SideBar method_list={method_list} active_method={active_method} />
        {/* Method Component */}
        <Routes>
          <Route exact path='/' element={<Home/>} />
          {
            method_list.map((element) => (
              <Route exact path={`/${element[1]}`} element={<Method method_route={element[1]} method_name={element[0]} get_active_method={get_active_method} />} />
            ))
          }
        </Routes>
      </section>
      {/* Switch of routes for each method*/}
    </main>
  )
}

export default App
