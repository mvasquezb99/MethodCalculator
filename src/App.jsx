import './App.css'
import Method from './components/Method'
import { Route, Routes } from 'react-router-dom'
import { useState } from 'react'
import Home from './components/Home'
import SideBar from './components/SideBar'

function App() {
  const [active_method, setActive_method] = useState("");
  const method_list = {
    "Capitulo 1": [
      ['Biseccion', 'biseccion', 'regular'],
      ['Punto fijo', 'puntoFijo', 'regular'],
      ['Regla falsa', 'reglaFalsa', 'regular'],
      ['Newton', 'newton', 'regular'],
      ['Secante', 'secante', 'regular'],
      ['Newton M1', 'newton_mod1', 'regular'],
      ['Newton M2', 'newton_mod2', 'regular']
    ],
    "Capitulo 2": [
      ['Seidel-Gauss', 'mat_scidel', 'matrix'],
      ['Jacobi', 'mat_jacobi', 'matrix'],
      ['SOR', 'mat_sor', 'matrix']
    ],
    "Capitulo 3": [
      ['Vandermonte', 'vandermonde', 'polinomial'],
      ['Interpolación de Newton', 'newton_interpol', 'polinomial'],
      ['Interpolación de Larange', 'lagrange_interpol', 'polinomial'],
      ['Spline cubica', 'spline_cubica', 'polinomial']
    ]
  };

  const get_active_method = (method) => {
    setActive_method(method);
  };

  return (
    <main id="content_wrapper" className="flex h-screen w-full flex-col items-center">
      <section className="flex h-screen w-full flex-row">
        {/* Sidebar component */}
        <SideBar chapters={method_list} active_method={active_method} />
        {/* Method Component */}
        <Routes>
          <Route exact path="/" element={<Home />} />
          {
            Object.values(method_list).flat().map((method, index) => (
              <Route
                key={index}
                exact
                path={`/${method[1]}`}
                element={
                  <Method
                    method_route={method[1]}
                    method_name={method[0]}
                    get_active_method={get_active_method}
                    type={method[2]}
                  />
                }
              />
            ))
          }
        </Routes>
      </section>
    </main>
  );
}

export default App;
