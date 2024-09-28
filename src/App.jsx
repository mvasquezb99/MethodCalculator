import './App.css'
import Method from './components/Method'
import { Route, Routes } from 'react-router-dom'
import Navbar from './components/Navbar'
import SideBar from './components/SideBar'
function App() {
  const method_list = [['Biseccion', 'biseccion'],
  ['Punto fijo', 'puntoFijo'],
  ['Regla falsa', 'reglaFalsa'],
  ['Newton', 'newton'],
  ['Secante', 'secante'],
  ['Newton M1', 'newton_mod1'],
  ['Newton M2', 'newton_mod2'],
  ]; // Refactorizar a objeto, soy una gueva 
  return (
    <main id="content_wrapper" className='flex h-full w-full flex-col items-center'>
      {/* Navbar component */}
      <Navbar />
      <section className='flex h-max w-full flex-row'>
        {/* Sidebar component */}
        <SideBar method_list={method_list} />
        {/* Method Component */}
        <Routes>
          <Route exact path='/' element={<h1 className='text-center w-full h-fit text-3xl'>Analisis numerico</h1>} />
          {
            method_list.map((element) => (
              <Route exact path={`/${element[1]}`} element={<Method method_route={element[1]} method_name={element[0]} />} />
            ))
          }
        </Routes>
      </section>
      {/* Switch of routes for each method*/}
    </main>
  )
}

export default App
