import './App.css'
import Metodo from './components/Metodo'

function App() {
  return (
    <main id="content_wrapper" className='flex h-max w-full flex-col items-center'>
      <h1 className='text-center w-full h-fit text-3xl'>Analisis numerico</h1>
      <Metodo method_name={"biseccion"}/>
    </main>
  )
}

export default App
