import React, { useEffect, useState } from "react";
import InputGroup from "./InputGroup";
function MethodForm({ method_obj, put_method, method_type }) {

    const [input_data, set_data] = useState(method_obj);
    const [error_mssg, set_errormssg] = useState("");

    const update_data = (e) => {
        set_data((input_data) => {
            return {
                ...input_data,
                [e.target.name]: e.target.value
            }
        })
    }

    const check_input = (input) => {

        for (const key in input) {
            if (key !== "use_cs" && input[key] === "") {
                return false;
            }
        }

        switch (method_type) {
            case "regular":
                return true;
            case "matrix":
                // Check if its square
                let matrix = input["A"].split(";");
                let b = input["b"].split(";");
                let x0 = input["x0"].split(";");
        
                let length_ = matrix.length;
                let matrix_cpy = matrix;

                for (let i = 0; i < length_; i++) {
                    matrix_cpy = matrix[i].trim();
                    matrix_cpy = matrix_cpy.split(" ");
                    console.log(matrix_cpy);

                    if (matrix_cpy.length !== length_) {
                        set_errormssg("La matriz no es cuadrada.")
                        return false;
                    }
                }

                if(b.length !== length_ || x0.length !== length_) {
                    set_errormssg("El vector b o el X0 no cumplen con las dimensiones correctas.")
                    return false
                }

                return true;
            case "polinomial":
                const vX = input["x"].split(" ");
                const vY = input["y"].split(" ");
                if (vX.length !== vY.length) {
                    set_errormssg("Los vectores no tienen la misma cantidad de coordenadas");
                    return false;
                }
                return true;
            default:
                break;
        }
    }

    const on_submit = (e) => {
        e.preventDefault();
        let error_check = check_input(input_data);

        if (error_check) {
            set_errormssg("OK");
            put_method(input_data);
        } else {
            // set_errormssg("Ha habido un error con tus datos.")
        }
    }


    useEffect(() => {
        set_errormssg("");

    },[method_obj])

    return (
        <div className="rounded-md p-2 border border-[#c2c2c2] h-fit">
            <form action="" className="flex w-80 h-full justify-start items-start flex-col text-start" onSubmit={on_submit}>
                <h1 className="text-start text-xl mb-3 border-b border-b-[#c2c2c2] border-dotted w-full">Ingreso de datos</h1>
                <InputGroup method_obj={method_obj} update_data={update_data} method_type={method_type} />
                <small className={`pt-2 pl-0.5 ${error_mssg !== "OK" ? "text-red-500" : "text-green-500"}`}>{error_mssg}</small>
                <div className="w-full h-full flex items-end">
                    <button type="submit" className="bg-[#00509d] p-1 rounded-lg w-20 mt-2 text-white hover:bg-blue-500 transition-all ease-out">Enviar!</button>
                </div>
            </form>
        </div>

    )
}


export default MethodForm;
