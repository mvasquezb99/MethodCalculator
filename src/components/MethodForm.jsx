import React, { useState } from "react";
import InputGroup from "./InputGroup";
function MethodForm({ method_obj, put_method }) {

    const [input_data, set_data] = useState(method_obj);

    const update_data = (e) => {
        set_data((input_data) => {
            return {
                ...input_data,
                [e.target.name]: e.target.value
            }
        })
    }
    const on_submit = (e) => {
        e.preventDefault();
        put_method(input_data);
    }

    return (
        <div className="rounded-md p-2 border border-[#c2c2c2] h-fit">
            <form action="" className="flex w-80 h-full justify-start items-start flex-col text-start" onSubmit={on_submit}>
                <h1 className="text-start text-xl mb-3 border-b border-b-[#c2c2c2] border-dotted w-full">Ingreso de datos</h1>
                <InputGroup method_obj={method_obj} update_data={update_data} />
                <div className="w-full h-full flex items-end">
                    <button type="submit" className="bg-[#00509d] p-1 rounded-lg w-20 mt-2 text-white">Enviar!</button>
                </div>
            </form>
        </div>

    )
}


export default MethodForm;
