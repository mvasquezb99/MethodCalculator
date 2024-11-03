import React from "react";

function Home() {
    return (
        <div className="flex flex-col items-center pt-4">
            <h1 className="text-center text-5xl font-bold mb-10 text-gray-800">Análisis Numérico</h1>
            <p className="text-center text-xl mb-4 text-gray-600">
                Bienvenido a la aplicación de Análisis Numérico. Aquí podrás explorar 
                diferentes métodos numéricos para resolver problemas matemáticos.
            </p>
            <p className="text-center text-lg text-gray-500 mb-8">
                Selecciona un capítulo en la barra lateral para comenzar.
            </p>
            <img 
                src="/images/Pair programming-rafiki.png" 
                className="w-[350px] h-[350px] object-cover" 
            />
        </div>
    );
}

export default Home;
