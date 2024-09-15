import './App.css'
import Method from './components/Method'
import { Route, Routes } from 'react-router-dom'
import Navbar from './components/Navbar'
import SideBar from './components/SideBar'
function App() {
  const method_list = ['Biseccion', 'Punto fijo', 'Regla falsa', 'Newton'];
  return (
    <main id="content_wrapper" className='flex h-full w-full flex-col items-center'>
      {/* Navbar component */}
      <Navbar />
      <section className='flex h-max w-full flex-row'>
        {/* Sidebar component */}
        <SideBar method_list={method_list} />
        {/* Method Component */}
        <Routes>
          <Route path='/' element={<h1 className='text-center w-full h-fit text-3xl'>Analisis numerico</h1>} />
          <Route path='/biseccion' element={<Method method_name={"biseccion"} />} />
        </Routes>
      </section>
      {/* Switch of routes for each method*/}
    </main>
  )
}

export default App
