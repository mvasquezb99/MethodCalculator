import React from "react";

function InputGroup({ method_obj, update_data }) {
    const inputs = Object.keys(method_obj);

    function get_label(key, is_title) {
        switch (key) {
            case "a":
                return is_title ? "Limite inferior" : "0";
            case "b":
                return is_title ? "Limite superior" : "4"
            case "fx":
                return is_title ? "Función" : "exp(-x)+4"
            case "n_iter":
                return is_title ? "Numero de iteraciones" : "10"
            case "tol":
                return is_title ? "Tolerancia del error" : "0.5E-3"
            case "x0":
                return is_title ? "Valor inicial para X" : "0"
            case "g":
                return is_title ? "g(x) deseada" : "exp(-x)+4+x"
            case "m":
                return is_title ? "Multiplicidad de la función" : "2"
            default:
                break;
        }
    }

    return (
        <>
            {
                inputs.map((key) => (
                    <>
                        <label className="w-full" htmlFor={key}>{get_label(key,true)}</label>
                        <input className="w-full p-1 border border-[#c2c2c2] rounded-lg" type="text" name={key} placeholder={get_label(key,false)} onChange={update_data} />
                    </>
                ))
            }
        </>
    )
}

export default InputGroup;