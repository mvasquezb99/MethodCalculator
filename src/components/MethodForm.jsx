import React, { useState } from "react";

function MethodForm({ method_name, method_obj, put_method }) {

    const [input_data, set_data] = useState(method_obj);

    const update_data = (e) => {
        set_data((input_data) => {
            return {
                ...input_data,
                [e.target.name]: e.target.value
            }
        })
    }
    console.log(method_name);

    const on_submit = (e) => {
        e.preventDefault();
        console.log(input_data);
        put_method(input_data);
    }
    return (
        <div className="rounded-md p-2 border border-[#c2c2c2] h-fit">
            <form action="" className="flex w-80 h-fit justify-start items-start flex-col text-start" onSubmit={on_submit}>
                <h1 className="text-start text-xl mb-3 border-b border-b-[#c2c2c2] border-dotted w-full pb-2 ">Ingreso de datos</h1>
                {
                    method_name === "Biseccion" ? <>

                        <label className="w-full" htmlFor="func">Función</label>
                        <input className="w-full p-1" type="text" name="fx" placeholder="math.exp(-x)+x**2-13" onChange={update_data} />

                        <label className="w-full" htmlFor="li" >Limite inferior</label>
                        <input className="w-full p-1" type="text" name="a" id="" placeholder="2" onChange={update_data} />

                        <label className="w-full" htmlFor="sl" >Limite superior</label>
                        <input className="w-full p-1" type="text" name="b" id="" placeholder="4" onChange={update_data} />

                        <label className="w-full" htmlFor="tol" >Tolerancia</label>
                        <input className="w-full p-1" type="text" name="tol" id="" placeholder="0.05E-2" onChange={update_data} />

                        <label className="w-full" htmlFor="iter" >Numero de iteraciónes</label>
                        <input className="w-full p-1" type="text" name="n_iter" id="" placeholder="100" onChange={update_data} />
                        <button type="submit" className="bg-[#00509d] p-1 rounded-lg w-16 mt-3 text-white">Send!</button>
                    </> : ''
                }
            </form>
        </div>

    )
}


export default MethodForm;
