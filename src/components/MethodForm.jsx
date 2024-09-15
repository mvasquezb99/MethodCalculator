import React from "react";

function MethodForm({ handle_submit, method_name }) {

    return (
        <div className="w-1/2 h-3/4 flex justify-center items-center mt-6">
            <div className="rounded-md p-2 border border-[#c2c2c2] ">
                <form action="" className="flex w-80 h-max justify-start items-start flex-col text-start">
                    <h1 className="text-center text-xl mb-3">Ingreso de datos</h1>
                    {
                        method_name === "biseccion" ? <>

                            <label className="w-full" htmlFor="func">Función</label>
                            <input className="w-full p-1" type="text" name="func" placeholder="math.exp(-x)+x**2-13" />

                            <label className="w-full" htmlFor="li" >Limite inferior</label>
                            <input className="w-full p-1" type="text" name="il" id="" placeholder="2" />

                            <label className="w-full" htmlFor="sl" >Limite superior</label>
                            <input className="w-full p-1" type="text" name="sl" id="" placeholder="4" />

                            <label className="w-full" htmlFor="tol" >Tolerancia</label>
                            <input className="w-full p-1" type="text" name="tol" id="" placeholder="0.05E-2" />

                            <label className="w-full" htmlFor="iter" >Numero de iteraciónes</label>
                            <input className="w-full p-1" type="text" name="iter" id="" placeholder="100" />
                        </> : ''
                    }
                </form>
            </div>
        </div>
    )
}


export default MethodForm;