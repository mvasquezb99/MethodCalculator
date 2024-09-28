import React from "react";

function InputGroup({ method_obj, update_data }) {
    const inputs = Object.keys(method_obj);
    let type;
    function get_label(key, is_title) {
        switch (key) {
            case "a":
                type="number"
                return is_title ? "Limite inferior" : "0";
            case "b":
                type="number"
                return is_title ? "Limite superior" : "4"
            case "fx":
                type="text"
                return is_title ? "Función" : "exp(-x)+4"
            case "n_iter":
                type="number"
                return is_title ? "Numero de iteraciones" : "10"
            case "tol":
                type="text"
                return is_title ? "Tolerancia del error" : "0.5E-3"
            case "x0":
                type="number"
                return is_title ? "Valor inicial para X" : "0"
            case "x1":
                type="number"
                return is_title ? "Siguiente valor para X" : "1"
            case "g":
                type="text"
                return is_title ? "g(x) deseada" : "exp(-x)+4+x"
            case "m":
                type="number"
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