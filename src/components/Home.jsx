import React from "react";
import '/src/App.css'
function Home() {
    return (
        <main className="w-full h-screen flex items-center justify-center flex-col">
            <div className="w-full h-96 HomePage "></div>
            <div className="w-2/5 h-4/6 mt-4 p-10 flex justify-start flex-col bg-white border border-dotted border-[#c2c2c2] fixed rounded-md">
                <div className="w-full h-fit flex justify-center mb-3">
                    <svg className="w-20 h-20 text-center " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="#00509d" d="M116.7 33.8c4.5-6.1 11.7-9.8 19.3-9.8l240 0c7.6 0 14.8 3.6 19.3 9.8l112 152c6.8 9.2 6.1 21.9-1.5 30.4l-232 256c-4.5 5-11 7.9-17.8 7.9s-13.2-2.9-17.8-7.9l-232-256c-7.7-8.5-8.3-21.2-1.5-30.4l112-152zm38.5 39.8c-3.3 2.5-4.2 7-2.1 10.5l57.4 95.6L63.3 192c-4.1 .3-7.3 3.8-7.3 8s3.2 7.6 7.3 8l192 16c.4 0 .9 0 1.3 0l192-16c4.1-.3 7.3-3.8 7.3-8s-3.2-7.6-7.3-8L301.5 179.8l57.4-95.6c2.1-3.5 1.2-8.1-2.1-10.5s-7.9-2-10.7 1L256 172.2 165.9 74.6c-2.8-3-7.4-3.4-10.7-1z" /></svg>
                </div>
                <h1 className="text-center text-[#00509d] pb-4 mt-4 text-5xl">Crystal</h1>
                <p className="text-center text-[#00000] text-xl mb-3">Una calculadora para metodos estudiados en el cursos de analisis numerico en EAFIT.</p>
                <div className="text-[#00000] text-md ">
                    <h2 className="text-xl mb-1">Desarrollado por:</h2>
                    <li className="">Miguel Vásquez</li>
                    <li className="">Manuel Villegas</li>
                    <li className="">Carlos Mazo</li>
                    <li className="">Esteban Muriel</li>
                </div>

            </div>
        </main>
    )
}

export default Home;